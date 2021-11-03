import os
from publisher.commute import fstring

# Locate path
def path_finder():
    path_driver = os.getcwd()
    return path_driver + "//"


def commuter(document, extension_in, extension_out):

    try:
        os.system(f'unoconv -f "{extension_out[1:]}" "{path_finder()}{document + extension_in}"')
        print(f"Converted \"{extension_in}\" to \"{extension_out}\".")
        return document

    except FileNotFoundError:
        print(fstring.message["exception"]['file_not_found'])

    except UserWarning:
        print(fstring.message["exception"]['generic'])
        raise

    except Exception as unknown_error:
        print(f"Description: {unknown_error}")
