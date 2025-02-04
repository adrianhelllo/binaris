#Hetessy Adrián

def binarytodecimal():
    inputSzam = input("Enter your binary number here:  ")

    digits = list(inputSzam)
    digits.reverse()

    if len(digits) != 1:
        while digits[0] == '0':
            digits.pop(0)

    runningSum = 0
    i = 0

    for digit in digits:
        if digit == '1':
            runningSum += 2 ** i
        elif digit != '0':
            print("Your input is invalid.")
            break
        i += 1

    print(f"Your number in decimal is {runningSum}")

def decimaltobinary():
    inputNum = int(input("Enter your decimal number here:  "))
    list = []

    while inputNum > 0:
        r = inputNum % 2
        list.append(r)
        inputNum //= 2
    list.reverse()
    print(f"Your number in binary is {''.join(str(remainder) for remainder in list)}")

choice = int(input("Enter \"1\" for Decimal -> Binary || Enter \"2\" for Binary -> Decimal:   "))

if choice == 1:
    decimaltobinary()
elif choice == 2:
    binarytodecimal()
else:
    print("Invalid choice")















