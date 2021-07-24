alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  encoded = []
  for z in text:
    indexx = (alphabet.index(z)) + shift
    if indexx > 25:
      indexx = indexx - 26
      encoded.append(alphabet[indexx])
    else:

      encoded.append(alphabet[indexx])

  print(f"{''.join(encoded)}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
  decoded = []
  for z in text:
    indexx = (alphabet.index(z)) - shift
    decoded.append(alphabet[indexx])
  print(f"{''.join(decoded)}")  



  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

if direction == 'encode':
  encrypt(text, shift)
else:
  decrypt(text, shift)  
