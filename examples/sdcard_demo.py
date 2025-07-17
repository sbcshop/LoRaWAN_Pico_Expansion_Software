# Import required modules
from machine import Pin, UART, SPI
import vga1_bold_16x32 as font  # Large bold font
import vga1_8x16 as font1       # Smaller font
from time import sleep
import sdcard
import os


def sd_store(data):  # Test method for SD CARD
    spi=SPI(0,sck=Pin(18),mosi=Pin(19),miso=Pin(16)) # setting the SPI pins
    try:
        sd=sdcard.SDCard(spi,Pin(17))
        vfs = os.VfsFat(sd)
        os.mount(vfs, "/fc") # mount SD card
        print("Filesystem check")
        print(os.listdir("/fc")) # print the list of directory stored in the files of sd card
        fn = "/fc/TestFile.txt"  #create file with suitable name
        print()
        print("Single block read/write")
        
        with open(fn, "a") as f:
            n = f.write(data)  #write data to file
            print(n, "bytes written")
        
        with open(fn, "r") as f:
            result = f.read() # read data from the file
            print(len(result), "bytes read")
            print("Data written on File:")
            print(result) # Display the data read from the SD Card, which was previously written to the card as data.
        
        os.umount("/fc")
        
        
    except OSError as err:
        print(err)
        sleep(1)
     
sd_store("Hello World")

