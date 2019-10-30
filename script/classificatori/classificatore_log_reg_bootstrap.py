#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:04:11 2019

@author: leonardo
"""

import common
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Moduli di scikit-learn
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, roc_curve, roc_auc_score, confusion_matrix

from sklearn.ensemble import BaggingClassifier


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

                         
bag_clf=BaggingClassifier(LogisticRegression(), n_estimators=500, max_samples=27, bootstrap=True, n_jobs=-1, oob_score=True)

bag_clf.fit(X_train_n,Y_train)

print('Accuratezza sul training set: %.3f' % bag_clf.score(X_train_n, Y_train))

X_test_n=scaler.transform(X_test)  

print('Accuratezza sul test set: %.3f' % bag_clf.score(X_test_n, Y_test))


#cv_score = cross_val_score(clf, X_train_n, Y_train, cv=4)
#print('Risultati CrossValidation:\n', cv_score)


Y_test_pred=bag_clf.predict(X_test_n)


prec_score=precision_score(Y_test, Y_test_pred)
print('Precisione sul test set: %.3f' % prec_score)

rec_score=recall_score(Y_test, Y_test_pred)
print('Recall sul test set: %.3f' % rec_score)

F1_score=f1_score(Y_test, Y_test_pred)
print('F1 score sul test set: %.3f' % F1_score)

fpr, tpr, thresholds = roc_curve(Y_test, Y_test_pred)

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')


plot_roc_curve(fpr, tpr)
plt.show()
              

auc_score=roc_auc_score(Y_test, Y_test_pred)
print('AUC score sul test set: %.3f' % auc_score)

#MATRICE DI CONFUSIONE 

confmat = confusion_matrix(y_true=Y_test, y_pred=Y_test_pred)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


#MATRICE DI CONFUSIONE 2

Y_train_pred=bag_clf.predict(X_train_n)

confmat = confusion_matrix(y_true=Y_train, y_pred=Y_train_pred)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()

print('Accuratezza oob: %.3f' % bag_clf.oob_score_)


from sklearn.metrics import accuracy_score

print('Accuracy_score: %.3f' % accuracy_score(Y_test, Y_test_pred))
#DOVREBBE ESSERE UGUALE A :
#print('Accuratezza sul test set: %.3f' % bag_clf.score(X_test_n, Y_test))




