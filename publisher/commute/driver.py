from os import remove, rename, system

from publisher.commute import budgeter, commuter, cropper, fstring, standarder


def rename_files(result, format_parameters):
    name_with_height = str("{:.1f}".format(float(result['height'])))
    document_name_with_height = result['file'].replace("height",
                                                       name_with_height.replace(".", ""))
    document_name_with_height = document_name_with_height.replace("_crp", "mm")
    rename(f"{result['file']}.pdf",
           f"{document_name_with_height}.pdf")
    rename(f"{result['file']}.jpeg",
           f"{document_name_with_height}.jpeg")
    rename(f"{result['file'].replace('_crp', '')}.docx",
           f"{document_name_with_height}.docx")
    print("--------------------------------------------------------------------")
    if format_parameters['extension_out'] != ".docx" \
            and format_parameters['extension_out'] != ".pdf":
        rename(f"{result['file'].replace('_crp', '')}{format_parameters['extension_out']}",
               f"{document_name_with_height}{format_parameters['extension_out']}")
    if format_parameters['extension_in'] != ".docx" \
            and format_parameters['extension_in'] != ".pdf" \
            and format_parameters['extension_in'] != format_parameters['extension_out']:
        rename(f"{result['file'].replace('_crp', '')}{format_parameters['extension_in']}",
               f"{document_name_with_height}{format_parameters['extension_in']}")
    result['file'] = document_name_with_height.replace('_crp', '')
    print(document_name_with_height)
    format_parameters['document_name_with_height'] = document_name_with_height
    cropper.convert_pdf_to_greyscale(format_parameters)
    return result


def calculate_budget(result, format_parameters):
    if format_parameters['name_section'] in fstring.newspapers['budget_by_character']:
        budgeter.calculate_budget_by_character(result, format_parameters)
        budgeter.calculate_price_by_centimeter_square(result, format_parameters)
    else:
        budgeter.calculate_budget_by_centimeter(result, format_parameters)
        budgeter.calculate_price_by_centimeter_square(result, format_parameters)
    result['newspaper'] = format_parameters['name_section']
    result['chars_count'] = format_parameters['chars_count']

    return rename_files(result, format_parameters)


def manipulate_pdf(format_parameters):
    if format_parameters['format_out'] == fstring.formats["commute"][1] \
            or format_parameters['format_out'] == fstring.formats["commute"][4]:
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                          extension_out=fstring.formats["commute"][4])
        result = cropper.auto_crop_pdf(format_parameters)
        return calculate_budget(result, format_parameters)

    elif format_parameters['format_out'] == fstring.formats["commute"][3]:
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                          extension_out=fstring.formats["commute"][3])
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][3],
                          extension_out=fstring.formats["commute"][4])
        result = cropper.auto_crop_pdf(format_parameters)
        return calculate_budget(result, format_parameters)


    elif format_parameters['format_out'] == fstring.formats["commute"][2]:
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                          extension_out=fstring.formats["commute"][2])
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][2],
                          extension_out=fstring.formats["commute"][4])
        result = cropper.auto_crop_pdf(format_parameters)
        return calculate_budget(result, format_parameters)

    else:
        print(fstring.message["exception"]['format'])


def manipulate_docx(format_parameters):
    # Just for now
    try:
        format_parameters['chars_count'] = standarder.standardizer_docx(format_parameters)
        return manipulate_pdf(format_parameters)

    except Exception as unknown_error:
        print(format_parameters['document_name'])
        print(f"Description: {unknown_error}", "- driver.to_default")
        return


def road_map(format_parameters):
    if format_parameters['extension_in'] == fstring.formats["commute"][1]:
        print(fstring.message["info"]['conversion_not'])
        result = manipulate_docx(format_parameters)
    elif format_parameters['extension_in'] == fstring.formats["commute"][2] \
            or format_parameters['extension_in'] == fstring.formats["commute"][3] \
            or format_parameters['extension_in'] == fstring.formats["commute"][4] \
            or format_parameters['extension_in'] == fstring.formats["commute"][5] \
            or format_parameters['extension_in'] == fstring.formats["commute"][6]:

        commuter.commuter(format_parameters['document_name'],
                          format_parameters['extension_in'],
                          fstring.formats["commute"][1])
        result = manipulate_docx(format_parameters)

        if format_parameters['extension_in'] != fstring.formats["commute"][1]:
            commuter.commuter(format_parameters['document_name'],
                              fstring.formats["commute"][1],
                              format_parameters['extension_out'])

    else:
        print(fstring.message["exception"]['format_allowed'], "- driver.driver")

    print(result, " - result for driver")

    return result


def format_parameter(document_name, extension_in, newspaper, publication_type,
                     column, number_column, days, user_condensation, just_name):
    format_parameters = {
        # File info
        'document_name': str(document_name),
        'just_name': str(just_name),
        'extension_in': str(extension_in),
        'extension_out': str(newspaper['format_out']),
        'format_out': str(newspaper['format_out']),
        # Newspaper info
        'publication_type': publication_type,
        'price_cm': float(newspaper['price_cm']),
        'name_section': str(newspaper['name_section']),
        'column': float(column),
        'number_column': number_column,
        'height': float(newspaper['height']),
        'height_round': bool(newspaper['height_round']),
        'format_allowed': str(publication_type['format']),
        # Publication info
        'days': str(days),
        'user_condensation': str(user_condensation),
        'condensation': str(publication_type['condensation']),
        'edge': bool(newspaper['edge']),
        'bold': bool(publication_type['bold']),
        'italic': bool(publication_type['italic']),
        'underline': bool(publication_type['underline']),
        # Font info
        'font_index': int(newspaper['font_name']),
        'font_size': float(newspaper['font_size']),
        'font_size_company': float(newspaper['font_size_company']),
        'font_leading': float(newspaper['font_leading']),
        'font_leading_company': float(newspaper['font_leading_company']),
    }

    # Condensation definer
    if format_parameters[
        'user_condensation'] != 'default':  # and format_parameters['user_condensation'] => format_parameters['condensation_minimum']:
        format_parameters['condensation'] = format_parameters['user_condensation']

    # Font definer
    format_parameters['font_name'] = str(fstring.formats['font'][format_parameters['font_index']])

    print(format_parameters)
    return format_parameters
