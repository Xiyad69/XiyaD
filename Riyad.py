#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdfileg-open https://facebook.com/Xiyad.4040.XD/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf sex.so')
except:
    pass
os.system('rm -rf sex.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('sex.so'):
        os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/sex.cpython-311.so?raw=true -o sex.so') 
        import sex  
    else:
        import sex
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ') 
