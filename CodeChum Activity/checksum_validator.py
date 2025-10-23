string = input("Enter string: ")
key = int(input("Enter key: "))

checkSum = 0
i = 0

while i < len(string):
    letter = string[i]
    i += 1
    numStr = ''

    while i < len(string) and string[i].isdigit():
        numStr += string[i]
        i += 1

    numbers = int(numStr)
    asciiVal = ord(letter)
    checkSum += asciiVal * numbers

if (checkSum % key == 0):
    print("Result: Valid")
else:
    print("Result: Corrupt")
