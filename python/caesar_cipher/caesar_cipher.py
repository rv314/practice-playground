# letter list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#################################################################
def caesar(direction, plain_text, shift_amount):
  if direction == 'encode':
    text_list = []
    for t in plain_text:
      text_list.append(t)

    for idx, value in enumerate(text_list):
      if value in alphabet:
        pos = alphabet.index(value)
        new_pos = pos + shift
        if new_pos > 25:
          reset_pos = new_pos - 25
          text_list[idx] = alphabet[reset_pos]
        else:
          text_list[idx] = alphabet[new_pos]
    encrypted_message = ''.join(text_list)
    print(f"Encrypted message is '{encrypted_message}'")
  elif direction == 'decode':
    encrypt_list = []
    for e in plain_text:
      encrypt_list.append(e)
    for idx, value in enumerate(encrypt_list):
      if value in alphabet:
        pos = alphabet.index(value)
        new_pos = pos - shift
        if new_pos < 0:
          reset_pos = new_pos + 25
          encrypt_list[idx] = alphabet[reset_pos]
        else:
          encrypt_list[idx] = alphabet[new_pos]
    decrypted_message = ''.join(encrypt_list)
    print(f"Decrypted message is '{decrypted_message}'")

##################################################################
caesar(direction=direction, plain_text=text, shift_amount=shift)