import picamera
import time

path = "/home/pi/src6/06_multimedia"

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()d
    time.sleep(3)
    # camera.capture('%s/photo.jpg' %path)
    camera.start_recording('%s/video.h264' %path)
    input('press enter to stop')
    camera.stop_recording()

finally:
    camera.stop_preview()