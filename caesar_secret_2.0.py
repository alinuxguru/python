alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(text, shift):
  output = []
  for z in text:
    indexx = (alphabet.index(z))
    if direction == 'encode':

      indexx = (alphabet.index(z)) + shift
      if indexx > 25:
        indexx = indexx - 26
        output.append(alphabet[indexx])
      else:
        output.append(alphabet[indexx])

    # elif direction == 'decode':

    elif direction == 'decode':
      indexx -= shift
      output.append(alphabet[indexx])
  
  print(f"{''.join(output)}") 
    
caesar(text, shift)

      
