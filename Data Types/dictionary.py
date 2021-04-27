age = {"Harry":27, "mary":10, "john":39}
print(age["john"])
#print(age["scary"])

#bad_dict = {[1,2,3]: "one two three"}
#print(bad_dict)

squares= {1: 1, 2: 4, 3: 9, 4: 16, 8: 64,}
print(squares)
squares[3]=15
print(squares)

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])

print(4 in primes)
print(5 in primes)

pairs={1:"apple",
       "orange":[2,3,4],
       True: False,
       None: "True",}
print((pairs.get("orange")))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

fib = {1: 1, 2: 1, 3: 2, 4: 3,}
print(fib.get(4, 0) + fib.get(7, 5))
