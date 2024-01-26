import numpy as np
import pandas as pd

from numpy.random import rand

df  = pd.DataFrame(rand( 50 , 3)*10, columns = 'Hours_studied Hours_slept iQ '.split())
from random import choice
location = []
for i in range(50):
    
    location.append(choice(["New Delhi" , "Pune" , "Bangalore"]))

df['Location'] = location
df.head()
df['Marks'] = (1.73 + (3.34*df['Hours_studied'])
                    + (2.45*df['Hours_slept'])
                    + (1.83*df['iQ']  ))
df['Marks'] =  df['Marks'] +np.random.rand(50)*20
               
df.to_csv('Students.csv',index=False)

dataset = pd.read_csv('Students.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])],  remainder='passthrough')
print(ct)

X = np.array(ct.fit_transform(X))
print(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train , y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(y_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

np.set_printoptions(precision=2)
print("\n\n\nPredicted  Actual")
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
np.set_printoptions(precision=2)
print(np.concatenate((X_test ,y_pred.reshape(len(y_pred),1) ,y_test.reshape(len(y_test),1)) ,1))

print(len(y_pred))
print(y_test)
print(y_pred)