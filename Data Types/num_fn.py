a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)

nums=[55,44,33,22,11]

if all([i>5 for i in nums]):
    print("all larger than 5")

if any([i%2==0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
