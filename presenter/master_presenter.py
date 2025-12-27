from operator import itemgetter

from view.year_view import *
from view.month_view import *
from model.day_date_model import *

from constant.dictionary_of_constants import (
    PARAMETER_CONDITION,
    MESSAGE_PROGRAM,
    OFFSET_IN_YEAR,
    ERROR_MESSAGE,
    NUMBERS
    )
from constant.list_constant import LEAP_YEARS_LIST

two = itemgetter( 'two' ) ( NUMBERS )

class MasterPresenter :
    __date_time_model = None
    __date_time_counter_view = None
    
    __year_view = YearView()
    __month_view = MonthView()
    __day_date_model = DayDateModel()

    def __init__ ( self,  date_time_model, date_time_counter_view ) :
        MasterPresenter.__date_time_model = date_time_model
        MasterPresenter.__date_time_counter_view = date_time_counter_view
        

    def initialization ( self ) :
        self.__check_value_from_input()
        

    def __check_value_from_input ( self ) :
        value_year = self.__year_view.get_data_year()

        if value_year == PARAMETER_CONDITION['first_condition']:
            self.__date_time_counter_view.stop_counter()
            print(MESSAGE_PROGRAM['first_message'])
            return
        elif not value_year.isdigit() or (value_year < PARAMETER_CONDITION['second_condition'] or value_year > PARAMETER_CONDITION['third_condition']):
            self.__check_value_from_input()
            return

        self.__get_data_month ( value_year )
        

    def __get_data_month (self,  year ) :
        data_of_month = {}
        offset_in_days = OFFSET_IN_YEAR[year]

        for number_month in MONTH_OF_YEAR:
            day = 0

            if LEAP_YEARS_LIST.count( year ) > 0 and number_month == two :
                day += 1
            
            data_month = self.__month_view.get_data_month(number_month, offset_in_days, day)
            data_by_day = self.__day_date_model.initialization(
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

        self.__check_render_data_month ( data_of_month,  year )
        

    def  __check_render_data_month (self, data_of_month,  year) :
        if type( data_of_month ) != dict :
            raise ValueError( ERROR_MESSAGE['value_error'] )

        date_and_time = self.__date_time_model.get_date_and_time()
        print('\n' + year, 'год')
        print('\n', date_and_time, '\n')
        
        for name_key, data in data_of_month.items():
            print('\n' + name_key + '\n')
            for value in data:
                print(value)
    
