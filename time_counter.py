from time import time, gmtime, sleep

from datetime_modul import return_date_and_time

SEC_IN_MIN = 60

def coll_counter():
    flag = 'end' 
    switch = 'start'

    time_in_seconds = time()
    sec = SEC_IN_MIN - gmtime(time_in_seconds).tm_sec
    while switch != flag:
        sleep( sec )
        data_time = return_date_and_time()
        sec = SEC_IN_MIN
        print(data_time)
