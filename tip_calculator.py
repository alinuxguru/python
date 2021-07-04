#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator")
bill = int(input("What was the total bill: "))
tip_percentage = int(input("What percentage tip would you like to give?, 10, 12 or 15?:"))
people = int(input("How many people to split the bill: "))
#bill = 150
if (tip_percentage == 10):
  each_person_pay = (bill / people) * 1.10
elif (tip_percentage == 12):
  each_person_pay = (bill / people) * 1.12
else:
  each_person_pay = (bill  / people) * 1.15  

#each_person_pay = (150.00 / 5) * 1.12
#decimal_place = round(each_person_pay,2)
decimal_place = "{:.2f}".format(each_person_pay)
print(f"Each person pay: {decimal_place}" )
