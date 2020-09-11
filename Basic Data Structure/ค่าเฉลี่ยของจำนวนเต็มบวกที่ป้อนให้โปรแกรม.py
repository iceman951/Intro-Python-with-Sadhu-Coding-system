number = []
value = 0
while(value>=0):
    value = int(input('Enter number: '))
    if value < 0 : break
    number.append(value)
print('Minimum number is', min(number))
print('Maximum number is', max(number))