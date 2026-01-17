def error():
    a=0
    try:
        a=int(input("Enter the number: "))
    except ValueError:
        print("Try Again, enter an integer")
        return error()
    return a

print(error())