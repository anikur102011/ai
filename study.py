# -*- coding: utf-8 -*-
"""study.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10E2dcpCXu_xnlXkVzlf0q3AXt_k4ajly
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('./drive/MyDrive/Colab Notebooks/student_scores.csv')
df.head(5)

X=df.iloc[:,:-1]
y=df.iloc[:,-1]
X.head(5)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import MultinomialNB
reg1 = MultinomialNB()
reg1.fit(X_train,y_train)
plt.scatter(X_train,y_train)
plt.plot(X_train,reg1.predict(X_train))

reg1.score(X_test,y_test)

reg1.predict([[4]])

from sklearn.svm import SVC
reg2 = SVC()
reg2.fit(X_train, y_train)
plt.scatter(X_train,y_train)
plt.plot(X_train,reg2.predict(X_train))

reg2.score(X_test,y_test)

reg2.predict([[2]])

from sklearn.linear_model import LinearRegression
reg3 = LinearRegression()
reg3.fit(X_train,y_train)
plt.scatter(X_train,y_train)
plt.plot(X_train,reg3.predict(X_train))

reg3.score(X_test,y_test)

reg3.predict([[3]])

from sklearn.linear_model import LogisticRegression
reg4 = LogisticRegression(random_state=0)
reg4.fit(X_train,y_train)
plt.scatter(X_train,y_train)
plt.plot(X_train,reg4.predict(X_train))

reg4.score(X_test,y_test)

reg4.predict([[10]])

from sklearn.tree import DecisionTreeClassifier
reg5=DecisionTreeClassifier()
reg5.fit(X_train,y_train)
plt.scatter(X_train,y_train)
plt.plot(X_train,reg5.predict(X_train))

reg5.score(X_test,y_test)

reg5.predict([[10]])

# @title K Means Clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

km = KMeans(n_clusters=3)
yp = km.fit_predict(df)
yp

df['cluster'] = yp
df.head(10)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1['Hours'],df1['Scores'],color='blue')
plt.scatter(df2['Hours'],df2['Scores'],color='green')
plt.scatter(df3['Hours'],df3['Scores'],color='yellow')



scaler = MinMaxScaler()

scaler.fit(df[['Hours']])
df['Hours'] = scaler.transform(df[['Hours']])

scaler.fit(df[['Scores']])
df['Scores'] = scaler.transform(df[['Scores']])
df.head()

km = KMeans(n_clusters=2)
y_predicted = km.fit_predict(df[['Hours','Scores']])
y_predicted

df['cluster']=y_predicted
df.head()

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1['Hours'],df1['Scores'],color='blue')
plt.scatter(df2['Hours'],df2['Scores'],color='green')
plt.scatter(df3['Hours'],df3['Scores'],color='yellow')