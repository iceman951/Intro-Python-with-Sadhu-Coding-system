print("""Select 2 options
 - 1 encrypt with ROT 13
 - 2 decrypt with ROT 13
 """)
option = int(input("Choose option: "))
text = input('Enter text: ')
ciphertext = ''
plain = ''

if option == 1:
    for c in text:
        if c >= 'A' and c <= 'Z':
            if chr(ord(c) + 13) <= 'Z':
                ciphertext += chr(ord(c) + 13)
            elif chr(ord(c) + 13) > 'Z':
                ciphertext += chr(ord(c) - 13)
        elif c >= 'a' and c <= 'z':
            if chr(ord(c) + 13) <= 'z':
                ciphertext += chr(ord(c) + 13)
            elif chr(ord(c) + 13) > 'z':
                ciphertext += chr(ord(c) - 13)
        else:
            ciphertext += c
    ciphertext = '\"' + ciphertext + '\"'
    print('Ciphertext is',ciphertext)
elif option == 2:
    for c in text:
        if c >= 'A' and c <= 'Z':
            if chr(ord(c) - 13) >= 'A':
                ciphertext += chr(ord(c) - 13)
            elif chr(ord(c) - 13) < 'A':
                ciphertext += chr(ord(c) + 13)
        elif c >= 'a' and c <= 'z':
            if chr(ord(c) - 13) >= 'a':
                ciphertext += chr(ord(c) - 13)
            elif chr(ord(c) - 13) < 'a':
                ciphertext += chr(ord(c) + 13)
        else:
            ciphertext += c
    ciphertext = '\"' + ciphertext + '\"'
    print('Plaintext is',ciphertext)