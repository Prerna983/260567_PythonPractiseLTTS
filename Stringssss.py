# n=input("Input: ")
# if n=='Spathiphyllum':
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif n=='spathiphyllum':
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not "+n+"!")


income = float(input("Enter the annual income: "))

if income <= 0:
    tax=0
elif income<85528:
    tax = (18*income)/100;
    tax = tax - 556.2
else:
    tax = (32*(income-85528))/100
    tax = 14839.2 + tax

tax = round(tax, 0)

if tax <= 0:
    tax = 0

print("The tax is:", tax, "thalers")


