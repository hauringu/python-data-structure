# -*- coding: utf-8 -*- 
# @Time : 2021/4/23 9:32 
# @Author : HGuoo 
# @File : uuid_create.py

import uuid


uid = str(uuid.uuid4())
suid = ''.join(uid.split('-'))
print(suid)
print(len("0d4835f11b1636631b0f98447f819f3c") == len(suid))