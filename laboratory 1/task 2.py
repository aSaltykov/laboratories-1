import re

def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}(\.[0-9]{1,})?$', value)):
            flag = False
            value = int(value)
        else:
            print("Помилка")
    return value

print("Волошенюк Юрій КМ-94 \nЛаборатора робота №1\nВаріант  №6\n ")

value_1 = do_input_int("Введіть перше число\n")
value_2 = do_input_int("Введіть друге число\n")
if value_1 != value_2:
    if value_1 > value_2:
        value_2 = value_1
    else:
        value_1 = value_2
else:
    value_1 = 0
    value_2 = 0
print("a =", value_2 ,"b =",value_2)