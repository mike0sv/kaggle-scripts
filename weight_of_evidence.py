from __future__ import division
import pandas as pd, numy as np
"""
don't think this is actually what I intened to do
but I used this for BNP Paribas contest
and I gained some score)
maybe I'll rewrite this in future
"""

def woe_oof(col, target, cv=None):
    if cv is None:
        cv = [([x for x in range(len(target))], [x for x in range(len(target))])]
    res = np.zeros(col.shape)
    values = col.unique()
    for train, test in cv:
        Xtrain, Xtest = col.iloc[train], col.iloc[test]
        Ytrain, Ytest = target.iloc[train], target.iloc[test]
        mean = Ytrain.sum() / len(Ytrain)
        print mean
        woe = dict()
        for val in values:
            try:
                good = Ytrain[Xtrain == val].sum()
                total = Xtrain.value_counts()[val]
                woe[val] =  (total - good) / good
                #print val, total
            except:
                print val, good, total,
                woe[val] = np.nan
        res[test] = Xtest.apply(lambda x: np.log(woe[x] / mean))
    return res

def woe(train_col, test_col, target):
    res_train, res_test = np.zeros(train_col.shape), np.zeros(test_col.shape)
    values = train_col.unique()
    mean = target.sum() / len(target)
    print mean
    woe = dict()
    for val in values:
        try:
            good = target[train_col == val].sum()
            total = train_col.value_counts()[val]
            woe[val] =  (total - good) / good
            #print val, total
        except:
            print val, good, total,
            woe[val] = np.nan
            
    def get_woe(woe, key):
        try:
            return woe[key]
        except:
            return np.nan
        
    res_train = train_col.apply(lambda x: np.log(woe[x] / mean))
    res_test = test_col.apply(lambda x: np.log(get_woe(woe, x) / mean))
    return res_train, res_test