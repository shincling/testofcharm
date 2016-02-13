#-*- coding:utf-8 -*-
import re
f_test=open(r'/home/shin/DeepLearning/数据集/qa22_plane_1000_test.txt','r')
f_train=open(r'/home/shin/DeepLearning/数据集/qa22_plane_1000_train.txt','r')
cont1=f_test.read()
cont2=f_train.read()
cont1=re.findall(r'[0-9]* 。',cont1)
print cont1

'fffff'