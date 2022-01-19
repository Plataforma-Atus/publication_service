import logging
from os import rename

from publisher.commute import fstring, standarder

from publisher.commute.cropper import DocumentAdjustments

from publisher.commute.commuter import ConvertingFile

from publisher.commute.budgeter import Budget

logging.basicConfig(level=logging.INFO)


def rename_files(result, format_parameters):
    name_with_height: str = str("{:.1f}".format(float(result['height'])))
    document_name_with_height = result['file'].replace(
        "height",
        name_with_height.replace(".", "")
    )
    document_name_with_height = document_name_with_height.replace("_crp", "mm")
    rename(f"{result['file']}.pdf",
           f"{document_name_with_height}.pdf")
    rename(f"{result['file']}.jpeg",
           f"{document_name_with_height}.jpeg")
    rename(f"{result['file'].replace('_crp', '')}.docx",
           f"{document_name_with_height}.docx")

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
    logging.info(document_name_with_height)
    format_parameters['document_name_with_height'] = document_name_with_height
    DocumentAdjustments.convert_pdf_to_greyscale(format_parameters)
    return result


def calculate_budget(result, format_parameters):
    if format_parameters['name_section'] in fstring.newspapers['budget_by_character']:
        Budget.calculate_budget_by_character(result, format_parameters)
        Budget.calculate_price_by_centimeter_square(result, format_parameters)
    else:
        Budget.calculate_budget_by_centimeter(result, format_parameters)
        Budget.calculate_price_by_centimeter_square(result, format_parameters)
    result['newspaper'] = format_parameters['name_section']
    result['chars_count'] = format_parameters['chars_count']

    return rename_files(result, format_parameters)


class Manipulation:

    @staticmethod
    def pdf(format_parameters: dict):
        if any(map(lambda x: format_parameters['format_out'] == x, (fstring.formats['commute'][i] for i in [1, 4]))):
            ConvertingFile.commuter(
                format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                extension_out=fstring.formats["commute"][4]
            )
            result = DocumentAdjustments.auto_crop_pdf(format_parameters)
            return calculate_budget(result, format_parameters)

        elif format_parameters['format_out'] == fstring.formats["commute"][3]:
            ConvertingFile.commuter(
                format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                extension_out=fstring.formats["commute"][3]
            )
            ConvertingFile.commuter(
                format_parameters['document_name'], extension_in=fstring.formats["commute"][3],
                extension_out=fstring.formats["commute"][4]
            )
            result = DocumentAdjustments.auto_crop_pdf(format_parameters)
            return calculate_budget(result, format_parameters)

        elif format_parameters['format_out'] == fstring.formats["commute"][2]:
            ConvertingFile.commuter(
                format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                extension_out=fstring.formats["commute"][2]
            )
            ConvertingFile.commuter(
                format_parameters['document_name'], extension_in=fstring.formats["commute"][2],
                extension_out=fstring.formats["commute"][4]
            )
            result = DocumentAdjustments.auto_crop_pdf(format_parameters)
            return calculate_budget(result, format_parameters)

        else:
            logging.info(fstring.message["exception"]['format'])

    @staticmethod
    def docx(format_parameters: dict):
        try:
            format_parameters['chars_count'] = standarder.standardizer_docx(format_parameters)
            return Manipulation.pdf(format_parameters)

        except Exception as unknown_error:
            logging.info(format_parameters['document_name'])
            logging.info(f"Description: {unknown_error}", "- driver.to_default")
            return


class Checking:

    @staticmethod
    def input_extension(format_parameters: dict):
        extension_in = format_parameters['extension_in'].replace(" ", "")

        if extension_in == fstring.formats["commute"][1]:
            logging.info(fstring.message["info"]['conversion_not'])
            result = Manipulation.docx(format_parameters)

        elif any(map(lambda x: format_parameters['extension_in'] == x,
                     (fstring.formats['commute'][i] for i in range(6, 1, -1)))):
            ConvertingFile.commuter(
                format_parameters['document_name'],
                format_parameters['extension_in'],
                fstring.formats["commute"][1]
            )
            result = Manipulation.docx(format_parameters)

            if format_parameters['extension_in'] != fstring.formats["commute"][1]:
                ConvertingFile.commuter(
                    format_parameters['document_name'],
                    fstring.formats["commute"][1],
                    format_parameters['extension_out']
                )

        else:
            logging.info(fstring.message["exception"]['format_allowed'], "- driver.driver")

        logging.info(result, " - result for driver")

        return result


class InputData:

    @staticmethod
    def format_parameter(
            document_name: str, extension_in: str, newspaper, publication_type,
            column, number_column, days, user_condensation, just_name: str
    ) -> dict:
        format_parameters = {
            'document_name': document_name,
            'just_name': just_name,
            'extension_in': extension_in,
            'extension_out': str(newspaper['format_out']),
            'format_out': str(newspaper['format_out']),
            'publication_type': publication_type,
            'price_cm': float(newspaper['price_cm']),
            'name_section': str(newspaper['name_section']),
            'column': float(column),
            'number_column': number_column,
            'height': float(newspaper['height']),
            'height_round': bool(newspaper['height_round']),
            'format_allowed': str(publication_type['format']),
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
        condensation_definer(format_parameters)

        # Font definer
        format_parameters['font_name'] = str(fstring.formats['font'][format_parameters['font_index']])

        print(format_parameters)
        return format_parameters


def condensation_definer(format_parameters) -> None:
    if format_parameters['user_condensation'] != 'default':
        format_parameters['condensation'] = format_parameters['user_condensation']
