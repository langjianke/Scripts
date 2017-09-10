import os
import sys
import time

filename = sys.argv[1]
#print 'adb shell screencap -p /sdcard/%s.png'%(filename)
os.popen('adb shell screencap -p /sdcard/%s.png'%(filename))
os.popen('adb pull /sdcard/%s.png'%(filename))
os.popen('adb shell rm /sdcard/%s.png'%(filename))
