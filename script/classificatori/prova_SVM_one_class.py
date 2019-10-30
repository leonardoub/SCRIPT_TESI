#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:44:20 2019

@author: leonardo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm


xx,yy=np.meshgrid(np.linspace(-5,5,500), np.linspace(-5,5,500))

np.random.seed(17)

#GENERATE DATA

X=0.3*np.random.randn(100,2)  #costruisce una matrice 100x2 con campioni presi da una distribuzione normale con media 0 e varianza 1

X_train=np.r_[X+2,X-2]  #concatena le due matrici costruendo una matrice 200x2

#GENERATE SOME REGULAR NEW OBSERVATIONS

X=0.3*np.random.randn(20,2) 
X_test=np.r_[X+2,X-2]

#GENERATE SOME ABNORMAL NEW OBSERVATIONS

X_outliers=np.random.uniform(low=-4, high=4, size=(20, 2)) #preleva dei campioni dalla distibuzione uniforme


plt.scatter([a[0] for a in X_train], [a[1] for a in X_train])

plt.scatter([a[0] for a in X_outliers], [a[1] for a in X_outliers])

plt.scatter([a[0] for a in X_test], [a[1] for a in X_test])

plt.legend(['positive in train data', 'outliers in test data', 'positive in test data'], loc='upper left') 
plt.show()

print('nu=0.5')

clf=svm.OneClassSVM()

clf.fit(X_train)

Z=clf.decision_function(np.c_[xx.ravel(), yy.ravel()]) #c_ concatena lungo il secondo asse, affianca verticalmente; ravel restituisce un array 1-D

Z=Z.reshape(xx.shape)

plt.title('Outside red circle is extimating outlier region')

plt.contourf(xx, yy, Z, levels=[Z.min(),0], colors='gray')

a=plt.contour(xx, yy, Z, levels=[0], linewidths=4, color='red')

plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')


s=40

b1=plt.scatter(X_train[:,0], X_train[:,1], s=s, edgecolors='k')

c=plt.scatter(X_outliers[:,0], X_outliers[:,1], s=s, edgecolors='k')

b2=plt.scatter(X_test[:,0], X_test[:,1], s=s, edgecolors='k')

plt.legend([b1,c,b2],["positive in train data", "outliers in test data", "positive in test data"], loc="upper left")

plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned frontier", "training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.show()

#

y_pred_train=clf.predict(X_train)
y_pred_test=clf.predict(X_test)
y_pred_outliers=clf.predict(X_outliers)

n_error_train=y_pred_train[y_pred_train==-1].size
n_error_test=y_pred_test[y_pred_test==-1].size
n_error_outliers=y_pred_outliers[y_pred_outliers==-1].size

print("Percentage of correctly classify positive class in train set: "+str(1-n_error_train/len(X_train)))
print("Percentage of correctly classify positive class in test set: "+str(1-n_error_test/len(X_test)))
print("Percentage of correctly classify outliers: "+str(1-n_error_outliers/len(X_outliers)))
print("Accuracy in the entrie test set: "+ str(1-(n_error_test+n_error_outliers)/(len(X_test)+len(X_outliers))))

#########

print('nu=0.1')

clf=svm.OneClassSVM(nu=0.1)
clf.fit(X_train)


Z=clf.decision_function(np.c_[xx.ravel(), yy.ravel()]) #c_ concatena lungo il secondo asse, verticalmente; ravel restituisce un array 1-D

Z=Z.reshape(xx.shape)

plt.title('Outside red circle is extimating outlier region')

plt.contourf(xx, yy, Z, levels=[Z.min(),0], colors='gray')

a=plt.contour(xx, yy, Z, levels=[0], linewidths=4, color='red')

plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')


s=40

b1=plt.scatter(X_train[:,0], X_train[:,1], s=s, edgecolors='k')

c=plt.scatter(X_outliers[:,0], X_outliers[:,1], s=s, edgecolors='k')

b2=plt.scatter(X_test[:,0], X_test[:,1], s=s, edgecolors='k')

plt.legend([b1,c,b2],["positive in train data", "outliers in test data", "positive in test data"], loc="upper left")

plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned frontier", "training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.show()

#

y_pred_train=clf.predict(X_train)
y_pred_test=clf.predict(X_test)
y_pred_outliers=clf.predict(X_outliers)

n_error_train=y_pred_train[y_pred_train==-1].size
n_error_test=y_pred_test[y_pred_test==-1].size
n_error_outliers=y_pred_outliers[y_pred_outliers==-1].size

print("Percentage of correctly classify positive class in train set: "+str(1-n_error_train/len(X_train)))
print("Percentage of correctly classify positive class in test set: "+str(1-n_error_test/len(X_test)))
print("Percentage of correctly classify outliers: "+str(1-n_error_outliers/len(X_outliers)))
print("Accuracy in the entrie test set: "+ str(1-(n_error_test+n_error_outliers)/(len(X_test)+len(X_outliers))))


############
print('nu=0.1 e gamma=10')

clf = svm.OneClassSVM(nu=0.1,gamma=10)
clf.fit(X_train)

Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("Outside red circle is extimating outlier region")
plt.contourf(xx, yy, Z, levels=[Z.min(), 0], colors="gray")
a = plt.contour(xx, yy, Z, levels=[0], linewidths=4, colors='red')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], s=s, edgecolors='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], s=s,
                edgecolors='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], s=s,
                 edgecolors='k')
plt.legend([b1,c,b2],["positive in train data", "outliers in test data", "positive in test data"], loc="upper left")
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned frontier", "training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.show()

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
print("Percentage of correctly classify positive class in train set: "+str(1-n_error_train/len(X_train)))
print("Percentage of correctly classify positive class in test set: "+str(1-n_error_test/len(X_test)))
print("Percentage of correctly classify outliers: "+str(1-n_error_outliers/len(X_outliers)))
print("Accuracy in the entrie test set: "+ str(1-(n_error_test+n_error_outliers)/(len(X_test)+len(X_outliers))))

###########
print('nu=0.1 e gamma=0.0001')

clf = svm.OneClassSVM(nu=0.1,gamma=0.0001)
clf.fit(X_train)


Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("Outside red circle is extimating outlier region")
plt.contourf(xx, yy, Z, levels=[Z.min(), 0], colors="gray")
a = plt.contour(xx, yy, Z, levels=[0], linewidths=4, colors='red')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], s=s, edgecolors='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], s=s,
                edgecolors='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], s=s,
                 edgecolors='k')
plt.legend([b1,c,b2],["positive in train data", "outliers in test data", "positive in test data"], loc="upper left")
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned frontier", "training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.show()

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
print("Percentage of correctly classify positive class in train set: "+str(1-n_error_train/len(X_train)))
print("Percentage of correctly classify positive class in test set: "+str(1-n_error_test/len(X_test)))
print("Percentage of correctly classify outliers: "+str(1-n_error_outliers/len(X_outliers)))
print("Accuracy in the entrie test set: "+ str(1-(n_error_test+n_error_outliers)/(len(X_test)+len(X_outliers))))

################

clf = svm.OneClassSVM(kernel="poly", degree=2,nu=0.1)
clf.fit(X_train)


Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("Outside red circle is extimating outlier region")
plt.contourf(xx, yy, Z, levels=[Z.min(), 0], colors="gray")
a = plt.contour(xx, yy, Z, levels=[0], linewidths=4, colors='red')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], s=s, edgecolors='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], s=s,
                edgecolors='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], s=s,
                 edgecolors='k')
plt.legend([b1,c,b2],["positive in train data", "outliers in test data", "positive in test data"], loc="upper left")
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned frontier", "training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.show()

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
print("Percentage of correctly classify positive class in train set: "+str(1-n_error_train/len(X_train)))
print("Percentage of correctly classify positive class in test set: "+str(1-n_error_test/len(X_test)))
print("Percentage of correctly classify outliers: "+str(1-n_error_outliers/len(X_outliers)))
print("Accuracy in the entrie test set: "+ str(1-(n_error_test+n_error_outliers)/(len(X_test)+len(X_outliers))))



