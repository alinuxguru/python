def greet():
  print("Hello, ")
  print("Good Morning!")
  print("Have a nice day!")

greet()

def greet_with_name(name):
  print(f"Hi, {name}")
  print(f"How do you do {name}?")

greet_with_name("Santhakumar")

def greet_with(name, location):
  print(f"Hi, {name} ")
  print(f"Do you like this place, {location}")

greet_with("Santhakumar", "Kumbakonam")

# parameter is name of arguments, here 'name' is a parameter
# Arguments is actual one, Santhakumar is an argument


#function with keyword arguments
def greet_with(name, location):
  print(f"Hi, {name} ")
  print(f"Do you like this place, {location}")

greet_with(name="Sathakumar", location="Kudandhai") ## name="Santhakumar" is a keyword argument
