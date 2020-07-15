# encoding: utf-8
'''
@author: td.wu
@contact: tdwu@iflytek.com
@file: infer.py
@time: 2020/7/14 20:42
'''



print ("")
from bert import Ner

model = Ner("./chinese_out_put")

output = model.predict("我")



print ("...infer...")
print (output)
