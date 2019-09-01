import tensorflow as tf

w = tf.Variable(0.3,tf.float32)
b = tf.Variable(0.3,tf.float32)
x = tf.placeholder(tf.float32)

y = w*x+b
Y = tf.placeholder(tf.float32)
##f = tf.Variable((y-Y)**2)

loss = tf.reduce_sum(tf.square(y-Y))
opt = tf.train.GradientDescentOptimizer(0.001)
t = opt.minimize(loss)
init = tf.global_variables_initializer()
s = tf.Session()
s.run(init)

a = [1,2,3,4]
k = [2,3,4,5]
##for i in range(500):
##    print(s.run([t,loss],{Y: k , x: a}))
##    print(s.run([w,b]))

print(s.run([t,loss],{Y: k , x: a}))
print(s.run([w,b]))

##s = tf.Session()
##print(s.run(c))
