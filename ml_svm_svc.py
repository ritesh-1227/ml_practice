from sklearn import svm
import pandas as pd
import matplotlib.pyplot as plt
import time

clf = svm.SVC(kernel = 'linear')

data = pd.read_csv(r'headbrain.csv')
##print(data)

X_train = pd.concat([data[:200]['Brain Weight(grams)'],data[:200]['Head Size(cm^3)']],axis = 1)
Y_train = data[:200]['Gender']
X_test = pd.concat([data[200:237]['Brain Weight(grams)'],data[200:2037]['Head Size(cm^3)']],axis = 1)
Y_test = data[200:237]['Gender']


X_test_x = X_test['Brain Weight(grams)']
X_test_y = X_test['Head Size(cm^3)']

trained = clf.fit(X_train,Y_train)
res = trained.predict(X_test)
print(res)
print(trained.score(X_test,Y_test))
X_test_x.index = range(0,37)
for i in range(len(X_test_x)):
    if res[i] == 1:
        plt.plot(X_test_x.iloc[i],X_test_y.iloc[i],'r+')
        plt.pause(1e-10)
        time.sleep(0.01)
    else:
        plt.plot(X_test_x.iloc[i],X_test_y.iloc[i],'b^')
        plt.pause(1e-10)
        time.sleep(0.01)
    
    
plt.show()
