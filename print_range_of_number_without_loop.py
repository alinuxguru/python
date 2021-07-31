#Print 1 to 100

#Print 1 to 100 without loop 
def print_number(num):
    if num > 0:
        print_number(num - 1)
        print(num)

print_number(100)        

#or 

print([*range(1, 101)])

#or 
print([*range(True,ord("e"))])
