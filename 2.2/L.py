a = int(input())
b = int(input())
c = int(input())

print("YES" if max(a, b, c) * 2 < a + b + c else "NO")
