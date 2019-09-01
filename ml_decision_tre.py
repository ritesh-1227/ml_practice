from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt


clf = DecisionTreeClassifier()
f = [[23,5000,0],[26,10000,0],[28,40000,1],[35,70000,1]]
l = ['No','No','Yes','Yes']
trained = clf.fit(f,l)
res = trained.predict([[15,30000,0],[40,40000,1]])
print(res)
