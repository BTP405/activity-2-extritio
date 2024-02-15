def isPrimeNum(num):
    """checks if recieved number is a prime number"""
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def getPrimeNumbers(n):
    """returns list of prime numbers between 2 and n"""
    return [num for num in range(2, n+1) if isPrimeNum(num)]

# output should be: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
print(getPrimeNumbers(30))
