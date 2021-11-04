from django.urls import reverse
import requests
from django.test import Client
from http import HTTPStatus

import pytest


def test_create_publication_api():
    url = 'http://192.168.48.3:8003/create_publication/'
    payload = {
        "document_name": "documents/Atus-Produção/2021/PV-3/11-4/PV-3_ATarde-BA_TESTANDO_Sema_1_2xheight",
        "just_name": "Atus-Produção/2021/PV-3/11-4/PV-3_ATarde-BA_TESTANDO_Sema_1_2xheight",
        "extension_in": ".docx",
        "extension_out": ".pdf",
        "format_out": ".pdf",
        "publication_type": {
            "name": "92ed96d4-c5f1-41d1-8e7a-ca3d71220113",
            "newspaper_section_id": "d8bd0bc1-4587-4996-9da3-c7b4730fe7f7",
            "create_at": "2021-10-13T13:09:30.786Z",
            "modify_at": "2021-10-13T13:24:16.590Z",
            "instructions": "",
            "margin": "None",
            "estimated_budget_delivery": 1,
            "font_name": 1,
            "font_size": "6.00",
            "font_leading": "6.00",
            "font_size_company": "6.00",
            "font_leading_company": "6.00",
            "bold": True,
            "italic": True,
            "underline": True,
            "tracking": "-10",
            "condensation": "90.00",
            "special_format": True,
            "format": "2"
        },
        "price_cm": 150.0,
        "name_section": "Legal - A Tarde - BA",
        "column": 9.2,
        "number_column": "2",
        "height": 52.0,
        "height_round": True,
        "format_allowed": "2",
        "days": "1",
        "user_condensation": "default",
        "condensation": "90.00",
        "edge": True,
        "bold": True,
        "italic": True,
        "underline": True,
        "font_index": 1,
        "font_size": 6.0,
        "font_size_company": 6.0,
        "font_leading": 6.0,
        "font_leading_company": 6.0,
        "font_name": "Arial"
    }
    response = requests.post(url, data=payload)


def test_create_publication_bad_request():
    url = 'http://192.168.48.3:8003/create_publication/'

    resp = requests.get(url)
    assert resp.status_code == 500


def test_post_not_found():
    url = 'http://192.168.48.3:8003/create_publications/'

    response = requests.get(url)
    assert response.status_code == 404

