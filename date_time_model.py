from datetime import datetime

from list_constant import attribute_list

class DateTimeModel :

    def get_date_and_time ( self ) :
        result = ''
        today = datetime.today()

        for attribute in attribute_list :
            data_attribute = getattr(today, attribute)
            if attribute == 'day' :
                day = today.strftime('%d')
                result += day
            elif attribute == 'month' :
                month = today.strftime('%m')
                result += f'.{month}'
            else :
                result += f'.{data_attribute}'

        hour = today.strftime('%H')
        minute = today.strftime('%M')
        result += f'\n {str(hour)}:{str(minute)}'
        
        return result
