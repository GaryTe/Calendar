from operator import itemgetter
from time import time, gmtime

from constant.dictionary_of_constants import NUMBERS, WEEKDAY, NAME_DAY

seven, five, zero, six, one = itemgetter( 'seven', 'five', 'zero', 'six', 'one' ) ( NUMBERS )
working_day, day_off = itemgetter( 'working_day', 'day_off' ) ( WEEKDAY ) 

class DayDateModel :

    def initialization (
        self,
        data,
        indicator,
        number_days_of_month,
        number_days_of_offset
        ) :

        self.__data = data
        self.__indicator = indicator
        self.__number_days_of_month = number_days_of_month
        self.__number_days_of_offset = number_days_of_offset

        self.__number_days_of_week = seven
        self.__number_days_of_working = five
        self.__number_offset_in_days = zero
        self.__day_off = {
            'saturday': six,
            'sunday': seven
            }
        self.__list_days = []

        data = self.__write_name_and_date_of_day()
        return data

    def __write_name_and_date_of_day ( self ) :
        if self.__indicator == True:
            self.__list_days = []

        day_counter = ( self.__number_days_of_week - six ) + self.__number_days_of_offset
        key_value_day = self.__number_days_of_offset
        self.__number_offset_in_days = self.__number_days_of_offset if ( self.__number_days_of_offset != zero ) else self.__number_offset_in_days
        exit_ = False

        for number in range ( day_counter, self.__number_days_of_week + one ) :
            if number <= self.__number_days_of_working and number <= self.__number_days_of_month :
                key_value_day += one
                self.__list_days.append(self.__get_line(number, working_day, key_value_day))
            elif number == self.__day_off['saturday'] and number <= self.__number_days_of_month :
                key_value_day += one
                self.__list_days.append(self.__get_line(number, day_off, key_value_day))
            elif number == self.__day_off['sunday'] and number <= self.__number_days_of_month :
                key_value_day += one
                self.__list_days.append(self.__get_line(number, day_off, key_value_day))
            else :
                exit_ = True
                self.__number_offset_in_days = key_value_day
                break

        if exit_ == False :
            self.__number_days_of_week = self.__number_days_of_week + seven
            self.__number_days_of_working = self.__number_days_of_working + seven
            self.__day_off['saturday'] = self.__number_days_of_working + one
            self.__day_off['sunday'] = self.__day_off['saturday'] + one

            self.__indicator = False
            self.__number_days_of_offset = zero
            
            self.__write_name_and_date_of_day()

        return {
            'data_month': self.__list_days,
            'offset': self.__number_offset_in_days
            }

    def __get_line (
        self,
        number,
        indicator_weekday,
        key_value_day
        ) :
        time_in_seconds = time()
        year = gmtime(time_in_seconds).tm_year
        mon = gmtime(time_in_seconds).tm_mon
        day = gmtime(time_in_seconds).tm_mday

        year_, month = itemgetter('year', 'month') ( self.__data )

        line = ' '
        number_day = number - self.__number_offset_in_days

        if indicator_weekday == working_day and (mon != month and year == year_) :
            line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число'
            return line

        if indicator_weekday == working_day and (mon == month and year == year_) :
            line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число - (сегодняшней день)' if(day == number_day) else f'{NAME_DAY[str(key_value_day)]} : {number_day} число'
            return line

        if indicator_weekday == working_day and year != year_ :
            line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число'
            return line

        if indicator_weekday == day_off :
            value = '(выходной день)' if (day != number_day) else '(сегодняшней день)'
            line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число - {value}'
            return  line
        
