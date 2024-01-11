---
layout: post
title: Logistic Regression & Cancer Prediction
tags: ['hacks']
categories: ['CSP', 'Week 2']
---

```python
import pandas as pd
```

### Dataset Import


```python
dataset = pd.read_csv('breast_cancer.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
```

### Split dataset into training & test set


```python
import sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X_test)
print(X_train)
print(y_test)
print(y_train)
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    /tmp/ipykernel_1283/3606614524.py in <module>
    ----> 1 import sklearn
          2 from sklearn.model_selection import train_test_split
          3 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
          4 print(X_test)
          5 print(X_train)


    ModuleNotFoundError: No module named 'sklearn'


### Train logistic regression model with data set


```python
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)
```

### Predicting the results


```python
y_pred = classifier.predict(X_test)
print(y_pred)
```

### Confusion Matrix


```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
```

### Computing the accuracy with k-Fold Cross Validation


```python
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
```
