def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("Enter array size: "))
numbers = list(map(int, input("Enter the numbers: ").split()))

primes = sorted([num for num in numbers if is_prime(num)])

if len(primes) < 2:
    print("Not enough primes to form a gap.")
else:
    max_gap = 0
    prime1, prime2 = 0, 0
    for i in range(1, len(primes)):
        gap = primes[i] - primes[i - 1]
        if gap > max_gap:
            max_gap = gap
            prime1, prime2 = primes[i - 1], primes[i]

    print(f"Largest gap is: {max_gap} between primes {prime1} and {prime2}")
