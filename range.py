# range 範圍
# python 內建功能：清單產生器

import random

range(5)      # [0,1,2,3,4] 註：結尾值不包含,等同於 range(0,5)
range(3)      # [0,1,2]     註：           等同於 range(0,3)
range(2,5)    # [2,3,4]     註：有含起始值,不含結尾值 
range(2,10,3) # [2,5,8]     註：第三數表示step,每次跳多少
range(3,8,2)  # [3,5,7]
range(10,3,-2)# [10,8,6,4]  註：step 也可以是負數,代表遞減

for i in range(100):
	r=random.randint(1,1000)
	print('第',i+1,'次,亂數值為：',r)
