from operator import itemgetter

from return_line import return_line
from dictionary_of_constants import NAME_DAY, NUMBERS, WEEKDAY

seven, five, zero, six, one = itemgetter('seven', 'five', 'zero', 'six', 'one') (NUMBERS)
working_day, day_off = itemgetter('working_day', 'day_off') (WEEKDAY)

days_of_week = seven
days_of_working = five
offset_in_days = zero
list_days = []

days_off = {
    'saturday': six,
    'sunday': seven
    }

def  return_name_and_date_of_days(
    data_for_function_return_line,
    resetting_variable_original_value = False,
    days_of_month = zero,
    days_of_displacement = zero
    ):
    global list_days, days_of_week, days_of_working, offset_in_days

    if resetting_variable_original_value == True:
        list_days = []
    
    day_counter = (days_of_week - six) + days_of_displacement
    key_value_day = days_of_displacement
    offset_in_days = days_of_displacement if (days_of_displacement != zero) else offset_in_days
    exiting_the_function = False
    
    for number in range(day_counter, days_of_week + one):
        if number <= days_of_working and number <= days_of_month:
            key_value_day += one
            list_days.append(return_line(data_for_function_return_line, working_day, key_value_day, number, offset_in_days))
        elif number == days_off['saturday'] and number <= days_of_month:
            key_value_day += one
            list_days.append(return_line(data_for_function_return_line, day_off, key_value_day, number, offset_in_days))
        elif number == days_off['sunday'] and number <= days_of_month:
            key_value_day += one
            list_days.append(return_line(data_for_function_return_line, day_off, key_value_day, number, offset_in_days))
        else:
            offset_in_days = key_value_day
            exiting_the_function = True
            days_of_week = seven
            days_of_working = five
            days_off['saturday'] = six
            days_off ['sunday'] = seven
            return
            

    if exiting_the_function == False:
        days_of_week = days_of_week + seven
        days_of_working = days_of_working + seven
        days_off['saturday'] = days_of_working + one
        days_off['sunday'] = days_off['saturday'] + one

        return_name_and_date_of_days(
            data_for_function_return_line = data_for_function_return_line,
            days_of_month = days_of_month
        )
   
    return {
        'data_month': list_days,
        'offset': offset_in_days
        }
    
