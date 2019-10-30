#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:50:43 2019

@author: leonardo
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X=iris.drop("class", axis=1).values
Y=iris["class"].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=0.3, random_state=0)

#due opzioni: implementarla da soli

from sklearn.model_selection import KFold

lr=LogisticRegression()

kfold=KFold(n_splits=10, random_state=1)
scores=[]

for k, (train, test) in enumerate(kfold.split(X_train)):
    
    lr.fit(X_train[train], Y_train[train])
    score=lr.score(X_train[test],Y_train[test])
    scores.append(score)
    print("fold %d: Accuracy=%.4f" % (k,score))
    
 
accuracy=np.array(scores).mean()
print("Validation accuracy=%.4f" % accuracy)



from sklearn.model_selection import StratifiedKFold


lr=LogisticRegression()

kfold=StratifiedKFold(n_splits=10, random_state=1)
scores=[]

for k, (train, test) in enumerate(kfold.split(X_train, Y_train)):
    
    lr.fit(X_train[train], Y_train[train])
    score=lr.score(X_train[test],Y_train[test])
    scores.append(score)
    print("fold %d: Accuracy=%.4f" % (k,score))


#secondo metodo: utilizzare la cross validation come fosse una funzione di score
    
from sklearn.model_selection import cross_val_score

lr=LogisticRegression()

score=cross_val_score(lr, X_train, Y_train, cv=10)

score.mean()

lr.fit(X_train, Y_train)







