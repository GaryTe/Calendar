from time import time, gmtime
from operator import itemgetter

from dictionary_of_constants import NAME_DAY, WEEKDAY

time_in_seconds = time()
year = gmtime(time_in_seconds).tm_year
mon = gmtime(time_in_seconds).tm_mon
day = gmtime(time_in_seconds).tm_mday

working_day, day_off = itemgetter('working_day', 'day_off') (WEEKDAY)

def return_line(
    data_comparison,
    indicator_weekday,
    key_value_day,
    number,
    offset_in_days
    ):

    year_, month = itemgetter('year', 'month') (data_comparison)
    
    line = ' '
    number_day = number - offset_in_days

    if indicator_weekday == working_day and (mon != month and year == year_):
        line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число'
        return line
    
    if indicator_weekday == working_day and (mon == month and year == year_):
        line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число - (сегодняшней день)' if(day == number_day) else f'{NAME_DAY[str(key_value_day)]} : {number_day} число'
        return line

    if indicator_weekday == working_day and year != year_:
        line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число'
        return line
    
    if indicator_weekday == day_off:
        line = f'{NAME_DAY[str(key_value_day)]} : {number_day} число - (выходной день)'
        return  line
