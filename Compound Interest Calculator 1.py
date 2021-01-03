# -*- coding: utf-8 -*-
"""
Spyder Editor

This program is used to calculate simple compound interest earned from investment
"""
print ("Bank Interest Calculator 1")

principle = int(input('What is the principle amount? '))
addition = int(input('How much will you contribute every year? '))
rate = float(input("What is the interest rate per year? "))
real_rate = rate * 0.01
time = int(input('What is the number of years you will invest? '))

i = 1

# After the first year

print ('Total after year',i,'is', principle * (1 + real_rate))
principle = principle * (1 + real_rate)

# After 2nd year and beyond

while i < time:
    principle = (principle + addition) * (1 + real_rate)
    i = i + 1
    print ('Total after year', i, 'is', principle)

# the end