from rest_framework import serializers

from publisher import models


class UFSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UF
        fields = ('uf', 'name', 'region')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('name', 'uf', 'size', 'capital')


class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newspaper
        fields = ('name', 'city', 'official_newspaper', 'active_newspaper', 'printed', 'id')


class FontSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Font
        fields = ('name', 'id')


class NewspaperSectionSerializer(serializers.ModelSerializer):
    newspaper_id = NewspaperSerializer()
    font_name = FontSerializer()
    font_name_alternative = FontSerializer()

    class Meta:
        model = models.NewspaperSection
        fields = ('name_section', 'id', 'newspaper_id', 'width_1', 'width_2', 'width_3', 'width_4', 'width_5',
                  'width_6', 'width_7', 'width_8', 'width_9', 'width_10', 'gutter', 'height', 'font_name',
                  'font_name_alternative', 'font_size', 'font_leading', 'font_size_company', 'font_leading_company',
                  'edge', 'bold', 'italic', 'underline', 'tracking', 'condensation', 'format_out', 'price_cm',
                  'height_round')


class PublicationTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PublicationTypeName
        fields = ('name', 'description', 'id')


class PublicationTypeSerializer(serializers.ModelSerializer):
    name = PublicationTypeNameSerializer()
    newspaper_section_id = NewspaperSectionSerializer()
    font_name = FontSerializer()

    class Meta:
        model = models.PublicationType
        fields = ('name', 'special_format', 'estimated_budget_delivery', 'newspaper_section_id', 'margin', 'font_name',
                  'font_size', 'format', 'font_size_company', 'font_leading', 'font_leading_company', 'bold', 'italic',
                  'underline', 'tracking', 'condensation', 'id')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('name', 'email', 'phone', 'phone_secondary', 'cellphone', 'id')


class PublicationSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer()
    publication_type_id = PublicationTypeSerializer()

    class Meta:
        model = models.Publication
        fields = ('title', 'document_name', 'calculated_price', 'days', 'height', 'client_id', 'publication_type_id',
                  'id')
