import matplotlib 
import matplotlib.pyplot as plt
import numpy as np 
import tensorflow as tf 

boston = tf.keras.datasets.boston_housing
(train_x,train_y),(test_x,test_y) = boston.load_data(test_split=0) #我们让测试数据为0

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False

factor = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE",
            "DIS","RAD","TAX","PTRATIO","B-1000","LASTAT","MEDV"]
plt.figure(num='13辅图',figsize=(12,12))

#第一步，逐一取出这些因素
for i in range(13):
    plt.subplot(4,4,i+1)
    plt.scatter(train_x[:,i],train_y,s=3)
    plt.ylabel("prices($1000's)")
    plt.title(str(i+1)+"."+factor[i]+" - Prices")

#设置填充,调整子图空白，布局。

plt.tight_layout()
plt.subplots_adjust(wspace =0.35, hspace =0.33,top=0.93,right=0.95,left=0.05,bottom=0.03)#调整子图间距
#设置全局标题
plt.suptitle("各个因素与房价的关系",x=0.5,y=1,fontsize=20)
plt.show()

############################################

for i in range(1,14):
    if i<10:
        print("%d"%(i),"-- "+factor[i-1])
    else:
        print("%d"%(i),"- "+factor[i-1])
input_n = int(input("请选择属性："))
if 0<input_n<14:
    plt.figure(num=("波士顿数据图"+str(factor[input_n-1])))
    #绘制散点图
    
    plt.scatter(train_x[:,input_n-1],train_y,s=3)
    plt.ylabel("prices($1000's)")
    plt.title(str(input_n)+"."+factor[input_n-1]+" - Prices")

#设置填充,调整子图空白，布局。

plt.tight_layout()
plt.show()