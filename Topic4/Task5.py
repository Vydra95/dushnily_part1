"""Координатная плоскость"""

x = int(input())
y = int(input())

if x < 0 and y < 0:
    print("III четверть")

if x < 0 < y:
    print("II четверть")

if y < 0 < x:
    print("IV четверть")

if x > 0 and y > 0:
    print("I четверть")
