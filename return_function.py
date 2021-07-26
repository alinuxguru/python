def reprint_my_name(first_name, last_name):
  if first_name == '' or last_name == '':
    return "You didn't provide valid inputs"
 
  f_name = first_name.title() 
  l_name = last_name.title()
  return f"{f_name} {l_name}"
  

output = reprint_my_name("Santhakumar", "palraj")
print(output)
print(reprint_my_name(input("What is your first name?: "), input("What is your last name?: ")))
