import logging

from publisher.commute import fstring
from publisher.commute.commuter import ConvertingFile
from publisher.repository.extension_file_manipulation import Manipulation


class ValidatorExtension:

    @staticmethod
    def input_extension(format_parameters: dict):
        extension_in = format_parameters['extension_in'].replace(" ", "")

        if extension_in == fstring.formats["commute"][1]:
            print(fstring.message["info"]['conversion_not'])
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
            logging.error(fstring.message["exception"]['format_allowed'], "- driver.driver", exc_info=True)

        print(result, " - result for driver")

        return result