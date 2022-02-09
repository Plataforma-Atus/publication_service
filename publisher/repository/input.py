from publisher.commute import fstring


class InputData:
    @staticmethod
    def format_parameter(
            document_name: str, extension_in: str, newspaper, publication_type,
            column, number_column, days, user_condensation, just_name: str
    ) -> dict:
        format_parameters = {
            'document_name': document_name,
            'just_name': just_name,
            'extension_in': extension_in,
            'extension_out': str(newspaper['format_out']),
            'format_out': str(newspaper['format_out']),
            'publication_type': publication_type,
            'price_cm': float(newspaper['price_cm']),
            'name_section': str(newspaper['name_section']),
            'column': float(column),
            'number_column': number_column,
            'height': float(newspaper['height']),
            'height_round': bool(newspaper['height_round']),
            'format_allowed': str(publication_type['format']),
            'days': str(days),
            'user_condensation': str(user_condensation),
            'condensation': str(publication_type['condensation']),
            'edge': bool(newspaper['edge']),
            'bold': bool(publication_type['bold']),
            'italic': bool(publication_type['italic']),
            'underline': bool(publication_type['underline']),
            # Font info
            'font_index': int(newspaper['font_name']),
            'font_size': float(newspaper['font_size']),
            'font_size_company': float(newspaper['font_size_company']),
            'font_leading': float(newspaper['font_leading']),
            'font_leading_company': float(newspaper['font_leading_company']),
        }

        # Condensation definer
        condensation_definer(format_parameters)

        # Font definer
        format_parameters['font_name'] = str(fstring.formats['font'][format_parameters['font_index']])

        print(format_parameters)
        return format_parameters


def condensation_definer(format_parameters) -> None:
    if format_parameters['user_condensation'] != 'default':
        format_parameters['condensation'] = format_parameters['user_condensation']