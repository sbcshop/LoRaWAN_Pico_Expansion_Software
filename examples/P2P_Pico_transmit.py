''' P2P Transmit Demo code '''

#import required library module
from machine import UART,SPI,Pin
import st7789py as st7789
import time
from time import sleep
import vga1_bold_16x32 as font

# UART communication between RP2040 and RAK3172
uart = UART(0,baudrate = 115200,tx = Pin(0),rx = Pin(1))

def module_reset():
    lwanRST = Pin(12, Pin.OUT)
    lwanRST.on() 
    sleep(0.1)  
    lwanRST.off()
    sleep(0.1)  
    lwanRST.on()
    print("Module Reset Done!")

module_reset()

# Define buttons as INPUT, due to internal circuitry of Pico uncomment suitable choice
# for Pico 2 
button1 = Pin(14,Pin.IN)
button2 = Pin(15,Pin.IN)

# for Pico or Pico W
#button1 = Pin(14,Pin.IN,Pin.PULL_UP)
#button2 = Pin(15,Pin.IN,Pin.PULL_UP)

def displayValue(text, x = 10, y = 20):
    tft.text(font,text, x, y, st7789.YELLOW)# print on tft screen
    tft.rect(0, 0, 240, 135, st7789.CYAN) # param (x, y, rectangle_length, rectangle_breadth, color)
    
def send_command(command):  
    uart.write(command+'\r\n')
    time.sleep(0.1)
    response = uart.readline()
    #print(response)
    return response


def p2p_setup():
    # command sequence require to put RAK3172 node module in P2P Receive
    res = send_command('AT')  # Simple Module response test command
    #print(res)
    
    # NWM = 0 - P2P mode, 1 - LoRaWAN Mode
    res = send_command('AT+NWM=0')
    #print(res)
    
    # Stop if any Previous receive command execute to avoid busy message
    res = send_command('AT+PRECV=0')
    #print(res)
    
    # To enable or disable P2P encryption, 0 - for disable and 1 - for enable
    res = send_command('AT+ENCRY=0')
    #print(res)
    
    #Set P2P Parameters settings, required only once
    
    res = send_command('AT+P2P=903000000:7:0:0:14:5')
    print(res)
    
    res = send_command('AT+P2P=?')  # to confirm if setting done
    print(res)
    

def module_response_check():
    while uart.any():
        response = uart.readline()
        try:
            # Convert bytes to string if needed
            if isinstance(response, bytes):
                response = response.decode('utf-8', 'ignore')
                print(f"Module Response : {response}")
                if "+EVT:TXP2P" in str(response):
                    displayValue("Transmit OK", 20, 90)
                    print("Transmit Success")
                    sleep(1)
                    
        except Exception as e:
            print("Parsing error:", e)


    
p2p_setup()		# Command sequence to setup for P2P transmit mode

# Initialize SPI interface for the onboard display
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))

# Initialize the ST7789 TFT display
tft = st7789.ST7789(
    spi,135,240,
    cs=Pin(9, Pin.OUT),
    dc=Pin(8, Pin.OUT),
    backlight=Pin(13, Pin.OUT),
    rotation=1
    )

tft.init
tft.fill(0)
displayValue("P2P Tx Demo", 40, 40)
sleep(2)

tft.fill(0)
displayValue("Click Buttons", 10, 30)
sleep(1)

last_time = time.ticks_ms()  # get current time in ms

while 1:
    if button1.value()==0:
        tft.fill(0)
        displayValue("BT1 Pressed!", 20, 30)
        print("BT1 Pressed!")
        send_command('AT+PSEND=01')  # send payload data as byte 
    
    if button2.value()==0:
        tft.fill(0)
        displayValue("BT2 Pressed!", 20, 30)
        print("BT2 Pressed!")
        send_command('AT+PSEND=02')	# send payload data as byte 
    
    module_response_check()
    
    if time.ticks_diff(time.ticks_ms(), last_time) >= 5000:
        tft.fill(0)
        displayValue("Click Buttons", 10, 30)
        last_time = time.ticks_ms()  # reset timer
        
    time.sleep(0.2)
