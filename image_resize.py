from PIL import Image
from resizeimage import resizeimage

for i in range (0,5):
    num=4570+i
    img_path='/home/liuyejia/Downloads/img/n01503061_'+str(num)+'.JPEG'
    fd_img = open(img_path, 'r')
    img = Image.open(fd_img)
    img = img.resize((200, 200), Image.BILINEAR)
    img.save('/home/liuyejia/Downloads/img/n01503061_'+str(num)+'_thumbnail.JPEG', "JPEG")
    fd_img.close()

