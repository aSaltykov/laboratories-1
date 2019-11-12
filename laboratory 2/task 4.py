import re
print("Волошенюк Юрій КМ-94 \nЛаборатора робота №2\nВаріант  №6\n ")
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

def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print("Помилка")
    return value

value = do_input_float("Введіть значення х \n")

number = do_input_int("Введіть кількість операцій \n")

sum = 0
for i in range(1, number):
    sum = sum + (value - i) / i ** 2
print("Сума =", round(sum, 4))



