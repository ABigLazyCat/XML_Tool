#encoding:utf-8

####################################################################################

__author__ = 'ABigLazyCat'

####################################################################################

import csv
import sys
import codecs

reload(sys)
sys.setdefaultencoding('utf-8')


def cvs_write(csv_name, csv_head, csv_info):
	f = open(csv_name,'w')
	f.write(codecs.BOM_UTF8) #避免中文字符乱码
	csvwriter = csv.writer(f)
	#写入表头
	csvwriter.writerow(csv_head)
	for i in csv_info:
		csvwriter.writerow(i)
	f.close()