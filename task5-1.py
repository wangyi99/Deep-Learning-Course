import numpy as np
np.random.seed(612)
a = np.random.rand(1000,)
x = int(input("请输入一个1~100的整数："))
y = range(1,1001)
m = 1
for i in range(1,1001):
    if i%x==0:
        print(m,"\t",i,"\t",a[i-1])
        i+=1
        m+=1
    else:
        i+=1
    
