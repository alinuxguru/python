height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#print(height)
bmi = round(weight / (height ** 2))
print(bmi)

if bmi < 18.5:
  print("Your BMI is 18, you are underweight.")
elif bmi > 18.5 and bmi < 25:
  print("Your BMI is 22, you have a normal weight.")
elif bmi > 25 and bmi < 30:
  print("Your BMI is 28, you are slightly overweight") 
elif bmi > 30 and bmi < 35:
  print("Your BMI is 33, you are obese.") 
else:
  print("Your BMI is 40, you are clinically obese")  

