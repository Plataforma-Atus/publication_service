import logging
from math import ceil
from os import remove, rename, system

from pdf2image import convert_from_path
from pdfCropMargins import crop
from PyPDF2 import PdfFileReader, PdfFileWriter

from publisher.commute import fstring

logging.basicConfig(level=logging.INFO)


def read_pdf_size(document_name, format_parameters):
    write_pdf = PdfFileWriter()

    with open(f'{document_name}.pdf', "rb") as pdf_file:
        read_pdf = PdfFileReader(f'{document_name}.pdf')
    number_of_pages = read_pdf.getNumPages()
    total_height: int = 0
    width: int = 0
    total_height, width = result_width_and_height(format_parameters, number_of_pages, read_pdf, total_height, width,
                                                  write_pdf)

    result = cut_out_pdf(document_name, total_height, width, write_pdf)
    return result


def result_width_and_height(format_parameters, number_of_pages, read_pdf, total_height, width, write_pdf):
    for page_number in range(number_of_pages):
        page = read_pdf.getPage(page_number)

        width: float = float(page.mediaBox.getWidth()) * 0.3527780 / 10  # Convert user unit to cm
        height: float = float(page.mediaBox.getHeight()) * 0.3527780 / 10  # Convert user unit to cm

        if (format_parameters['height_round']) is True:
            rounded_height = ceil(height)
            if (format_parameters['name_section']) in fstring.newspapers['budget_by_half_centimeter']:
                rounded_height = 0.5 * ceil(height * 2)
            page.scaleTo(float(page.mediaBox.getWidth()), rounded_height * 0.393701 * 72)
            height = rounded_height
        write_pdf.addBlankPage(1, 1)
        write_page = write_pdf.getPage(page_number)
        write_page.mergeScaledPage(page, 1, True)
        total_height: float = total_height + float(height)
        logging.info(
            "Page:", page_number, "-",
            "Height(cm):", "{:.2f}".format(float(height)), "-",
            "Width(cm):", "{:.2f}".format(float(width))
        )
    return total_height, width


def cut_out_pdf(document_name, total_height, width, write_pdf):
    with open(f'{document_name}_scl.pdf', "wb") as pdf_file:
        write_pdf.write(pdf_file)
    crop(["-x", "300", "-y", "300",
          "-dcb", "ALL",
          f"{document_name}_scl.pdf",
          f"-o{document_name}.pdf",
          "-a4", "0", "0", "0", "0",
          "-p", "0"])
    remove(f"{document_name}_scl.pdf")
    result = {
        'file': str(document_name),
        'width': "{:.2f}".format(float(width)),
        'height': "{:.2f}".format(float(total_height))
    }
    return result


def convert_pdf_to_greyscale(format_parameters):
    document_name_with_height = format_parameters['document_name_with_height']
    system(f'gs \
               -sDEVICE=pdfwrite \
               -sProcessColorModel=DeviceGray \
               -sColorConversionStrategy=Gray \
               -dOverrideICC \
               -o "{document_name_with_height}_GS.pdf" \
               -f "{document_name_with_height}.pdf"')
    remove(f"{document_name_with_height}.pdf")
    rename(f"{document_name_with_height}_GS.pdf", f"{document_name_with_height}.pdf")


def make_pdf_preview(document_name):
    try:
        pdf_image = convert_from_path(
            f"{document_name}_crp.pdf",
            size=(300, None),
            transparent=False,
        )
        for page in pdf_image:
            updated_path = document_name
            page.save(
                f"{updated_path}_crp.jpeg",
                'JPEG'
            )
    except FileNotFoundError:
        logging.info(fstring.message["exception"]['file_not_found'])
    except ValueError:
        logging.info(fstring.message["exception"]['value'])


def auto_crop_pdf(format_parameters):
    document_name = format_parameters['document_name']
    try:
        crop(["-x", "300", "-y", "300",
              "-dcb", "ALL", "-cd",
              f"{document_name}.pdf",
              f"-o{document_name}_crp.pdf",
              "-p 0"])
        rename(f"{document_name}.pdf", f"{document_name}_ref.pdf")
        remove(f"{document_name}_ref.pdf")
        pdf_cropped = f'{document_name}_crp'
        make_pdf_preview(document_name)
        return read_pdf_size(pdf_cropped, format_parameters)
    except FileNotFoundError:
        logging.info(fstring.message["exception"]['file_not_found'])
    except ValueError:
        logging.info(fstring.message["exception"]['value'])
    except Exception as unknown_error:
        logging.info(f"Description: {unknown_error}")
