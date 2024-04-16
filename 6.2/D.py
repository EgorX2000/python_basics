import pandas as pd


def cheque(price_list, **kwargs):
    products = sorted(kwargs)
    table = {
        "product": products,
        "price": [price_list[product] for product in products],
        "number": [kwargs[product] for product in products],
        "cost": [price_list[product] * kwargs[product] for product in products]
    }
    return pd.DataFrame(table)


def discount(receipt):
    ans = receipt.copy()
    for i in ans.index:
        if ans.loc[i, "number"] > 2:
            ans.loc[i, "cost"] *= 0.5
    return ans
