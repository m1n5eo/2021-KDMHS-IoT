from lcd import drivers
import datetime
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 18
display = drivers.Lcd()

try:
    while True:
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string(now.strftime("%x%X"), 1)
        display.lcd_display_string(('%.1f\'C, %.1f%%' %(t, h)), 2)
finally:
    display.lcd_clear()