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

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)


# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)