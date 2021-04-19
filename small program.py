# x=2
# y=4
# x=x//y
# y=y//x
# print(y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
mins+=dura

hour=hour+(mins//60)
mins%=60
hour%=24

print(hour,":",mins)

x = float(input("Enter value for x: "))

# Write your code here.
y=1/(x+1/(x+1/(x+1/x)))
print("y =", y)

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

num_1 = input("Enter the first number: ") # Enter 12
num_2 = input("Enter the second number: ") # Enter 21

print(num_1 + num_2) # the program returns 1221

x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")

x = input("Enter a number: ") # The user enters 2
print(type(x))

