height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
conv_height = float(height)
conv_weight = float(weight)
#print(type(conv_height))
bmi_value = round(weight / (height ** 2))
print(int(bmi_value))
