n = int(input())
m = int(input())
t = int(input())

time = n * 60 + m + t
print(f"{((time // 60) % 24):0>2}:{(time % 60):0>2}")
