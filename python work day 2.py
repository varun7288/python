#Check if a number is prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 29
print("Number:", num)
print("Prime" if is_prime(num) else "Not Prime")


#Find the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = 5
print("Number:", num)
print("Factorial:", factorial(num))

#Print the Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = 7
print("Fibonacci series up to", n, "terms:")
print(fibonacci(n))

#Find the sum of digits of a given number
def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

num = 1234
print("Number:", num)
print("Sum of digits:", sum_of_digits(num))

#Reverse the digits of a given number
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

num = 1234
print("Number:", num)
print("Reversed:", reverse_number(num))
