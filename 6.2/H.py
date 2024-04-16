import pandas as pd


def update(journal):
    ans = journal.copy()
    for i in ans.index:
        ans.loc[i, "average"] = (
            ans.loc[i, "maths"] + ans.loc[i, "physics"] + ans.loc[i, "computer science"]) / 3

    return ans.sort_values(["average", "name"], ascending=(False, True))
