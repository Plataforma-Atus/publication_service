from publisher.commute.cropper import convert_pdf_to_greyscale
from publisher.commute.driver import format_parameter, rename_files, road_map
from publisher.commute.standarder import extract_text, run_text


def test_road_map(format_parameters):
    response = road_map(format_parameters)

    assert True


def test_format_parameter(document_name, newspaper, publication_type, just_name, extension_in, column, number_column,
                          days, user_condensation):
    response = format_parameter(
        document_name, extension_in, column, number_column, days,
        user_condensation, newspaper, publication_type, just_name
    )

