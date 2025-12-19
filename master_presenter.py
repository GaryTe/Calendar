from year_view import *
from month_view import *
from day_date_model import *

from dictionary_of_constants import PARAMETER_CONDITION, MESSAGE_PROGRAM, OFFSET_IN_YEAR, ERROR_MESSAGE

class MasterPresenter :
    _date_time_model = None
    _date_time_counter_view = None
    
    _year_view = YearView()
    _month_view = MonthView()
    _day_date_model = DayDateModel()

    def __init__ ( self,  date_time_model, date_time_counter_view ) :
        MasterPresenter._date_time_model = date_time_model
        MasterPresenter._date_time_counter_view = date_time_counter_view

    def initialization ( self ) :
        self.check_value_from_input()

    def check_value_from_input ( self ) :
        value_year = self._year_view.get_data_year()

        if value_year == PARAMETER_CONDITION['first_condition']:
            self._date_time_counter_view.stop_counter()
            print(MESSAGE_PROGRAM['first_message'])
            return
        elif not value_year.isdigit() or (value_year < PARAMETER_CONDITION['second_condition'] or value_year > PARAMETER_CONDITION['third_condition']):
            self.check_value_from_input()
            return

        self.get_data_month ( value_year )

    def get_data_month (self,  year ) :
        data_of_month = {}
        offset_in_days = OFFSET_IN_YEAR[year]

        for number_month in MONTH_OF_YEAR:
            data_month = self._month_view.get_data_month(number_month, offset_in_days)
            data_by_day = self._day_date_model.initialization(
                {
                    'year': int(year),
                    'month': int(number_month)
                },
                True,
                data_month['value_days_of_month'],
                offset_in_days
                )

            data_of_month[data_month['name_month']] = data_by_day['data_month']
            offset_in_days = data_by_day['offset']

        self.check_render_data_month ( data_of_month,  year )

    def  check_render_data_month (self, data_of_month,  year) :
        if type( data_of_month ) != dict :
            raise ValueError( ERROR_MESSAGE['value_error'] )

        date_and_time = self._date_time_model.get_date_and_time()
        print('\n' + year, 'год')
        print('\n', date_and_time, '\n')
        
        for name_key, data in data_of_month.items():
            print('\n' + name_key + '\n')
            for value in data:
                print(value)
    
