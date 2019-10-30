#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:56:06 2019

@author: leonardo
"""


# Utility per il caricamento dei dati e la visualizzazione dei risultati
import common
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Moduli di scikit-learn
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, roc_auc_score, confusion_matrix



dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

data=pd.read_csv(dataset_path)

X=data.drop('0',axis=1)
X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=data.iloc[:,140]

#X_train,X_test,Y_train,Y_test=train_test_split(X,Y)

#from sklearn import preprocessing
#
#scaler = preprocessing.StandardScaler().fit(X_train)
#X_train_n=scaler.transform(X_train)  

                         
clf=DecisionTreeClassifier(max_depth=4)

clf.fit(X,Y)

from sklearn.tree import export_graphviz
export_graphviz(clf, out_file='/home/leonardo/Scrivania/tree.dot', feature_names=X.T.index, rounded=True, filled=True)

