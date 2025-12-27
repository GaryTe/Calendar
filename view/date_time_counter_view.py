from time import time, gmtime, sleep

from constant.variabl_constant import SEC_IN_MIN
from constant.list_constant import VALUE_SWITCH

start, end = VALUE_SWITCH

class DateTimeCounterView :
     __date_time_model = None

     __switch = start

     def __init__ ( self, date_time_model ) :
          DateTimeCounterView.__date_time_model = date_time_model

     def coll_counter ( self ) :
          flag = end

          time_in_seconds = time()
          sec = SEC_IN_MIN - gmtime(time_in_seconds).tm_sec

          while self.__switch != flag :
               sleep( sec )
               data_day_and_time = self.__date_time_model.get_date_and_time()
               sec = SEC_IN_MIN
               print(data_day_and_time)

     def stop_counter ( self ) :
          self.__switch = end
