from dictionary_of_constants import OFFSET_IN_YEAR, MONTH_OF_YEAR
from return_name_and_date_of_days import return_name_and_date_of_days

data_of_year = {}

def get_data_month(year):
    global data_of_year
    
    offset_in_days = OFFSET_IN_YEAR[year]
    
    for number_month in MONTH_OF_YEAR:
        month = MONTH_OF_YEAR[number_month]['name']
        data_of_year[month] = []
        value_days_of_month = MONTH_OF_YEAR[number_month]['days_of_month'] + offset_in_days

        data_by_day = return_name_and_date_of_days(
            True,
            days_of_month = value_days_of_month,
            days_of_displacement = offset_in_days
        )

        data_of_year[month] = data_by_day['data_month']
        offset_in_days = data_by_day['offset']
        
    return data_of_year
