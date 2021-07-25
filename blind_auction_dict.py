from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bid_dictionary = {}
wish = True

def find_bid_winner(name, bid):
  
    bid_dictionary[name] = bid
    #bid_dictionary["bid_price"] = bid
    #print(bid_dictionary)


while wish:

  bider_name = input("Please type your name: ")
  bider_price = int(input("Please enter your Bid Price(in $): "))
  find_bid_winner(name = bider_name, bid = bider_price)
  clear()
  continue_bid = input("If other user wants to bid? yes/no: ").lower()

  if continue_bid == 'no' or continue_bid != 'yes':
    max = 0
    for key in bid_dictionary:
      if max < bid_dictionary[key]:
        max = bid_dictionary[key]
    print(f"The bid winner is {key}")    
    #print(max)    
    wish = False
   
  else:
    find_bid_winner(name = bider_name, bid = bider_price)

print(bid_dictionary)
