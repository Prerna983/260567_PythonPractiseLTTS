print(", ".join(["spam", "eggs", "ham"]))

print("Hello ME".replace("ME", "World"))

print("This is a sentence.".startswith("This"))

print("This is a sentence".endswith("sentence"))

print("This is a sentence".upper())

print("spam, eggs, ham".split(","))

print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

print('aBcD'.capitalize())

print("Eta".find("ta"))
print('lambda30'.isalnum())

# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

print('moooo'.islower())
print(' \n '.isspace())
print(" ".isspace())
print('MOOOO'.isupper())

print(" ## ".join(["omicron", "pi", "rho"]))

print("SiGmA=60".lower())

print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
print("Apple juice".replace("juice", ""))

print("tau tau tau".rfind("ta"))
print("cisco.com".rstrip(".com"))
print("phi       chi\npsi".split())

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

