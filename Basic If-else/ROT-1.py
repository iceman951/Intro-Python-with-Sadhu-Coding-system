text = input("Enter 3 characters: ").upper()
new_text = ''

for c in text:
    if ord(c) == 90:
        new_text = new_text + 'A'
    else:
        new_text = new_text + chr(ord(c)+1)

print("Ciphertext is",new_text)
