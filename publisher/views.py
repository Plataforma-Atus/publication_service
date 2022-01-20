import logging
from datetime import date
from json import dumps
from os import path

from django.core.files.storage import default_storage as storage
from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from publisher.commute.driver import Checking, InputData
from publisher.commute import driver, fstring
from publisher.domain import require, Formatting


@csrf_exempt
@require(
    'data', 'newspaper', 'newspaper_name', 'publication_type', 'column', 'number_column', 'pv_os', 'pvos_number',
    'title', 'days', 'extension_in', 'user_condensation', 'client', 'file'
)
def create_publication(
        request, data, newspaper, newspaper_name, publication_type, column, number_column, pv_os,
        pvos_number, title, days, extension_in, user_condensation, client, file
):
    date_file: date = date.today()

    full_name = Formatting.formatting_file_path(
        client, date_file, days, extension_in, newspaper_name, number_column,
        publication_type, pv_os, pvos_number, title
    )

    if storage.exists(full_name):
        storage.delete(full_name)

    just_name, extension_in = path.splitext(storage.save(full_name, file))
    document_name = fstring.paths['documents'] + just_name

    format_parameters = InputData.format_parameter(
        document_name, extension_in, newspaper,
        publication_type, column, number_column,
        days, user_condensation, just_name
    )

    result = Checking.input_extension(format_parameters)
    result['format_out'] = newspaper['format_out']

    try:
        logging.info(fstring.message["info"]['process_success'])

        return HttpResponse(dumps(result), content_type=fstring.formats['http']['json'])
    except result[None]:
        raise Http404(fstring.message['http']['404'])
    except Exception as http_error:
        logging.info(result)
        logging.info(f"Description: {http_error}")
