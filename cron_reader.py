import sys
import time

# Get current time (clock seconds)
tm = time.localtime()

# For each line in stdin...
for line in sys.stdin:
	line_elements = line.split(' ')
	# Extract the times
	minute  = line_elements[0]
	hour    = line_elements[1]
	command = ' '.join(line_elements[2:])
	if minute == ['*']:
		minute = list(range[0,60])
	else:
		minute = [minute,]
	if hour == '*':
		hour = list(range[0,24])
	else:
		hour = [hour,]
	for m in minute:
		for h in hour:
			# calculate time
			runtime = time.localtime(tm.tm_year, tm.tm_mon, tm.tm_mday, h, m, tm.tm_sec, tm.tm_wday, tm.tm_yday, tm.tm_isdst)
			if runtime > tm:
				print('Next run at: ' + str(runtime.tm_hour) + ':' + str(runtime.tm_min)
				# TODO: tidy up and work out if tomorrow or not
				break
