import numpy as np
import tensorflow as tf

x1 = tf.constant([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00,114.00,106.69, 138.05,
53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
x2 = tf.constant([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2],dtype=tf.float32)
y = tf.constant([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,62.00, 133.00, 51.00,
45.00, 78.50, 69.65, 75.69, 95.30])

x0 = tf.ones(len(x1))
X = tf.stack((x0,x1,x2),axis=1)
Y = tf.reshape(y,[-1,1])

Xt = tf.transpose(X)
XtX_1 = tf.linalg.inv(tf.matmul(Xt,X))
XtX_1_Xt = tf.matmul(XtX_1,Xt)
w = tf.matmul(XtX_1_Xt,Y)

w = tf.reshape(w,[-1])

print("多元线性回归方程: ")
print("Y=" ,w[1].numpy(), "*x1+", w[2].numpy(), "*x2+",w[0].numpy())

print("请输入房屋面积和房间数，预测房屋销售价格: ")
# x1_test=float (input("商品房面积(20-500):"))
while True:
    x1_test=float (input("商品房面积(20-500):"))
    if 20<=x1_test<=500:
        break
    else:
        print("对不起，超出范围，请重新输入商品房面积(20-500):")
        continue
while True:
    x2_test=int (input("房间数(1-10之间的整数): "))
    if 1<=x2_test<=10:
        break
    else:
        print("对不起，超出范围，请重新输入房间数（1-10）")
        continue

y_pred = w[1]*x1_test+w[2]*x2_test+w[0]
print (" 预测价格:",y_pred.numpy(),"万元") 