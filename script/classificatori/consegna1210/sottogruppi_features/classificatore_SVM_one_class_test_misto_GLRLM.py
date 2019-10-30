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
X=X.iloc[:,56:72]

for index, value in enumerate(Y):   #vedi se si può usare enumerate
    if Y[index] == 0:
        Y[index] = -1


X0=X
Y0=Y
for index, value in enumerate(Y):
    if Y[index] == 1:
        X0=X0.drop([index])
        Y0=Y0.drop([index])
X1=X
Y1=Y
for index, value in enumerate(Y):
    if Y[index] == -1:
        X1=X1.drop([index])
        Y1=Y1.drop([index])


X1_train,X1_test,Y1_train,Y1_test=train_test_split(X1,Y1, train_size=26)


scaler = preprocessing.StandardScaler().fit(X1_train)
X1_train_n=scaler.transform(X1_train)  
X1_test_n=scaler.transform(X1_test)  
X0_outliers_n=scaler.transform(X0)

#UNIRE X1_test_n E X0_outliers_n in X_TEST_n
X_TEST_n=np.concatenate((X1_test_n, X0_outliers_n))

#UNIRE Y1_test E Y0
Y_TEST=np.concatenate((Y1_test, Y0))   


                  
clf=OneClassSVM(gamma='auto', nu=0.1)

clf.fit(X1_train_n)



Y1_pred_train=clf.predict(X1_train_n)
Y_pred_TEST=clf.predict(X_TEST_n)


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

#box plot

df_train=clf.decision_function(X1_train_n)
score_samples_train=clf.score_samples(X1_train_n)



plt.scatter(df_train, np.arange(0,26,1), s=5)
plt.axvline(x=0, color='red')
plt.show()





#TEST SET

#matrice di confusione

confmat = confusion_matrix(y_true=Y_TEST, y_pred=Y_pred_TEST)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()


acc_score=accuracy_score(Y_TEST, Y_pred_TEST)
print(f'Accuratezza sul test set: {acc_score}')

prec_score=precision_score(Y_TEST, Y_pred_TEST)
print('Precisione sul test set: %.3f' % prec_score)

rec_score=recall_score(Y_TEST, Y_pred_TEST)
print('Recall sul test set: %.3f' % rec_score)

F1_score=f1_score(Y_TEST, Y_pred_TEST)
print('F1 score sul test set: %.3f' % F1_score)


#box plot


df_TEST=clf.decision_function(X_TEST_n)
score_samples_TEST=clf.score_samples(X_TEST_n)


plt.scatter(df_TEST, np.arange(0,12,1), s=5)
plt.axvline(x=0, color='red')
plt.show()




#ROC CURVE 

fpr, tpr, thresholds = roc_curve(Y_TEST, Y_pred_TEST)

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')


plot_roc_curve(fpr, tpr)
plt.show()
              

auc_score=roc_auc_score(Y_TEST, Y_pred_TEST)
print('AUC score sul test set: %.3f' % auc_score)









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
