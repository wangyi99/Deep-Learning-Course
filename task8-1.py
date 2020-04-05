import tensorflow as tf
import numpy as np

x = tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

X = tf.reduce_mean(x)
Y = tf.reduce_mean(y)

i = 0
m = 0
while i<10:
    w1 = tf.subtract(x[i],X)
    w2 = tf.subtract(y[i],Y)
    z1 = tf.multiply(w1,w2)
    m = tf.add(m,z1)
    i = tf.add(i,1)
    # z = ((x[i]-X)*(y[i]-Y))/((x[i]-X)*(x[i]-X))
    # w += z
    # i+=1
j=0
n=0
while j<10:
    w3 = tf.subtract(x[j],X)
    z2 = tf.pow(w3,2)
    n = tf.add(n,z2)
    j = tf.add(j,1)
w = tf.divide(m,n)

b1 = tf.multiply(w,X)
b = tf.subtract(Y,b1)
print(w)
print(b)