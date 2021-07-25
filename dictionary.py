# Dictionary in Python
dict1 = {key:value}
dict2 = {key1:value1, key2:value2, key3:vaule3}
dict3 = {"key": "value"} ## string type key

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

#Retreiving item in Dictionary 
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

#Adding new item into Dicionary 
programming_dictionary["Loop"] = "The action of somethinng do it over and over again"

print(programming_dictionary)

#Create empty ditctionary
empty_dict = {}

# wipe out a dictionary
print(programming_dictionary)
programming_dictionary = {}
print(programming_dictionary)

#Editing item in a dictionary
programming_dictionary["Bug"] = "It's a Bug of wrong code"
print(programming_dictionary)

#Loop item in a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
