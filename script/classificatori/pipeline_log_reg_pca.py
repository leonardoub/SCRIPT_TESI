#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:07:33 2019

@author: leonardo
"""

import pandas as pd
import numpy as np

# Moduli di scikit-learn

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline


dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

data=pd.read_csv(dataset_path)

X=data.drop('0',axis=1)
X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=data.iloc[:,140]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y)


pipe_lr=Pipeline([('scl', StandardScaler()),('pca',PCA(n_components=2)), ('clf', LogisticRegression(random_state=1))])

pipe_lr.fit(X_train, Y_train)

print('Test Accuracy: %.3f' % pipe_lr.score(X_test, Y_test))




