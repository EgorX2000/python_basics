import pandas as pd


def need_to_work_better(journal):
    ans = journal.copy()
    return ans[(ans["maths"] == 2) | (ans["physics"] == 2) | (ans["computer science"] == 2)]
