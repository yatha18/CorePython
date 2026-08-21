marks = int(input("Enter marks: "))

if marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 40:
    print("D Grade")
else:
    print("Fail")