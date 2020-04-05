from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np 

mnist = tf.keras.datasets.mnist
(train_x, train_y),(test_x, test_y) = mnist.load_data()
plt.rcParams['font.family'] = 'SimHei'
factor = ["标签值：",]
plt.figure(figsize=(6,6))


for i in range(16):
    num = np.random.randint(1,50000)
    plt.subplot(4,4,i+1)
    plt.axis("off")
    plt.imshow(train_x[num],cmap='gray')
    a = train_y[num]
    plt.title(str(factor[0])+str(train_y[num]),fontsize=14)

plt.tight_layout(rect=[0,0,1,0.9])
plt.suptitle("MNIST测试集样本",x=0.5,y=1,fontsize=20,color="red")
plt.show()