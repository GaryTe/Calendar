from time import time, gmtime, sleep

from variabl_constant import SEC_IN_MIN

class DateTimeCounterView :
     _date_time_model = None

     _switch = 'start'

     def __init__ ( self, date_time_model ) :
          DateTimeCounterView._date_time_model = date_time_model

     def coll_counter ( self ) :
          flag = 'end'

          time_in_seconds = time()
          sec = SEC_IN_MIN - gmtime(time_in_seconds).tm_sec

          while self._switch != flag :
               sleep( sec )
               data_day_and_time = self._date_time_model.get_date_and_time()
               sec = SEC_IN_MIN
               print(data_day_and_time)

     def stop_counter ( self ) :
          self._switch = 'end'
