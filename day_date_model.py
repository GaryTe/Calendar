from operator import itemgetter
from time import time, gmtime

from dictionary_of_constants import NUMBERS, WEEKDAY, NAME_DAY

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

        self.data = data
        self.indicator = indicator
        self.number_days_of_month = number_days_of_month
        self.number_days_of_offset = number_days_of_offset

        self.number_days_of_week = seven
        self.number_days_of_working = five
        self.number_offset_in_days = zero
        self.day_off = {
            'saturday': six,
            'sunday': seven
            }
        self.list_days = []

        data = self.write_name_and_date_of_day()
        return data

    def write_name_and_date_of_day ( self ) :
        if self.indicator == True:
            self.list_days = []

        day_counter = ( self.number_days_of_week - six ) + self.number_days_of_offset
        key_value_day = self.number_days_of_offset
        self.number_offset_in_days = self.number_days_of_offset if ( self.number_days_of_offset != zero ) else self.number_offset_in_days
        exit_ = False

        for number in range ( day_counter, self.number_days_of_week + one ) :
            if number <= self.number_days_of_working and number <= self.number_days_of_month :
                key_value_day += one
                self.list_days.append(self.get_line(number, working_day, key_value_day))
            elif number == self.day_off['saturday'] and number <= self.number_days_of_month :
                key_value_day += one
                self.list_days.append(self.get_line(number, day_off, key_value_day))
            elif number == self.day_off['sunday'] and number <= self.number_days_of_month :
                key_value_day += one
                self.list_days.append(self.get_line(number, day_off, key_value_day))
            else :
                exit_ = True
                self.number_offset_in_days = key_value_day
                break

        if exit_ == False :
            self.number_days_of_week = self.number_days_of_week + seven
            self.number_days_of_working = self.number_days_of_working + seven
            self.day_off['saturday'] = self.number_days_of_working + one
            self.day_off['sunday'] = self.day_off['saturday'] + one

            self.indicator = False
            self.number_days_of_offset = zero
            
            self.write_name_and_date_of_day()

        return {
            'data_month': self.list_days,
            'offset': self.number_offset_in_days
            }

    def get_line (
        self,
        number,
        indicator_weekday,
        key_value_day
        ) :
        time_in_seconds = time()
        year = gmtime(time_in_seconds).tm_year
        mon = gmtime(time_in_seconds).tm_mon
        day = gmtime(time_in_seconds).tm_mday

        year_, month = itemgetter('year', 'month') ( self.data )

        line = ' '
        number_day = number - self.number_offset_in_days

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
            line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число - (выходной день)'
            return  line
        
