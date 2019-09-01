from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(hidden_layer_sizes = (1000),max_iter = 10000,random_state=42)
f = [[150,1],[170,1],[180,1],[155,1],[100,0],[90,0],[85,0],[110,0]]
l = ['m','m','m','m','o','o','o','o']
trained = clf.fit(f,l)
res = trained.predict([[140,1],[126,0]])
print(res)
