# coding=utf-8
# @Time    : 2017-11-16 13:38
# @Useage  : fileutils
# @Author  : crazylaser
# @File    : fileclass.py
# @Software: PyCharm
import os, shutil,chardet,zipfile


class File(object):
    #初始方法判断是否存在
    def __init__(self, url=os.getcwd()):
        # self.url = url
        url = url.replace("\\","/")
        #传入unicode 判断文件是否存在调用系统组件 gbk判断
        # 去除文件初始化的判断
        # if not os.path.exists(url):
        #     print u"文件路径不存在"
        #     exit(1)
        self.url = url
    #获取文件夹名字或文件名字
    def name(self):
        # return os.path.split(mulu)[1]
        # return os.path.basename(self.mulu)
        return self.url.split("/")[-1]
    # 获取文件上一级路径
    def locate(self):
        return '/'.join(self.url.split("/")[:-1])
    # 获取文件全路径
    def value(self):
        return self.url
    #删除文件或文件夹
    def delete(self):
        if os.path.isdir(self.url):
            shutil.rmtree(self.url)
        else:
            os.remove(self.url)
    # 重命名文件或文件夹
    def rename(self, newname):
        os.renames(self.url, '/'.join(self.url.split("/")[:-1]) + "/" + newname)
        self.url = '/'.join(self.url.split("/")[:-1]) + "/" + newname
    #创建文件夹或文件
    def create(self, filename):
        filename = filename.encode("gbk")
        print os.path.splitext(filename)
        if self.contains(filename.decode("gbk")):
            print u"文件已存在"
            # 此处中断函数
            # exit(1)
        else:
            if '.' in filename and os.path.splitext(filename)[1] != '.war':
                open(self.url + os.sep + filename, 'w').close()
            else:
                os.makedirs(self.url + os.sep + filename)
    # 显示文件夹里第一层文件
    def list(self):
        return os.listdir(self.url)
    #获取文件夹目录树
    def listall(self):
        walk = os.walk(self.url)
        walkarr = []
        resultarr = []
        for i in walk:
            walkarr.append(i)
        for i in walkarr:
            # if walkarr.index(i) != 0:
            if not (any(i[2]) or any(i[1])):
                resultarr.append(i[0])
                # print i[0]
            if any(i[2]):
                for file2 in i[2]:
                    resultarr.append(i[0] + "/" + file2)
                    # print i[0] + "\\" + file2
        return resultarr
    # 清除文件夹或文件内容
    def clean(self):
        if os.path.isdir(self.url):
            for file in self.list():
                listfile = File(self.url + os.sep + file)
                listfile.delete()
                # shutil.rmtree(self.url)
                # os.makedirs(self.url.encode("gbk"))
        else:
            file = open(self.url, "w")
            file.write("")
            file.close()
    # 判断文件夹是否含有文件
    def contains(self, filename):
        flag = False
        # print filename
        # for file2 in os.listdir(self.url):
        #     print file2
        for file2 in os.listdir(self.url):
            flag = flag or file2 == filename.encode("gbk")
        return flag
    # 向文件中写入字符串或字符串列表
    def write(self, str1):
        if not os.path.isdir(self.url):
            if type(str1) == str:
                file = open(self.url, "a+")
                file.write(str1)
                file.close()
            else:
                for item in str1:
                    file = open(self.url, "a+")
                    file.write(str(item))
                    file.close()
    # 读取文件内容并打印
    def read(self):
        if not os.path.isdir(self.url):
            file = open(self.url, "a+")
            # 读取全部内容
            print file.read()
            # 读取一行
            # print file.readline()
            file.close()
    # 复制文件或文件夹
    def copy(self, targetdir):
        if not os.path.exists(targetdir.encode("gbk")):
            print u"文件路径不存在"
            self.mkdir(targetdir.encode("gbk"))
            print u"已创建路径"
        # print self.url
        print targetdir.encode("gbk") + os.sep + self.name()
        if not os.path.isdir(self.url):
            shutil.copy(self.url, targetdir.encode("gbk") + os.sep + self.name())
        else:
            shutil.copytree(self.url, targetdir.encode("gbk") + os.sep + self.name())
    # 调用os方法创建多重文件路径 创建全路径非当前文件的相对路径
    def mkdir(self,targetdir):
        if  os.path.exists(targetdir.encode("gbk")):
            print u"文件夹已存在"
        else:
            os.makedirs(targetdir)
    # ###############################################################获取文件内容并返回list
    def  getTextList(self):
        list1 = []
        for i in open(self.url, "a+").read().split("\n"):
            list1.append(i+"\n")
        return list1
    # 文件快速跳级
    def cd(self,str1):
        if str1 == "..":
            print self.locate()
            return File(self.locate())
        else:
            # url是类的属性非方法
            return File(self.url+"/"+str1)
    # 创建文件本身
    def generate(self):
        if not os.path.exists(self.url):
            if '.' in self.name() and os.path.splitext(self.name())[1] != '.war':
                if not os.path.exists(self.locate()):
                    os.makedirs(self.locate())
                open(self.url, 'w').close()
            else:
                os.makedirs(self.url)

    def zip(self):
        # .war文件无法压缩
        # name = self.name()
        # # if ".war" in self.name:
        # #     self.rename("tempname")
        # #     flag1 = True
        # #     # name = self.name().replace(".war","")
        # #     filezip.rename(filezip.name().split(".")[0]+".war"+".zip")
        # # else:
        # shutil.make_archive(name, 'zip', self.url)
        # filezip = File(os.getcwd()).cd(name + ".zip")
        # filezip.copy(self.locate())
        # filezip.delete()

        #zipfile模块压缩 空文件夹压缩为文件目前未找到有效的解决方法 zipfile模块没有删除文件方法
        z = zipfile.ZipFile(self.url + ".zip", 'w', zipfile.ZIP_DEFLATED)
        for i in self.listall():
            file2 = File(i)
            if '.' in file2.name() and os.path.splitext(file2.name())[1] != '.war':
                z.write(i, i.replace(self.locate(), ""))
            else:
                file2.create("notexist.txt")
                i = file2.cd("notexist.txt").url
                z.write(i, i.replace(self.locate(), ""))
                file2.clean()
        z.close()
    def has(self,filename):
        filename = filename.decode("utf8")
        return os.path.exists(self.url + os.sep + filename)
if __name__ == '__main__':
    file1 = File(r"C:")
    #所有传入值用utf8编码
    # file1.mkdir(u"c:/u新建文本文档/新建文本文档2/新建文本文档3")
    file2 = File(u"c:\\u新建文本文档")
    file2 = File(r"c:\u新建文本文档".decode("utf8"))
    # for i in file2.listall():
    #     tempi = i
    #     print chardet.detect(i)
    #     print tempi.encode("utf8")
    print file2.cd(u"新建文本文档.txt").url.encode("utf8")
    file2.cd(u"新建文本文档.txt").delete()
