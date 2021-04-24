# Write a Python program to find the repeated items of a tuple

l = tuple(map(int, input("Enter tuple: ").split(" ")))
l1 = list(set(l))

# for i in l1:
#     c = 0
#     for j in l:
#
#         if i == j:
#             c = c + 1
#     if c > 1:
#         print(i)

for i in l1:
    c = l.count(i)
    #print(c)
    if c > 1:
        print(i)
