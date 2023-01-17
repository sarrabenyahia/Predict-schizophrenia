#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 02:11:17 2022
 
@author: benyahiasarra9@gmail.com, pepegarsanz@gmail.com
"""
  
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC, NuSVC
from sklearn.ensemble import GradientBoostingClassifier
 
class ROIsFeatureExtractor(BaseEstimator, TransformerMixin):
    """Select only the 284 ROIs features:"""
    def fit(self, X, y):
        return self
 
    def transform(self, X):
        return X[:, :284]

def get_estimator():
    """Build your estimator here."""
    estimator = make_pipeline(
        ROIsFeatureExtractor(),
        StandardScaler(),
        VotingClassifier(estimators=[('gb', GradientBoostingClassifier(learning_rate=0.5, max_depth = 3, min_samples_leaf = 1, max_features ='log2', n_estimators = 100, subsample = 1)), 
                                        ('nu_svc', NuSVC(nu=0.5, gamma =0.0001, kernel = 'rbf', probability=True, class_weight="balanced" )), 
                                        ('svm', SVC(C=10, class_weight = 'balanced', gamma ='scale', kernel = 'rbf', probability=True ))], 
                            voting='soft'))
    return estimator
 