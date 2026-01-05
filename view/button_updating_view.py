from tkinter import *

class ButtonUpdatingView :
    __window = None

    def __init__ ( self, window ) :
        ButtonUpdatingView.__window = window

    def create_label ( self, handler_updating_calendar_by_day ) :
        
        button = Button(
            ButtonUpdatingView.__window,
            text = 'Перезапустить календарь',
            command = handler_updating_calendar_by_day
            )
        button.place( x = 55, y = 10 )
