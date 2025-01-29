"""Угадать случайное число"""

# STDLIB
import random


number = random.randrange(1, 10)
guess = int(input())

while guess != number:
    print("Try again!")
    guess = int(input())

print("You're right!")
