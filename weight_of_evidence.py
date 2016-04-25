from __future__ import division, print_function
import pandas as pd, numpy as np
"""
don't think this is actually what I intened to do
but I used this for BNP Paribas contest
and I gained some score)
maybe I'll rewrite this in future
"""
def weight_of_evidence_cv(col, target, cv=None):
    if cv is None:
        cv = [([x for x in range(len(target))], [x for x in range(len(target))])]
    if type(cv) == int:
        from sklearn.cross_validation import StratifiedKFold
        cv = StratifiedKFold(target, cv)
    res = np.zeros(col.shape)
    for train, test in cv:
        Xtrain, Xtest = col.iloc[train], col.iloc[test]
        Ytrain, _ = target.iloc[train], target.iloc[test]
        _, res[test] = weight_of_evidence(Xtrain, Xtest, Ytrain)
    return res

def weight_of_evidence(train_col, test_col, target):
    mean = target.mean()
    df = pd.DataFrame()
    df['v'] = train_col
    df['t'] = target
    good = df.groupby('v')['t'].sum()
    total = df.v.value_counts()
    woe = np.log(((total - good) / good) / mean)

    return train_col.apply(lambda x: woe[x] if x in woe.index else np.nan), \
           test_col.apply(lambda x: woe[x] if x in woe.index else np.nan)

def test():
    a = pd.Series(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'])
    c = pd.Series(['a', 'b', 'c'])
    b = pd.Series([1, 1, 0, 1, 0, 0, 1, 0])
    print(weight_of_evidence_cv(a, b))

if __name__ == '__main__':
    test()