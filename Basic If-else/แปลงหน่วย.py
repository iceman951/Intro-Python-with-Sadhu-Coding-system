import re

def unit_converter(val, unit_in, unit_out):
    unit = {'mm':0.001, 'cm':0.01, 'm':1.0}
    return val*unit[unit_in]/unit[unit_out]

value = str(input("Enter value in mm, cm, and m: "))
goal_unit = str(input("Enter unit to convert in mm, cm, m: "))
value_unit = ''.join(c for c in value if c.isalpha())
digit_value = re.findall(r"[-+]?\d*\.\d+|\d+", value)
result_number = unit_converter(float(digit_value[0]), value_unit, goal_unit)
txt =  "Value after unit conversion is {:.1f}" + goal_unit
print(txt.format(result_number))