import math
x1 = float(input("Введите значение первой переменной: "))
x2 = float(input("Введите значение второй переменной: "))
x3 = float(input("Введите значение третьей переменной: "))
x4 = float(input("Введите значение четвертой переменной: "))
x5 = float(input("Введите значение пятой переменной: "))

x1_sin = str("{0:.2f}".format(math.sin(x1)))
x1_factorial = str("{0:.2f}".format(math.factorial(x1)))
x1_exp = str("{0:.2f}".format(math.exp(x1)))
x1_log = str("{0:.2f}".format(math.log10(x1)))
x1_pow_y = int(input("Введите степень для х1: "))
x1_pow = str("{0:.2f}".format(math.pow(x1, x1_pow_y)))

print("Функции для х1:" + x1_sin + " - это функция синуса - возвращает синус значения" + "; " + "\n"
      + x1_factorial + " - это функция факториала" + "; " + "\n"
      + x1_exp  + " - функция экспоненты в степени х1" + "; " + "\n"
      + x1_log + " - функция логарифма по основанию 10" + "; " + "\n"
      + x1_pow + " - функция вычисляет значения х1 в степени у")

print("---------------")

x2_sin = str("{0:.2f}".format(math.sin(x2)))
x2_factorial = str("{0:.2f}".format(math.factorial(x2)))
x2_exp = str("{0:.2f}".format(math.exp(x2)))
x2_log = str("{0:.2f}".format(math.log10(x2)))
x2_pow_y = int(input("Введите степень для х2: "))
x2_pow = str("{0:.2f}".format(math.pow(x2, x2_pow_y)))

print("Функции для х2:" + x2_sin + " - это функция синуса - возвращает синус значения" + "; " + "\n"
      + x2_factorial + " - это функция факториала" + "; " + "\n"
      + x2_exp  + " - функция экспоненты в степени х2" + "; " + "\n"
      + x2_log + " - функция логарифма по основанию 10" + "; " + "\n"
      + x2_pow + " - функция вычисляет значения х2 в степени у")

print("---------------")

x3_sin = str("{0:.2f}".format(math.sin(x3)))
x3_factorial = str("{0:.2f}".format(math.factorial(x3)))
x3_exp = str("{0:.2f}".format(math.exp(x3)))
x3_log = str("{0:.2f}".format(math.log10(x3)))
x3_pow_y = int(input("Введите степень для х3: "))
x3_pow = str("{0:.2f}".format(math.pow(x3, x3_pow_y)))

print("Функции для х3:" + x3_sin + " - это функция синуса - возвращает синус значения" + "; " + "\n"
      + x3_factorial + " - это функция факториала" + "; " + "\n"
      + x3_exp  + " - функция экспоненты в степени х3" + "; " + "\n"
      + x3_log + " - функция логарифма по основанию 10" + "; " + "\n"
      + x3_pow + " - функция вычисляет значения х3 в степени у")

print("---------------")

x4_sin = str("{0:.2f}".format(math.sin(x4)))
x4_factorial = str("{0:.2f}".format(math.factorial(x4)))
x4_exp = str("{0:.2f}".format(math.exp(x4)))
x4_log = str("{0:.2f}".format(math.log10(x4)))
x4_pow_y = int(input("Введите степень для х4: "))
x4_pow = str("{0:.2f}".format(math.pow(x4, x4_pow_y)))

print("Функции для х4:" + x4_sin + " - это функция синуса - возвращает синус значения" + "; " + "\n"
      + x4_factorial + " - это функция факториала" + "; " + "\n"
      + x4_exp  + " - функция экспоненты в степени х4" + "; " + "\n"
      + x4_log + " - функция логарифма по основанию 10" + "; " + "\n"
      + x4_pow + " - функция вычисляет значения х4 в степени у")

print("---------------")

x5_sin = str("{0:.2f}".format(math.sin(x5)))
x5_factorial = str("{0:.2f}".format(math.factorial(x5)))
x5_exp = str("{0:.2f}".format(math.exp(x5)))
x5_log = str("{0:.2f}".format(math.log10(x5)))
x5_pow_y = int(input("Введите степень для х5: "))
x5_pow = str("{0:.2f}".format(math.pow(x5, x5_pow_y)))

print("Функции для х5:" + x5_sin + " - это функция синуса - возвращает синус значения" + "; " + "\n"
      + x5_factorial + " - это функция факториала" + "; " + "\n"
      + x5_exp  + " - функция экспоненты в степени х5" + "; " + "\n"
      + x5_log + " - функция логарифма по основанию 10" + "; " + "\n"
      + x5_pow + " - функция вычисляет значения х5 в степени у")

print("---------------")

print ("Индивидуальное задаение")
print("---------------")

x = int(input("Введите значение х: "))
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
d = int(input("Введите значение d: "))
c = int(input("Введите значение c: "))
if (x < 10):
    fi = math.tan(x / (3 + a)) - math.log(b*3 + 7)
    print (fi)
else:
    omega = c * math.cbrt(x**2 + (d * 3)**1.2)
    print(omega)
    