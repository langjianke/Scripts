import io
import time
import subprocess
import sys

from myColor import setColor as sc


cmd = 'adb logcat -v time'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

#color mapping, define the key word and the color you want to use
#currently only the keyword here will be printed, otherwise not print out
#this can be use to filter the wantted metrics

colorMap = {
'uiClick':'dark_yellow',
'uiPageView':'dark_yellow',
'clientInfo':'yellow',
'clickedAddContent':'yellow',
'streamingInitiated':'green',
'sportStreamingInitiated':'green',
'sportStreamingInitiationFailed':'red',
'streamingTerminated':'dark_red',
'sportStreamingTerminated':'dark_red',
'streamingRequiredReBuffering':'gray',
'sportStreamingRequiredRebuffering':'gray',
'localPlaybackTerminated':'dark_purple',
'trackStreamed':'pink',
'terminationReason':'dark_yellow',
'downloadInitiated':'dark_green',
'trackDownloaded':'blue',
'downloadTerminated':'dark_red',
'trackPlayedLocally':'dark_green',
'clickedOnStoreLink':'dark_green',
##below are the atrributs
'initialPlaybackDelayMilliseconds':'dark_yellow',
'contentSubscriptionMode':'dark_yellow',
'transferSpeedBPS':'dark_yellow',
'selectionSourceType':'dark_yellow',
'streamOrDRMTech':'dark_yellow',
'downloadSource':'dark_yellow',
'asin':'dark_yellow',
'linkType':'dark_yellow',
}

keyWords = colorMap.keys()
MTS_Event = 'AmznMusic_MTSEventTransformer'

while(True):
      retcode = proc.poll() #returns None while subprocess is running
      line = proc.stdout.readline()
      if (MTS_Event in line):
          flag = False #when there is keyWord, print the line
          for word in keyWords:
              if (word in line):
                  flag = True
                  line = line.replace(word, sc(colorMap[word], word))
          if flag:
              print line
      if(retcode is not None):
          break
