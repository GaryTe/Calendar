from get_data_month import get_data_month
from dictionary_of_constants import PARAMETER_CONDITION, MESSAGE_PROGRAM

def get_data_year():
    value = input(MESSAGE_PROGRAM['second_message'])
    edit_value = value.strip()
    
    if edit_value == PARAMETER_CONDITION['first_condition']:
        return edit_value
    elif not edit_value.isdigit() or (edit_value < PARAMETER_CONDITION['second_condition'] or value > PARAMETER_CONDITION['third_condition']):
        return edit_value

    data_month = get_data_month(edit_value)
    print('\n' + edit_value, 'год')
    return data_month
