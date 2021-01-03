#!/usr/bin/env python
"""
Een python rekenmachine script dat het volgende omvat:
Een zelf gemaakte python header
het script vraagt de gebruiker om 2 natuurlijke getallen in te geven
Deze 2 natuurlijke getallen vermeerderen, verminderen, vermenigvuldigen of delen
"""

__author__ = "Jens Vansteenvoort"
__email__ = "jens.vansteenvoort@student.kdg.be"
__status__ = "Development"

#vraagt om de getallen in te geven
num1 = input('Enter first number: ')
oper = input('Enter + - * / ')
num2 = input('Enter second number: ')

#doet de bewerking van de 2 getallen
if oper == '+':
    sum = float(num1) + float(num2)
if oper == '-':
    sum = float(num1) - float(num2)
if oper == '*':
    sum = float(num1) * float(num2)
if oper == '/':
    sum = float(num1) / float(num2)

#print de bewerking en uitkomst
if oper == '+'or'-'or'*'or'/':
    print('{0}{2}{1}={3}'.format(num1, num2, oper, sum))