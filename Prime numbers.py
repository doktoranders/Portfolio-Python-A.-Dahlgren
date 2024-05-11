def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def primeGenerator(start, end):
    for num in range(start, end):
        if isPrime(num):
            yield num

# Sample Input
start = int(input())
end = int(input())

# Sample Output
result = list(primeGenerator(start, end))
print(result)  # Output: [11, 13, 17, 19]