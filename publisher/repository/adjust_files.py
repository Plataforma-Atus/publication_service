from os import rename

from publisher.commute.cropper import DocumentAdjustments


class Rename:
    @staticmethod
    def files(result, format_parameters):
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
        print(document_name_with_height)

        format_parameters['document_name_with_height'] = document_name_with_height
        DocumentAdjustments.convert_pdf_to_greyscale(format_parameters)
        return result
