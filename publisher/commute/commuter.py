import logging
from os import getcwd, system

from publisher.commute import fstring

logging.basicConfig(level=logging.INFO)


class ConvertingFile:

    @staticmethod
    def __path_finder():
        return f"{getcwd()}//"

    @staticmethod
    def commuter(document, extension_in, extension_out):
        try:
            system(
                f'unoconv -f "{extension_out[1:]}" "{ConvertingFile.__path_finder()}{document + extension_in}"'
            )
            logging.info(f"Converted \"{extension_in}\" to \"{extension_out}\".")

        except FileNotFoundError:
            logging.info(fstring.message["exception"]['file_not_found'])

        except UserWarning:
            logging.info(fstring.message["exception"]['generic'])
            raise

        except Exception as unknown_error:
            logging.info(f"Description: {unknown_error}")
