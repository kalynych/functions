
def fibonacci_naive(n):
    assert 0 <= n <= 100
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive (n - 2)

n = int(input("Enter number here: "))
print(fibonacci_naive(n))

print(f"All fibonacci numbers for {n} in descending order:")
while n > 0:
    print(fibonacci_naive(n))
    n -= 1




