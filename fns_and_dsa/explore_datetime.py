from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.now()
    print(f"current date and time:{current_date}")

def calculate_future_date():
    no_of_days = int(input("Enter the number of days to add to the current date: "))
    no_of_days = timedelta(days=no_of_days)
    future_date = current_date + no_of_days
    print(f"Future date: {future_date}")



if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()