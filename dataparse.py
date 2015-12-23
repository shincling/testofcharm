#-*- coding:utf-8 -*-
import random
import re

namedict=['张三','李四','王五','赵六','田七','许八','钟九','周杰伦','解晓东','蔡依林']
f=open(r'/home/shin/DeepLearning/MemoryNetwork/QA/planeplane_shin','r')
fw=open(r'/home/shin/DeepLearning/MemoryNetwork/QA/planeplane_shin_rand_1000_train.txt','w')
content=f.read()
#print content
ac=content.split('1 您好')
ac=ac[1:-1]
file=''
for story in ac:
    story='1 您好'+story
    story=story.replace('373522197607234547',str(random.randint(10000000,99999999)))
    story=story.replace('周涛',namedict[random.randint(0,9)])
    file=file+story

fw.write(file)
f.close()
fw.close()


'''
fw=open(r'/home/shin/DeepLearning/数据集/qa23_plane_train_rand.txt','w')
content_rand=content.replace('373522197607234547',str(random.randint(10000000,99999999)))
content_rand=content_rand.replace('timetime','20'+str(random.randint(10,15))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,31)))
fw.write(content_rand)
fw.close()
f.close()

'''
