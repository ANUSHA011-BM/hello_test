first python code
def getFactorial(num):
    if num == 0:
        return 1

    return num * getFactorial(num - 1)


num = 6
fact = getFactorial(num)

print("Factorial of", num, "is", fact)
