text = str(input("Enter value in mm, cm, and m: "))
goal_unit = input('Enter unit to convert in mm, cm, m: ').strip()

SI = 0.0
value = ''

if text.find('mm') != -1:
    SI = float(text.split('mm')[0])/1000.0
elif text.find('cm') != -1:
    SI = float(text.split('cm')[0])/100.0
elif text.find('m') != -1:
    SI = float(text.split('m')[0])/1.0

if goal_unit == 'mm':
    value = str(SI*1000) + 'mm'
elif goal_unit == 'cm':
    value = str(SI*100) + 'cm'
elif goal_unit == 'm':
    value = str(SI) + 'm'

print('Value after unit conversion is',value)