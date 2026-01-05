from tkinter import *
from tkinter import ttk

class CalendarView :

    __calendar = None

    def create_text (
        self,
        handler_get_data_year,
        handler_get_data_month
        ) :
        data_text = handler_get_data_year( handler_get_data_month )
        
        CalendarView.__calendar = Text( bd = 3, height = 33, width = 42 )
        CalendarView.__calendar.place( x = 1, y = 42)

        ys = ttk.Scrollbar( orient = "vertical", command = CalendarView.__calendar.yview )
        ys.place( height = 535, x = 343, y = 45 )

        CalendarView.__calendar["yscrollcommand"] = ys.set

        CalendarView.__calendar.insert( '1.0', data_text )

    def change_value_calendar ( self, data_text ) :
        CalendarView.__calendar.replace("1.0", END, data_text)
