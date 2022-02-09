
from publisher.commute import fstring

from publisher.commute.budgeter import Budget

from publisher.repository.adjust_files import Rename


class Calculate:
    @staticmethod
    def budget(result, format_parameters):
        if format_parameters['name_section'] in fstring.newspapers['budget_by_character']:
            Budget.calculate_budget_by_character(result, format_parameters)
            Budget.calculate_price_by_centimeter_square(result, format_parameters)
        else:
            Budget.calculate_budget_by_centimeter(result, format_parameters)
            Budget.calculate_price_by_centimeter_square(result, format_parameters)

        result['newspaper'] = format_parameters['name_section']
        result['chars_count'] = format_parameters['chars_count']

        return Rename.files(result, format_parameters)
