# Program to display the names of all months
import calendar

def list_months():
    months = list(calendar.month_name)  # Retrieve month names from the calendar module
    print("Names of the months:")
    for month in months[1:]:
        print(month)

if __name__ == "__main__":
    list_months()
