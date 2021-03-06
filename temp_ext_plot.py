# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:37:20 2016

@author: ondrej
"""
import time, datetime
from pylab import *

files = ['/Users/ondrej/temp_log.txt','/Users/ondrej/temp_ext_log.txt']
fig, ax = plt.subplots()

for fl in files:
    f=open(fl)
    txt = f.read().split('\n')[1:-1]
    
    #x = zeros(len(txt))
    xx = list()
    y = zeros(len(txt))
    
    i=0
    for l in txt:
        y[i] = float(l.split('t=')[1])
        #x[i] = time.mktime(datetime.datetime.strptime(l.split('.')[0],"%Y-%m-%d %H:%M:%S").timetuple()) #date = datetime.datetime.fromtimestamp(ts)
        xx.append(datetime.datetime.strptime(l.split('.')[0],"%Y-%m-%d %H:%M:%S")+datetime.timedelta(hours=1))
        i+=1
        
    dates = date2num(xx)
    if fl == files[0]:    
    	ax.plot_date(dates, y,'-r')
    else:
	ax2 = ax.twinx()
	ax2.plot_date(dates, y,'-b')

ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(arange(0, 25, 2)))
ax.xaxis.set_major_formatter(DateFormatter("%a %Y-%m-%d"))
ax.xaxis.set_minor_formatter(DateFormatter('%H:%M'))
ax.xaxis.set_tick_params(which='major', pad=15)

#ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()
ax.grid(True)
ax.xaxis.grid('on',which='major')
ax.set_ylabel('temperature inside')
ax2.set_ylabel('temperature outside')
tight_layout()
show()
