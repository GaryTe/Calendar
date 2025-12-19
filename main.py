from date_time_model import *
from master_presenter import *
from date_time_counter_view import *

date_time_model = DateTimeModel()
date_time_counter_view = DateTimeCounterView(date_time_model)
master_presenter = MasterPresenter(date_time_model, date_time_counter_view)

master_presenter.initialization()
date_time_counter_view.coll_counter()
