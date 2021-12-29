import requests


def test_create_docx(payload):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-2/12-27/PV-2_BrasíliaAgora-DF_QWEQWEQW_Sema_2_3x70mm',
                        'width': '14.60', 'height': '7.00', 'price': '3150.00', 'price_by_cm': '30.82',
                        'newspaper': 'Particulares - Brasília Agora - DF', 'chars_count': 4875, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_diario_cuiaba(payload_diario_de_cuiba):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_diario_de_cuiba, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DC-MT_PDF_Edital_1_2x110mm', 'width': '5.60',
                        'height': '11.00', 'price': '3300.00', 'price_by_cm': '53.57',
                        'newspaper': 'Terceiros - DC - MT', 'chars_count': 4845, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_folha_sp(payload_folha_sp):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_folha_sp, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_Folha-SP_PDF_Sema_1_1x190mm',
                        'width': '4.60',
                        'height': '19.00', 'price': '19.00', 'price_by_cm': '0.22',
                        'newspaper': 'Empresarial - Folha - SP',
                        'chars_count': 4875, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_mato_grosso(payload_mato_grosso):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_mato_grosso, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DOMT-MT_PDF_Edital_1_1x161mm',
                        'width': '9.40', 'height': '16.15', 'price': '145.35', 'price_by_cm': '0.96',
                        'newspaper': 'Terceiros - DOMT - MT', 'chars_count': 4836, 'format_out': '.docx'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_ro(payload_ro):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_ro, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DORO-RO_PDF_Edital_1_1x200mm',
                        'width': '9.00',
                        'height': '20.00', 'price': '870.48', 'price_by_cm': '4.84',
                        'newspaper': 'Terceiros - DORO - RO',
                        'chars_count': 4836, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_parana(payload_parana):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_parana, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DOPR-PR_PDF_Ata_1_1x150mm', 'width': '8.01',
                        'height': '15.00', 'price': '450.00', 'price_by_cm': '3.75',
                        'newspaper': 'Comércio, Indústria e Serviços - DOPR - PR', 'chars_count': 4725,
                        'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_pernambuco(payload_pe):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_pe, files=files)
    expected_payload = {
        'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DiáriodePernambuco-PE_PDF_Sema_1_2x130mm',
        'width': '6.27', 'height': '13.00', 'price': '3900.00', 'price_by_cm': '47.85',
        'newspaper': 'Classificados - Diário de Pernambuco - PE', 'chars_count': 4875,
        'format_out': '.pdf'
    }

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_df(payload_df):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_df, files=files)
    expected_payload = {
        'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_BrasíliaAgora-DF_PDF_Edital_1_1x190mm',
        'width': '4.60', 'height': '19.00', 'price': '2850.00', 'price_by_cm': '32.61',
        'newspaper': 'Particulares - Brasília Agora - DF', 'chars_count': 4836, 'format_out': '.pdf'
    }

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_minas_gerais(payload_minas_gerais):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_minas_gerais, files=files)
    expected_payload = {
        'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DOMG-MG_PDF_Edital_1_2x60mm',
        'width': '12.49', 'height': '6.00', 'price': '1075.08', 'price_by_cm': '14.35',
        'newspaper': 'Particulares - DOMG - MG', 'chars_count': 4836, 'format_out': '.rtf'
    }

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_amazonas(payload_amazonas):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_amazonas, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DOAM-AM_PDF_Edital_1_1x190mm',
                        'width': '9.49', 'height': '19.00', 'price': '1482.00', 'price_by_cm': '8.22',
                        'newspaper': 'Particulares - DOAM - AM', 'chars_count': 4836, 'format_out': '.docx'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_create_maranhao(payload_maranhao):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=payload_maranhao, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-4/12-27/PV-4_DOMA-MA_PDF_Sema_1_2x100mm',
                        'width': '17.00', 'height': '10.00', 'price': '140.00', 'price_by_cm': '0.82',
                        'newspaper': 'Terceiros - DOMA - MA', 'chars_count': 4875, 'format_out': '.rtf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_a_gazeta_df(a_gazeta_df):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=a_gazeta_df, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-444/12-27/PV-444_AGazeta-DF_TEST_Sema_2_1x340mm',
                        'width': '3.00', 'height': '34.00', 'price': '5100.00', 'price_by_cm': '50.00',
                        'newspaper': 'Particulares - A Gazeta - DF', 'chars_count': 4875, 'format_out': '.pdf'}
    assert response.json() == expected_payload
    assert response.status_code == 200


def test_a_gazeta_mt(a_gazeta_mt):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}

    response = requests.post(url, data=a_gazeta_mt, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-444/12-27/PV-444_AGazeta-MT_TEST_Edital_2_1x145mm',
                        'width': '4.60', 'height': '14.50', 'price': '169.07', 'price_by_cm': '2.53',
                        'newspaper': 'Terceiros - A Gazeta - MT', 'chars_count': 4836, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_valor_economico_rj(valor_economico_rj):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}
    response = requests.post(url, data=valor_economico_rj, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-2/12-27/PV-2_ValorEconômico-RJ_TEST_Ata_1_3x120mm',
                        'width': '14.60', 'height': '12.00', 'price': '1490.40', 'price_by_cm': '8.51',
                        'newspaper': 'Empresarial - Valor Econômico - RJ', 'chars_count': 4725, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_o_progresso_ma(o_progresso_ma):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}
    response = requests.post(url, data=o_progresso_ma, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-2/12-27/PV-2_OProgresso-MA_TEST_Sema_1_1x220mm',
                        'width': '4.50', 'height': '22.00', 'price': '3300.00', 'price_by_cm': '33.33',
                        'newspaper': 'Terceiros - O Progresso - MA', 'chars_count': 4875, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_o_estado_ms(o_estado_ms):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}
    response = requests.post(url, data=o_estado_ms, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-2/12-27/PV-2_OEstado-MS_TEST_Sema_1_1x380mm',
                        'width': '2.69', 'height': '38.00', 'price': '1233.48', 'price_by_cm': '12.07',
                        'newspaper': 'Classificados - O Estado - MS', 'chars_count': 4875, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200


def test_o_dia_sp(o_dia_sp):
    url = 'http://localhost:8003/create_publication'

    file = 'tests/PV-7543.docx'

    files = {'file': open(file, 'rb')}
    response = requests.post(url, data=o_dia_sp, files=files)
    expected_payload = {'file': 'documents/Atus-Teste/2021/PV-2/12-27/PV-2_ODia-SP_TEST_Edital_1_2x100mm',
                        'width': '9.60', 'height': '10.00', 'price': '3000.00', 'price_by_cm': '31.25',
                        'newspaper': 'Noticiário - O Dia - SP', 'chars_count': 4836, 'format_out': '.pdf'}

    assert response.json() == expected_payload
    assert response.status_code == 200
