import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['font.sans-serif'] = 'SimHei'

img = Image.open('lena.tiff')
img_r,img_g,img_b = img.split()
plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis('off')
img1=img_r.resize((50,50))
plt.imshow(img1,cmap='gray')
plt.title('R-缩放',fontsize=14)

plt.subplot(222)
img2=img_g.transpose(Image.FLIP_LEFT_RIGHT)
img22=img2.transpose(Image.ROTATE_270)
plt.imshow(img22,cmap='gray')
plt.title('G-镜像+旋转',fontsize=14)

plt.subplot(223)
plt.axis('off')
img3=img_b.crop((0,0,150,150))
plt.imshow(img3,cmap='gray')
plt.title('B-裁剪',fontsize=14)

plt.subplot(224)
plt.axis('off')
img4=Image.merge('RGB',[img_r,img_g,img_b])
plt.imshow(img4)

plt.title('图像的色彩模式',fontsize=14)
img4.save('test.png')

plt.suptitle("图像基本操作",x=0.5,y=1,fontsize=20,color="blue")
plt.show()