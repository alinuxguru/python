age = input("What is your current age?")
rest_age = 90 - int(age)  ## calculate life time as 90 years
#print(type(rest_age))
remaining_days = rest_age * 365 # a year has 365 days,52 weeks, 12 months
remaining_weeks = rest_age * 52 
remaining_months = rest_age * 12
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left")
