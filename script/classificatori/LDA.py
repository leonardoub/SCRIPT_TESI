#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:24:37 2019

@author: leonardo
"""


import pandas as pd
import numpy as np

# Moduli di scikit-learn

from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

data=pd.read_csv(dataset_path)

X=data.drop('0',axis=1)
X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=data.iloc[:,140]


from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(X)
X_n=scaler.transform(X)  


                        
lda=LinearDiscriminantAnalysis(n_components=2)
X_new=lda.fit_transform(X_n,Y)


#c1=lda.components_

A=lda.explained_variance_ratio_
