#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:33:46 2019

@author: leonardo
"""


# Utility per il caricamento dei dati e la visualizzazione dei risultati
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Moduli di scikit-learn

from sklearn.svm import OneClassSVM
from sklearn.model_selection import cross_val_score, GridSearchCV, ParameterGrid, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score, confusion_matrix
from sklearn.decomposition import PCA
from sklearn import preprocessing

dataset_path = '/home/leonardo/Scrivania/TESI/tabelle/tab_outcome_bW1_classificazione.csv' 

X=pd.read_csv(dataset_path)

X=X.drop(X.columns[np.arange(0,33)], axis=1)
X=X.drop(X.columns[np.arange(93,107)], axis=1)

Y=X.iloc[:,93]
X=X.drop('0',axis=1)

for i in range(len(Y)):
    if Y[i]==0:
        Y[i]=-1


X0=X
Y0=Y
for i in range(len(Y)):
    if Y[i] == 1:
        X0=X0.drop([i])
        Y0=Y0.drop([i])
X1=X
Y1=Y
for i in range(len(Y)):
    if Y[i] == -1:
        X1=X1.drop([i])
        Y1=Y1.drop([i])


X1_train,X1_test,Y1_train,Y1_test=train_test_split(X1,Y1)


scaler = preprocessing.StandardScaler().fit(X1_train)
X1_train_n=scaler.transform(X1_train)  
X1_test_n=scaler.transform(X1_test)  
X0_outliers_n=scaler.transform(X0)


pca = PCA(n_components=0.95)
reducer = pca.fit(X1_train_n)
X1_train_n_reduced=reducer.transform(X1_train_n)  
X1_test_n_reduced=reducer.transform(X1_test_n)  
X0_outliers_n_reuced=reducer.transform(X0_outliers_n)
       



                  
clf=OneClassSVM(gamma='auto', nu=0.5)

clf.fit(X1_train_n_reduced)



Y1_pred_train=clf.predict(X1_train_n_reduced)
Y1_pred_test=clf.predict(X1_test_n_reduced)
Y0_pred_outliers=clf.predict(X0_outliers_n_reuced)


#VALUTAZIONE

#TRAIN SET

#matrice di confusione

confmat = confusion_matrix(y_true=Y1_train, y_pred=Y1_pred_train)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


acc_score=accuracy_score(Y1_train,Y1_pred_train)
print(f'Accuratezza sul train set: {acc_score}')

prec_score=precision_score(Y1_train,Y1_pred_train)
print('Precisione sul train set: %.3f' % prec_score)

rec_score=recall_score(Y1_train,Y1_pred_train)
print('Recall sul train set: %.3f' % rec_score)

F1_score=f1_score(Y1_train,Y1_pred_train)
print('F1 score sul train set: %.3f' % F1_score)

#TEST SET

#matrice di confusione

confmat = confusion_matrix(y_true=Y1_test, y_pred=Y1_pred_test)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


acc_score=accuracy_score(Y1_test, Y1_pred_test)
print(f'Accuratezza sul test set: {acc_score}')

prec_score=precision_score(Y1_test, Y1_pred_test)
print('Precisione sul test set: %.3f' % prec_score)

rec_score=recall_score(Y1_test, Y1_pred_test)
print('Recall sul test set: %.3f' % rec_score)

F1_score=f1_score(Y1_test, Y1_pred_test)
print('F1 score sul test set: %.3f' % F1_score)

#OUTLIERS SET

#matrice di confusione

confmat = confusion_matrix(y_true=Y0, y_pred=Y0_pred_outliers)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


acc_score=accuracy_score(Y0, Y0_pred_outliers)
print(f'Accuratezza sul outliers set: {acc_score}')

prec_score=precision_score(Y0, Y0_pred_outliers)
print('Precisione sul outliers set: %.3f' % prec_score)

rec_score=recall_score(Y0, Y0_pred_outliers)
print('Recall sul outliers set: %.3f' % rec_score)

F1_score=f1_score(Y0, Y0_pred_outliers)
print('F1 score sul outliers set: %.3f' % F1_score)












#
#from sklearn.model_selection import cross_val_predict
#
#Y_train_pred_1 = cross_val_predict(clf, X_train_n, Y_train, cv=4)
#
#
#Y_train_pred=clf.predict(X_train_n)
#
#confmat_1 = confusion_matrix(y_true=Y_train, y_pred=Y_train_pred_1)
#
#fig, ax = plt.subplots(figsize=(2.5, 2.5))
#ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
#for i in range(confmat_1.shape[0]):
#    for j in range(confmat_1.shape[1]):
#            ax.text(x=j, y=i, s=confmat_1[i, j], va='center', ha='center')
#plt.xlabel('predicted label')
#plt.ylabel('true label')
#plt.show()
#
##ROC CURVE 2
#
#fpr, tpr, thresholds = roc_curve(Y_train, Y_train_pred_1)
#
#def plot_roc_curve(fpr, tpr, label=None):
#    plt.plot(fpr, tpr, linewidth=2, label=label)
#    plt.plot([0, 1], [0, 1], 'k--')
#    plt.axis([0, 1, 0, 1])
#    plt.xlabel('False Positive Rate')
#    plt.ylabel('True Positive Rate')
#
#
#plot_roc_curve(fpr, tpr)
#plt.show()
#              
#
#auc_score=roc_auc_score(Y_train, Y_train_pred_1)
#print('AUC score sul test set: %.3f' % auc_score)
#
