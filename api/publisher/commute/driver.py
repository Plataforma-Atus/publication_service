from publisher.commute import commuter, cropper, standarder, fstring, budgeter

# Estimate automatic budget
def to_budget(result, format_parameters):

    if format_parameters['name_section'] == "Terceiros - DORO - RO":
        budgeter.budget_char(result, format_parameters)
        budgeter.budget_cm_square(result, format_parameters)
    else:
        budgeter.budget_cm(result, format_parameters)
        budgeter.budget_cm_square(result, format_parameters)
    result['newspaper'] = format_parameters['name_section']
    result['chars_count'] = format_parameters['chars_count']

    return result

# Auto crop all pages
def to_crop(format_parameters):
    if format_parameters['format_out'] == fstring.formats["commute"][1] \
            or format_parameters['format_out'] == fstring.formats["commute"][4]:
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                          extension_out=fstring.formats["commute"][4])
        result = cropper.auto_crop_pdf(format_parameters)
        to_budget(result, format_parameters)
        return result

    elif format_parameters['format_out'] == fstring.formats["commute"][3]:
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                          extension_out=fstring.formats["commute"][3])
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][3],
                          extension_out=fstring.formats["commute"][4])
        result = cropper.auto_crop_pdf(format_parameters)
        to_budget(result, format_parameters)
        return result


    elif format_parameters['format_out'] == fstring.formats["commute"][2]:
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                          extension_out=fstring.formats["commute"][2])
        commuter.commuter(format_parameters['document_name'], extension_in=fstring.formats["commute"][2],
                          extension_out=fstring.formats["commute"][4])
        result = cropper.auto_crop_pdf(format_parameters)
        to_budget(result, format_parameters)
        return result

    else:
        print(fstring.message["exception"]['format'])

# Standard the document to newspaper section defaults
def to_default(format_parameters):
    # Just for now
    try:
        format_parameters['chars_count'] = standarder.doc_default(format_parameters)
        return to_crop(format_parameters)

    except Exception as unknown_error:
        print(format_parameters['document_name'])
        print(f"Description: {unknown_error}", "- driver.to_default")
        return

# Driver file to final format
def driver(format_parameters):

    if format_parameters['extension_in'] == fstring.formats["commute"][1]:
        print(fstring.message["info"]['conversion_not'])
        result = to_default(format_parameters)
    elif format_parameters['extension_in'] == fstring.formats["commute"][2] \
            or format_parameters['extension_in'] == fstring.formats["commute"][3] \
            or format_parameters['extension_in'] == fstring.formats["commute"][4] \
            or format_parameters['extension_in'] == fstring.formats["commute"][5]\
            or format_parameters['extension_in'] == fstring.formats["commute"][6]:

        commuter.commuter(format_parameters['document_name'],
                          format_parameters['extension_in'],
                          fstring.formats["commute"][1])
        result = to_default(format_parameters)

        if format_parameters['extension_in'] != fstring.formats["commute"][1]:
            commuter.commuter(format_parameters['document_name'],
                              fstring.formats["commute"][1],
                              format_parameters['extension_out'])

    else:
        print(fstring.message["exception"]['format_allowed'],"- driver.driver")

    print(result, " - result for driver")
    return result

# Define args
def format_parameter(document_name, extension_in, newspaper, publication_type,
                     column, number_column, days, user_condensation, just_name):
    format_parameters = {
        # File info
        'document_name':str(document_name),
        'just_name':str(just_name),
        'extension_in':str(extension_in),
        'extension_out':str(newspaper['format_out']),
        'format_out':str(newspaper['format_out']),
        # Newspaper info
        'publication_type':publication_type,
        'price_cm':float(newspaper['price_cm']),
        'name_section': str(newspaper['name_section']),
        'column':float(column),
        'number_column':number_column,
        'height':float(newspaper['height']),
        'height_round':bool(newspaper['height_round']),
        'format_allowed':str(publication_type['format']),
        #Publication info
        'days':str(days),
        'user_condensation':str(user_condensation),
        'condensation':str(publication_type['condensation']),
        'edge':bool(newspaper['edge']),
        'bold':bool(publication_type['bold']),
        'italic':bool(publication_type['italic']),
        'underline':bool(publication_type['underline']),
        # Font info
        'font_index':int(newspaper['font_name']),
        'font_size':float(newspaper['font_size']),
        'font_size_company':float(newspaper['font_size_company']),
        'font_leading':float(newspaper['font_leading']),
        'font_leading_company':float(newspaper['font_leading_company']),
    }

    # Condensation definer
    if format_parameters['user_condensation'] != 'default':
        format_parameters['condensation'] = format_parameters['user_condensation']

    # Font definer
    format_parameters['font_name'] = str(fstring.formats['font'][format_parameters['font_index']])

    print(format_parameters)
    return format_parameters
