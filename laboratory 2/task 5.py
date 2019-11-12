import re
def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[1-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print("Помилка")
    return value

print("Волошенюк Юрій КМ-94 \nЛаборатора робота №2\nВаріант  №6\n ")

value = do_input_int("Введіть межі піднесенння до квадрату\n")

for i in range(1, value + 1):
    print(i, "*", i, "=", i * i)

print("Робота програми завершена ")