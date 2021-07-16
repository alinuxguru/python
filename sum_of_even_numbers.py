total = 0
for z in range(0, 101, 2):
  total += z
  #print(z)
print(total)

sum = 0
for z in range(2, 101, 2):
  sum += z 
  #print(z)
print(sum)  

sum2 = 0
for z in range(1,101):
  if z % 2 == 0:
    sum2 += z 
print(sum2) 
