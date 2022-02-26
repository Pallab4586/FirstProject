print("Enter your First Number")
num1 = int(input())
print("Enter your Second Number")
num2 = int(input())
print("Enter your Operator")
num3 = input()
if num3 == "+":
    add = num1+num2
    print("Your answer is", add)
elif num3 == "-":
    subtract = num1-num2
    print("Your answer is", subtract)
elif num3 == "*":
    multiply = num1*num2
    print("Your answer is", multiply)
elif num3 == "/":
    divide = num1/num2
    print("Your answer is", divide)

else:
    print("Invalid Input")


