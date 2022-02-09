import logging

from publisher.commute.commuter import ConvertingFile

from publisher.commute import fstring

from publisher.commute.cropper import DocumentAdjustments
from publisher.commute.standarder import Standardizer

from publisher.repository.calculations import Calculate


class Manipulation:

    @staticmethod
    def pdf(format_parameters: dict):
        if any(map(lambda x: format_parameters['format_out'] == x, (fstring.formats['commute'][i] for i in [1, 4]))):
            ConvertingFile.commuter(
                format_parameters['document_name'], extension_in=fstring.formats["commute"][1],
                extension_out=fstring.formats["commute"][4]
            )
            result = DocumentAdjustments.auto_crop_pdf(format_parameters)
            return Calculate.budget(result, format_parameters)

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
            return Calculate.budget(result, format_parameters)

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
            return Calculate.budget(result, format_parameters)

        else:
            logging.error(fstring.message["exception"]['format'], exc_info=True)

    @staticmethod
    def docx(format_parameters: dict):
        try:
            format_parameters['chars_count'] = Standardizer.docx(format_parameters)
            return Manipulation.pdf(format_parameters)

        except Exception as unknown_error:
            print(format_parameters['document_name'])
            logging.error(f"Description: {unknown_error}", "- driver.to_default", exc_info=True)
            return