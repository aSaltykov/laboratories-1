import re

def do_float(message):
    flag = False
    while not flag:
        value = input(message)
        if bool(re.match('^[+-]{0,1}[0-9]{1,}(\.[0-9]{1,}){0,1}$', value)):
            flag = True
            value = float(value)
        else:
            print("Помилка")
    return value
print("Волошенюк Юрій КМ-94 \nЛаборатора робота №1\nВаріант  №6\n ")

x = do_float("Введіть значення x\n")

if x<=7:
  Fx=3*x-9
else:
   Fx=1/(x**2-4)

print("F(x) =", round(Fx, 6))