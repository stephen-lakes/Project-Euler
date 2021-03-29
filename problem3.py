"""
Problem 3
=========
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
target_number = 13195 #600851475143
largest_prime_factor = 2

while largest_prime_factor <= target_number:
    if target_number % largest_prime_factor == 0:
        target_number = target_number / largest_prime_factor
    else:
        largest_prime_factor += 1

print(largest_prime_factor)