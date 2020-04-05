import tensorflow as tf
import numpy as np

x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

i = 0
m1 = 0
while i<10:
    M1 = tf.multiply(x[i],y[i])
    m1 = tf.add(m1,M1)
    i = tf.add(i,1)
m2 = tf.multiply(m1,10)

m3 = tf.reduce_sum(x)
m4 = tf.reduce_sum(y)
m5 = tf.multiply(m3,m4)
w1 = tf.subtract(m2,m5)

j = 0
n1 = 0
while j<10:
    M2 = tf.pow(x[j],2)
    n1 = tf.add(n1,M2)
    j = tf.add(j,1)
n2 = tf.multiply(n1,10)

n3 = tf.pow(m3,2)
w2 = tf.subtract(n2,n3)

w = tf.divide(w1,w2)

a1 = tf.multiply(w,m3)
b1 = tf.subtract(m4,a1)
b = tf.divide(b1,10)

print(w)
print(b)