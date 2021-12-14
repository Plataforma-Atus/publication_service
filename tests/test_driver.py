from publisher.commute.driver import checking_input_extension, format_parameter
from publisher.commute.standarder import special_adjust

from publisher.commute.driver import condensation_definer


def test_checking_input_extension(format_parameters):
    response = checking_input_extension(format_parameters)

    assert True


def test_format_parameter(
        document_name_cropper, newspaper, publication_type, just_name, extension_in, column, number_column,
        days, user_condensation
):
    response = format_parameter(
        document_name=document_name_cropper, extension_in=extension_in, column=column, number_column=number_column,
        days=days,
        user_condensation=user_condensation, newspaper=newspaper, publication_type=publication_type, just_name=just_name
    )
    expected_format_parameter = {'document_name': 'PV-444_AGazeta-TO_TESTING_Edital_2_2xheight_crp.pdf',
                                 'just_name': 'Atus-Produção/2021/PV-444/12-8/PV-444_Noticiário-A Tribuna_TESTANDO_Edital_1_4xheight',
                                 'extension_in': '.docx', 'extension_out': '.pdf', 'format_out': '.pdf',
                                 'publication_type': {'name': '4caaa63a-eb46-4e1f-951a-01843132b0a2',
                                                      'newspaper_section_id': '4f0bd6df-a07f-4484-b8bd-270c9b404665',
                                                      'create_at': '2021-09-27T13:06:17.242Z',
                                                      'modify_at': '2021-09-27T13:08:14.083Z', 'instructions': '',
                                                      'margin': None, 'estimated_budget_delivery': 1, 'font_name': 1,
                                                      'font_size': '6.00', 'font_leading': '6.00',
                                                      'font_size_company': '6.00', 'font_leading_company': '6.00',
                                                      'bold': True, 'italic': True, 'underline': True, 'tracking': '0',
                                                      'condensation': '90.00', 'special_format': True, 'format': '1',
                                                      'format_type': 'Edital'}, 'price_cm': 161.0,
                                 'name_section': 'Legal - Noticiário - A Tribuna - ES', 'column': 21.9,
                                 'number_column': '4', 'height': 36.5, 'height_round': True, 'format_allowed': '1',
                                 'days': '1', 'user_condensation': '99.00', 'condensation': '99.00', 'edge': True,
                                 'bold': True, 'italic': True, 'underline': True, 'font_index': 1, 'font_size': 6.0,
                                 'font_size_company': 6.0, 'font_leading': 6.0, 'font_leading_company': 6.0,
                                 'font_name': 'Arial'}

    assert response == expected_format_parameter


def test_special_adjust(format_parameters):
    response = special_adjust(format_parameters)
    assert True


def test_condensation_definer(format_parameters) -> None:
    response = condensation_definer(format_parameters)
    assert response is None
