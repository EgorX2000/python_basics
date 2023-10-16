import math

numbers = list(set(map(int, input().split(sep="; "))))

primes = dict()
for i in range(len(numbers)):
    primes[numbers[i]] = list()
    for j in range(len(numbers)):
        if math.gcd(numbers[i], numbers[j]) == 1:
            primes[numbers[i]].append(numbers[j])
    if len(primes[numbers[i]]) == 0:
        del primes[numbers[i]]
    else:
        primes[numbers[i]].sort()

for number in sorted(primes):
    print(str(number) + " - " +
          str(primes[number]).removeprefix("[").removesuffix("]"))
