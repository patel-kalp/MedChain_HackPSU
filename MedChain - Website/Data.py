
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import js2py

plt.style.use('bmh')



#Store the data into data frame
df = pd.read_csv('COVID_PA_COUNTIES.csv')


plt.figure(figsize=(16,8))
plt.title('PA COVID DATA TRACKER')
plt.xlabel('Northern Region Counties of Pennsylvania')
plt.ylabel('Infection Trend (+/-)')
plt.plot(df['Confirmed'])
y = js2py.eval_js(plt.show())

#get the confirmed growth per county
df = df[['Confirmed']]

#get the daily confirmed growth
df = df[['Confirmed']]

#Create a variable to predict 'x' months out into the future
future_trend = 3
#create a new column (target) shifted 'x' units/months up
df['Prediction'] = df[['Confirmed']].shift(-future_trend)

#Create the feature data set (X) and convert it to a numpy array and remove the last 'x' rows/days
X = np.array(df.drop(['Prediction'], 1))[:-future_trend]

#Create the feature data set (X) and convert it to a numpy array and remove the last 'y' rows/days
Y = np.array(df.drop(['Prediction'], 1))[:-future_trend]

#create the target data set (y) and convert it to a numpy array and get all of the target values except the last 'x' rows/days
Y = np.array(df['Prediction'])[:-future_trend]

#split the data into 75% train and 25% test
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.25)

#Create and train the Support Vector Machine (Regressor)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#Create the models
#Create the decision tree regression model
tree = DecisionTreeRegressor().fit(x_train, y_train)
#Create the linear regression model
lr = LinearRegression().fit(x_train, y_train)

#get the last 'x' rows of the feature data set
future_months = 3
x_future = df.drop(['Prediction'], 1)[:-future_months]
x_future = x_future.tail(future_months)
x_future = np.array(x_future)

#show the tree prediction model
tree_prediction = tree.predict(x_future)

#show the linear regression prediction model
lr_prediction = lr.predict(x_future)

#show the SVR prediction model 
svr_rbf_prediction = svr_rbf.predict(x_future)

#visualize the data
predictions = tree_prediction

valid = df[X.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Decision Trees Model')
plt.xlabel('Northern Pennsylvania Region COVID Tracker')
plt.ylabel('Infection Trend (+/- in the # of Confirmed Cases)')
plt.plot(df['Confirmed'])
plt.plot(valid[['Confirmed', 'Predictions']])
plt.legend(['Original', 'Value', 'Prediction'])
f = js2py.eval_js(plt.show())


print(f, y)
#print(y)
print(tree.score(x_test, y_test))
