def inv(c):
    if 'a' <= c <= 'z':
        return chr(122 - ord(c) + 97)
    if 'A' <= c <= 'Z':
        return chr(90 - ord(c) + 65)
    return c
text = str(input("Enter 5 characters: "))
output = ''.join(inv(c) for c in text)
print("Encryption is",output.lower())