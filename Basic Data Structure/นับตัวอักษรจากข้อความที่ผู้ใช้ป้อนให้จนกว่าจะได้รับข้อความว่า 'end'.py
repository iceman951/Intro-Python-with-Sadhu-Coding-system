counts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
text = ''
sentence =''
while True:
    text = input('Enter string: ').strip().lower()
    if text == 'end': break
    else: sentence += text
for i in range(len(sentence)):
    if sentence[i] >= 'a' and sentence[i] <= 'z':
        index = ord(sentence[i]) -97
        counts[index] += 1
print('''******************************
*     Alphabet Counting      *
******************************''')
for i in range(len(counts)):
    if counts[i] > 0:
        character = chr(ord('a') + i)
        print(character,counts[i])
print('******************************')