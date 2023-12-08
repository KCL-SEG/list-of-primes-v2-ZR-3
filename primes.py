"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes must be a positive integer")

    prime_list = []
    current_num = 2

    while len(prime_list) < number_of_primes:
        is_prime = True

        for num in prime_list:
            if current_num % num == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(current_num)

        current_num += 1

    return prime_list
