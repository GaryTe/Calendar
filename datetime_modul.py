from datetime import datetime

attribute_list = ['day', 'month', 'year']

def return_date_and_time():
    result = ''
    today = datetime.today()
    
    for attribute in attribute_list:
        day = getattr(today, attribute)
        if attribute == 'day':
            namber = today.strftime('%d')
            result += namber
        else:
            result += f'.{str(day)}'
    hour = today.hour
    minute = today.minute
    result += f'\n {str(hour)}:{str(minute)}'
    return result
