# 1 print name age and city one line 
print("Name: Kiran, Age: 20, City: Rajkot")

# 2 user input two number print sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# 3 Convert temperature from Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

# 4 Store your name in a variable and print it in uppercase
name = "kiran"
print(name.upper())

# 5 Ask the user for their birth year and calculate current age
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)

# 6 Swap the values of two variables
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 7 Calculate the area of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle:", area)

# 8 Check if a number is positive or negative
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")
    
# 9 Ask for two numbers and print their average
  a = float(input("Enter first number: "))
  b = float (input("Enter second number: "))
average = (a + b) / 2
print("Average =", average)