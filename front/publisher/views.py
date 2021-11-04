import os
from datetime import date
import json
import requests
from django.core import serializers as serializer_section
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from publisher.commute import fstring
from publisher import models, serializer


class UFViewSet(viewsets.ModelViewSet):
    queryset = models.UF.objects.all()
    serializer_class = serializer.UFSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializer.CitySerializer


class NewspaperViewSet(viewsets.ModelViewSet):
    queryset = models.Newspaper.objects.all()
    serializer_class = serializer.NewspaperSerializer


class FontViewSet(viewsets.ModelViewSet):
    queryset = models.Font.objects.all()
    serializer_class = serializer.FontSerializer


class NewspaperSectionViewSet(viewsets.ModelViewSet):
    queryset = models.NewspaperSection.objects.all()
    serializer_class = serializer.NewspaperSectionSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializer.ClientSerializer


class PublicationTypeNameViewSet(viewsets.ModelViewSet):
    queryset = models.PublicationTypeName.objects.all()
    serializer_class = serializer.PublicationTypeNameSerializer


class PublicationTypeViewSet(viewsets.ModelViewSet):
    queryset = models.PublicationType.objects.all()
    serializer_class = serializer.PublicationTypeSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = models.Publication.objects.all()
    serializer_class = serializer.PublicationSerializer


# Get all infos for publication start
def publications(request):
    data = dict()
    data['newspapers'] = models.Newspaper.objects.all().order_by('name')
    data['clients'] = models.Client.objects.all()

    return render(request, 'index.html', data)


# Populate drop-down list of Sections
def newspaper_section_dropdown(request):
    newspaper_sections = models.NewspaperSection.objects.filter(newspaper_id=request.POST.get('newspaper')).order_by(
        'name_section')
    newspaper_sections_dropdown = serializer_section.serialize('json', newspaper_sections)
    return HttpResponse(newspaper_sections_dropdown)


# Populate drop-down list of Publication Types
def publication_type_dropdown(request):
    publication_types = models.PublicationType.objects.filter(
        newspaper_section_id=request.POST.get('newspaper_section')).order_by('name')
    newspaper_section = models.NewspaperSection.objects.get(pk=request.POST.get('newspaper_section'))
    newspaper_section_columns = serializer.NewspaperSectionSerializer(newspaper_section)
    publication_type_name = serializer.PublicationTypeSerializer(publication_types, many=True)
    data = {
        'publication_type_name': publication_type_name.data,
        'newspaper_section_columns': newspaper_section_columns.data
    }
    return HttpResponse(JSONRenderer().render(data))


# Just to finish and store publication
def store_publication(request, result, document_name, publication_type):
    publication = models.Publication(
        title=request.POST.get('title'),
        publication_type_id=publication_type[0],
        client_id=models.Client.objects.get(pk=request.POST.get('client')),
        document_name=document_name,
        calculated_price=result['price'],
        calculated_price_unity=result['price'],
        height=result['height'],
        days=request.POST.get('days'),
    )
    publication.save()


# Define local storage, date, document and a client
def create_publication(request):
    client = models.Client.objects.filter(pk=request.POST.get('client'))
    client_json = serializer_section.serialize('json', client)
    client = client.get(pk=request.POST.get('client'))
    title = request.POST.get('title')
    pv_os = request.POST.get('pv-os')
    pvos_number = request.POST.get('pv-os-number')
    days = request.POST.get('days')

    date_file = date.today()

    file = request.FILES['file']

    document_name, extension_in = os.path.splitext(file.name)

    full_name = (str(client) + "/" +
                 str(date_file.year) + "/" +
                 str(pv_os) + "-" +
                 str(pvos_number) + "/" +
                 str(date_file.month) + "-" +
                 str(date_file.day) + "/" +
                 "Original" + "/" +
                 str(pv_os) + "-" +
                 str(pvos_number) + "_" +
                 str(title).upper() + "_" +
                 str(days) +
                 str(extension_in))

    if default_storage.exists(full_name):
        default_storage.delete(full_name)

    file_name = default_storage.save(full_name, file)
    document_name_without_extension = document_name
    document_name = "documents/" + document_name

    results = dict()
    results['results'] = []

    # Loop for newspapers
    number_newspaper = 1
    while request.POST.get('publication_type_' + str(number_newspaper)):
        newspaper = models.NewspaperSection.objects.filter(
            pk=request.POST.get('newspaper_section_' + str(number_newspaper)))
        publication_type = models.PublicationType.objects.filter(
            pk=request.POST.get('publication_type_' + str(number_newspaper)))
        publication_type_name = serializer.PublicationTypeSerializer(publication_type, many=True)
        publication_type_name = (publication_type_name.data[0]['name']['name'])

        newspaper_column = request.POST.get('newspaper_cols_' + str(number_newspaper))
        user_condensation = request.POST.get('user_condensation_' + str(number_newspaper))

        newspaper_json = serializer_section.serialize('json', newspaper)
        publication_type_json = serializer_section.serialize('json', publication_type)

        data = {'newspaper': newspaper_json,
                'publication_type': publication_type_json,
                'client': client_json,
                'column': newspaper_column,
                'pv_os': pv_os,
                'pvos_number': pvos_number,
                'days': days,
                'user_condensation': user_condensation,
                'title': title,
                'publication_type_name': publication_type_name,
                'extension_in': extension_in
                }

        file_resource = default_storage.open(file_name, mode='rb')
        files = {'file': file_resource}

        # Just for test
        # print(data)

        result = requests.post(fstring.urls['api'], files=files, data=data)
        result = json.loads(result.content)
        file_resource.close()

        result['doc_name'] = document_name_without_extension

        # Save publication
        store_publication(request, result, document_name, publication_type)

        results['results'].append(result)

        number_newspaper = number_newspaper + 1

    return render(request, 'result.html', results)
