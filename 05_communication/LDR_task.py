import RPi.GPIO as GPIO
import time
import spidev
import time

LEDPIN = 18

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)

def analog_read(channel):
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0)
        if reading < 512:
            GPIO.output(LEDPIN, GPIO.HIGH)
        else:
            GPIO.output(LEDPIN, GPIO.LOW)
        print("Reading=%d" % reading)
        time.sleep(0.5)
finally:
    spi.close()