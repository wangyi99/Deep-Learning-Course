import numpy as np
x = np.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = np.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

xmean = np.mean(x)
ymean = np.mean(y)

i = 0
w = 0
while i<10:
    z = ((x[i]-xmean)*(y[i]-ymean))/((x[i]-xmean)*(x[i]-xmean))
    w += z
    i+=1
print("w的值为：%f"%(w))
b = ymean - w*xmean
print("b的值为：%f"%(b))