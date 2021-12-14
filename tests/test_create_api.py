from django.urls import reverse

from publisher.commute.driver import format_parameter


def test_create_api(client):
    url = reverse("create_publication")
    payload = {'data': ['{"newspaper": [{"model": "publisher.newspapersection", "pk": '
                        '"d8bd0bc1-4587-4996-9da3-c7b4730fe7f7", "fields": {"name_section": "Legal - A Tarde - BA", '
                        '"newspaper_id": "b84843d2-353c-4543-b913-b038ef66a5eb", "width_1": "4.30", "width_2": '
                        '"9.20", "width_3": "14.00", "width_4": "18.80", "width_5": "23.60", "width_6": "28.50", '
                        '"width_7": "0.00", "width_8": "0.00", "width_9": "0.00", "width_10": "0.00", '
                        '"gutter": "0.206", "height": "52.0", "minimum_height": null, "maximum_height_budget": null, '
                        '"font_name": 1, "font_name_alternative": 1, "font_size": "6.00", "font_leading": "6.00", '
                        '"font_size_company": "6.00", "font_leading_company": "6.00", "tracking": "-10", '
                        '"condensation": "90.00", "format_out": ".pdf", "price_cm": "150.00", "price_cm_square": '
                        '"150.00", "price_extra_color": "150.00", "bold": true, "italic": true, "underline": true, '
                        '"edge": true, "height_round": true, "deadline_days": "2021-10-13", "deadline_hour": 17, '
                        '"circulate_days": "2021-10-13", "create_at": "2021-10-13T12:51:43.506Z", "modify_at": '
                        '"2021-10-13T13:23:40.805Z"}}], "publication_type": [{"model": "publisher.publicationtype", '
                        '"pk": "50347dfc-bd32-4bbc-a8e0-b61663fdfc7f", "fields": {"name": '
                        '"92ed96d4-c5f1-41d1-8e7a-ca3d71220113", "newspaper_section_id": '
                        '"d8bd0bc1-4587-4996-9da3-c7b4730fe7f7", "create_at": "2021-10-13T13:09:30.786Z", '
                        '"modify_at": "2021-10-13T13:24:16.590Z", "instructions": "", "margin": null, '
                        '"estimated_budget_delivery": 1, "font_name": 1, "font_size": "6.00", "font_leading": "6.00", '
                        '"font_size_company": "6.00", "font_leading_company": "6.00", "bold": true, "italic": true, '
                        '"underline": true, "tracking": "-10", "condensation": "90.00", "special_format": true, '
                        '"format": "2"}}], "client": [{"model": "publisher.client", '
                        '"pk": "d1cf4ecd-bf96-42ce-ab29-2238e22677a8", "fields": {"name": '
                        '"Atus-Produ\\u00e7\\u00e3o", "email": "felipe.francisco@atus.com.br", "phone": "1199999999", '
                        '"phone_secondary": "1199999998", "cellphone": "11999999997", "create_at": '
                        '"2021-10-11T22:12:34.558Z", "modify_at": "2021-10-11T22:12:34.558Z"}}], "column": "width_3", '
                        '"pv_os": "PV", "pvos_number": "2", "days": "1", "user_condensation": "80.00", '
                        '"title": "fdfdfdfdf", "publication_type_name": "Sema", "extension_in": ".docx"}']}
    response = client.post(url, data=payload)


def test_create_publication_bad_request(client):
    url = reverse("create_publication")
    response = client.get(url)
    assert response.status_code == 405


def test_post_not_found(client):
    payload = {
        "newspaper": "test",
        "newspaper_name": "test1",
        "publication_type": "test3",
        "publication_type_name":
            "testando",
        "pv_os": "1.2",
        "pvos_number": "123",
        "title": "titulo",
        "days": "1",
        "number_column": "234",
        "extension_in": "pdf",
        "user_condensation": "sim",
        "client": "victorhugo"
    }
    url = reverse("create_publication")
    response = client.get(url, payload)
    assert response.status_code == 405


def test_format_parameter(document_name_cropper, newspaper, publication_type, column, number_column, days,
                          user_condensation, just_name, extension_in):

    payload_format = format_parameter(document_name=document_name_cropper, extension_in=extension_in,
                                      newspaper=newspaper, publication_type=publication_type,
                                      column=column, number_column=number_column, days=days,
                                      user_condensation=user_condensation, just_name=just_name)

    assert payload_format
