from tkinter import *

class ButtonIncreaseYearView :
    __window = None

    def __init__ ( self, window ) :
        ButtonIncreaseYearView.__window = window

    def create_button ( self, handler_increase_year ) :
        button = Button(
            ButtonIncreaseYearView.__window,
            text = '>',
            command = handler_increase_year
            )

        button.place( x = 250, y = 10 )
