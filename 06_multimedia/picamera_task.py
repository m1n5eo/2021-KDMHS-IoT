import picamera
import time

path = "/home/pi/src6/06_multimedia"

camera = picamera.PiCamera()

try:
    while True:
        select = int(input("photo:1, video:2, exit:9 > "))
        camera.resolution = (640, 480)
        camera.start_preview()
        now = time.strftime("%Y%m%d_%H%M%S")
        if select == 1:
            time.sleep(3)
            camera.capture('%s/%s.jpg' %(path, now))
            print("사진 촬영")
        elif select == 2:
            input('press enter to recoding..')
            camera.start_recording('%s/%s.h264' %(path, now))
            print("동영상 촬영")
            time.sleep(3)
            camera.stop_recording()
        elif select == 9:
            break
        else:
            print("incorrect command")

finally:
    camera.stop_preview()