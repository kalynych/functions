n = int(input("Enter positive number: "))

reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number *= 10
    reversed_number += digit
    n = n // 10

print(reversed_number)