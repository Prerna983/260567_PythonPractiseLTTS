#Write a Python program to find the second smallest number in a list

l=list(map(int,input("enter list: ").split(" ")))
l.sort()

unique_list = []
for x in l:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)
print(unique_list[1])