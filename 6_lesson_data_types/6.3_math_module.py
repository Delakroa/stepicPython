# ���� �����: ������ math

# 1.������ math
# 2.������� �����

# ���������. ���� �������� ������ math, ������� �������� �������������� ������� �� ������ � ������������� �������.

# ������

# ��� ��� ����������, ����� �� ����������� ����� Python �������� ��������� ������������� �������, ������� ��� �����������
# � ������ � �������������. ����� ������� ��������� � ������. � Python ������� ���������� ���������� �������, �������
# ����� ���������� � ����� ����������

# ������ math

# ������ math � ���� �� ������������ � Python. ���� ������ ������������� �������� ���������� ��� ���������� ����������
# � ������������� ������� (������� � ��������� ������).

# ��� ������������� ���� ������� � ������ ��������� ���������� ���������� ������, ��� �������� �������� import:

import math

# ����������� ���

# ����� ����������� ������ �� ����� ������������ ��� �������. ����� �� �����:

# ��������� \sqrt2 (������ ���������� �� ����);
# ��������� ����� 3.83.8 �� ���������� ������ ����� ����� � ����

# ��������������� ����������� ���, �������� ������ �������� ���:

import math

num1 = math.sqrt(2)     # ���������� ����� ����������� �� ����
num2 = math.ceil(3.8)   # ���������� ����� �����
num3 = math.floor(3.8)  # ���������� ����� ����

print(num1)
print(num2)
print(num3)

# � �������:
#
# 1.4142135623730951
# 4
# 3

# ---------------------------------------------------------------------------------------------------------------

# ����������� ����������� �������

# ��� ����� �������� �� ������� ����, ��� ������ ������� �� ��������� ��������� �������� ������ � ������ �����.
# � ������ �������, ���� ������� ������������ ���������� �����, �� ����� ����� (���������� �������� �������� ������
# � ������� �����) ����� ��������� ��������� � ������� � ����� �����������. ��� ����, ����� �� ��������� ��������
# ������ � ������ ����� ��� ������ �������, �� ����� ��������� ���:

from math import *

num1 = sqrt(2)     # ���������� ����� ����������� �� ����
num2 = ceil(3.8)   # ���������� ����� �����
num3 = floor(3.8)  # ���������� ����� ����

print(num1)
print(num2)
print(num3)

# ����� �������, ����������� ������ ��������� �������:

from math import *

# ��������� �� ������ �������� ������ � ������ �����. ��� ����� ������� �����������, ������������� ���������
# ��� ������� ������ math.

# ���� ����� ������������ ������ ��������� ������� ������, �� �� ����� ������������� ������ �� ��������� �������:

from math import sqrt, ceil

# ������ �� ����� �������� ������� sqrt() � ceil() ��� �������� math., ������ �� �� ����� ������� �������
# floor(), ��� ��� ��� �� ����������:

from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))

print(floor(12.8))  # �������� � ������, ��� ��� ������� floor �� ����������

# ---------------------------------------------------------------------------------------------------------------

# ������ ������� ������ math

# ������ �������� ����� ������������ ������� ������ math:
#
#
# ����������
# int()	��������� ����� � ������� ����
# round(x)	��������� ����� x �� ���������� ������. ���� ������� ����� ����� ����� 0.5, �� ����� �����������
# �� ���������� ������� �����
#
# round(x, n)	��������� ����� x �� n ������ ����� �����
# floor(x)	��������� ����� x ���� (����)
# ceil(x)	��������� ����� x ����� (��������)
# abs(x)	������ ����� x (���������� ��������)

# �����, ���������, ������� � ���������
# sqrt(x)	���������� ������ ����� x
# pow(x, n)	���������� ����� x � ������� n
# log(x)	����������� �������� ����� x. ��������� ������������ ��������� ����� ����� e
# log10(x)	���������� �������� ����� x. ��������� ����������� ��������� ����� ����� 10
# log(x, b)	�������� ����� x �� ��������� b
# factorial(n)	��������� ������������ ����� n

# �������������
# degrees(x)	����������� ���� x, �������� � ��������, � �������
# radians(x)	����������� ���� x, �������� � ��������, � �������
# cos(x)	������� ���� x, ����������� � ��������
# sin(x)	����� ���� x, ����������� � ��������
# tan(x)	������� ���� x, ����������� � ��������
# acos(x)	���������� ���� � �������� �� 00 �� \pi?, cos �������� ����� x
# asin(x)	���������� ���� � �������� �� - \frac{\pi}{2}?2
# atan2(y, x)	�������� ���� (� ��������) ����� � ������������ (x, y)

# !!!��� ���������� ����������� ����� ����� ��������������� ����� n ** 0.5, ������ math.sqrt(n)!!!

# ---------------------------------------------------------------------------------------------------------------

# ������ �������� ������ math

# ������ math ������������� ��� ���������� �������������� ��������:

# pi	����� \pi = 3.141592653589793?=3.141592653589793
# e	����� e = 2.718281828459045e= 2.718281828459045 (��������� ������)

# ����������

# ���������� 1. ��� ������� ������ math ���������� ��������, ������� ����� ������� �� �����, ��������� ������ ����������
# ��� ������������ � �������������� ���������.
#
# ���������� 2. ��� ������������� ������� int(), float(), abs(), min(), max(), round() ���������� ������ math ���
# �������������. ��� ��� ���������� ���������� �������.
#
# ���������� 3. ����� ������� pow(x, n) ����� �������� �������������� ��������� ���������� � �������: x**n.

# ---------------------------------------------------------------------------------------------------------------
# ��������� ����������

# �� ��������� ��������� ���������� ����� ����� �������(x1; y1) � (x2: y2) ������������ ��� p = sqrt (x_1 - x_2) ** 2
# + (y_1 - y_2) ** 2

# �������� ��������� ������������ ��������� ���������� ����� ����� �������, ���������� ������� ������.

# ������ ������� ������
# �� ���� ��������� �������� ������ ������������ �����, ������ �� ��������� ������ - x1, y1, x2, y2

# ������ �������� ������
# ��������� ������ ������� ���� ����� � ��������� ����������.


from math import *
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(p)

# ---------------------------------------------------------------------------------------------------------------

# ������� � �����

# �������� ��������� ������������ ������� ����� � ����� ���������� �� ��������� ������� R.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ������������ ����� R.
#
# ������ �������� ������
# ��������� ������ ������� ��� ����� � ������� ����� � ����� ���������� ������� R.

from math import pi
r = float(input())
s = pi * r ** 2
c = 2 * pi * r
print(s)
print(c)

# ---------------------------------------------------------------------------------------------------------------

# ������� ��������

# � ���������� �������� ��������� ������� ��������:

# ������� �������������� ����� a � b: (a + b) / 2
# ������� �������������� ����� a � b: sqrt(a * b)
# ������� ������������� ����� a � b: (2 * a * b) / (a + b)
# ������� ������������ ����� a � b: sqrt((pow(a, 2) + pow(b, 2)) / 2)

# ������ ������� ������
# �� ���� ��������� �������� ��� ������������ ����� a � b, ������ �� ��������� ������.
#
# ������ �������� ������
# ��������� ������ ������� 4 ����� � ������� ��������������, ��������������, ������������� � ������������.

from math import sqrt, pow
a = float(input())
b = float(input())
arithmetic_mean_of_numbers = (a + b) / 2
geometric_mean_of_numbers = sqrt(a * b)
harmonic_mean_of_numbers = (2 * a * b) / (a + b)
root_mean_square_of_numbers = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(arithmetic_mean_of_numbers)
print(geometric_mean_of_numbers)
print(harmonic_mean_of_numbers)
print(root_mean_square_of_numbers)

# ---------------------------------------------------------------------------------------------------------------

# ������������������ ���������

# �������� ���������, ����������� �������� ������������������� ���������
# sin(x) + cos(x) + pow(tan(x), 2)

# �� ��������� ����� �������� x.
#
# ������ ������� ������
# �� ���� ��������� �������� ���� ������������ ����� x ���������� � ��������.
#
# ������ �������� ������
# ��������� ������ ������� ���� ����� � �������� ������������������� ���������.
#
# ���������� 1. ������������������ ������� ��������� �������� � ��������. ����� ��������� ������� � �������,
# �������������� ��������

# r = (x * pi) / 180

# ���������� 2. ������ math �������� ���������� ������� radians(), ������� ��������� ���� �� �������� � ���� � ��������.

from math import sqrt, pow, radians, pi, cos, sin, tan
x = float(input())
r = (x * pi) / 180  # ��������� �� �������� � ��������
print(sin(r) + cos(r) + pow(tan(r), 2))

# ---------------------------------------------------------------------------------------------------------------

# ��� � �������

# �������� ���������, ����������� �������� ceil(x) + floor(x) �� ��������� ������������� ����� x.

# ������ ������� ������
# �� ���� ��������� �������� ���� ������������ ����� xx.

# ������ �������� ������
# ��������� ������ ������� ���� ����� � �������� ���������� ���������.

# ����������: ceil(x) � ������� �����, floor(x) � ��� �����.

from math import ceil, floor

x = float(input())
print(ceil(x) + floor(x))

# ---------------------------------------------------------------------------------------------------------------

# ���������� ���������

# ���� ��� ������������ ����� aa, bb, cc. �������� ���������, ������� ������� ������������ ����� ����������� ���������
# (a * x) ** 2 + (b * x) + c = 0.

# ������ ������� ������
# �� ���� ��������� �������� ��� ������������ ����� a != 0 b, c, ������ �� ��������� ������.

# ������ �������� ������
# ��������� ������ ������� ������������ ����� ��������� ���� ��� ���������� ��� ����� ���� ������ � ��������� ������.

# ����������. ���� ��������� ����� ��� �����, �� ������� ������� �� � ������� �����������.

from math import *
a = float(input())
b = float(input())
c = float(input())

d = pow(b, 2) - (4 * a * c)
if d > 0:
    x1 = (- b + sqrt(d)) / (2 * a)
    x2 = (- b - sqrt(d)) / (2 * a)
    x_min = min(x1, x2)
    x_max = max(x1, x2)
    print(x_min)
    print(x_max)
elif d == 0:
    print(-b / (2 * a))
elif d < 0:
    print("��� ������")

# ---------------------------------------------------------------------------------------------------------------

# ���������� �������������

# ���������� ������������� � �������� �������������, � �������� ����� ��� ������� � ��� ���� ����� �������� ���������.
# ������� ����������� �������������� � ������ ������� aa � ����������� ������ nn ����������� �� �������:

# s = (n * pow(a, 2)) / (4 * tan(pi / n))

# ���� ��� �����: ����������� ����� n � ������������ ����� a. �������� ���������, ������� ������� �������
# ���������� ����������� ��������������.

# ������ ������� ������
# �� ���� ��������� �������� ��� ����� nn � aa, ������ �� ��������� ������.

# ������ �������� ������
# ��������� ������ ������� ������������ ����� � ������� ��������������.

from math import *

n = float(input())
a = float(input())

s = (n * pow(a, 2)) / (4 * tan(pi / n))
print(s)

# ---------------------------------------------------------------------------------------------------------------
