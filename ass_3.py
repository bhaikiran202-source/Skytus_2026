# 1 calculate  remainder two number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Remainder =", a % b)


# 2 check even or odd number
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3 wmpare two number print large one
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger number =", a)
else:
    print("Larger number =", b)


# 4 calculate the square and cube of number
n = int(input("Enter a number: "))

print("Square =", n*n)
print("Cube =", n*n*n)


# 5 check two entered number sre equal
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Not equal")


# 6 take two number print true if both are positive else false
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > 0 and b > 0:
    print(True)
else:
    print(False) 


# 7 convert float to integer 
x = float(input("Enter a float number: "))

y = int(x)
print("Integer value =", y)


# 8 take a number string  convert to int, and multiply by 10 
s = input("Enter a number: ")

n = int(s)
print("Result =", n * 10)


# 9 oprerators to check multiple conditions
a = int(input("Enter a number: "))

if a > 0 and a < 100:
    print("Number is between 1 and 99")

if a < 0 or a > 100:
    print("Number is either negative or greater than 100")


#  10 divide two numbers and print quotient and remainder separately
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient =", a // b)
print("Remainder =", a % b)


