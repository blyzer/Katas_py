def find_fib(number):
    if number == 1 or number == 2:
        return 1
    else:
        counter = 3
        prev = 1
        curr = 1
        while counter <= number:
            temp = prev
            prev = curr
            curr = temp + prev
            counter += 1
        return curr

print(find_fib(8))

def fib(number):
    if number <= 2:
        return 1
    else:
            return fib(number - 1) + fib(number - 2)

print(fib(8))

def factorialNonRecursive(number):
    counter = 1
    answer = 1
    while counter <= number:
        answer *= counter
        counter += 1
    return answer

print(factorialNonRecursive(6))

def factorial(number):
    if number == 1: # base case
        return number
    else:      # recursive step
        return number * factorial(number - 1)

print(factorial(6))