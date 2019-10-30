#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:56:13 2019

@author: leonardo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Moduli di scikit-learn
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, roc_auc_score, confusion_matrix



dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

data=pd.read_csv(dataset_path)

X=data.drop('0',axis=1)
X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=data.iloc[:,140]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y)

from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(X_train)
X_train_n=scaler.transform(X_train)  

  
param_grid=[{}]  





                     
clf=LogisticRegression()

clf.fit(X_train_n,Y_train)
