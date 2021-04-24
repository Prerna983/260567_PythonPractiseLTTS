# Write a Python program to convert a list of tuples into a dictionary

def Convert(tup, di):
    di = dict(tup)
    return di


tups = [("mango", 10), ("ball", 12), ("pizza", 14), ("bag", 25), ("water", 30)]
dictionary = {}
di=dict(tups)

print(di)