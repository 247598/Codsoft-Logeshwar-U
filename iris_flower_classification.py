# -*- coding: utf-8 -*-
"""Iris Flower Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jsC9LmPDlow8sf4J1wvqvpod5lll7Suu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('IRIS.csv')

df.head()
df.columns
df.info()
df.describe()

sns.pairplot(df , hue = 'species' , markers = [ 'o' , 's' , 'D'])
plt.show()

plt.figure(figsize=(14, 10))
for i, column in enumerate(df.columns[:-1]):
  plt.subplot(2, 2, i + 1)
  sns.violinplot(x='species', y=column, data=df, inner='quartile')
  plt.title(f'{column} distribution by species')
  plt.show()

X = df.drop(['species'] , axis = 1)
y = df['species']
X_train , X_test , y_train , y_test = train_test_split(X , y, test_size = 0.25, random_state = 10)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_train = pd.DataFrame(data=X_train, columns=cols)

X_test = scaler.transform(X_test)

X_test = pd.DataFrame(data=X_test, columns=cols)

X_train.head()

svc = SVC()
svc.fit(X_train , y_train)
y_pred = svc.predict(X_test)
print("Model Accuracy score with default hypoparameters: {0:0.2f}" . format(accuracy_score(y_test, y_pred)))

y_pred_train = svc.predict(X_train)
print(y_pred_train)
print('Training-set accuracy score: {0:0.4f}'.format(accuracy_score(y_train, y_pred_train)))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)