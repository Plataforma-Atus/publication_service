import pytest

from publisher.commute.budgeter import calculate_budget_by_centimeter


@pytest.fixture
def result():
    return {'file': 'documents/Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight_crp', 'width': '11.70',
            'height': '9.00', 'price': '5400.00'}


@pytest.fixture
def format_parameters():
   return {'document_name': 'documents/Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight', 'just_name': 'Atus-Teste/2021/PV-2/12-7/PV-2_AGazeta-SP_TESTANDO_Ata_2_4xheight', 'extension_in': '.docx', 'extension_out': '.pdf', 'format_out': '.pdf', 'publication_type': {'name': '94d2b678-2e97-4a42-a490-c2026bec5166', 'newspaper_section_id': 'c83ff6c4-909a-4193-bd3b-6f3ac3e21e6d', 'create_at': '2021-10-25T12:45:56.558Z', 'modify_at': '2021-10-25T12:45:56.559Z', 'instructions': '', 'margin': None, 'estimated_budget_delivery': 1, 'font_name': 1, 'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00', 'font_leading_company': '6.00', 'bold': True, 'italic': True, 'underline': True, 'tracking': '-10', 'condensation': '90.00', 'special_format': True, 'format': '0', 'format_type': 'Ata'}, 'price_cm': 150.0, 'name_section': 'Classificados - A Gazeta - SP', 'column': 11.7, 'number_column': '4', 'height': 52.0, 'height_round': True, 'format_allowed': '0', 'days': '2', 'user_condensation': 'default', 'condensation': '90.00', 'edge': True, 'bold': True, 'italic': True, 'underline': True, 'font_index': 1, 'font_size': 6.0, 'font_size_company': 6.0, 'font_leading': 6.0, 'font_leading_company': 6.0, 'font_name': 'Arial', 'document': '<docx.document.Document object at 0x7f64e853a980>', 'docx_default': '<docx.document.Document object at 0x7f64e0bab340>', 'text_index': 0, 'initial_paragraph': '<docx.text.paragraph.Paragraph object at 0x7f64e1491a90>', 'texts_flowing': '<docx.text.paragraph.Paragraph object at 0x7f64e141a8b0>', 'paragraph': '<docx.text.paragraph.Paragraph object at 0x7f64e144b9d0>', 'texts': '<docx.text.run.Run object at 0x7f64e0b526a0>', 'chars_count': 4725}


@pytest.fixture
def calculate_budget():
    return calculate_budget_by_centimeter(result, format_parameters)

