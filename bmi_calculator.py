height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
conv_height = float(height)
conv_weight = float(weight)
#print(type(conv_height))
bmi_value = conv_height / (conv_weight * conv_weight)
print(int(bmi_value))
