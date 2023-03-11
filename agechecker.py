# Import necessary modules
import datetime
import sys
from dateutil.relativedelta import relativedelta

# Get user's selection
selection = input("""What would you like to do?
    (1) Get someones age by birthdate
    (2) Get someones birth year by age
    (3) Get someones age on a specific date
    (4) Exit
    Selection: """)

# Define function to get age based on birthdate
def get_age():
    # Get person's name and birthdate from user input
    name = input("\nWhat's the persons name?:\n")
    month,day,year = input("When's their birthday? (Format: X/X/XXXX):\n").split('/')
    monthnow,daynow,yearnow = input("Todays date? (Format: X/X/XXXX):\n").split('/')
    # Convert birthdate and current date to datetime.date objects
    birthdate = datetime.date(int(year), int(month), int(day))
    today = datetime.date(int(yearnow), int(monthnow), int(daynow))
    # Calculate the age and print it
    age = (today - birthdate).days // 365
    print(f"The {name} is {age} years old.")

# Define function to get birth year based on age
def get_birthyear():
    # Get person's name, current date, and age from user input
    name = input("\nWhat's the persons name?:\n")
    monthnow,daynow,yearnow = input("\nTodays date? (Format: X/X/XXXX):\n").split('/')
    today = datetime.date(int(yearnow), int(monthnow), int(daynow))
    age = input("\nHow old are they?\n")
    # Calculate birth year and print it
    birthyear = today - relativedelta(years = int(age))
    print(f"\n{name} was born in {birthyear.year}.\n")

# Define function to get age based on specific date
def get_specificdate():
    # Get person's name, birthdate, and specific date from user input
    name = input("\nWhat's the persons name?:\n")
    month,day,year = input("When's their birthday? (Format: X/X/XXXX):\n").split('/')
    birthdate = datetime.date(int(year), int(month), int(day))
    smonth,sday,syear = input("\nWhat's the specific date you'd like to know the age for? (Format: X/X/XXXX):\n").split('/')
    specificdate = datetime.date(int(syear), int(smonth), int(sday))
    # Calculate the age and print it
    age = (specificdate - birthdate).days // 365
    print(f"On {smonth}/{sday}/{syear}, {name} will be {age} years old.")

# Execute the function based on user's selection
if selection == '1':
    get_age()
elif selection == '2':
    get_birthyear()
elif selection == '3':
    get_specificdate()
elif selection == '4':
    sys.exit("\n Goodbye\n") # Using sys.exit() so I can add a message
