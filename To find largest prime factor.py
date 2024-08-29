def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    factors.sort()
    print("Largest factor is ",factors[-1])
    return factors
n = int(input("Enter a no: "))
print(prime_factors(n))
    
