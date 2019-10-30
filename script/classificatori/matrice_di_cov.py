#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:49:51 2019

@author: leonardo
"""

#COSTRUIRE LA MATRICE DI COVARIANZA, DOVREBBE ESSERE 93*93
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione_bis.csv' 

data=pd.read_csv(dataset_path)

X=data.drop(data.columns[0],axis=1)

#MATRICE DI COVARIANZA, DATI NON NORMALIZZATI

cov_mat=np.cov(X.T)

plt.imshow(cov_mat)
plt.colorbar()
plt.show()

#MATRICE DI COVARIANZA, DATI NORMALIZZATI

from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(X)
X_n=scaler.transform(X)  

cov_mat_n=np.cov(X_n.T)

plt.imshow(cov_mat_n)
plt.colorbar()
plt.show()

#MATRICE DI COVARIANZA, DATI NORMALIZZATI CON corrcoef

cov_mat_corr=np.corrcoef(X.T)

plt.imshow(cov_mat_corr)
plt.colorbar()
plt.show()