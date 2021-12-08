from publisher.commute.budgeter import (calculate_budget_by_centimeter,
                                        calculate_budget_by_character,
                                        calculate_price_by_centimeter_square,
                                        make_budget)


def test_calculate_budget_by_centimeter(result, format_parameters):
    response = calculate_budget_by_centimeter(result, format_parameters)
    response = float(response[1]['price_cm']) * float(response[1]['height']) * float(
        response[1]['number_column'])
    assert response == 31200.0


def test_make_budget(result, format_parameters):
    response = make_budget(result, format_parameters)
    response_newspaper = response[1]['name_section']
    response_price_cm = response[0]['price_cm']
    response_width = response[1]['column']
    assert response_width == 11.7
    assert response_price_cm == 150.0
    assert response_newspaper == 'Classificados - A Gazeta - SP'


def test_calculate_budget_by_character(result, format_parameters):
    response = calculate_budget_by_character(result, format_parameters)
    result_price = float(response[1]['price_cm']) * float(response[1]['chars_count'])
    assert result_price


def test_calculate_price_by_centimeter_square(result, format_parameters):
    response = calculate_price_by_centimeter_square(result, format_parameters)
    response = float(response[0]['price']) / float(response[0]['height']) * float(response[0]['width'])
    assert response == 7020.0


