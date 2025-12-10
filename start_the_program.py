from get_data_year import get_data_year
from time_counter import coll_counter
from datetime_modul import return_date_and_time
from dictionary_of_constants import PARAMETER_CONDITION, MESSAGE_PROGRAM

def start_the_program():
    value = get_data_year()

    if type(value) == dict:
        date_and_time = return_date_and_time()
        print('\n', date_and_time, '\n')
        for name_key, data in value.items():
            print('\n' + name_key + '\n')
            for value in data:
                print(value)
        return
    elif value == PARAMETER_CONDITION['first_condition']:
        return MESSAGE_PROGRAM['first_message']
    elif not value.isdigit() or (value < PARAMETER_CONDITION['second_condition'] or value > PARAMETER_CONDITION['third_condition']):
        start_the_program()

start_the_program()
coll_counter()
