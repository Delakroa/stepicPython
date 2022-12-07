# Тема урока: условный оператор

# Вложенные условия
# Каскадные условия
# Решение задач
# Аннотация. Изучим вложенный и каскадный условный оператор.
#
# Вложенный оператор
# Внутри условного оператора можно использовать любые инструкции языка Python, в том числе и условный оператор.
# Получаем вложенное ветвление: после одной развилки в ходе исполнения программы появляется другая развилка.
# При этом вложенные блоки имеют больший размер отступа (+4 пробела для каждого следующего уровня).

# if условие1:
#     блок кода
# else:
#     if условие2:
#         блок кода
#     else:
#         if условие3:
#             блок кода
#         ...

# В предыдущем уроке мы разбирали задачу об определении координатной четверти точки. Программу можно переписать
# с использованием вложенного оператора:

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')

# В данном случае уровень вложенности равен двум, так что программа одинаково хорошо читается как с помощью
# использования логического оператора and, так и с помощью вложенного оператора.
#
# Рассмотрим программу, которая переводит стобалльную оценку в пятибалльную. Для её реализации нужно воспользоваться
# вложенным условным оператором:

grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

# В этом примере уровень вложенности настолько глубок, что код становится трудно понять.
#
# Выбор из нескольких альтернатив – это обычное дело, здесь имеет смысл избегать глубокого вложения.
# Для этого в Python есть каскадный условный оператор.
#
# Мы не могли написать 5 независимых if-ов, поскольку в таком случае было бы напечатано сразу несколько значений
# пятибалльной оценки.

# -----------------------------------------------------------------------------------------------------------------

# Каскадный условный оператор

# Если требуется проверить несколько условий, в языке Python используется каскадный условный оператор.
#
# Синтаксис каскадного условного оператора имеет следующий вид:
#
# if условие1:
#     блок кода
# elif условие2:
#     блок кода
# ...
# else:
#     блок кода

# При исполнении такого условного оператора сначала проверяется условие 1. Если оно является истинным,
# то исполняется блок кода, который следует сразу после него, вплоть до выражения elif. Остальная часть
# конструкции игнорируется. Однако если условие 1 является ложным, то программа перескакивает непосредственно к
# следующему выражению elif и проверяет условие 2. Если оно истинное, то исполняется блок кода, который следует сразу
# после него, вплоть до следующего выражения elif. И остальная часть условного оператора тогда игнорируется.
# Этот процесс продолжается до тех пор, пока не будет найдено условие, которое является истинным, либо пока больше
# не останется выражений elif. Если ни одно условие не является истинным, то исполняется блок кода после выражения else.

# Приведенный ниже фрагмент кода является примером каскадного условного оператора if-elif-else. Этот фрагмент кода
# работает так же, как предыдущий код, использующий вложенный условный оператор.

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

# Обратите внимание на выравнивание и выделение отступом, которые применены в инструкции if-elif-else: выражения
# if, elif и else выравнены и исполняемые по условию блоки выделены отступом.
#
# Инструкция if-elif-else не является обязательной, потому что ее логика может быть запрограммирована вложенными
# инструкциями if-else. Однако длинная серия вложенных инструкций if-else имеет два характерных недостатка:
#
# программный код может стать сложным и трудным для восприятия;
# из-за необходимого выделения отступом продолжительная серия вложенных инструкций if-else может стать слишком длинной,
# чтобы целиком уместиться на экране монитора без горизонтальной прокрутки.
# Логика инструкции if-elif-else обычно прослеживается легче, чем длинная серия вложенных инструкций if-else.
# И поскольку в инструкции if-elif-else все выражения выровнены, длина строк в данной инструкции, как правило, короче.

# Запомни. Заключительный блок else в операторе if-elif-else является необязательным.

# ------------------------------------------------------------------------------------------------------------------

# Решение задач

# Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
#
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:
#
# 1 способ. Использование вложенного условного оператора.

a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

# 2 способ. Использование каскадного условного оператора.

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)

# 3 способ. Использование каскадного условного оператора и логического оператора or.

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)

# -------------------------------------------------------------------------------------------------------------------

# Гонка спидстеров
# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать без причины,
# и узнать у своего друга Циско Рамона есть ли смысл принимать вызов. Циско получил данные, что скорость
# Зума равна nn, а скорость Флэша равна kk.
#
# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.
#
# Формат входных данных
# На вход программе подаётся два целых числа nn и kk, скорость Зума и Флэша.
#
# Формат выходных данных
# Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно
# вывести "Don't know".

speed_k, speed_n = int(input()), int(input())
if speed_k > speed_n:
    print('NO')
elif speed_k < speed_n:
    print('YES')
else:
    print("Don't know")

# ----------------------------------------------------------------------------------------------------------------

# Вид треугольника

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого
# равны введенным числам.
#
# Формат входных данных
# На вход программе подаются три числа – длины сторон существующего треугольника.
#
# Формат выходных данных
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

a, b, c = int(input()), int(input()), int(input())
if a == b != c or a != b == c or a == c != b:
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
else:
    print('Разносторонний')

# -------------------------------------------------------------------------------------------------------------------

# Среднее число

# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
#
# Формат входных данных
# На вход программе подаётся три различных целых числа, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести среднее число.
#
# Примечание. Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.

a, b, c = int(input()), int(input()), int(input())
if b > a > c or b < a < c:
    print(a)
elif a > b > c or a < b < c:
    print(b)
elif b > c > a or b < c < a:
    print(c)

# Второй вариант:

a, b, c = int(input()), int(input()), int(input())
if c < a:
    a, c = c, a
if b < a:
    a, b = b, a
if c < b:
    b, c = c, b
print(b)

# ------------------------------------------------------------------------------------------------------------------

# Количество дней

# Дан порядковый номер месяца (1,2,…, 12). Напишите программу, которая выводит на экран количество
# дней в этом месяце. Принять, что год является невисокосным.
#
# Примечание. Постарайтесь написать программу, так чтобы в ней было не более трех условий.
#
# Формат входных данных
# На вход программе подаётся одно целое число – порядковый номер месяца.
#
# Формат выходных данных
# Программа должна вывести количество дней в этом месяце.

# Мой вариант:

month = int(input())
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(31)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(28)

# Второй вариант:

a = int(input())
if a in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif a in (4, 6, 9, 11):
    print(30)
elif a == 2:
    print(28)

# ----------------------------------------------------------------------------------------------------------------

# Церемония взвешивания
# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех
# весовых категорий:
#
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.
#
# Формат входных данных
# На вход программе подаётся одно целое число.
#
# Формат выходных данных
# Программа должна вывести текст – название весовой категории.

the_weight = int(input())
if the_weight < 60:
    print('Легкий вес')
elif the_weight < 64:
    print('Первый полусредний вес')
elif the_weight < 69:
    print('Полусредний вес')

# ----------------------------------------------------------------------------------------------------------------

# Самописный калькулятор

# Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением
# одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым
# ранее числам, в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите
# текст «На ноль делить нельзя!».
#
# Формат входных данных
# На вход программе подаются два целых числа, каждое на отдельной строке, и строка.
#
# Формат выходных данных
# Программа должна вывести результат применения операции к введенным числам или соответствующий текст, если операция
# неверная либо если происходит деление на ноль.

x, z, y = int(input()), int(input()), str(input())
if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    if z != 0:
        print(x / z)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')

# ----------------------------------------------------------------------------------------------------------

# Цветовой микшер

# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит
# что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.
#
# Формат входных данных
# На вход программе подаются две строки, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.
#
# Примечание 1. Если смешать красный и красный, то получится красный и т.д

a, b = str(input()), str(input())

if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print('фиолетовый')

elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
    print('оранжевый')

elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
    print('зеленый')

elif a == 'красный' and b == 'красный':
    print('красный')

elif a == 'синий' and b == 'синий':
    print('синий')

elif a == 'желтый' and b == 'желтый':
    print('желтый')

else:
    print('ошибка цвета')

# ----------------------------------------------------------------------------------------------------------

# Цвета колеса рулетки.

# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
#
# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным
# или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне
# диапазона от 0 до 36.
#
# Формат входных данных
# На вход программе подаётся одно целое число.
#
# Формат выходных данных
# Программа должна вывести цвет кармана либо сообщение «ошибка ввода», если введённое число лежит вне диапазона
# от 0 до 36.

# Первый вариант

x = int(input())
if x == 0:
    print("зеленый")
elif 1 <= x <= 10:
    if x % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= x <= 18:
    if x % 2 == 0:
        print("красный")
    else:
        print("черный")
elif 19 <= x <= 28:
    if x % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 29 <= x <= 36:
    if x % 2 == 0:
        print("красный")
    else:
        print("черный")
else:
    print("ошибка ввода")

# Второй вариант

x = int(input())
if x == 0:
    print("зеленый")
elif (1 <= x <= 10 or 19 <= x <= 28) and x % 2 == 0:
    print('черный')
elif (1 <= x <= 10 or 19 <= x <= 28) and x % 2 != 0:
    print('красный')
elif (11 <= x <= 18 or 29 <= x <= 36) and x % 2 == 0:
    print('красный')
elif (11 <= x <= 18 or 29 <= x <= 36) and x % 2 != 0:
    print('черный')
else:
    print('ошибка ввода')


# Вариант c платформы

x = int(input())
if 0 <= x < 37:
    if (0 < x < 11 or 18 < x < 29) and x % 2 or (10 < x < 19 or 28 < x < 37) and x % 2 == 0:
        print('красный')
    elif x == 0:
        print('зеленый')
    else:
        print('черный')
else:
    print('ошибка ввода')

# ----------------------------------------------------------------------------------------------------------

# Пересечение отрезков

# На числовой прямой даны два отрезка: [a1; b1] и [a2; b2]. Напишите программу, которая находит их пересечение.

# Пересечением двух отрезков может быть:

# - отрезок;
# - точка;
# - пустое множество.

# Формат входных данных
# На вход программе подаются 4 целых числа a1,b1,a2,b2, каждое на отдельной строке. Гарантируется, что a1 < b1 и a2 <
# b2.

# Формат выходных данных
# Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое
# множество».


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a2 > b1 or a1 > b2:
    print('пустое множество')
elif a1 == b2:
    print(a1)
elif a2 == b1:
    print(a2)
else:
    if a1 > a2:
        a2 = a1
    if b1 < b2:
        b2 = b1
    print(a2, b2)

# ----------------------------------------------------------------------------------------------------------

