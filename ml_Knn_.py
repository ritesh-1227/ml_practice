import matplotlib.pyplot as plt
f = [[10,5],[40,7],[5,3],[2,4]]
l = ['good','good','bad','bad']
list_good = []
list_bad = []
for i in range(len(l)):
    if l[i]=='good':
        list_good.append(f[i])
    elif l[i] == 'bad':
        list_bad.append(f[i])
good_saving = []
good_habit = []
bad_saving = []
bad_habit = []
for i in range(len(list_good)):
    good_saving.append(list_good[i][0])
    good_habit.append(list_good[i][1])
for i in range(len(list_bad)):
    bad_saving.append(list_bad[i][0])
    bad_habit.append(list_bad[i][1])
print(good_saving)
print(good_habit)
print(bad_saving)
print(bad_habit)
test_data = [input('Enter the test data : ').split(' ') for i in range(2)]
print(test_data)
test_saving = []
test_habit = []
for i in range(len(test_data)):
    test_saving.append(int(test_data[i][0]))
    test_habit.append(int(test_data[i][1]))
d_g = []
d_b = []
dist_sq_g = 0
dist_sq_b = 0
k = min(len(bad_habit),len(good_habit))
for i in range(len(test_data)):
    dist_sq_g = ((test_saving[i]-good_saving[i])**2+(test_habit[i]-good_habit[i])**2)
    d_g.append(dist_sq_g**0.5)
    dist_sq_b = ((test_saving[i]-bad_saving[i])**2+(test_habit[i]-bad_habit[i])**2)
    d_b.append(dist_sq_b**0.5)
print(d_g)
print(d_b)

final_dist_g = []
final_dist_b = []
for i in range(k):
    final_dist_g.append(min(d_g))
    final_dist_b.append(min(d_b))
    d_g.remove(min(d_g))
    d_b.remove(min(d_b))
print(final_dist_g)
print(final_dist_b)
d_min = min((sum(final_dist_g)/len(final_dist_g)),(sum(final_dist_b)/len(final_dist_b)))
print(d_min)
for i in range(k):
    if d_min == (sum(final_dist_g)/len(final_dist_g)):
        print('good')
    else:
        print('bad')
plt.plot(good_saving,good_habit,'r*')
plt.plot(bad_saving,bad_habit,'b*')
plt.show()
