import os
import time

while(1):
	ret = os.system("ping -c 1 -w2 192.168.0.2")
	
	if ret == 0:
		_os_ready = True;
	else:
		_os_ready = False;
	
	print _os_ready;

	time.sleep(2);