# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@Tool:        Sublime Text3
@DateTime:    2018-08-21 17:20:07
'''
#subject:send email，https://github.com/ZYunH/zmail/blob/master/README-cn.md

import zmail
import os
import time
import re

#获取指定文件夹文件列表
def fs(ph,tp='.',kw=None):
	fp=[]#ph文件路径/tp文件类型/kw关键字段
	for filename in os.listdir(ph):
		if kw is None or kw in filename:
			if tp is None or tp in filename:
				fp.append(filename)
			else:
				None
		else:
			None
	return fp


def Smail(attachment=None):
	mail = {
	    'subject': 'Test',  # Anything you want.
	    'content': 'From zmail!',  # Anything you want.
	    'attachments': attachment# Absolute path will be better,like[r'E:/TEST/123.jpg'].
	}
	try:
		server = zmail.server('chen_zhou@vip.sina.com', 'cz1991')#发件人邮箱
		# server.send_mail(['chen_zhou@vip.sina.com','1185192325@qq.com'], mail)#收件人邮箱列表
		if attachment==[] or attachment is None :
			print('Sent Successfully @',time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),'#With no attachments.')
		else:
			print('Sent Successfully @',time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),'#Pay attention to attachments',[''.join(re.sub('(.*?/)','',i)) for i in attachment])#打印添加的附件文件名称
	except:
		print('Falied,Please check or try again!')


if __name__ == '__main__':
	ph='E:/test/'#标准书写,请以/结尾
	files=fs(ph,tp='.',kw='')
	attachment=[ph+filename for filename in files]
	Smail(attachment)


#如果指定的文件夹内包含子文件夹，不指定文件类型或为空（tp=''）的情况下，会导致邮件发送失败，通过设置tp='.'或不添加tp参数，可避免文件夹作为上传附件的异常错误。

