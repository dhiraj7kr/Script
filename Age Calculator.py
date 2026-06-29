# ==================================================
# File Name: Age_Calculator.py
# Author   : Dhiraj
# Purpose  : Calculate age from date of birth
# ==================================================

from datetime import datetime

# Get user input
birth_date = input("Enter your birth date (DD-MM-YYYY): ")

try:
    # Convert input string to date
    dob = datetime.strptime(birth_date, "%d-%m-%Y")

    # Get today's date
    today = datetime.today()

    # Calculate age
    age = today.year - dob.year

    # Adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print(f"\nYour age is {age} years.")

except ValueError:
    print("\nInvalid date format! Please enter the date as DD-MM-YYYY.")
