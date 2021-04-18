num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")

grade=int(input("Enter marks: "))
if grade<40:
    print("F")
elif grade>=40 and grade<=60:
    print(("C"))
elif grade>60 and grade<=80:
    print("B")
elif (grade>80 and grade<=100):
    print("A")

age=int(input("Enter age:"))
if age>=18:
    print("Eligible to vote")
    if age>=21:
        print(("Allowed for casino!"))
    else:
        print("Not allowed for casino!")
else:
    print("Not yet mature!")