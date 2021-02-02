# -*- coding: utf-8 -*-
"""XGBoost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1llNst83kKhbm1TF2h5_D8PsWrANRMteo

# XGB Regressor on Diabetes Dataset (sklearn)
"""

from sklearn import datasets
X,y = datasets.load_diabetes(return_X_y=True)

from xgboost import XGBRegressor

from sklearn.model_selection import cross_val_score

scores = cross_val_score(XGBRegressor(objective='reg:squarederror'), X, y, scoring='neg_mean_squared_error')
(-scores)**0.5

"""# XGB Classifier on Diabetes Dataset (sklearn)"""

url = 'https://media.githubusercontent.com/media/PacktPublishing/Hands-On-Gradient-Boosting-with-XGBoost-and-Scikit-learn/master/Chapter02/heart_disease.csv'
import pandas as pd
df = pd.read_csv(url)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
print(X)
print(y)

from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
cross_val_score(XGBClassifier(), X, y)