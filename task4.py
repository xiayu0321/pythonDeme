#! /usr/bin/env python3

height = 1.75
weight = 80.5
BMI = weight / height / height

if BMI < 18.5:
    print("so sink")
elif BMI < 25:
    print('normal')
elif BMI < 28:
    print('overweight')
elif BMI < 32:
    print('fat')
else:
    print('so fat')
