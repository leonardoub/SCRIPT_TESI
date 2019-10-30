#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:12:45 2019

@author: leonardo
"""


import pandas as pd
import numpy as np

# Moduli di scikit-learn

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler


dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

data=pd.read_csv(dataset_path)

X=data.drop('0',axis=1)
X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=data.iloc[:,140]


rdn_clf=RandomForestClassifier(n_estimators=500, n_jobs=-1)
rdn_clf.fit(X, Y)

Y_pred_rf=rdn_clf.predict(X)



for name, score in zip(X.T.index, rdn_clf.feature_importances_):

    print(name, score)





















