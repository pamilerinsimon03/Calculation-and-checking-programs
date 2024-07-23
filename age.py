print("This program calculates how much time you have left on earth")
age = input("Enter your current age: ")
expected_years = 90
years_left = expected_years - int(age)
expected_days = years_left * 365
expected_weeks = years_left * 52
expected_months = years_left * 12
print(f"You have {years_left} years, {expected_days} days, {expected_weeks} weeks, and {expected_months} months left.")