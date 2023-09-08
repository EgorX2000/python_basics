pv = int(input())
vv = int(input())
tv = int(input())

d = {pv: "Петя", vv: "Вася", tv: "Толя"}

tab = f"""{" " * 10}{d[max(pv, vv, tv)]}{" " * 10}
{" " * 2}{d[pv + vv + tv - max(pv, vv, tv) - min(pv, vv, tv)]}{" " * 18}
{" " * 18}{d[min(pv, vv, tv)]}{" " * 2}
   II      I      III   
"""

print(tab)
