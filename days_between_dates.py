from datetime import datetime

def calculate_days_between():
    try:
        # Ask the user for the first date
        date1_str = input("Enter the first date (DD/MM/YYYY): ")
        # Ask the user for the second date
        date2_str = input("Enter the second date (DD/MM/YYYY): ")
        
        # Convert the input strings to datetime objects
        date1 = datetime.strptime(date1_str, "%d/%m/%Y")
        date2 = datetime.strptime(date2_str, "%d/%m/%Y")
        
        # Calculate the difference in days
        difference = abs((date2 - date1).days)
        
        # Print the number of days between the two dates
        print(f"The number of days between {date1_str} and {date2_str} is {difference} days.")
    
    except ValueError:
        print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
calculate_days_between()


