import pytest

from publisher.commute.budgeter import calculate_budget_by_centimeter


@pytest.fixture
def result():
    return {'file': 'documents/Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight_crp', 'width': '11.70',
            'height': '9.00', 'price': '5400.00'}


@pytest.fixture
def format_parameters_cropper():
    return {'document_name': 'PV-444_AGazeta-TO_TESTING_Edital_2_2xheight_crp.pdf'
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
    return {'name': '4caaa63a-eb46-4e1f-951a-01843132b0a2',
            'newspaper_section_id': '4f0bd6df-a07f-4484-b8bd-270c9b404665', 'create_at': '2021-09-27T13:06:17.242Z',
            'modify_at': '2021-09-27T13:08:14.083Z', 'instructions': '', 'margin': None, 'estimated_budget_delivery': 1,
            'font_name': 1, 'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00',
            'font_leading_company': '6.00', 'bold': True, 'italic': True, 'underline': True, 'tracking': '0',
            'condensation': '90.00', 'special_format': True, 'format': '1', 'format_type': 'Edital'}


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


@pytest.fixture
def document_name_cropper():
    return 'PV-444_AGazeta-TO_TESTING_Edital_2_2xheight_crp.pdf'


@pytest.fixture
def data():
    return {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                     '"8fafb863-765d-485b-9aa3-63047c2b0119", "fields": {"name_section": "Notici\\u00e1rio - A Gazeta '
                     '- SP", "newspaper_id": "069d9b80-2ada-4152-bef8-964cce3c4dd9", "width_1": "4.60", "width_2": '
                     '"9.60", "width_3": "14.60", "width_4": "19.60", "width_5": "24.60", "width_6": "29.70", '
                     '"width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", '
                     '"height": "52.0", "minimum_height": "1.0", "maximum_height_budget": "52.0", "font_name": 1, '
                     '"font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": '
                     '"6.00", "font_leading_company": "6.00", "tracking": "-10", "condensation": "90.00", '
                     '"format_out": ".pdf", "price_cm": "150.00", "price_cm_square": "150.00", "price_extra_color": '
                     '"150.00", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, '
                     '"deadline_days": "2021-10-25", "deadline_hour": 17, "circulate_days": "2021-10-25", '
                     '"create_at": "2021-10-25T12:37:08.974Z", "modify_at": "2021-10-25T12:44:07.404Z"}}], '
                     '"publication_type": [{"model": "publisher.publicationtype", '
                     '"pk": "04ca8b3d-a8b6-4941-9958-370f1218cfb6", "fields": {"name": '
                     '"94d2b678-2e97-4a42-a490-c2026bec5166", "newspaper_section_id": '
                     '"8fafb863-765d-485b-9aa3-63047c2b0119", "create_at": "2021-10-25T12:45:40.569Z", "modify_at": '
                     '"2021-10-25T12:45:40.569Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
                     '"font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", '
                     '"font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": '
                     '"-10", "condensation": "90.00", "special_format": true, "format": "0"}}], "client": [{"model": '
                     '"publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": '
                     '"Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": '
                     '"1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": '
                     '"2021-07-06T21:47:43.293Z"}}], "column": "width_3", "pv_os": "PV", "pvos_number": "2", '
                     '"days": "1", "user_condensation": "87.00", "title": "test de create", "publication_type_name": '
                     '"Ata", "extension_in": ".docx"}']}


@pytest.fixture
def file():
    with open('tests/default.docx', 'rb') as file:
        data = file.read()
        return data


@pytest.fixture
def payload():
    return {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                     '"1c8ff5e8-9087-40e7-946e-2bac7b2a9732", "fields": {"name_section": "Particulares - '
                     'Bras\\u00edlia Agora - DF", "newspaper_id": "dc6503f5-d022-4d61-b478-2139c3d05460", "width_1": '
                     '"4.60", "width_2": "9.60", "width_3": "14.60", "width_4": "19.60", "width_5": "24.60", '
                     '"width_6": "29.70", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": '
                     '"0.00", "gutter": "0.206", "height": "54.0", "minimum_height": "1.0", "maximum_height_budget": '
                     '"54.0", "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": '
                     '"6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", '
                     '"condensation": "90.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": '
                     '"150.00", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, '
                     '"edge": true, "height_round": true, "deadline_days": "2021-10-27", "deadline_hour": 17, '
                     '"circulate_days": "2021-10-27", "create_at": "2021-10-27T15:17:42.887Z", "modify_at": '
                     '"2021-10-27T15:17:42.887Z"}}], "publication_type": [{"model": "publisher.publicationtype", '
                     '"pk": "8e4ea252-291f-4b97-84b6-5c045b578896", "fields": {"name": '
                     '"92ed96d4-c5f1-41d1-8e7a-ca3d71220113", "newspaper_section_id": '
                     '"1c8ff5e8-9087-40e7-946e-2bac7b2a9732", "create_at": "2021-10-27T15:18:19.548Z", "modify_at": '
                     '"2021-10-27T15:18:19.548Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
                     '"font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", '
                     '"font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": '
                     '"-10", "condensation": "90.00", "special_format": true, "format": "2"}}], "client": [{"model": '
                     '"publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": '
                     '"Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": '
                     '"1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": '
                     '"2021-07-06T21:47:43.293Z"}}], "column": "width_3", "pv_os": "PV", "pvos_number": "2", '
                     '"days": "2", "user_condensation": "default", "title": "qweqweqw", "publication_type_name": '
                     '"Sema", "extension_in": ".docx"}']}


@pytest.fixture
def payload_folha_sp():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "585ec107-5eeb-44e5-9026-b365dc1f46e5", '
        '"fields": {"name_section": "Empresarial - Folha - SP", "newspaper_id": '
        '"a6df9e6b-58b6-4f99-9d06-42cbea9a6fe6", "width_1": "4.60", "width_2": "9.60", "width_3": "14.60", '
        '"width_4": "19.60", "width_5": "24.60", "width_6": "29.60", "width_7": "0.00", "width_8": "0.00", '
        '"width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "52.0", "minimum_height": null, '
        '"maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", '
        '"font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", '
        '"condensation": "80.00", "format_out": ".pdf", "price_cm": "1.00", "price_cm_square": "1.00", '
        '"price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, '
        '"height_round": true, "deadline_days": "2021-07-19", "deadline_hour": 1, "circulate_days": "2021-07-19", '
        '"create_at": "2021-07-19T00:37:09.994Z", "modify_at": "2021-10-26T21:56:35.884Z"}}], "publication_type": [{'
        '"model": "publisher.publicationtype", "pk": "383cef43-bf84-4103-947f-157d93512894", "fields": {"name": '
        '"92ed96d4-c5f1-41d1-8e7a-ca3d71220113", "newspaper_section_id": "585ec107-5eeb-44e5-9026-b365dc1f46e5", '
        '"create_at": "2021-07-19T00:38:04.642Z", "modify_at": "2021-10-11T16:47:14.686Z", "instructions": "", '
        '"margin": null, "estimated_budget_delivery": 2, "font_name": 3, "font_size": "8.00", "font_leading": "8.00", '
        '"font_size_company": "6.00", "font_leading_company": "6.00", "bold": true, "italic": true, "underline": '
        'true, "tracking": "0", "condensation": "80.00", "special_format": false, "format": "2"}}], "client": [{'
        '"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", '
        '"email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": '
        '"11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], '
        '"column": "width_1", "pv_os": "PV", "pvos_number": "4", "days": "1", "user_condensation": "80.00", '
        '"title": "pdf", "publication_type_name": "Sema", "extension_in": ".docx"}']}


@pytest.fixture
def payload_diario_de_cuiba():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "84175811-d99f-41cb-bacd-8de2101b4833", "fields": {"name_section": "Terceiros - DC - MT", "newspaper_id": "85b3f575-810d-4c3e-865a-36101a4fecfe", "width_1": "2.60", "width_2": "5.60", "width_3": "8.60", "width_4": "11.60", "width_5": "14.60", "width_6": "17.60", "width_7": "20.60", "width_8": "23.60", "width_9": "26.60", "width_10": "29.60", "gutter": "0.206", "height": "52.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "5.00", "font_leading": "5.00", "font_size_company": "5.00", "font_leading_company": "5.00", "tracking": "-10", "condensation": "87.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": "150.00", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, "deadline_days": "2021-07-12", "deadline_hour": 1, "circulate_days": "2021-07-12", "create_at": "2021-07-12T14:02:56.209Z", "modify_at": "2021-11-10T20:13:59.329Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "ce8b1a1d-9699-4fb3-92a3-192adfe12aa4", "fields": {"name": "4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": "84175811-d99f-41cb-bacd-8de2101b4833", "create_at": "2021-07-19T00:24:37.827Z", "modify_at": "2021-09-22T01:35:42.924Z", "instructions": "", "margin": null, "estimated_budget_delivery": 2, "font_name": 1, "font_size": "4.90", "font_leading": "4.90", "font_size_company": "4.90", "font_leading_company": "4.90", "bold": true, "italic": true, "underline": true, "tracking": "0", "condensation": "87.00", "special_format": false, "format": "1"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_2", "pv_os": "PV", "pvos_number": "4", "days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": "Edital", "extension_in": ".docx"}']}


@pytest.fixture
def payload_ro():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "c2686346-da3e-4e20-a532-d2716b143fcf", "fields": {"name_section": "Terceiros - DORO - RO", "newspaper_id": "5ea59335-59fa-434f-b12a-fe7384f9f63d", "width_1": "9.00", "width_2": "18.00", "width_3": "0.00", "width_4": "0.00", "width_5": "0.00", "width_6": "0.00", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "27.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "8.00", "font_leading": "9.60", "font_size_company": "8.00", "font_leading_company": "9.60", "tracking": "0", "condensation": "100.00", "format_out": ".pdf", "price_cm": "0.18", "price_cm_square": "0.18", "price_extra_color": "0.18", "bold": true, "italic": true, "underline": true, "edge": false, "height_round": true, "deadline_days": "2021-09-30", "deadline_hour": 17, "circulate_days": "2021-09-30", "create_at": "2021-09-30T17:14:13.162Z", "modify_at": "2021-09-30T17:14:13.162Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "f3e41e7a-82a5-43c5-8852-7f9310491d2c", "fields": {"name": "4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": "c2686346-da3e-4e20-a532-d2716b143fcf", "create_at": "2021-09-30T18:04:48.188Z", "modify_at": "2021-09-30T18:04:48.188Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, "font_name": 1, "font_size": "8.00", "font_leading": "9.60", "font_size_company": "8.00", "font_leading_company": "9.60", "bold": true, "italic": true, "underline": true, "tracking": "0", "condensation": "100.00", "special_format": true, "format": "1"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "4", "days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": "Edital", "extension_in": ".docx"}']}


@pytest.fixture
def payload_mato_grosso():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "742fc0e4-ca94-45b4-b636-d72d8dfe72d5", "fields": {"name_section": "Terceiros - DOMT - MT", "newspaper_id": "1e374a5d-c1d5-4827-b224-7c8426ed5fdb", "width_1": "9.40", "width_2": "19.40", "width_3": "0.00", "width_4": "0.00", "width_5": "0.00", "width_6": "0.00", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "27.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "8.00", "font_leading": "9.00", "font_size_company": "8.00", "font_leading_company": "9.00", "tracking": "0", "condensation": "100.00", "format_out": ".docx", "price_cm": "9.00", "price_cm_square": "9.00", "price_extra_color": "9.00", "bold": true, "italic": true, "underline": true, "edge": false, "height_round": false, "deadline_days": "2021-07-12", "deadline_hour": 1, "circulate_days": "2021-07-12", "create_at": "2021-07-12T14:01:34.585Z", "modify_at": "2021-10-02T19:13:57.612Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "2bbd7c4e-f184-421d-af76-01292b853b8c", "fields": {"name": "4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": "742fc0e4-ca94-45b4-b636-d72d8dfe72d5", "create_at": "2021-07-19T00:24:12.617Z", "modify_at": "2021-07-19T00:24:12.617Z", "instructions": "", "margin": null, "estimated_budget_delivery": 2, "font_name": 1, "font_size": "8.00", "font_leading": "8.00", "font_size_company": "8.00", "font_leading_company": "8.00", "bold": true, "italic": true, "underline": true, "tracking": "0", "condensation": "100.00", "special_format": false, "format": "1"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "4", "days": "1", "user_condensation": "74.00", "title": "pdf", "publication_type_name": "Edital", "extension_in": ".docx"}']}


@pytest.fixture
def payload_parana():
    return {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                     '"f269b21f-cc26-4207-959f-8d653e4e85c2", "fields": {"name_section": "Com\\u00e9rcio, '
                     'Ind\\u00fastria e Servi\\u00e7os - DOPR - PR", "newspaper_id": '
                     '"c90b1f4b-ea5f-4f6b-aa02-b94981cf75a5", "width_1": "8.00", "width_2": "17.00", "width_3": '
                     '"25.00", "width_4": "0.00", "width_5": "0.00", "width_6": "0.00", "width_7": "0.00", '
                     '"width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "31.0", '
                     '"minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": '
                     '1, "font_size": "7.00", "font_leading": "7.00", "font_size_company": "7.00", '
                     '"font_leading_company": "7.00", "tracking": "-10", "condensation": "90.00", "format_out": '
                     '".pdf", "price_cm": "30.00", "price_cm_square": "30.00", "price_extra_color": "150.00", '
                     '"bold": true, "italic": true, "underline": true, "edge": false, "height_round": true, '
                     '"deadline_days": "2021-07-19", "deadline_hour": 1, "circulate_days": "2021-07-19", "create_at": '
                     '"2021-07-19T13:36:22.402Z", "modify_at": "2021-10-27T10:57:39.363Z"}}], "publication_type": [{'
                     '"model": "publisher.publicationtype", "pk": "db6fe7af-24e1-4d42-bae9-dce17195b473", "fields": {'
                     '"name": "94d2b678-2e97-4a42-a490-c2026bec5166", "newspaper_section_id": '
                     '"f269b21f-cc26-4207-959f-8d653e4e85c2", "create_at": "2021-07-19T13:36:44.200Z", "modify_at": '
                     '"2021-07-19T13:36:44.200Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
                     '"font_name": 1, "font_size": "7.00", "font_leading": "7.00", "font_size_company": "7.00", '
                     '"font_leading_company": "7.00", "bold": true, "italic": true, "underline": true, "tracking": '
                     '"0", "condensation": "100.00", "special_format": false, "format": "0"}}], "client": [{"model": '
                     '"publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": '
                     '"Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": '
                     '"1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": '
                     '"2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "4", '
                     '"days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": "Ata", '
                     '"extension_in": ".docx"}']}


@pytest.fixture
def payload_pe():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "673e14ad-38bc-4129-b4b1-326012dce51f", '
        '"fields": {"name_section": "Classificados - Di\\u00e1rio de Pernambuco - PE", "newspaper_id": '
        '"cf36459f-f379-4680-bce8-a5a901058948", "width_1": "2.90", "width_2": "6.27", "width_3": "9.56", "width_4": '
        '"12.85", "width_5": "16.13", "width_6": "19.40", "width_7": "22.70", "width_8": "26.00", "width_9": "0.00", '
        '"width_10": "0.00", "gutter": "0.206", "height": "38.0", "minimum_height": null, "maximum_height_budget": '
        'null, "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", '
        '"font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", "condensation": "90.00", '
        '"format_out": ".pdf", "price_cm": "150.00", "price_cm_square": "150.00", "price_extra_color": "150.00", '
        '"bold": true, "italic": true, "underline": true, "edge": false, "height_round": true, "deadline_days": '
        '"2021-10-06", "deadline_hour": 16, "circulate_days": "2021-10-06", "create_at": "2021-10-06T12:49:22.337Z", '
        '"modify_at": "2021-10-06T12:49:22.337Z"}}], "publication_type": [{"model": "publisher.publicationtype", '
        '"pk": "ff1c27ef-9dec-45c8-9aaf-6262f0e1a78f", "fields": {"name": "92ed96d4-c5f1-41d1-8e7a-ca3d71220113", '
        '"newspaper_section_id": "673e14ad-38bc-4129-b4b1-326012dce51f", "create_at": "2021-10-06T13:27:46.058Z", '
        '"modify_at": "2021-10-06T13:27:46.058Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
        '"font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", '
        '"font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": "-10", '
        '"condensation": "90.00", "special_format": true, "format": "2"}}], "client": [{"model": "publisher.client", '
        '"pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", '
        '"phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": '
        '"2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_2", "pv_os": "PV", '
        '"pvos_number": "4", "days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": '
        '"Sema", "extension_in": ".docx"}']}


@pytest.fixture
def payload_df():
    return {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                     '"1c8ff5e8-9087-40e7-946e-2bac7b2a9732", "fields": {"name_section": "Particulares - '
                     'Bras\\u00edlia Agora - DF", "newspaper_id": "dc6503f5-d022-4d61-b478-2139c3d05460", "width_1": '
                     '"4.60", "width_2": "9.60", "width_3": "14.60", "width_4": "19.60", "width_5": "24.60", '
                     '"width_6": "29.70", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": '
                     '"0.00", "gutter": "0.206", "height": "54.0", "minimum_height": "1.0", "maximum_height_budget": '
                     '"54.0", "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": '
                     '"6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", '
                     '"condensation": "90.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": '
                     '"150.00", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, '
                     '"edge": true, "height_round": true, "deadline_days": "2021-10-27", "deadline_hour": 17, '
                     '"circulate_days": "2021-10-27", "create_at": "2021-10-27T15:17:42.887Z", "modify_at": '
                     '"2021-10-27T15:17:42.887Z"}}], "publication_type": [{"model": "publisher.publicationtype", '
                     '"pk": "495a6949-4476-420f-91c1-fb03c41a484b", "fields": {"name": '
                     '"4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": '
                     '"1c8ff5e8-9087-40e7-946e-2bac7b2a9732", "create_at": "2021-10-27T15:18:32.659Z", "modify_at": '
                     '"2021-10-27T15:18:32.659Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
                     '"font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", '
                     '"font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": '
                     '"-10", "condensation": "90.00", "special_format": true, "format": "1"}}], "client": [{"model": '
                     '"publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": '
                     '"Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": '
                     '"1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": '
                     '"2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "4", '
                     '"days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": "Edital", '
                     '"extension_in": ".docx"}']}


@pytest.fixture
def payload_minas_gerais():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "a6a10ba5-d2c9-45fc-ba15-99d9f13e5a50", '
        '"fields": {"name_section": "Particulares - DOMG - MG", "newspaper_id": '
        '"2e73c46e-447b-4f83-b073-3e95dac65891", "width_1": "6.00", "width_2": "12.50", "width_3": "19.00", '
        '"width_4": "25.50", "width_5": "0.00", "width_6": "0.00", "width_7": "0.00", "width_8": "0.00", "width_9": '
        '"0.00", "width_10": "0.00", "gutter": "0.206", "height": "32.0", "minimum_height": "10.0", '
        '"maximum_height_budget": null, "font_name": 2, "font_name_alternative": 2, "font_size": "6.00", '
        '"font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "0", '
        '"condensation": "100.00", "format_out": ".rtf", "price_cm": "89.59", "price_cm_square": "89.59", '
        '"price_extra_color": "89.59", "bold": true, "italic": true, "underline": true, "edge": false, '
        '"height_round": true, "deadline_days": "2021-07-19", "deadline_hour": 1, "circulate_days": "2021-07-19", '
        '"create_at": "2021-07-19T12:23:27.632Z", "modify_at": "2021-10-05T16:32:34.422Z"}}], "publication_type": [{'
        '"model": "publisher.publicationtype", "pk": "b0eacda1-2dde-482c-98c2-0d39a66993a4", "fields": {"name": '
        '"4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": "a6a10ba5-d2c9-45fc-ba15-99d9f13e5a50", '
        '"create_at": "2021-07-19T12:25:17.271Z", "modify_at": "2021-07-19T12:25:17.271Z", "instructions": "", '
        '"margin": null, "estimated_budget_delivery": 1, "font_name": 2, "font_size": "6.00", "font_leading": "6.00", '
        '"font_size_company": "6.00", "font_leading_company": "6.00", "bold": true, "italic": true, "underline": '
        'true, "tracking": "0", "condensation": "100.00", "special_format": true, "format": "1"}}], "client": [{'
        '"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", '
        '"email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": '
        '"11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], '
        '"column": "width_2", "pv_os": "PV", "pvos_number": "4", "days": "1", "user_condensation": "80.00", '
        '"title": "pdf", "publication_type_name": "Edital", "extension_in": ".docx"}']}


@pytest.fixture
def payload_amazonas():
    return {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                     '"d1f07a59-df17-4c16-a773-058b91081349", "fields": {"name_section": "Particulares - DOAM - AM", '
                     '"newspaper_id": "af1cd89b-d79b-4992-ba80-9a2410333b9b", "width_1": "9.50", "width_2": "18.20", '
                     '"width_3": "0.00", "width_4": "0.00", "width_5": "0.00", "width_6": "0.00", "width_7": "0.00", '
                     '"width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "27.0", '
                     '"minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": '
                     '1, "font_size": "8.00", "font_leading": "9.60", "font_size_company": "10.00", '
                     '"font_leading_company": "12.00", "tracking": "0", "condensation": "100.00", "format_out": '
                     '".docx", "price_cm": "78.00", "price_cm_square": "78.00", "price_extra_color": "78.00", '
                     '"bold": true, "italic": true, "underline": true, "edge": false, "height_round": true, '
                     '"deadline_days": "2021-09-28", "deadline_hour": 16, "circulate_days": "2021-09-28", '
                     '"create_at": "2021-09-28T18:18:40.114Z", "modify_at": "2021-10-11T13:25:11.245Z"}}], '
                     '"publication_type": [{"model": "publisher.publicationtype", '
                     '"pk": "5a108a68-ec89-413f-a90b-5a93a35c8c34", "fields": {"name": '
                     '"4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": '
                     '"d1f07a59-df17-4c16-a773-058b91081349", "create_at": "2021-09-28T18:20:44.118Z", "modify_at": '
                     '"2021-09-28T18:20:44.118Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
                     '"font_name": 1, "font_size": "8.00", "font_leading": "9.60", "font_size_company": "10.00", '
                     '"font_leading_company": "12.00", "bold": true, "italic": true, "underline": true, "tracking": '
                     '"0", "condensation": "100.00", "special_format": true, "format": "1"}}], "client": [{"model": '
                     '"publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": '
                     '"Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": '
                     '"1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": '
                     '"2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "4", '
                     '"days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": "Edital", '
                     '"extension_in": ".docx"}']}


@pytest.fixture
def payload_maranhao():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "4d090e91-2f91-47ed-b36a-b853cde26d93", '
        '"fields": {"name_section": "Terceiros - DOMA - MA", "newspaper_id": "250954bc-773f-47a9-864f-74c581e10e48", '
        '"width_1": "8.50", "width_2": "17.00", "width_3": "0.00", "width_4": "0.00", "width_5": "0.00", "width_6": '
        '"0.00", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", '
        '"height": "24.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 2, '
        '"font_name_alternative": 2, "font_size": "9.00", "font_leading": "9.00", "font_size_company": "9.00", '
        '"font_leading_company": "9.00", "tracking": "0", "condensation": "100.00", "format_out": ".rtf", "price_cm": '
        '"7.00", "price_cm_square": "7.00", "price_extra_color": "7.00", "bold": true, "italic": true, "underline": '
        'true, "edge": false, "height_round": true, "deadline_days": "2021-09-27", "deadline_hour": 17, '
        '"circulate_days": "2021-09-27", "create_at": "2021-09-27T12:15:31.635Z", "modify_at": '
        '"2021-10-15T21:35:12.956Z"}}], "publication_type": [{"model": "publisher.publicationtype", '
        '"pk": "b529b97b-ece9-4f46-841e-aef7d011876e", "fields": {"name": "92ed96d4-c5f1-41d1-8e7a-ca3d71220113", '
        '"newspaper_section_id": "4d090e91-2f91-47ed-b36a-b853cde26d93", "create_at": "2021-09-27T12:16:34.640Z", '
        '"modify_at": "2021-09-27T12:18:05.206Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
        '"font_name": 2, "font_size": "9.00", "font_leading": "9.00", "font_size_company": "9.00", '
        '"font_leading_company": "9.00", "bold": true, "italic": true, "underline": true, "tracking": "0", '
        '"condensation": "100.00", "special_format": true, "format": "2"}}], "client": [{"model": "publisher.client", '
        '"pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", '
        '"phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": '
        '"2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_2", "pv_os": "PV", '
        '"pvos_number": "4", "days": "1", "user_condensation": "80.00", "title": "pdf", "publication_type_name": '
        '"Sema", "extension_in": ".docx"}']}


@pytest.fixture
def a_gazeta_df():
    return {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                     '"b33c4403-94f5-40f5-9289-a56b916c465b", "fields": {"name_section": "Particulares - A Gazeta - '
                     'DF", "newspaper_id": "b150643c-c980-4a07-9ade-95898587e94c", "width_1": "3.00", "width_2": '
                     '"6.30", "width_3": "9.60", "width_4": "12.90", "width_5": "16.20", "width_6": "19.50", '
                     '"width_7": "22.80", "width_8": "26.10", "width_9": "0.00", "width_10": "0.00", '
                     '"gutter": "0.206", "height": "38.0", "minimum_height": "1.0", "maximum_height_budget": "38.0", '
                     '"font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", '
                     '"font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", "condensation": '
                     '"90.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": "150.00", '
                     '"price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, '
                     '"height_round": true, "deadline_days": "2021-10-27", "deadline_hour": 17, "circulate_days": '
                     '"2021-10-27", "create_at": "2021-10-27T15:10:29.125Z", "modify_at": '
                     '"2021-10-27T15:10:29.125Z"}}], "publication_type": [{"model": "publisher.publicationtype", '
                     '"pk": "bd7189ec-15ef-44d1-9026-7cef80781dc3", "fields": {"name": '
                     '"92ed96d4-c5f1-41d1-8e7a-ca3d71220113", "newspaper_section_id": '
                     '"b33c4403-94f5-40f5-9289-a56b916c465b", "create_at": "2021-10-27T15:11:06.556Z", "modify_at": '
                     '"2021-10-27T15:11:06.556Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, '
                     '"font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", '
                     '"font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": '
                     '"-10", "condensation": "90.00", "special_format": true, "format": "2"}}], "client": [{"model": '
                     '"publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": '
                     '"Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": '
                     '"1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": '
                     '"2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "444", '
                     '"days": "2", "user_condensation": "default", "title": "test", "publication_type_name": "Sema", '
                     '"extension_in": ".docx"}']}


@pytest.fixture
def a_gazeta_mt():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "8ba47d0f-7a9b-4f95-9d5d-3e5dfad72fcb", "fields": {"name_section": "Terceiros - A Gazeta - MT", "newspaper_id": "5d2590d3-d5ea-4157-ad17-d5336226ccef", "width_1": "4.60", "width_2": "9.60", "width_3": "14.60", "width_4": "19.60", "width_5": "24.60", "width_6": "29.60", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "52.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "5.00", "font_leading": "5.00", "font_size_company": "5.00", "font_leading_company": "5.00", "tracking": "0", "condensation": "87.00", "format_out": ".pdf", "price_cm": "11.66", "price_cm_square": "11.66", "price_extra_color": "11.66", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, "deadline_days": "2021-07-19", "deadline_hour": 1, "circulate_days": "2021-07-19", "create_at": "2021-07-19T00:32:19.129Z", "modify_at": "2021-10-11T14:45:24.255Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "d34df0dc-7ce2-4e51-93c2-44bbb82fe251", "fields": {"name": "4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": "8ba47d0f-7a9b-4f95-9d5d-3e5dfad72fcb", "create_at": "2021-07-19T00:35:04.597Z", "modify_at": "2021-09-27T13:09:26.091Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, "font_name": 1, "font_size": "4.50", "font_leading": "4.50", "font_size_company": "4.50", "font_leading_company": "4.50", "bold": true, "italic": true, "underline": true, "tracking": "-10", "condensation": "90.00", "special_format": false, "format": "1"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "444", "days": "2", "user_condensation": "default", "title": "test", "publication_type_name": "Edital", "extension_in": ".docx"}']}


@pytest.fixture
def valor_economico_rj():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "8e229728-e31b-47a9-9af0-e29099595a06", "fields": {"name_section": "Empresarial - Valor Econ\\u00f4mico - RJ", "newspaper_id": "d34851ae-b37d-499f-b8be-c25a5c180fc1", "width_1": "4.60", "width_2": "9.60", "width_3": "14.60", "width_4": "19.60", "width_5": "24.60", "width_6": "29.60", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "52.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "8.00", "font_leading": "8.00", "font_size_company": "8.00", "font_leading_company": "8.00", "tracking": "-10", "condensation": "90.00", "format_out": ".pdf", "price_cm": "41.40", "price_cm_square": "41.40", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, "deadline_days": "2021-07-26", "deadline_hour": 1, "circulate_days": "2021-07-26", "create_at": "2021-07-26T18:03:32.690Z", "modify_at": "2021-10-11T14:44:50.501Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "d2acbfda-5c5b-42b1-8b18-7082eda75b9a", "fields": {"name": "94d2b678-2e97-4a42-a490-c2026bec5166", "newspaper_section_id": "8e229728-e31b-47a9-9af0-e29099595a06", "create_at": "2021-09-27T12:01:35.894Z", "modify_at": "2021-09-27T12:01:35.894Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, "font_name": 1, "font_size": "8.00", "font_leading": "8.00", "font_size_company": "8.00", "font_leading_company": "8.00", "bold": true, "italic": true, "underline": true, "tracking": "-10", "condensation": "90.00", "special_format": true, "format": "0"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_3", "pv_os": "PV", "pvos_number": "2", "days": "1", "user_condensation": "default", "title": "test", "publication_type_name": "Ata", "extension_in": ".docx"}']}


@pytest.fixture
def o_progresso_ma():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "a935ed06-cfe4-4c14-b977-a4bbac0ce224", "fields": {"name_section": "Terceiros - O Progresso - MA", "newspaper_id": "31c4c36e-1137-4f4e-97b9-f92aeb2b8d71", "width_1": "4.50", "width_2": "9.50", "width_3": "14.50", "width_4": "19.50", "width_5": "24.50", "width_6": "29.50", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.500", "height": "42.0", "minimum_height": "1.0", "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", "condensation": "90.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": "150.00", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, "deadline_days": "2021-10-18", "deadline_hour": 16, "circulate_days": "2021-10-18", "create_at": "2021-10-18T00:05:31.290Z", "modify_at": "2021-10-18T00:05:31.290Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "8389fb18-6d32-46d2-bde5-eba9b6fa940c", "fields": {"name": "92ed96d4-c5f1-41d1-8e7a-ca3d71220113", "newspaper_section_id": "a935ed06-cfe4-4c14-b977-a4bbac0ce224", "create_at": "2021-10-18T00:07:07.242Z", "modify_at": "2021-10-29T21:09:22.415Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, "font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": "-10", "condensation": "90.00", "special_format": true, "format": "2"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "2", "days": "1", "user_condensation": "default", "title": "test", "publication_type_name": "Sema", "extension_in": ".docx"}']}


@pytest.fixture
def o_estado_ms():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "6c95759e-7cc7-4635-982f-b50788f88a49", "fields": {"name_section": "Classificados - O Estado - MS", "newspaper_id": "73045b8d-acf5-420a-8afe-557be80c0634", "width_1": "2.70", "width_2": "5.70", "width_3": "8.70", "width_4": "11.70", "width_5": "14.70", "width_6": "17.70", "width_7": "20.70", "width_8": "26.70", "width_9": "26.70", "width_10": "29.70", "gutter": "0.206", "height": "52.0", "minimum_height": "1.0", "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", "condensation": "90.00", "format_out": ".pdf", "price_cm": "32.46", "price_cm_square": "32.46", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, "deadline_days": "2021-10-20", "deadline_hour": 17, "circulate_days": "2021-10-20", "create_at": "2021-10-20T14:52:37.252Z", "modify_at": "2021-10-20T14:52:37.252Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "e0791c19-fcc1-4856-97d1-f52cda843ab8", "fields": {"name": "92ed96d4-c5f1-41d1-8e7a-ca3d71220113", "newspaper_section_id": "6c95759e-7cc7-4635-982f-b50788f88a49", "create_at": "2021-10-20T14:54:35.741Z", "modify_at": "2021-10-20T14:56:38.249Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, "font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": "-10", "condensation": "90.00", "special_format": true, "format": "2"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_1", "pv_os": "PV", "pvos_number": "2", "days": "1", "user_condensation": "default", "title": "test", "publication_type_name": "Sema", "extension_in": ".docx"}']}


@pytest.fixture
def o_dia_sp():
    return {'data': [
        '{"newspaper": [{"model": "publisher.newspapersection", "pk": "ff21193e-5751-45b4-840a-8bc5263f1dd8", "fields": {"name_section": "Notici\\u00e1rio - O Dia - SP", "newspaper_id": "3c1f2f0a-d17f-4e2e-9f4f-05a2a170929a", "width_1": "4.60", "width_2": "9.60", "width_3": "14.60", "width_4": "19.60", "width_5": "24.60", "width_6": "29.70", "width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", "gutter": "0.206", "height": "52.0", "minimum_height": null, "maximum_height_budget": null, "font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", "condensation": "90.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": "150.00", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, "edge": true, "height_round": true, "deadline_days": "2021-09-30", "deadline_hour": 14, "circulate_days": "2021-09-30", "create_at": "2021-09-30T18:47:06.373Z", "modify_at": "2021-10-11T13:21:26.010Z"}}], "publication_type": [{"model": "publisher.publicationtype", "pk": "7ecefdb8-6c0a-4a16-842c-ae6280a016ba", "fields": {"name": "4caaa63a-eb46-4e1f-951a-01843132b0a2", "newspaper_section_id": "ff21193e-5751-45b4-840a-8bc5263f1dd8", "create_at": "2021-09-30T18:48:14.728Z", "modify_at": "2021-09-30T18:48:14.728Z", "instructions": "", "margin": null, "estimated_budget_delivery": 1, "font_name": 1, "font_size": "6.00", "font_leading": "6.00", "font_size_company": "6.00", "font_leading_company": "6.00", "bold": true, "italic": true, "underline": true, "tracking": "-10", "condensation": "90.00", "special_format": true, "format": "1"}}], "client": [{"model": "publisher.client", "pk": "16357abe-b1f7-4f6d-a402-4e27c076bbd8", "fields": {"name": "Atus-Teste", "email": "teste@atus.com.br", "phone": "1133333333", "phone_secondary": "1144444444", "cellphone": "11999999999", "create_at": "2021-07-06T21:47:43.293Z", "modify_at": "2021-07-06T21:47:43.293Z"}}], "column": "width_2", "pv_os": "PV", "pvos_number": "2", "days": "1", "user_condensation": "default", "title": "test", "publication_type_name": "Edital", "extension_in": ".docx"}']}
