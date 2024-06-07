import pandas as pd
from datetime import datetime, timedelta

class dateProcess:

    def __init__(self):
        pass 

    def get_first_day_of_current_month(self):

        current_date = datetime.today()

        first_day_of_current_month = current_date.replace(day=1)

        return first_day_of_current_month

    def get_last_day_of_previous_month(self):

        first_day_of_current_month = self.get_first_day_of_current_month()

        last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)

        return last_day_of_previous_month
    
    def get_string_last_day_of_previous_month(self, date_format: str):

        last_day_of_previous_month = self.get_last_day_of_previous_month()

        string_output = last_day_of_previous_month.strftime(date_format)

        return string_output
    
    def generate_date_range_to_current_time(self, starting_year: int, starting_month: int, starting_date: int):

        start_date = datetime(starting_year, starting_month, starting_date)
        end_date = datetime.now()

        date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days+1)]
        date_df = pd.DataFrame({'date': date_list})

        return date_list, date_df


d = dateProcess()
date = d.get_string_last_day_of_previous_month("%Y-%m-%d")
date_list, date_df = d.generate_date_range_to_current_time(2024, 6, 1)
print(date_df)