import logging


class Budget:

    def __init__(self):
        self.format_parameters = None

    def make_budget(self, result, format_parameters):
        result['newspaper'] = self.format_parameters['name_section']
        result['price_cm'] = float(self.format_parameters['price_cm'])
        result['width'] = float(self.format_parameters['column'])
        return result, format_parameters

    @staticmethod
    def calculate_budget_by_centimeter(result, format_parameters):
        result['price'] = "{:.2f}".format(
            (float(format_parameters['price_cm']) * float(result['height'])) * float(format_parameters['number_column'])
        )
        logging.info("R$", result['price'], " cm/col")
        return result, format_parameters

    @staticmethod
    def calculate_budget_by_character(result, format_parameters):
        result['price'] = "{:.2f}".format(
            (float(format_parameters['price_cm']) * float(format_parameters['chars_count'])))
        logging.info("R$", result['price'], " char")
        return result, format_parameters

    @staticmethod
    def calculate_price_by_centimeter_square(result, format_parameters):
        result['price_by_cm'] = "{:.2f}".format(
            (float(result['price'])) / (float(result['height']) * float(result['width'])))
        logging.info("R$ ", result['price_by_cm'], " cm_square")
        return result, format_parameters
