# -*- coding: utf-8 -*-
"""ISL_A2_CS19B025_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uC7rWu2E72cvf81_ZzvasgGrprUKA1mQ

ISL Assignment 2

Name: Aashrith

Roll: CS19B025

**Note:** Summary of all the resluts can be found at the bottom of the file.

#Imports
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_digits, make_circles
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

"""#Datasets"""

def get_circles_data():
    X_circles, y_circles = make_circles(n_samples=1000, noise=0.03)

    return X_circles, y_circles

# plt.scatter(X_circles[:, 0], X_circles[:, 1])

def get_digits_data():
    X_digits, y_digits = load_digits(return_X_y=True)
    return X_digits, y_digits

# X_digits.shape, y_digits.shape
# plt.matshow(X_digits[567].reshape(8,8))
# print(y_digits[567])

# all_results = {'Dataset': ['Concentric Circles', 'Concentric Circles', 'Concentric Circles', 'MNIST digits', 'MNIST digits', 'MNIST digits'], 'Classifier': ['Random Forest', 'SVC', 'MLP', 'Random Forest', 'SVC', 'MLP'], 'Best Parameters': []}

"""#Concentric Circles

###Random Forest
"""
def get_rf_results(X, y):
    rf = RandomForestClassifier()

    params = {'max_depth': [1, 10, None], 'criterion': ['gini', 'entropy']}

    clf = GridSearchCV(rf, params, scoring='roc_auc')

    clf.fit(X, y)

    # all_results['Best Parameters'].append(clf.best_params_)
    # clf.best_params_

    results_table = pd.DataFrame.from_dict(clf.cv_results_)
    results_table.sort_values(by='rank_test_score')

    return results_table

"""###SVC"""

def get_svc_results(X, y):
    svc = SVC()

    params = {'kernel': ['linear', 'rbf'], 'C': [1, 10, 100]}

    clf = GridSearchCV(svc, params, scoring='roc_auc')

    clf.fit(X, y)

    # all_results['Best Parameters'].append(clf.best_params_)
    # clf.best_params_

    results_table = pd.DataFrame.from_dict(clf.cv_results_)
    results_table.sort_values(by='rank_test_score')

    return results_table

"""###MLP"""

def get_mlp_results(X, y):
    mlp = MLPClassifier()

    alphas = np.logspace(-1, 1, 5)

    params = {'hidden_layer_sizes': [(32), (64), (32, 32)], 'activation': ['identity', 'logistic', 'tanh', 'relu'], 'solver': ['lbfgs', 'sgd', 'adam'], 'alpha': alphas}

    clf = GridSearchCV(mlp, params, scoring='roc_auc')

    clf.fit(X, y)

    # all_results['Best Parameters'].append(clf.best_params_)
    # clf.best_params_

    results_table = pd.DataFrame.from_dict(clf.cv_results_)
    results_table.sort_values(by='rank_test_score')

    return results_table

"""#MNIST Digits

###Random Forest
"""

'''
rf = RandomForestClassifier()

params = {'max_depth': [1, 10, None], 'criterion': ['gini', 'entropy']}

clf = GridSearchCV(rf, params, scoring='roc_auc_ovr')

clf.fit(X_digits, y_digits)

all_results['Best Parameters'].append(clf.best_params_)
clf.best_params_

results_table = pd.DataFrame.from_dict(clf.cv_results_)
results_table.sort_values(by='rank_test_score')

"""###SVC"""

svc = SVC(probability=True)

params = {'kernel': ['linear', 'rbf'], 'C': [1, 10, 100], 'decision_function_shape': ['ovo', 'ovr']}

clf = GridSearchCV(svc, params, scoring='roc_auc_ovr')

clf.fit(X_digits, y_digits)

all_results['Best Parameters'].append(clf.best_params_)
clf.best_params_

results_table = pd.DataFrame.from_dict(clf.cv_results_)
results_table.sort_values(by='rank_test_score')

"""###MLP"""

mlp = MLPClassifier()

alphas = np.logspace(-1, 1, 5)

params = {'hidden_layer_sizes': [(32), (64), (32, 32)], 'activation': ['identity', 'logistic', 'tanh', 'relu'], 'solver': ['lbfgs', 'sgd', 'adam'], 'alpha': alphas}

clf = GridSearchCV(mlp, params, scoring='roc_auc_ovr')

clf.fit(X_digits, y_digits)

all_results['Best Parameters'].append(clf.best_params_)
clf.best_params_

results_table = pd.DataFrame.from_dict(clf.cv_results_)
results_table.sort_values(by='rank_test_score')

"""# Summary of Results"""

summary_table = pd.DataFrame.from_dict(all_results)
summary_table

'''