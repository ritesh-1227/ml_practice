from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

lr = LinearRegression()
X = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]
Y = [[21],[23],[45],[6],[78],[99],[12],[11],[11],[13]]
X_train = X[:5]
Y_train = Y[:5]
X_test = X[5:10]
Y_test = Y[5:10]
trained = lr.fit(X_train,Y_train)
Y_pred = lr.predict(X_test)
plt.plot(X_test,Y_test,'r+')
plt.plot(X_test,Y_pred)
plt.show()
