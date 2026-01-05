from tkinter import *

class LabelYearView :
    __get_year = ''
    
    __window = None
    __label = None

    def __init__ ( self, get_year, window ) :
        LabelYearView.__get_year = get_year
        LabelYearView.__window = window

    def create_label ( self ) :
        year = LabelYearView.__get_year()
        
        LabelYearView.__label = Label( LabelYearView.__window, text = f'{year} год' )
        LabelYearView.__label.place( x = 1, y = 1 )

    def change_value_label ( self, year ) :
        LabelYearView.__label.config( text = f'{year} год' )
