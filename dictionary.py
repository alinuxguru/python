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
  
#Nesting 
dict1 = {key = [list],
        key2 = {dict}
        }

#Nesting a list in a Dict
travel_history = {
  "India" = ["Chennai" ,"Delhi", "Mumbai"],
  "Spain" = ["Madrid", "Bareclona", "Sevillia"],
}
  
#Nesting a dictionary in a Dictionary
travel_history = {
  "India" = {"cities_visited" : ["Chennai" ,"Delhi", "Mumbai"], "total_visits" : 2},
  "Spain" = {"cities_visited" : ["Madrid", "Bareclona", "Sevillia"], "total_visits" : 5},  
}  

#Nesting a dictionary in a list
# a list travel_history has two items, which are dictionaries
travel_history = [
  {"country" : "India", "cities_visites" : ["Chennai" ,"Delhi", "Mumbai"], "total_visits" : 2},
  {"country" : "Spain", "cities_visited" : ["Madrid", "Bareclona", "Sevillia"], "total_visits" : 5}, 
]

#Separate a aboce list to easy ready

travel_history = [
  {
    "country" : "India", 
    "cities_visites" : ["Chennai" ,"Delhi", "Mumbai"],
    "total_visits" : 2
  },
  {
    "country" : "Spain", 
    "cities_visited" : ["Madrid", "Bareclona", "Sevillia"], 
    "total_visits" : 5
  }  
]

