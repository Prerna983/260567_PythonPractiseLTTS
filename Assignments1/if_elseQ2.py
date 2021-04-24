# Write a python program to check the user input abbreviation.
# If the user enters "lol", print "laughing out loud".
# If the user enters "rofl", print "rolling on the floor laughing".
# If the user enters "lmk", print "let me know".
# If the user enters "smh", print "shaking my head".

s=input("Enter an abbreviation: ")
if(s=='lol'):
    print("laughing out loud")
elif(s=='rofl'):
    print("rolling on the floor laughing")
elif(s=='lmk'):
    print("let me know")
elif(s=='smh'):
    print("shaking my head")
else:
    print("Enter in small letters")