# Write a Python program to find the second smallest number in a list

l=list(map(int,input("enter no:").split(" ")))
l.sort()
print(l[1])