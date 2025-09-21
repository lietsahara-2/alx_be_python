num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")

match (num1, num2, operation):
    case(num1, num2, "+"):
        print(f"the result is {num1+num2}")
    case(num1, num2, "-"):
            print(f"the result is {num1-num2}")
    case(num1, num2, "*"):
        print(f"the result is {num1*num2}")
    case(num1, num2, "/"):
        if num2!=0:
            print(f"the result is {num1/num2}")
        else:
            print("Cannot divide by zero")