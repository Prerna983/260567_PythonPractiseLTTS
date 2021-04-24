# Write a Python program to convert a list of tuples into a dictionary

l = list(map(int,input("Enter list of tuples: \n").split(" ")))
new_dict = current = {}
for name in l:
    current[name] = {}
    current = current[name]
print(new_dict)