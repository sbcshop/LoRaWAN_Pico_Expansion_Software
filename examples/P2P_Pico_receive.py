# P2P Receive Demo code 
'''
    In P2P device default is in Tx mode to save Power,
    P2P LoRa RX configurable duration value is from 1 to 65533 ms.
    
    For example,
    You can set 30000 ms and so the device will listen and wait for LoRa P2P Packets for 30 seconds.
    Automatically disable RX mode and switch to TX mode after the timeout.
    If the device did not receive any packets within the time period, then the callback after timeout is +EVT:RXP2P RECEIVE TIMEOUT.
    
    Specific functionality for =>
    65535 -> listen to P2P LoRa packets without a timeout, but stops when P2P LoRa packet is received and automatically switch to TX mode again.
    65534 -> continuous listen to P2P LoRa packets without any timeout and without moving to Tx mode.
    0     -> It disables LoRa P2P RX mode and switches to TX mode.
'''

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

def displayValue(text, x = 10, y = 20):
    sleep(0.5)#time delay
    tft.text(font,text, x, y, st7789.YELLOW)# print on tft screen
    tft.rect(0, 0, 240, 135, st7789.CYAN) # param (x, y, rectangle_length, rectangle_breadth, color)

def send_command(command):
    uart.write(command+'\r\n')
    sleep(1)
    response = uart.readline()
    sleep(0.1)
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
    
    #Set P2P Parameters settings, required only once
    '''
    res = send_command('AT+P2P=903000000:7:0:0:14:5')
    print(res)
    
    res = send_command('AT+P2P=?')  # to confirm if setting done
    print(res)
    '''
    

def activate_p2p_receive():
    #listen to P2P LoRa packets without a timeout, and automatically switch to Tx when Packet received
    res = send_command('AT+PRECV=65535')
    #print(res.decode('utf-8'))
    tft.fill(0)
    displayValue("P2P_Rx Mode", 20, 30)
    displayValue("Active", 60, 80)
    sleep(2)
    tft.fill(0)
    displayValue("Waiting..!", 20, 30)
    
def parse_received_data(response):
    try:
        # Convert bytes to string if needed
        if isinstance(response, bytes):
            response = response.decode('utf-8', 'ignore')
            print(f"Module Response : {response}")

        if "+EVT:RXP2P" in response:
            parts = response.strip().split(":")
            if len(parts) >= 4:
                data_value = parts[-1]
                print("Received Data Payload:", data_value)
                data_value = "Data: " + str(parts[-1])
                rssi_value = "RSSI: " + str(parts[2]) + " dBm"
                print(data_value)
                print(rssi_value)
                tft.fill(0)
                displayValue(data_value, 10, 30)
                displayValue(rssi_value, 10, 70)
            global rx_mode
            rx_mode = 0
            sleep(1)
            
    except Exception as e:
        print("Parsing error:", e)

p2p_setup() # setup function to run for P2P receive activation

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

rx_mode = 1
print("Waiting...!")

tft.init
tft.fill(0)
displayValue("P2P Rx Demo", 40, 40)
sleep(1)

activate_p2p_receive()

while 1:
  if uart.any():
    response = uart.readline()
    print(response)
    parse_received_data(response)
       
  if rx_mode == 0:
     activate_p2p_receive()
     rx_mode = 1
     print("Rx Mode Activated")
     print("Waiting!",end="")
     
  sleep(0.2)
  print(".", end="")


