# Write a Python program to find the second smallest number in a list

l=list(map(int,input("enter list: ").split(" ")))
l.sort()
print(l[1])