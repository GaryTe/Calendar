from tkinter import *
from time import strftime, time, gmtime


class LabelTimeDateView :
    __window = None
    __label = None

    def __init__ ( self, window ) :
        LabelTimeDateView.__window = window

    def create_label ( self ) :
        
        LabelTimeDateView.__label = Label( LabelTimeDateView.__window )
        LabelTimeDateView.__label.place( x = 320, y = 1  )

        sec = int(f'{gmtime(time()).tm_sec}000')
        offset_time = 60000 - sec

        LabelTimeDateView.__get_time_date( offset_time )

    def __get_time_date ( offset_time = 60000 ) :
        string_time = strftime( '%H : %M' )
        string_date = strftime( '%d . %m . %Y' )
        data_time_date = f'{string_time}\n{string_date}'

        LabelTimeDateView.__label.config(text = data_time_date)
        LabelTimeDateView.__label.after(offset_time, LabelTimeDateView.__get_time_date)
