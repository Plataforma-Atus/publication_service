# Budget starter | Collect essential info
def budget(result, format_parameters):
    result['newspaper'] = format_parameters['name_section']
    result['price_cm'] = float(format_parameters['price_cm'])
    result['width'] = float(format_parameters['column'])
    return result, format_parameters

# Calculate price by cm * height * columns
def budget_cm(result, format_parameters):
    result['price'] = "{:.2f}".format((float(format_parameters['price_cm']) * float(result['height'])) * float(format_parameters['column']))
    print("R$",result['price']," cm/col")
    return result, format_parameters

# Calculate price by characters * chars
def budget_char(result, format_parameters):
    result['price'] = "{:.2f}".format((float(format_parameters['price_cm']) * float(format_parameters['chars_count'])))
    print("R$",result['price']," char")
    return result, format_parameters

# Calculate price by square cm
def budget_cm_square(result, format_parameters):
    result_cm_2 = float(result['height']) * float(result['width'])
    result['price_by_cm'] = "{:.2f}".format((float(result['price'])) / float(result_cm_2))
    print("R$ ",result['price_by_cm'], " cm_square")
    return result, format_parameters
