#coding=utf-8
import os
count=0
def findSizeFile(path,size):
        global count
        tuples=os.walk(path)
        for root,dirs,files in tuples:
                for file in files:
                            if os.path.getsize(os.path.join(root,file))>size*1024*1024:
                                    count+=1
                                    print(f"文件:{os.path.join(root,file)}，u大小:{os.path.getsize(os.path.join(root,file))}")
path = "/workspace/All-in-One"
size = 1 #单位为MB
findSizeFile(path,size)
