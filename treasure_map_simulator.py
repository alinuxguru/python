# 🚨 Don't change the code below 👇
row1 = ["s","e","n"]
row2 = ["3","4","5"]
row3 = ["u","i","d"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")

#print(map[]) # 23 -->
horizonal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
#print(selected_row)
selected_row[horizonal - 1] = "X" ## simpleway, map[vertical - 1][horizonal - 1] = "X"

#print(selected_row)

print(f"{row1}\n{row2}\n{row3}")
