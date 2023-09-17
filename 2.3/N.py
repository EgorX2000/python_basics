def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    if n > 1:
        return 1


n = int(input())
if isprime(n):
    print("YES")
else:
    print("NO")
