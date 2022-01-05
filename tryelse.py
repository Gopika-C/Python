def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
divide(x,y)
