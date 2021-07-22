import math
#number of cans = (wall height ✖️ wall width) ÷ coverage per can.
def paint_calc(height, width, cover):
  number_of_cans = (height * width) / cover
  print(math.ceil(number_of_cans)) # round of to whole number
  
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
