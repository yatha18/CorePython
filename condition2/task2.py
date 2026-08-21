x = int(input("Enter a number: "))

if x > 0:
    if x % 2 != 0:
        result = x + 10
        print("Positive odd number")
        print("Result:", result)
    else:
        result = x * 2.5
        print("Positive even number")
        print("Result:", result)

elif x < 0:
    if x % 2 != 0:
        result = x - 10
        print("Negative odd number")
        print("Result:", result)
    else:
        result = x / 2.5
        print("Negative even number")
        print("Result:", result)

else:
    print("Number is zero")