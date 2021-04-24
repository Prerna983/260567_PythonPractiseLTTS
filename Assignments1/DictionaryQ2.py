# Write a Python program to convert a list into a nested dictionary of keys

l = list(map(int,input("Enter list of tuples: \n").split(" ")))
new_dict = current = {}
for name in l:
    current[name] = {}
    current = current[name]
print(new_dict)