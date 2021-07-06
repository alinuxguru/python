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


combined_string = name1 + name2 

t = combined_string.lower().count('t')
r = combined_string.lower().count('r')
u = combined_string.lower().count('u')
e = combined_string.lower().count('e')

true = t + r + u + e
#print(true)

l = combined_string.lower().count('l')
o = combined_string.lower().count('o')
v = combined_string.lower().count('v')
e = combined_string.lower().count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
  print(f"Your love_score is {love_score}, you go together like coke and mentos")
elif love_score >40 and love_score <50:
  print(f"Your love_score is {love_score}, you are alright together.")
else:
  print(f"Your love_score is {love_score}")
