from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current time and date: {formatted_date_time}")

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)

    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()

    
