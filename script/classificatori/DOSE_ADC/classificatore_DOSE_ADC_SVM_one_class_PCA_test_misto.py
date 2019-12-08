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

dataset_DOSE_path = '/home/leonardo/Scrivania/TESI/tabelle/ADC_DOSE/tab_outcome_bW1_classificazione.csv'
dataset_ADC_path = '/home/leonardo/Scrivania/TESI/tabelle/ADC_DOSE/tab_outcome_C_bc_100_for_classification.csv'

def preprocess_DOSE(dataset_path):
    X_DOSE = pd.read_csv(dataset_path)
    
    X_DOSE = X_DOSE.drop(X_DOSE.columns[np.arange(0,33)], axis=1)
    X_DOSE = X_DOSE.drop(X_DOSE.columns[np.arange(93,107)], axis=1)
    
    Y_DOSE = X_DOSE.iloc[:,93]
    X_DOSE = X_DOSE.drop('0',axis=1)
    
    return X_DOSE, Y_DOSE

#HO DOVUTO DEFINIRE LA FUNZIONE SOTTO PERCHÈ DA DOSE E CT VENGONO ESTRATTE UN NUMERO DIVERSO DI FEATURES 
#QUINDI CI SONO PROBLEMI CON GLI INDICI
#SE USASSI LE CT TRASFORMATE IN nii DA ME NON CI SAREBBE STATO BISOGNO DI DEFINIRE LA FUNZIONE SOTTO 
    
def preprocess_CT(dataset_path):
    X_CT=pd.read_csv(dataset_path)
    
    X_CT = X_CT.drop(X_CT.columns[np.arange(0,33)], axis=1)
    X_CT = X_CT.drop(X_CT.columns[np.arange(93,107)], axis=1)
    
    Y_CT=X_CT.iloc[:,93]
    X_CT=X_CT.drop('0',axis=1)
    
    return X_CT, Y_CT


def preprocess_pca(X, Y):

    
    for index, value in enumerate(Y):   #vedi se si può usare enumerate
        if Y[index] == 0:
            Y[index] = -1
    
    
    X0 = X
    Y0 = Y
    for index, value in enumerate(Y):
        if Y[index] == 1:
            X0 = X0.drop([index])
            Y0 = Y0.drop([index])
    X1 = X
    Y1 = Y
    for index, value in enumerate(Y):
        if Y[index] == -1:
            X1 = X1.drop([index])
            Y1 = Y1.drop([index])
    
    
    X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1, train_size=23, random_state=0)
    
    
    scaler = preprocessing.StandardScaler().fit(X1_train)
    X1_train_n = scaler.transform(X1_train)  
    X1_test_n = scaler.transform(X1_test)  
    X0_outliers_n = scaler.transform(X0)
    
    #UNIRE X1_test_n E X0_outliers_n in X_TEST_n
    X_TEST_n = np.concatenate((X1_test_n, X0_outliers_n))
    
    #UNIRE Y1_test E Y0
    Y_TEST = np.concatenate((Y1_test, Y0))   
    
    
    pca = PCA(n_components=8)
    reducer = pca.fit(X1_train_n)
    X1_train_n_reduced = reducer.transform(X1_train_n)  
    X_TEST_n_reduced = reducer.transform(X_TEST_n)  

    return X1_train_n_reduced, Y1_train, X_TEST_n_reduced, Y_TEST


X_DOSE, Y_DOSE = preprocess_DOSE(dataset_DOSE_path)
DOSE_X1_train_n_reduced, DOSE_Y1_train, DOSE_X_TEST_n_reduced, DOSE_Y_TEST = preprocess_pca(X_DOSE, Y_DOSE)

X_ADC, Y_ADC = preprocess_CT(dataset_ADC_path)
ADC_X1_train_n_reduced, ADC_Y1_train, ADC_X_TEST_n_reduced, ADC_Y_TEST = preprocess_pca(X_ADC, Y_ADC)


TOT_X1_train_n_reduced = np.concatenate((DOSE_X1_train_n_reduced, ADC_X1_train_n_reduced), axis=1)
TOT_Y1_train = DOSE_Y1_train
TOT_X_TEST_n_reduced = np.concatenate((DOSE_X_TEST_n_reduced, ADC_X_TEST_n_reduced), axis=1)
TOT_Y_TEST = DOSE_Y_TEST 
                  
clf=OneClassSVM(gamma='auto', nu=0.1)

clf.fit(TOT_X1_train_n_reduced)


TOT_Y1_pred_train=clf.predict(TOT_X1_train_n_reduced)
TOT_Y_pred_TEST=clf.predict(TOT_X_TEST_n_reduced)


#VALUTAZIONE

#TRAIN SET

#matrice di confusione

confmat = confusion_matrix(y_true=TOT_Y1_train, y_pred=TOT_Y1_pred_train)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.5)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.title('CONFUSION MATRIX \n SVM one-class con PCA \n Feautures: DOSE ADC \n train set', y = 1.2)
plt.show()


acc_score=accuracy_score(TOT_Y1_train,TOT_Y1_pred_train)
print(f'Accuratezza sul train set: {acc_score}')

prec_score=precision_score(TOT_Y1_train,TOT_Y1_pred_train)
print('Precisione sul train set: %.3f' % prec_score)

rec_score=recall_score(TOT_Y1_train,TOT_Y1_pred_train)
print('Recall sul train set: %.3f' % rec_score)

F1_score=f1_score(TOT_Y1_train,TOT_Y1_pred_train)
print('F1 score sul train set: %.3f' % F1_score)


#box plot

df_train=clf.decision_function(TOT_X1_train_n_reduced)
#score_samples_train=clf.score_samples(X1_train_n_reduced)



plt.scatter(df_train, np.arange(0,23,1), s=5)
plt.axvline(x=0, color='red')
plt.show()



#TEST SET

#matrice di confusione

confmat = confusion_matrix(y_true=TOT_Y_TEST, y_pred=TOT_Y_pred_TEST)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.title('CONFUSION MATRIX \n SVM one-class con PCA \n Feautures: DOSE ADC \n test set', y = 1.2)
plt.show()


acc_score=accuracy_score(TOT_Y_TEST, TOT_Y_pred_TEST)
print(f'Accuratezza sul test set: {acc_score}')

prec_score=precision_score(TOT_Y_TEST, TOT_Y_pred_TEST)
print('Precisione sul test set: %.3f' % prec_score)

rec_score=recall_score(TOT_Y_TEST, TOT_Y_pred_TEST)
print('Recall sul test set: %.3f' % rec_score)

F1_score=f1_score(TOT_Y_TEST, TOT_Y_pred_TEST)
print('F1 score sul test set: %.3f' % F1_score)


#box plot


df_TEST=clf.decision_function(TOT_X_TEST_n_reduced)
#score_samples_TEST=clf.score_samples(X_TEST_n_reduced)


plt.scatter(df_TEST, np.arange(0,12,1), s=5)
plt.axvline(x=0, color='red')
plt.show()




#ROC CURVE 

fpr, tpr, thresholds = roc_curve(TOT_Y_TEST, TOT_Y_pred_TEST)

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')


plot_roc_curve(fpr, tpr)
plt.show()
              

auc_score=roc_auc_score(TOT_Y_TEST, TOT_Y_pred_TEST)
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
