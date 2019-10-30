#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:07:18 2019

@author: leonardo
"""



import pandas as pd
import numpy as np

# Moduli di scikit-learn

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

data=pd.read_csv(dataset_path)

X=data.drop('0',axis=1)
X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=data.iloc[:,140]


from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(X)
X_n=scaler.transform(X)  


                        
pca=PCA(n_components=2)
X_2=pca.fit_transform(X_n)


c1=pca.components_

A=pca.explained_variance_ratio_


##CALCOLO DEL NUMERO MINIMO DI COMPONENTI PER PRESERVARE IL 95% DELLA VARIANZA
#
#pca = PCA()
#pca.fit(X_n)
#cumsum = np.cumsum(pca.explained_variance_ratio_)
#d = np.argmax(cumsum >= 0.95) + 1


#C'È UN MODO PIÙ RAPIDO: SI PUÒ SETTARE n_components = ad UN FLOAT COMPRESO TRA 0 ED 1, ESSO INDICHERÀ LA VARIANZA CHE SI VORRÀ MANTENERE

pca = PCA(n_components=0.95)
X_reduced = pca.fit_transform(X_n)

 










