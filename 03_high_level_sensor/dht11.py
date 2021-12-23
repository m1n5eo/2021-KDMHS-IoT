import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperate=%.1f*, Humidity=%.1f%%' %(t, h))
        else:
            print('Read Error')
finally:
    print('bye')