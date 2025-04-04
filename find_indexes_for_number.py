### Enter element to find, display array index number
### if repeated number, print all indexes 
### if not found, "element not found"
elements_list = [5, 5, 3, 5, 3, 6, 6, 8, 9]
user_input = int(input("Please enter number: "))

# if user_input in elements_list:
#     print(f"{user_input} is in list")
# try:
#     index = elements_list.index(user_input)
#     print(f"{user_input} found at index {index}")
# except ValueError:
#     print(f"{user_input} not found in list")  

indices = []
for index, num in enumerate(elements_list):
    if num == user_input:
        indices.append(index)

if indices:
    print(f"{user_input} found at index {indices}")
else:
    print(f"{user_input} not found")    
