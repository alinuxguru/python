def reprint_my_name(first_name, last_name):
  f_name = first_name.title() 
  l_name = last_name.title()
  return f"{f_name} {l_name}"
  

output = reprint_my_name("Santhakumar", "palraj")
print(output)
print(reprint_my_name("Santhakumar", "pAlrAJ"))
