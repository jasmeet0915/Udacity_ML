#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = SVC(kernel="rbf", C = 10000.0)  ### Accuracy:  0.8924914675767918 with C = 10000
### slicing the training dataset to reduce training time
### only 1% of original data left
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

start = time()
clf.fit(features_train, labels_train)
end = time()
print
print "Training time: ", end - start
start = time()
labels_predict = clf.predict(features_test)
end = time()
print
print "Prediction time: ", end - start

accuracy = accuracy_score(labels_test, labels_predict)
print "Accuracy: ", accuracy
print "Prediction of element 10", labels_predict[10]
print "Prediction of element 26", labels_predict[26]
print "Prediction of element 50", labels_predict[50]


count = 0
for i in range(len(labels_predict)):
    if labels_predict[i] == 1:
        count = count + 1
print "No. of emails by Chris:", count
#########################################################


