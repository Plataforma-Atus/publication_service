def make_budget(result, format_parameters):
    result['newspaper'] = format_parameters['name_section']
    result['price_cm'] = float(format_parameters['price_cm'])
    result['width'] = float(format_parameters['column'])
    return result, format_parameters


def calculate_budget_by_centimeter(result, format_parameters):
    result['price'] = "{:.2f}".format(
        (float(format_parameters['price_cm']) * float(result['height'])) * float(format_parameters['number_column']))
    print("R$", result['price'], " cm/col")
    return result, format_parameters


def calculate_budget_by_character(result, format_parameters):
    result['price'] = "{:.2f}".format((float(format_parameters['price_cm']) * float(format_parameters['chars_count'])))
    print("R$", result['price'], " char")
    return result, format_parameters


def calculate_price_by_centimeter_square(result, format_parameters):
    result['price_by_cm'] = "{:.2f}".format(
        (float(result['price'])) / (float(result['height']) * float(result['width'])))
    print("R$ ", result['price_by_cm'], " cm_square")
    return result, format_parameters


