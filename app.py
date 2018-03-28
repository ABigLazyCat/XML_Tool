#encoding:utf-8

####################################################################################

__author__ = 'ABigLazyCat'

####################################################################################
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import lxml.etree.ElementTree as ET

import translate
import csv_generator






def xml_read(in_path):

	#各种所需变量
	clip_info_list = []
	clip_info_dict = {}
	clip_attrib = ('clipname', 'clip_duration',  'source_in', 'source_out', 'record_in', 'record_out', 'filename', 'file_duration', 'file_rate', 'start_timecode', 'reelname')
	timeline_info_list = []
	csv_info = []
	#读取xml文件
	tree = ET.parse(in_path)
	root = tree.getroot()

	#生成文件名
	timeline_name = tree.find('sequence/name').text
	timeline_flames_rate = tree.find('sequence/rate/timebase').text
	timeline_duration_flames = tree.find('sequence/duration').text
	timeline_duration_timecode = translate.flame2timecode(int(timeline_duration_flames),int(timeline_flames_rate) )
	csv_name = "%s-%spfs-%s.csv"%(timeline_name, timeline_flames_rate, timeline_duration_timecode)


	#读取需要的xml信息
	for clips in tree.iterfind('sequence/media/video/track/clipitem/'):
		if clips.tag == 'name':
			clipname = str(clips.text.rstrip('.mov'))
			clip_info_list.append(clipname)
		if clips.tag == 'duration':
			clip_duration = clips.text
			clip_info_list.append(clip_duration)
		if clips.tag == 'in':
			source_in = clips.text
			clip_info_list.append(source_in)
		if clips.tag == 'out':
			source_out = clips.text
			clip_info_list.append(source_out)
		if clips.tag == 'start':
			record_in = clips.text
			clip_info_list.append(record_in)
		if clips.tag == 'end':
			record_out = clips.text
			clip_info_list.append(record_out)
		if clips.tag == 'file':
			filename = clips.attrib['id']
			clip_info_list.append(filename)
			file_duration = clips.find('duration')
			if file_duration != None:
				file_duration = clips.find('duration').text
				clip_info_list.append(file_duration)
				file_rate = clips.find('timecode/rate/timebase').text
				clip_info_list.append(file_rate)
				start_timecode = clips.find('timecode/string').text
				clip_info_list.append(start_timecode)
				reel = clips.find('timecode/reel')
				if reel != None:
					reelname = reel.find('name').text
					clip_info_list.append(reelname)
				else:
					clip_info_list.append('Lose_reelname')
			else:
				lose_list = ['file_duration', 'file_rate', 'start_timecode', 'reelname']
				clip_info_list.extend(lose_list)
			print clip_info_list
			clip_info_dict = dict(zip(clip_attrib, tuple(clip_info_list)))
			timeline_info_list.append(clip_info_dict)
			csv_info.append(tuple(clip_info_list))
			clip_info_list = []

	csv_generator.cvs_write(csv_name, clip_attrib,csv_info)



if __name__ == '__main__':
	xml_read('Reel.xml')




