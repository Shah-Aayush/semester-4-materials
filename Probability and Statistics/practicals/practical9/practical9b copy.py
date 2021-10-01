#on boston house-prices dataset
#Samples Total 506
#Dimensionality 13
#Features real, positive
#targets real
import numpy as np
from sklearn import datasets, linear_model, metrics
from sklearn.preprocessing import StandardScaler
# Load the boston dataset
X, y = datasets.load_boston(return_X_y=True)
X_train=X[0:400,:]
y_train=y[0:400]
X_test=X[400:506,:]
y_test=y[400:506]

print(X_train)
print(X_test)

#
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test=scaler.transform(X_test)
# Create linear regression object
regr = linear_model.SGDRegressor(max_iter=1000,learning_rate='constant', eta0=0.01)
# Train the model using the training sets
regr.fit(X_train, y_train)
predictions=regr.predict(X_test)
print("Predictions :")
print(predictions)
# Calculating the mean squared error of the prediction
# Calculating the mean absolute error of the prediction
mse = np.sum((predictions-y_test)**2)/len(y_test)
mae = np.sum(abs(predictions-y_test))/len(y_test)
print(f'Mean Square Error : {mse}')
print(f'Mean Absolute Error : {mae}')
print(f'Predicted Coefficients : ')
# Calculating the slope 
for i in range(len(regr.coef_)):
    print(f'x{i+1} : {(regr.coef_)[i]}')
print(f'Predicted Intercept : {(regr.intercept_)[0]}')
