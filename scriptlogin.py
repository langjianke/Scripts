import sys
import os
import time


commonPassword = 'davidtest'
adbsh_keyevent = 'adb shell input keyevent '
adbsh_text = 'adb shell input text '

accounts = {
'us1':'xcwei+davidtest1@amazon.com'+'&'+commonPassword,
'us2':'xcwei+davidtest2@amazon.com'+'&'+commonPassword,
'uk1':'xcwei+daviduk1@amazon.com'+'&'+commonPassword,
'uk2':'xcwei+daviduk2@amazon.com'+'&'+commonPassword,
'de1':'xcwei+davidde1@amazon.com'+'&'+commonPassword,
'de2':'xcwei+davidde2@amazon.com'+'&'+commonPassword,
}

def fireTV_Login(username, password):
    os.popen(adbsh_text+username)
    time.sleep(1)
    os.popen(adbsh_keyevent+'85')
    time.sleep(2)
    os.popen(adbsh_text+password)
    time.sleep(1)
    os.popen(adbsh_keyevent+'85')
    time.sleep(15)
    os.popen(adbsh_keyevent+'66')
    time.sleep(3)

def kindle_Login(username, password):
    os.popen(adbsh_text+username)
    time.sleep(1)
    os.popen(adbsh_keyevent+'20')
    time.sleep(1)
    os.popen(adbsh_text+password)
    time.sleep(1)
    os.popen(adbsh_keyevent+'66')
    time.sleep(3)

if __name__ == "__main__":
    dev_type = sys.argv[1]
    acc = sys.argv[2]
    print '---\n'+'account log in is %s, device type is %s' %(acc, dev_type)

    if acc in accounts:
        username,password = accounts[acc].split('&')
    else:
        username,password = sys.argv[2],sys.argv[3]

    print 'username: '+username+'\n'+'password: '+password

    if dev_type == 'kindle':
        print 'kindle log in'
        kindle_Login(username, password)
    elif dev_type == 'firetv':
        print 'firetv log in'
        fireTV_Login(username, password)
    else:
        print 'do not know the device type'

    print 'done with login account %s\n---' %(sys.argv[1])
