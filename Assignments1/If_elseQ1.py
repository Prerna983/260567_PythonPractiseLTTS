# Write a Python program to get next day of a given date using if-elif-else

year=int(input("enter year:"))
if (year%4 == 0):
    f=1
elif (year%400 == 0):
    f=1
elif (year%100 == 0):
    f=0
else:
    f=0

month=int(input("enter month from 1-12:"))
l=[1,3,5,7,8,10,12]
l2=[4,6,9,11]
if month in l:
    d=31
elif month in l2:
    d=30
else:
    if f == 1:
        d=29
    else:
        d=28

day=int(input("enter date between 1-31:"))
if day<d:
    print(day+1)
elif day > d:
    print("enter valid date")
else:
    print(1)