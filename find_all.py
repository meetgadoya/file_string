import fnmatch
import os
import time
import operator
class find_all:
    def __init__(self):
        self.d={}

        self.files=[]
        for filename in os.listdir(os.getcwd()):
            if fnmatch.fnmatch(filename, 'P*.txt'):
                file_obj=open(filename,"r",encoding="utf8")
                self.files.append(filename)
                for line in file_obj:
                    for word in line.split():
                        if word=='\n':
                            continue

                        self.d[(filename,word)] = 1
                file_obj.close()

        # self.d = sorted(self.d.items(), key=operator.itemgetter(1))
        # print("hi")
        # print("hello")
        # print(self.d)

    def find_property(self,strings):
        li=[]
        for eachfile in self.files:
            count=0
            for string in strings:
                if (eachfile,string) in self.d.keys():
                        count+=1
                        # if(self.d[(eachfile,string)])>1:
                        #     print((eachfile,string),self.d[(eachfile,string)])
                        #     break
                        # count+=self.d[(eachfile,string)]
            if(count==0):
                continue
            li.append((eachfile,count))
        # print("li")
        # print(li)
        li=sorted(li,key=lambda x:-x[1])
        print(li)



        ################################################################################################################
        # li={}
        # res=[]
        # for k in self.d.keys():
        #     if k[1] in strings:
        #         if k[0] in li:
        #             li[k[0]]+=1
        #         else:
        #             li[k[0]]=1
        #
        # # res=list(li)
        # for key, value in li.items():
        #     temp = [key, value]
        #     res.append(temp)
        # res=sorted(res,key=lambda x:-x[1])
        # print("LI")
        # print(li)
        # print(res)




find=find_all()


for filename in os.listdir(os.getcwd()):
    if fnmatch.fnmatch(filename, 'sample*.txt'):
        start = time.time()
        word_list=[]
        print(filename)
        file_obj = open(filename, "r", encoding="utf8")
        for line in file_obj:
            for word in line.split():
                word_list.append(word)
        find.find_property(word_list)
        end = time.time()
        print("Time took", (end - start),"seconds\n")


