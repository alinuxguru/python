for z in range(1,101):
  if z % 3 == 0 and z % 5 == 0:
    print("FizzBuzz")
  elif z % 3 == 0:
    print("Fizz")  
  elif z % 5 == 0:
    print("Buzz") 
  else:
    print(z)
