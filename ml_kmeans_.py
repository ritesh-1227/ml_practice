from sklearn.cluster import KMeans
cls = KMeans(n_clusters = 2)
f = [[1,2],[2,3],[15,4],[8,7],[4,6],[3,6],[8,3],[2,4],[6,6]]

trained = cls.fit(f)
res = trained.predict([[5,9],[9,9],[4,1],[4,4],[10,11],[11,11]])
print(res)
print(trained.cluster_centers_)



##
##a = [1,2,5]
##b = a
##del b[0]
##print(a)
