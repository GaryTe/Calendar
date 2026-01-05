from time import time, localtime, strftime

from constant.dictionary_of_constants import (
    PARAMETER_CONDITION,
    MESSAGE_PROGRAM
    )

tm_year = strftime('%Y', localtime(time()))

class YearModel :
    __year = tm_year
    
    def get_data_year (
        self,
        handler_get_data_month,
        year = __year
        ) :

        YearModel.__year = year
        
        data_of_month = handler_get_data_month( year )

        data_text = YearModel.__get_data_text( data_of_month )

        return data_text

    def get_year ( seif ) :
        return YearModel.__year

    def __get_data_text ( data_of_month ) :
        data_text = ''
        
        for name_key, data in data_of_month.items():
            data_text += '\n' + name_key + '\n'
            for value in data:
                data_text += value + '\n'

        return data_text

    def reduce_year ( self,  handler_get_data_month) :
        if YearModel.__year == '2025' :
            return

        year = str(int(YearModel.__year) - 1)

        data_text = self.get_data_year( handler_get_data_month,  year)

        return data_text

    def increase_year ( self,  handler_get_data_month) :
        if YearModel.__year == '2036' :
            return

        year = str(int(YearModel.__year) + 1)

        data_text = self.get_data_year( handler_get_data_month,  year)

        return data_text
    
