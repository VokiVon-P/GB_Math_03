# попытка сделать задание - но все время вылетает по переполнению (( видимо нужен математический трюк ))

import math
import numpy as np

from math import factorial, pow, sqrt, pi, e


def stirling_factorial(n):
       if n == 0:
           return 1
       else:
           return np.longdouble(sqrt(2*pi*n))*np.power(np.longdouble(n/e), np.longdouble(n))


def calc_n(n:int):
    
    if n < 150:
        fact = float()
    else:
        fact = stirling_factorial(n)

    sq = np.longdouble(fact)**(1/n)
    res = n/sq
    return res



diff = 1e-7
print(type(diff))
n = 1
delta = 1
delta_param = 10*diff
res_n = calc_n(n)    

while True:
    n +=delta
    res_next = calc_n(n)
    test = abs(res_next - res_n) 
    """
    if test <= 100*diff:
        delta = 10


    if test <= 10*diff:
        delta = 1    
    """

    if test <= diff:
        break

    res_n = res_next

print(f"При n = {n} lim = {res_next} c точностью {diff}")



