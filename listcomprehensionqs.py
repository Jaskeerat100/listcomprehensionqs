fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(fruit.count(vowel) for vowel in 'aeiou') > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(fruit.count(vowel) for vowel in 'aeiou') == 2]
print(fruits_with_only_two_vowels)

# Exercise 5
fruits_with_more_than_5_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_5_chars)

# Exercise 6
fruits_with_exactly_5_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_exactly_5_chars)

# Exercise 7
fruits_with_less_than_5_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_5_chars)

# Exercise 8
fruits_length = [len(fruit) for fruit in fruits]
print(fruits_length)

# Exercise 9
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

# Exercise 10
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Exercise 11
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

# Exercise 12
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

# Exercise 13
negative_numbers = [num for num in numbers if num < 0]
print(negative_numbers)

# Exercise 14
numbers_with_two_or_more_numerals = [num for num in numbers if len(str(abs(num))) >= 2]
print(numbers_with_two_or_more_numerals)

# Exercise 15
numbers_squared = [num**2 for num in numbers]
print(numbers_squared)

# Exercise 16
odd_negative_numbers = [num for num in numbers if num < 0 and num % 2 != 0]
print(odd_negative_numbers)

# Exercise 17
numbers_plus_5 = [num + 5 for num in numbers]
print(numbers_plus_5)

# BONUS
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in numbers if is_prime(num)]
print(primes)
