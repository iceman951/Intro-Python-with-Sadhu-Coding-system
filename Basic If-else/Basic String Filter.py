text = str(input('Enter text: '))
filter_word = str(input('Enter filter word: '))
result = '"' + text.replace(filter_word, '*'*len(filter_word)) + '"'
print("Text after filter is",result)