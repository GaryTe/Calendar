from datetime import datetime
from operator import itemgetter

from constant.list_constant import ATTRIBUTE_LIST

day_, month_, _ = ATTRIBUTE_LIST 

class DateTimeModel :

    def get_date_and_time ( self ) :
        result = ''
        today = datetime.today()

        for attribute in  ATTRIBUTE_LIST:
            data_attribute = getattr(today, attribute)
            if attribute == day_ :
                day = today.strftime('%d')
                result += day
            elif attribute == month_ :
                month = today.strftime('%m')
                result += f'.{month}'
            else :
                result += f'.{data_attribute}'

        hour = today.strftime('%H')
        minute = today.strftime('%M')
        result += f'\n {str(hour)}:{str(minute)}'
        
        return result
