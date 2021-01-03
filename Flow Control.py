#!/usr/bin/env python
"""
a program for explaining flow control by using the while loop, and if
"""


__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"


number = 6
word = ['cat','monkey']


while number > 0:
    print(number)
    number -= 1


if number == 0:
    print('zero')

for w in word:
    print(w,len(w))