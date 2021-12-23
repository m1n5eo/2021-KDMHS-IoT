import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=RESET_PIN)

oled.fill(0)
oled.show()

image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

draw.text((0, 0), "1601", font=font, fill=255)
draw.text((0, 30), "Kim Min Seo", font=font2, fill=255)
draw.text((34, 46), "Fun IOT Class!!", font=font2, fill=255)

oled.image(image)
oled.show()