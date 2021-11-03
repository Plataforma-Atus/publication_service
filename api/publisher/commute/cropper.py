from os import remove, rename
from math import ceil

from PyPDF2 import PdfFileReader, PdfFileWriter

from pdf2image import convert_from_path

from pdfCropMargins import crop

from publisher.commute import fstring


# PDF Read
def pdf_read(document_name, format_parameters):
    # PDF definer
    # document_name = format_parameters['pdf_croped']
    write_pdf = PdfFileWriter()

    with open(f'{document_name}.pdf', "rb") as pdf_file:
        read_pdf = PdfFileReader(f'{document_name}.pdf')
    number_of_pages = read_pdf.getNumPages()
    total_height = 0
    width = 0

    for page_number in range(number_of_pages):
        page = read_pdf.getPage(page_number)

        # Unit definer
        width = float(page.mediaBox.getWidth()) * 0.3527780 / 10
        height = float(page.mediaBox.getHeight()) * 0.3527780 / 10

        # PDF Round
        if (format_parameters['height_round']) is True:
            rounded_height = ceil(height)
            #print(newspaper['name_section'])
            if  (format_parameters['name_section']) == "Terceiros - DC - MT" \
                or (format_parameters['name_section']) == "Terceiros - A Gazeta - MT": # and height < 10:
                rounded_height = 0.5 * ceil(height * 2) 
            page.scaleTo(float(page.mediaBox.getWidth()), rounded_height * 0.393701 * 72)
            height = rounded_height
        write_pdf.addBlankPage(1, 1)
        write_page = write_pdf.getPage(page_number)
        write_page.mergeScaledPage(page, 1, True)
        total_height = total_height + float(height)

        # Measures console view
        print("Page:", page_number, "-",
              "Height(cm):", "{:.2f}".format(float(height)), "-",
              "Width(cm):", "{:.2f}".format(float(width)))


    result = {
        'file': document_name,
        'width': "{:.2f}".format(float(width)),
        'height': "{:.2f}".format(float(total_height))
    }


    with open(f'{document_name}_scl.pdf', "wb") as pdf_file:
        write_pdf.write(pdf_file)

    crop(["-x", "300", "-y", "300",
          "-dcb", "ALL",
          f"{document_name}_scl.pdf",
          f"-o{document_name}.pdf",
          "-a4", "0", "0", "0", "0",
          "-p", "0"])

    # Remove PDF without crop
    remove(f"{document_name}_scl.pdf")

    return result

# Generate a preview image from PDF
def pdf_preview(document_name):
    try:
        pdf_image = convert_from_path(
            f"{document_name}_crp.pdf",
            size=(300, None),
            transparent=False,
        )
        for page in pdf_image:
            page.save(
                f"{document_name}_crp.jpeg",
                'JPEG'
            )

    except FileNotFoundError:
        print(fstring.message["exception"]['file_not_found'])

    except ValueError:
        print(fstring.message["exception"]['value'])

# PDF Reduction (with pdf_read)
def auto_crop_pdf(format_parameters):
    document_name = format_parameters['document_name']
    try:
        crop(["-x", "300", "-y", "300",
              "-dcb", "ALL", "-cd",
              #"-pdl", 
              f"{document_name}.pdf",
              f"-o{document_name}_crp.pdf",
              "-p 0"])


        # Rename Original PDF
        rename(f"{document_name}.pdf", f"{document_name}_ref.pdf")
        #remove(f"{document_name}_ref.pdf")

        # PDF cropped read
        pdf_cropped = f'{document_name}_crp'
        pdf_preview(document_name)

        return pdf_read(pdf_cropped, format_parameters)

    except FileNotFoundError:
        print(fstring.message["exception"]['file_not_found'])
    # teste
    except ValueError:
        print(fstring.message["exception"]['value'])
    # teste
    except Exception as unknown_error:
        print(f"Description: {unknown_error}")
