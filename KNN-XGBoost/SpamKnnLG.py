# Authors Linda Benboudiaf

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

datasets = pd.read_csv('/home/lbenboudiaf/Bureau/spamDetector/KNN-XGBoost/DataSets/spambase.csv')
#Shuffle the data
datasets = datasets.sample(frac=1) # we shuffle

## We ignore - drop the two collumns word_freq_george,word_freq_650.

datasets = datasets.drop(labels=['word_freq_george','word_freq_650'], axis=1)

# Split Data
X = datasets.iloc[:,0:55] #Data, don't worry it doesn't include the last colunm.
y = datasets.iloc[:,55] #Target


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.20, shuffle=True) # we shuffle again

'''We use LogisticRegression rather than Scaler is this test
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html'''
#.fit() is LogisticRegression classifier
lr_X = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr', max_iter=10000).fit(X_train, y_train)

# in order to determine the best value to 'K'
# in this case we have 2 classes so it is better ti have an odd number like 3, 7, 11 ...
import math
math.sqrt(len(y_test)) # it gives 30.34 so we take 29 as first best value to 'K'


# we calculate the average.
errorRatio = []
res = []
index = range(3,5)
for i in index:
    # Predict the test set results
    y_pred = lr_X.predict(X_test)
    res.append(mean_absolute_error(y_pred, y_test))
    errorRatio.append(np.mean(y_pred != y_test))

#print(classification_report(y_pred, y_test))
print(classification_report(y_pred, y_test))

### valeur de K
''''https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.figure.html'''
plt.figure(figsize=(14, 6))
plt.plot(index, errorRatio, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error ratio according to K values')
plt.xlabel('K values')
plt.ylabel('Error average')
plt.show()