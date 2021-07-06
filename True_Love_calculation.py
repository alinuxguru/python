#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number. 
e.g. 
/*`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53." */


lower_name1 = name1.lower()
#print(type(lower_name1))
lower_name2 = name2.lower()
#count1 = 0
count2 = 0

count1 = int(lower_name1.count('t')) + int(lower_name1.count('r')) + int(lower_name1.count('u')) + int(lower_name1.count('e'))
#count1 = "lower_name1".count('t') + lower_name1.count('r') + lower_name1.count('u') + lower_name1('e')

count2 = int(lower_name2.count('t')) + int(lower_name2.count('r')) + int(lower_name2.count('u')) + int(lower_name2.count('e'))
#print(count1 + count2)
first = count1 + count2

count3 = int(lower_name1.count('l')) + int(lower_name1.count('o')) + int(lower_name1.count('v')) + int(lower_name1.count('e'))

count4 = int(lower_name2.count('l')) + int(lower_name2.count('o')) + int(lower_name2.count('v')) + int(lower_name2.count('e'))

second = count3 + count4 

final_value = str(first) + str(second)
print(final_value)
score = int(final_value)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos")
elif score >40 and score <50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")




