#-*- coding:utf-8 -*-
import random
f=open(r'/home/shin/DeepLearning/数据集/qa23_plane_train','r')
content=f.read()
print content

fw=open(r'/home/shin/DeepLearning/数据集/qa23_plane_train_rand','w')
for i in range(1000):
    content_rand=content.replace('idnumber',str(random.randint(10000000,99999999)))
    content_rand=content_rand.replace('timetime','20'+str(random.randint(10,15))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,31)))
    fw.write(content_rand)
fw.close()
f.close()