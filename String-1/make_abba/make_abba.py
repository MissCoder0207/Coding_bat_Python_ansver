#Given two strings, a and b, return the result
#of putting them together in the order abba,
#e.g. "Hi" and "Bye" returns "HiByeByeHi".


#make_abba('Hi', 'Bye') → 'HiByeByeHi'
#make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
#make_abba('What', 'Up') → 'WhatUpUpWhat'

a = str(input('Enter your word: '))
b = str(input("Enter your second word: "))

def make_abba(a, b):
    return a + b + b + a

