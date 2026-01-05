from tkinter import *

class ButtonReduceYearView :
    __window = None

    def __init__ ( self, window ) :
        ButtonReduceYearView.__window = window

    def create_button ( self, handler_reduce_year ) :
        button = Button(
            ButtonReduceYearView.__window,
            text = '<',
            command = handler_reduce_year
            )

        button.place( x = 230, y = 10 )
