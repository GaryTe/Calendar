from dictionary_of_constants import NAME_DAY

days_of_week = 7
days_of_working = 5
offset_in_days = 0
list_days = []

days_off = {
    'saturday': 6,
    'sunday': 7
    }

def  return_name_and_date_of_days(
    resetting_variable_original_value = False,
    days_of_month = 0,
    days_of_displacement = 0
    ):
    global list_days, days_of_week, days_of_working, offset_in_days

    if resetting_variable_original_value == True:
        list_days = []
    
    day_counter = (days_of_week - 6) + days_of_displacement
    key_value_day = days_of_displacement
    offset_in_days = days_of_displacement if (days_of_displacement != 0) else offset_in_days
    exiting_the_function = False
    
    for number in range(day_counter, days_of_week + 1):
        if number <= days_of_working and number <= days_of_month:
            key_value_day += 1
            list_days.append(f'{NAME_DAY[str(key_value_day)]} : {number - offset_in_days} чесло')
        elif number == days_off['saturday'] and number <= days_of_month:
            key_value_day += 1
            list_days.append(f'{NAME_DAY[str(key_value_day)]} : {number - offset_in_days} чесло')
        elif number == days_off['sunday'] and number <= days_of_month:
            key_value_day += 1
            list_days.append(f'{NAME_DAY[str(key_value_day)]} : {number - offset_in_days} чесло')
        else:
            offset_in_days = key_value_day
            exiting_the_function = True
            days_of_week = 7
            days_of_working = 5
            days_off['saturday'] = 6
            days_off ['sunday'] = 7
            return
            

    if exiting_the_function == False:
        days_of_week = days_of_week + 7
        days_of_working = days_of_working + 7
        days_off['saturday'] = days_of_working + 1
        days_off['sunday'] = days_off['saturday'] + 1

        return_name_and_date_of_days(
        days_of_month = days_of_month
        )
   
    return {
        'data_month': list_days,
        'offset': offset_in_days
        }
    
