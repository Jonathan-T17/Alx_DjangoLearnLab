from datetime import datetime, timedelta

# Current date and time function
def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    date_format = "%Y-%m-%d %H:%M:%S"
    print("Current Date and Time:", current_date.strftime(date_format))
    return current_date  # return so we can reuse it later

# Calculate a future date function
def calculate_future_date(current_date):
    """Calculate and display the future date after adding user-specified days."""
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)
        date_format = "%Y-%m-%d"
        print("Future Date (after", number_of_days, "days):", future_date.strftime(date_format))
    except ValueError:
        print(" Please enter a valid integer.")

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
