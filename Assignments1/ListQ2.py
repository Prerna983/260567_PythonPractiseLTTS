# Write a Python program to change the position of every n-th value with the (n+1)th in a list

l= list(map(int, input("Enter list: ").split(" ")))
n = int(input("enter pos: "))

for i in range(n,l[n]-1):
    l[n + 1] = l[n]

print(l)