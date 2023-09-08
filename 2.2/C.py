pv = int(input())
vv = int(input())
tv = int(input())

if vv < pv > tv:
    print("Петя")
elif pv < vv > tv:
    print("Вася")
elif pv < tv > vv:
    print("Толя")
