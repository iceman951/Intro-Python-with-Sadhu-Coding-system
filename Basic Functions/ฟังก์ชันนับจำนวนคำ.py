def word_count(words):
    result = len(words.split()) 
    return result

count = 0
while True:
    row = str(input('Enter text: '))
    if row == 'end':
        break
    count += word_count(row)
print('Got',count,'words')