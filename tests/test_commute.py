from publisher.commute.driver import checking_input_extension, manipulate_docx, manipulate_pdf


def test_driver():
    format_parameters = {
        'document_name': 'documents/Atus-Produção/2021/PV-3/11-30/PV-3_A Tarde-BA_TESTANDO_Sema_2_1xheight',
        'just_name': 'Atus-Produção/2021/PV-3/11-30/PV-3_A Tarde-BA_TESTANDO_Sema_2_1xheight', 'extension_in': '.docx',
        'extension_out': '.pdf', 'format_out': '.pdf',
        'publication_type': {'name': '92ed96d4-c5f1-41d1-8e7a-ca3d71220113',
                             'newspaper_section_id': 'd8bd0bc1-4587-4996-9da3-c7b4730fe7f7',
                             'create_at': '2021-10-13T13:09:30.786Z', 'modify_at': '2021-10-13T13:24:16.590Z',
                             'instructions': '', 'margin': None, 'estimated_budget_delivery': 1, 'font_name': 1,
                             'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00',
                             'font_leading_company': '6.00', 'bold': True, 'italic': True, 'underline': True,
                             'tracking': '-10', 'condensation': '90.00', 'special_format': True, 'format': '2'},
        'price_cm': 150.0, 'name_section': 'Legal - A Tarde - BA', 'column': 4.3, 'number_column': '1', 'height': 52.0,
        'height_round': True, 'format_allowed': '2', 'days': '2', 'user_condensation': '87.00', 'condensation': '87.00',
        'edge': True, 'bold': True, 'italic': True, 'underline': True, 'font_index': 1, 'font_size': 6.0,
        'font_size_company': 6.0, 'font_leading': 6.0, 'font_leading_company': 6.0, 'font_name': 'Arial'}

    payload_driver = checking_input_extension(format_parameters)


def test_to_default():
    format_parameters = {
        'document_name': 'documents/Atus-Produção/2021/PV-3/11-30/PV-3_A Tarde-BA_TESTANDO_Sema_2_1xheight',
        'just_name': 'Atus-Produção/2021/PV-3/11-30/PV-3_A Tarde-BA_TESTANDO_Sema_2_1xheight',
        'extension_in': '.docx', 'extension_out': '.pdf', 'format_out': '.pdf',
        'publication_type': {'name': '92ed96d4-c5f1-41d1-8e7a-ca3d71220113',
                             'newspaper_section_id': 'd8bd0bc1-4587-4996-9da3-c7b4730fe7f7',
                             'create_at': '2021-10-13T13:09:30.786Z', 'modify_at': '2021-10-13T13:24:16.590Z',
                             'instructions': '', 'margin': None, 'estimated_budget_delivery': 1, 'font_name': 1,
                             'font_size': '6.00', 'font_leading': '6.00', 'font_size_company': '6.00',
                             'font_leading_company': '6.00', 'bold': True, 'italic': True, 'underline': True,
                             'tracking': '-10', 'condensation': '90.00', 'special_format': True, 'format': '2'},
        'price_cm': 150.0, 'name_section': 'Legal - A Tarde - BA', 'column': 4.3, 'number_column': '1', 'height': 52.0,
        'height_round': True, 'format_allowed': '2', 'days': '2', 'user_condensation': '87.00', 'condensation': '87.00',
        'edge': True, 'bold': True, 'italic': True, 'underline': True, 'font_index': 1, 'font_size': 6.0,
        'font_size_company': 6.0, 'font_leading': 6.0, 'font_leading_company': 6.0, 'font_name': 'Arial'}

    default_payload = manipulate_docx(format_parameters)

