import socket
import string
import time
#import vlc
import fcntl
import struct
from subprocess import call



def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

hostname=socket.gethostname()
try:
	IP=get_ip_address('wlan0')
except IOError:
	IP="127.0.0.1"

#IP=socket.gethostbyname(hostname)
if len(IP) == 0:
	IP="127.0.0.1"

nums=IP.split(".")
#mixer.init()
for num in nums:
    digits=map(int,str(num))
    for digit in digits:
        #play sound
        print(digit) 
	call(["mocp","-l", str(digit)+".mp3"])
	time.sleep(0.5) 
	#player= vlc.MediaPlayer(str(digit)+".mp3")
	#player.play() 
        #player.stop()
    call(["mocp","-l", "dot.mp3"]) 	         
    
        
