import math
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# print(is_prime(7))
# print(is_prime(100))

def nth_fibonacci(n: int) -> int:
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)

# Example usage:
# print(nth_fibonacci(6))  # Output: 5
# print(nth_fibonacci(9))  # Output: 21

def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test cases
# print(count_vowels("hello"))  # Output: 2
# print(count_vowels("world"))  # Output: 1

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test cases
# print(factorial(5))  # Output: 120
# print(factorial(6))  # Output: 720


def sum_of_digits(n: int) -> int:
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum
    

# # Test cases
# print(sum_of_digits(12345))  # Output: 15
# print(sum_of_digits(98765))  # Output: 35
 
def reverse_string(s: str) -> str:
    return s[::-1]

# print(reverse_string("helllooooo"))

def sum_of_squares(n: int) -> int:
    return sum(i**2 for i in range(1, n + 1))

# print(sum_of_squares(4))

def collatz_sequence_length(n: int) -> int:
    length = 1  # Count the initial number itself
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

# Test cases
# print(collatz_sequence_length(6))   # Output: 9
# print(collatz_sequence_length(27))  # Output: 112

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return False
        
    else:
        return False
    
# print(is_leap_year(1999))
# print(is_leap_year(2404))

def counts_words(s: str) -> str:
    words = s.split()
    return len(words)

# print(counts_words("Bek is the great BE"))

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# print(is_palindrome("RACECAR"))

def sum_of_multiple_numbers(n: int, x: int, y: int) -> int:
    multiple_sum = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            multiple_sum += i
    return multiple_sum

# print(sum_of_multiple_numbers(10, 3, 5))

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)
print(lcm(5, 7))
# print(gcd(56, 98))
# print(gcd(27, 15))

def count_characters(s: str, c: str) ->int:
    count = 0
    for char in s:
        if char == c:
            count += 1
    return count

# print(count_characters("hello world, ", "Bek is great BE / SWE and created astounding technology with high potential startup"))
# print(count_characters("apple", "p"))
#This function iterates through each character in the string s

def digit_count(n: int) -> int:
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

print(digit_count(123))
print(digit_count(4567))
