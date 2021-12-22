import functools
from dataclasses import dataclass
from json import loads
from re import sub

from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from django.utils.datastructures import MultiValueDictKeyError


class require:
    def __init__(self, *params):
        self.params = params

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request):
            if request.method != 'POST':
                return HttpResponseNotAllowed(permitted_methods=('post',))

            data = loads(request.POST.get('data'))
            newspaper = data['newspaper'][0]['fields']
            newspaper_name = newspaper['name_section'].split(' - ')
            publication_type = data['publication_type'][0]['fields']
            publication_type['format_type'] = data['publication_type_name']
            column = newspaper[data['column']]
            number_column = sub(r'[^\d]', '', data['column'])

            pv_os = data['pv_os']

            pvos_number = data['pvos_number']
            title = data['title'].replace(" ", "")

            days = data['days']
            extension_in = data['extension_in']
            user_condensation = data['user_condensation']
            client = data['client'][0]['fields']['name']

            file = request.FILES['file']
            newspaper_name[1] = newspaper_name[1].replace(" ", "")

            return view(
                request, data, newspaper, newspaper_name, publication_type, column, number_column, pv_os, pvos_number,
                title, days, extension_in, user_condensation, client, file

            )

        return wrapper


def formatting_file_path(
        client, date_file, days, extension_in, newspaper_name, number_column, publication_type, pv_os,
        pvos_number, title
):
    return f"{client}/{date_file.year}/{pv_os}-{pvos_number}/{date_file.month}-{date_file.day}/{pv_os}-{pvos_number}_{newspaper_name[1].rstrip()}-{newspaper_name[2]}_{title.upper()}_{publication_type['format_type']}_{days}_{number_column}xheight{extension_in}"
