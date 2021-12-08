from os import getcwd, system

from publisher.commute import fstring


# Locate path
def path_finder():
    path_driver = getcwd()
    return path_driver + "//"


def commuter(document, extension_in, extension_out):
    try:
        # if extension_out != ".pdf":
        system(f'unoconv -f "{extension_out[1:]}" "{path_finder()}{document + extension_in}"')
        print(f"Converted \"{extension_in}\" to \"{extension_out}\".")
            #return document
        # else:
        #
        #     system(f'gs \
        #             sDEVICE=pdfwrite \
        #            -sProcessColorModel=DeviceGray \
        #            -sColorConversionStrategy=Gray \
        #            -dOverrideICC \
        #            -o "{document_name_with_height}_GS.pdf" \
        #            -f "{document_name_with_height}.pdf"')
    except FileNotFoundError:
        print(fstring.message["exception"]['file_not_found'])

    except UserWarning:
        print(fstring.message["exception"]['generic'])
        raise

    except Exception as unknown_error:
        print(f"Description: {unknown_error}")

