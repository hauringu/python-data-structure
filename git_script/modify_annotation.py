# -*- coding: utf-8 -*- 
# @Time : 2021/5/25 15:57 
# @Author : HGuoo 
# @File : modify_annotation.py


import os


def modify(path):
    try:
        all_line = []
        with open(path, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                if "// ToStringFormat ..\n" == line:
                    print("两个点")
                    all_line.append("// ToStringFormat ...\n")
                elif "// ToStringFormat ...\n" == line:
                    print("三个点")
                    all_line.append("// ToStringFormat ..\n")
                else:
                    all_line.append(line)
            f.close()
        with open(path, 'w', encoding='UTF-8') as f:
            f.writelines(all_line)
            f.close()
    except:
        print("出错了")


path = 'log.go'
modify(path)
os.system("git add log/log.go" + path)
#os.system("git commit -m '--story=861918779 增加构建成功率'")
#os.system("git push")