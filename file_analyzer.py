#reading a file

filename=input("Enter a filename:")

with open(filename) as f:
    text=f.read()

print(text)

#counting frequency of a character
def count_char(text, char):
    count=0
    for c in text:
        if c==char:
            count+=1
    return count

print(count_char(text,"r"))

#finding what % of total text each character occupies
for char in "abcdefghijklmnopqrstuvwxyz":
    perc=100*count_char(text,char)/len(text)
    print("{0}-{1}%".format(char, round(perc,2)))

