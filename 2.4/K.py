def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    if n > 1:
        return 1


n = int(input())

count = 0
for i in range(n):
    i = int(input())
    if isprime(i):
        count += 1

print(count)
