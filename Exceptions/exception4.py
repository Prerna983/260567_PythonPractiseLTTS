try:
    var=10
    print(var+"hello")
    print(var/0)
    #print(var/2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error Occurred")