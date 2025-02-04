#Hetessy Adrián

print("Üdvözöllek! Ez a kód decimális számot binárisra, és vissza tud átváltani. 😄")
print("Csak pozitiv egész számokkal működik! ✅")


def binarytodecimal():
    inputSzam = input("Ird ide bináris számodat:  ")

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
            print("Érvénytelen bevitel.")
            break
        i += 1

    print(f"A számod decimálisban {runningSum}")

def decimaltobinary():
    inputNum = int(input("Ird ide decimális számodat:  "))
    list = []

    while inputNum > 0:
        r = inputNum % 2
        list.append(r)
        inputNum //= 2
    list.reverse()
    print(f"A számod binárisban {''.join(str(remainder) for remainder in list)}")

choice = int(input("Ird be a  \"1\" számot: decimális -> bináris || Ird be a \"2\" számot: bináris -> decimális:   "))

if choice == 1:
    decimaltobinary()
elif choice == 2:
    binarytodecimal()
else:
    print("Érvénytelen választás.")

print("Köszönöm, hogy kipróbáltad programomat! 😄")















