#encoding:utf-8

####################################################################################

__author__ = 'ABigLazyCat'

####################################################################################


def flame2timecode(flames, rate):
	hour = str(flames / ( 3600 * rate )).zfill(2)
	minute = str(flames / ( 60 * rate ) % 60).zfill(2)
	second = str(flames / rate % 60).zfill(2)
	flame = str(flames % rate).zfill(2)
	timecode = "%2s:%2s:%2s:%2s"%(hour, minute, second, flame)
	return timecode

def timecode2flame(timecode, rate):
	hour = int(timecode.split(':')[0]) * 3600 * rate
	minute = int(timecode.split(':')[1]) * 60 * rate
	second = int(timecode.split(':')[2]) * rate
	flame = int(timecode.split(':')[3])
	flames = hour+ minute+ second+ flame
	return flames

def rate_to_rate(source_rate, source_timecode, target_rate):
	duration_flames = timecode_to_flames(source_timecode, source_rate)
	target_timecode = flames_to_timecode(duration_flames, target_rate)
	return target_timecode