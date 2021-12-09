import pytest

from publisher.commute.budgeter import calculate_budget_by_centimeter


@pytest.fixture
def result():
    return {'file': 'documents/Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight_crp', 'width': '11.70',
            'height': '9.00', 'price': '5400.00'}


@pytest.fixture
def format_parameters_cropper():
    return {'document_name': 'documents/Atus-Produção/2021/PV-444/12-8/PV-444_Noticiário-A '
                             'Tribuna_TESTANDO_Edital_1_4xheight', 'just_name':
                'Atus-Produção/2021/PV-444/12-8/PV-444_Noticiário-A Tribuna_TESTANDO_Edital_1_4xheight', 'extension_in':
                '.docx', 'extension_out': '.pdf', 'format_out': '.pdf',
            'publication_type': {'name': '4caaa63a-eb46-4e1f-951a'
                                         '-01843132b0a2',
                                 'newspaper_section_id':
                                     '4b7fb698-862d-4ef7-9aa0-cd457448a032', 'create_at': '2021-08-09T18:11:42.799Z',
                                 'modify_at': '2021-08-09T18:11:42.799Z', 'instructions': '', 'margin': None,
                                 'estimated_budget_delivery': 1, 'font_name': 1, 'font_size': '6.00',
                                 'font_leading': '6.00', 'font_size_company': '6.00', 'font_leading_company': '6.00',
                                 'bold': True, 'italic': True, 'underline': True, 'tracking': '-10',
                                 'condensation': '90.00', 'special_format': True, 'format': '1',
                                 'format_type': 'Edital'}, 'price_cm': 161.0,
            'name_section': 'Legal - Noticiário - A Tribuna - ES', 'column': 21.9, 'number_column': '4', 'height': 36.5,
            'height_round': True, 'format_allowed': '1', 'days': '1', 'user_condensation': '99.00',
            'condensation': '99.00', 'edge': True, 'bold': True, 'italic': True, 'underline': True, 'font_index': 1,
            'font_size': 6.0, 'font_size_company': 6.0, 'font_leading': 6.0, 'font_leading_company': 6.0,
            'font_name': 'Arial', 'document': ' <docx.document.Document object at 0x7fcd00c33e40>',
            'docx_default': '<docx.document.Document object at 0x7fcd00c37f40>', 'text_index': 0,
            'initial_paragraph': '<docx.text.paragraph.Paragraph object at 0x7fcd00cc2610>',
            'texts_flowing': '<docx.text.paragraph.Paragraph object at 0x7fcd00cc2df0>',
            'paragraph': '<docx.text.paragraph.Paragraph object at 0x7fcd00c7c820>'}


@pytest.fixture
def format_parameters():
    return {
        'document_name': 'documents/Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight',
        'just_name': 'Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight', 'extension_in': '.docx',
        'extension_out': '.pdf', 'format_out': '.pdf',
        'publication_type': {'name': '94d2b678-2e97-4a42-a490-c2026bec5166',
                             'newspaper_section_id': 'c83ff6c4-909a-4193-bd3b-6f3ac3e21e6d',
                             'create_at': '2021-10-25T12:45:56.558Z', 'modify_at': '2021-10-25T12:45:56.559Z',
                             'instructions': '', 'margin': None, 'estimated_budget_delivery': 1, 'font_name': 1,
                             'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00',
                             'font_leading_company': '6.00', 'bold': True, 'italic': True, 'underline': True,
                             'tracking': '-10', 'condensation': '90.00', 'special_format': True, 'format': '0',
                             'format_type': 'Ata'}, 'price_cm': 150.0,
        'name_section': 'Classificados - A Gazeta - SP', 'column': 11.7, 'number_column': '4', 'height': 52.0,
        'height_round': True, 'format_allowed': '0', 'days': '2', 'user_condensation': 'default',
        'condensation': '90.00', 'edge': True, 'bold': True, 'italic': True, 'underline': True, 'font_index': 1,
        'font_size': 6.0, 'font_size_company': 6.0, 'font_leading': 6.0, 'font_leading_company': 6.0,
        'font_name': 'Arial', 'document': '<docx.document.Document object at 0x7f64e853a980>',
        'docx_default': '<docx.document.Document object at 0x7f64e0bab340>', 'text_index': 0,
        'initial_paragraph': '<docx.text.paragraph.Paragraph object at 0x7f64e1491a90>',
        'texts_flowing': '<docx.text.paragraph.Paragraph object at 0x7f64e141a8b0>',
        'paragraph': '<docx.text.paragraph.Paragraph object at 0x7f64e144b9d0>',
        'texts': '<docx.text.run.Run object at 0x7f64e0b526a0>', 'chars_count': 4725
    }


@pytest.fixture
def document_name():
    return 'documents/Atus-Produção/2021/PV-444/12-8/PV-444_Noticiário-A Tribuna_TESTANDO_Edital_1_4xheight'


@pytest.fixture
def newspaper():
    return {'name_section': 'Legal - Noticiário - A Tribuna - ES',
            'newspaper_id': '30bfaa48-36ba-49ce-9d87-0358bb591b26', 'width_1': '5.10', 'width_2': '10.70',
            'width_3': '16.30', 'width_4': '21.90', 'width_5': '26.70', 'width_6': '0.00', 'width_7': '0.00',
            'width_8': '0.00', 'width_9': '0.00', 'width_10': '0.00', 'gutter': '0.206', 'height': '36.5',
            'minimum_height': None, 'maximum_height_budget': None, 'font_name': 1, 'font_name_alternative': 1,
            'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00', 'font_leading_company': '6.00',
            'tracking': '-10', 'condensation': '90.00', 'format_out': '.pdf', 'price_cm': '161.00',
            'price_cm_square': '161.00', 'price_extra_color': '161.00', 'bold': True, 'italic': True, 'underline': True,
            'edge': True, 'height_round': True, 'deadline_days': '2021-08-09', 'deadline_hour': 1,
            'circulate_days': '2021-08-09', 'create_at': '2021-08-09T18:09:48.872Z',
            'modify_at': '2021-10-07T19:34:01.551Z'}


@pytest.fixture
def publication_type():
    return {'name_section': 'Legal - Noticiário - A Tribuna - ES',
            'newspaper_id': '30bfaa48-36ba-49ce-9d87-0358bb591b26', 'width_1': '5.10', 'width_2': '10.70',
            'width_3': '16.30', 'width_4': '21.90', 'width_5': '26.70', 'width_6': '0.00', 'width_7': '0.00',
            'width_8': '0.00', 'width_9': '0.00', 'width_10': '0.00', 'gutter': '0.206', 'height': '36.5',
            'minimum_height': None, 'maximum_height_budget': None, 'font_name': 1, 'font_name_alternative': 1,
            'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00', 'font_leading_company': '6.00',
            'tracking': '-10', 'condensation': '90.00', 'format_out': '.pdf', 'price_cm': '161.00',
            'price_cm_square': '161.00', 'price_extra_color': '161.00', 'bold': True, 'italic': True, 'underline': True,
            'edge': True, 'height_round': True, 'deadline_days': '2021-08-09', 'deadline_hour': 1,
            'circulate_days': '2021-08-09', 'create_at': '2021-08-09T18:09:48.872Z',
            'modify_at': '2021-10-07T19:34:01.551Z'}


@pytest.fixture
def just_name():
    return 'Atus-Produção/2021/PV-444/12-8/PV-444_Noticiário-A Tribuna_TESTANDO_Edital_1_4xheight'


@pytest.fixture
def extension_in():
    return '.docx'


@pytest.fixture
def column():
    return '21.90'


@pytest.fixture
def number_column():
    return '4'


@pytest.fixture
def days():
    return '1'


@pytest.fixture
def user_condensation():
    return '99.00'
