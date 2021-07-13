fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits[-7]) ##Strawberries
print(fruits[-5]) ## Apples
print(frutis[-1]) ## Pears
print(frutis[0]) ##Strawberries

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits) ## ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1]) ##Kale
print(dirty_dozen[0][1]) ##Nectarines
print(dirty_dozen[0][6]) #Pears
print(dirty_dozen[1][4]) #Potatoes
