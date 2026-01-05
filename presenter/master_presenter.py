from operator import itemgetter
from tkinter import *
from time import time, localtime, strftime

from view.calendar_view import *
from view.label_time_date_view import *
from view.label_year_view import *
from view.button_reduce_year_view import *
from view.button_increase_year_view import *
from view.button_updating_view import *
from model.year_model import *
from model.month_model import *
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
    __window = Tk()
    __year_model = YearModel()
    __month_model = MonthModel()
    __day_date_model = DayDateModel()
    
    __label_year_view = LabelYearView(
        __year_model.get_year,
        __window
        )
    __label_time_date_view = LabelTimeDateView( __window )
    __calendar_view = CalendarView()
    __button_reduce_year_view = ButtonReduceYearView( __window )
    __button_increase_year_view = ButtonIncreaseYearView( __window )
    __button_updating_view = ButtonUpdatingView( __window )

    def initialization ( self ) :
        MasterPresenter.__window.title( 'Календарь' )
        MasterPresenter.__window.resizable( 0, 0 )
        MasterPresenter.__window.geometry( '400x600' )

        MasterPresenter.__calendar_view.create_text(
            MasterPresenter.__year_model.get_data_year,
            self.__get_data_month
            )
        MasterPresenter.__label_year_view.create_label()
        MasterPresenter.__button_updating_view.create_label( self.updating_calendar_by_day )
        MasterPresenter.__button_reduce_year_view.create_button( self.handler_reduce_year )
        MasterPresenter.__button_increase_year_view.create_button( self.handler_increase_year )
        MasterPresenter.__label_time_date_view.create_label()
        
        MasterPresenter.__window.mainloop()

    def __get_data_month (self,  year ) :
        data_of_month = {}
        offset_in_days = OFFSET_IN_YEAR[year]

        for number_month in MONTH_OF_YEAR:
            day = 0

            if LEAP_YEARS_LIST.count( year ) > 0 and number_month == two :
                day += 1
            
            data_month = MasterPresenter.__month_model.get_data_month(number_month, offset_in_days, day)
            data_by_day = MasterPresenter.__day_date_model.initialization(
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

        return data_of_month

    def handler_reduce_year ( self ) :
        data_text = MasterPresenter.__year_model.reduce_year( self.__get_data_month )
        
        MasterPresenter.__label_year_view.change_value_label( self.__year_model.get_year() )
        MasterPresenter.__calendar_view.change_value_calendar( data_text )

    def handler_increase_year ( self ) :
        data_text = MasterPresenter.__year_model.increase_year( self.__get_data_month )
        
        MasterPresenter.__label_year_view.change_value_label( self.__year_model.get_year() )
        MasterPresenter.__calendar_view.change_value_calendar( data_text )

    def updating_calendar_by_day ( self ) :
        year = strftime('%Y', localtime(time()))
        data_text = self.__year_model.get_data_year( self.__get_data_month, year )

        self.__label_year_view.change_value_label( self.__year_model.get_year() )
        self.__calendar_view.change_value_calendar( data_text )
