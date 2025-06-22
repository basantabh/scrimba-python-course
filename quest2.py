a = int(input("Enter a number: "))

if a % 2 == 0:
    if a % 3 == 0:
        print(f"{a} is divisible by 6")
    else:
        print(f"{a} is not divisible by 6")
else:
    print(f"{a} is not divisible by 6")


