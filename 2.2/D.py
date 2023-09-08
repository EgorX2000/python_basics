pv = int(input())
vv = int(input())
tv = int(input())

d = {pv: "Петя", vv: "Вася", tv: "Толя"}
mas = [pv, vv, tv]
mas.sort(reverse=True)

for i in range(len(mas)):
    print(f"{i + 1}.", d[mas[i]])
