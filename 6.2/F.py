import pandas as pd


def best(journal):
    ans = journal.copy()
    return ans[(ans["maths"] > 3) & (ans["physics"] > 3) & (ans["computer science"] > 3)]
