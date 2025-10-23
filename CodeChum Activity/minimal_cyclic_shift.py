def shift(string):
    shifted = []
    for i in range(len(string)):
        newStr = string[i:] + string[:i]
        shifted.append(newStr)

    shifted.sort()

    return shifted[0]


stringInput = str(input("Enter string: "))
result = shift(stringInput)
print(f"Result: {result}")
