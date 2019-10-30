#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:47:50 2019

@author: leonardo
"""

import random
from scipy import stats

a=[random.gauss(5,2) for i in range(100)]

b=stats.shapiro(a)

#APPLICARE IL TEST DI SHAPIRO ALLA MATRICE DEI DATI PER VEDERE SE LE COLONNE SONO VETTORI NORMALI

import pandas as pd
import matplotlib.pyplot as plt

dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione_bis.csv' 

data=pd.read_csv(dataset_path)
X=data.drop(data.columns[0],axis=1)

for i in range(93):
    A=X.iloc[:,i]
    S=stats.shapiro(A)
    B=list(A)
    plt.hist(B)
    plt.show()
    print(S)