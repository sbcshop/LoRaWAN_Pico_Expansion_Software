# Demo Code for Onboard Display Testing with Buzzer

from machine import Pin, UART, SPI
import st7789py as st7789
import vga1_bold_16x32 as font  # Large bold font
import vga1_8x16 as font1       # Smaller font
from time import sleep

# Initialize SPI interface for the onboard display
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))

# Initialize the ST7789 TFT display
tft = st7789.ST7789(
    spi, 135, 240,
    cs=Pin(9, Pin.OUT),
    dc=Pin(8, Pin.OUT),
    backlight=Pin(13, Pin.OUT),
    rotation=1
)

# Define buttons as INPUT, due to internal circuitry of Pico uncomment suitable choice
# for Pico 2 
button1 = Pin(14,Pin.IN)
button2 = Pin(15,Pin.IN)

# for Pico or Pico W
#button1 = Pin(14,Pin.IN,Pin.PULL_UP)
#button2 = Pin(15,Pin.IN,Pin.PULL_UP)

# Define buzzer on GP21
buzzer = Pin(21, Pin.OUT)

def draw_box():
    """Draws a red border around the screen."""
    tft.fill(0)  # Clear screen with black background
    tft.fill_rect(0, 0, 5, 132, st7789.RED)      # Left border
    tft.fill_rect(235, 0, 5, 132, st7789.RED)    # Right border
    tft.fill_rect(0, 0, 235, 5, st7789.RED)      # Top border
    tft.fill_rect(0, 130, 240, 5, st7789.RED)    # Bottom border

def display_text(msg):
    """Display a message briefly and buzz."""
    buzzer.on()
    tft.fill(0)
    tft.text(font, msg, 30, 20, st7789.YELLOW)
    sleep(0.2)
    buzzer.off()
    sleep(0.3)
    tft.text(font, msg, 30, 20, st7789.BLACK)

# Initialize display
tft.init
tft.fill(0)

# Display initial message
tft.text(font1, "Hello !", 30, 30)
sleep(1)

draw_box()
tft.text(font, "LoRaWAN", 30, 20, st7789.YELLOW)
tft.text(font, "for ", 80, 60)
tft.text(font, "Pico", 100, 90, st7789.GREEN)
sleep(1)

tft.fill(0)
tft.text(font1, "Press Any Buttons", 30, 20, st7789.YELLOW)

print("Press Any Buttons")

while True:
    print("Button Value: ", button1.value(), button2.value())

    if button2.value() == 0:  # When button pressed
        display_text("BT2 Pressed!")
        print("BT2 Pressed!")
        sleep(0.2)

    elif button1.value() == 0:  # When button pressed
        display_text("BT1 Pressed!")
        print("BT1 Pressed!")
        sleep(0.2)

    sleep(0.1)
