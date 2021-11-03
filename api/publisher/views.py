from base64 import b64encode as encode
from datetime import date #strftime, strptime
from json import loads, dumps
from os import path
from re import sub

from django.core.files.storage import default_storage as storage
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from publisher.commute import driver, fstring


# Define local storage, date, document and a client, run services an return files and data
@csrf_exempt
def create_publication(request):
    # Parse newspaper info, then index
    newspaper = (loads(request.POST.get('newspaper')))[0]['fields']
    newspaper_name = (newspaper['name_section']).split(' - ')
    # Parse publication type info, then index
    publication_type = (loads(request.POST.get('publication_type')))[0]['fields']
    publication_type_name = request.POST.get('publication_type_name')
    # Parse request info, then index
    column = newspaper[request.POST.get('column')]
    number_column = sub(r'[^\d]', '', request.POST.get('column'))
    pv_os =  request.POST.get('pv_os')
    pvos_number = request.POST.get('pvos_number')
    title = (request.POST.get('title')).replace(" ", "")
    days = request.POST.get('days')
    extension_in = request.POST.get('extension_in')
    user_condensation = request.POST.get('user_condensation')
    client = (loads(request.POST.get('client')))[0]['fields']['name']
    date_file = date.today()

    # Parse file, indicate name, extension_in and path
    file = request.FILES['file']
    newspaper_name[1] = newspaper_name[1].replace(" ", "")
    print(file)
    full_name = (str(client) + "/" +
                 str(date_file.year) + "/" +
                 str(pv_os) + "-" +
                 str(pvos_number) + "/" +
                 str(date_file.month) + "-" +
                 str(date_file.day) + "/" +
                 str(pv_os) + "-" +
                 str(pvos_number) + "_" +
                 str(newspaper_name[1].rstrip()) + "-" +
                 str(newspaper_name[2]) + "_" +
                 str(title).upper() + "_" +
                 str(publication_type_name) + "_" +
                 str(days) + "_" +
                 str(number_column) + "x" +
                 "height" +
                 str(extension_in))

    if storage.exists(full_name):
        storage.delete(full_name)

    just_name, extension_in = path.splitext(storage.save(full_name, file))
    document_name = fstring.paths['documents'] + just_name

    # Run services
    format_parameters = driver.format_parameter(document_name, extension_in, newspaper, publication_type,
                                                column, number_column, days, user_condensation, just_name)
    result = driver.driver(format_parameters)
    result['format_out'] = newspaper['format_out']

    try:
        print(fstring.message["info"]['process_success'])
        return HttpResponse(dumps(result), content_type=fstring.formats['http']['json'])
    except result[None]:
        raise Http404(fstring.message['http']['404'])
    except Exception as http_error:
        print(result)
        print(f"Description: {http_error}")
