import logging
from os import getcwd, system

from publisher.commute import fstring

logging.basicConfig(level=logging.INFO)


# Locate path
def path_finder():
    path_driver = getcwd()
    return path_driver + "//"


def commuter(document, extension_in, extension_out):
    try:
        # if extension_out != ".pdf":
        system(f'unoconv -f "{extension_out[1:]}" "{path_finder()}{document + extension_in}"')
        logging.info(f"Converted \"{extension_in}\" to \"{extension_out}\".")

    except FileNotFoundError:
        logging.info(fstring.message["exception"]['file_not_found'])

    except UserWarning:
        logging.info(fstring.message["exception"]['generic'])
        raise

    except Exception as unknown_error:
        logging.info(f"Description: {unknown_error}")

