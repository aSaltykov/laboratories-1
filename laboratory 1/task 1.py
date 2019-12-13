import re


def do_input_float(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}(\.[0-9]{1,})?$', value)):
            flag = False
            value = float(value)
        else:
            print("Помилка")
    return value


print("Волошенюк Юрій КМ-94 \nЛаборатора робота №1\nВаріант  №6\n")
value = do_input_float("Введіть значення температури в градусах Цельсія\n")
value= value*9/5+32

print("Значення температури в градусах Фаренгейта =" ,value)
print ("Юра привет")