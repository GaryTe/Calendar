from dictionary_of_constants import MONTH_OF_YEAR

class MonthView :

    def get_data_month ( self, number_month, offset_in_days ) :
        month = MONTH_OF_YEAR[number_month]['name']
        value_days_of_month = MONTH_OF_YEAR[number_month]['days_of_month'] + offset_in_days

        return {
            'name_month' : month,
            'value_days_of_month' : value_days_of_month 
            }
