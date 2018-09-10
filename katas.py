def find_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        counter = 3
        prev = 1
        curr = 1
        while counter <= n:
            temp = prev
            prev = curr
            curr = temp + prev
            counter += 1
        return curr

print(find_fib(8))

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
            return fib(n - 1) + fib(n - 2)

print(fib(8))

def factorialNonRecursive(n):
    counter = 1
    answer = 1
    while counter <= n:
        answer *= counter
        counter += 1
    return answer

print(factorialNonRecursive(6))

def factorial(n):
    if n == 1: # base case
        return n
    else:      # recursive step
        return n * factorial(n - 1)

print(factorial(6))