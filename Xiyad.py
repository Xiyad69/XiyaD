#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
#os.system('xdg-open https://chat.whatsapp.com/BbnGtyHZcmZ3F8bDnwwFlG')
os.system('xdg-open https://facebook.com/Xiyad.404.XD/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf xd.so')
        os.system('rm -rf xd32.so')
except:
    pass
os.system('rm -rf xd.so')
os.system('rm -rf xd32.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('xd.so'):
        os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/xd.cpython-311.so?raw=true -o xd.so') 
        import xd  
    else:
        import xd
elif bit == '32bit':
	if not os.path.isfile(''):
		os.system('curl -L ') 
		import xd32  
	else:
		import xd32 
    #exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    

