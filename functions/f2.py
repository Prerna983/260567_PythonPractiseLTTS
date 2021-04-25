def shortest_length(x,y):
    if len(x)<len(y):
        return x
    else:
        return y

print(shortest_length("Hello", "hie"))
