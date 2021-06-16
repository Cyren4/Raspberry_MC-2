import time
import picamera
import datetime as dt
import os.path
from subprocess import call
import psutil

#initialisation

camera = picamera.PiCamera()
Rtime = 5
filename = dt.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
filepath = "/home/pi/Desktop/camera/"

#storage info

def freeStorage():
    path = '/'
    bytes_avail = psutil.disk_usage(path).free
    gigabytes_avail = bytes_avail / 1024 / 1024 / 1024
    return (gigabytes_avail)

#recording


camera.start_preview(fullscreen=False, window=(1000,-90,400,500))
camera.start_recording(filepath + filename + ".h264")

print("Start Recording")
while (freeStorage() > 1 and Rtime > 0):
    time.sleep(10)
    Rtime -= 10
        
camera.stop_recording()
camera.stop_preview()

#conversion

command = "MP4Box -add " + filepath + filename + ".h264 " + filepath + filename + ".mp4"
call([command], shell=True)
print("video conversion")
