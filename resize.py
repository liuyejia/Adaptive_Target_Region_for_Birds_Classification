import numpy as np
import cv2
import os

txt_file='/home/luwei/Downloads/CUB_200_2011/images.txt'
#store image path to path_list
path_list=[]
with open(txt_file) as f:
	for line in f:
		word=line.split()
		list=word[-1].split("/")
		path_list.append(list[-1])

new_img_path=r'/home/luwei/Downloads/CUB_200_2011/new_images'
if not os.path.exists(new_img_path):
	os.makedirs(new_img_path)
img_dir='/home/luwei/Downloads/CUB_200_2011/images'
#resize images and store to img_dir
for img_name in path_list:
	for subdir,dirs,files in os.walk(img_dir):
		for file in files:
			if file.endswith(img_name):
  				#print file
				#src=os.path.join(img_dir,file)
				#if file is not None:
				#file=file.lower()
				#os.rename(os.path.join(img_dir,file),os.path.join(img_dir,file).lower())	
				img=cv2.imread(os.path.join(subdir,file))
#				print img
				res=cv2.resize(img,(200,200),interpolation=cv2.INTER_CUBIC)
#                                print res
				#new_img=cv2.resize(file,(200,200))
#	                        os.path.join(new_img_path,res.split('/')[-1])

				cv2.imwrite(new_img_path+'/'+file,res)	

