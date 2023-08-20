

import  turtle as tur
import sys
from time import sleep


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def normal_star(siz, clr, point):
    if point <= 4:
        raise ValueError('Not enough point')

    tur.color(clr)

    for coprime in range(point // 2, 1, -1):
        if gcd(point, coprime) == 1:

            print("({},{})".format(point, coprime), file=sys.stderr)

            start = tur.position()

            for _ in range(point):
                tur.forward(siz)
                tur.left(360.0 / point * coprime)

            tur.setposition(start)

            return

    abnormal_star(siz, clr, point)


def abnormal_star(siz, clr, point):
    print("Exception:", point, file=sys.stderr)


for point in range(5, 6):
    tur.reset()
    normal_star(500, 'red', point)
    sleep(2)

tur.exitonclick()
