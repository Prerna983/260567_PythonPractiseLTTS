#celcius to fahrenheit converter

celsius = int(input("Celcius= "))


def conv(c):
    f = (9 / 5) * c + 32
    return f


fahrenheit = conv(celsius)
print(fahrenheit)