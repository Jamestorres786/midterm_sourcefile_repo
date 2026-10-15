num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print("Number is zero")
