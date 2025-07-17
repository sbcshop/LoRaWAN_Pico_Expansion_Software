# LoRaWAN_Pico_Expansion_Software

<img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/feature_banner.png"  width= "" height= "">

Powered by the Raspberry Pi Pico, our LoRaWAN Node opens the door to endless IoT possibilities. Featuring a high-performance LoRa module and a vibrant TFT display, this Node offers unparalleled connectivity and visual interaction for your projects. With support for multiple LoRaWAN bands and certifications, it's ready to revolutionize your IoT experience.
The RAK3172 LoRaWAN Node, powered by Raspberry Pi Pico, offers a versatile and powerful solution for your IoT projects. With its robust features, including LoRaWAN compliance, server platform compatibility, and support for P2P communication, it's poised to elevate your IoT experience to new heights.

This Github provides getting started instructions for LoRaWAN for Pico Expansion.


### Features:
- Powered by Pico/Pico W which has having Raspberry Pi RP2040 chip which is a 32-bit dual ARM Cortex-M0+ @133MHz 
- 264kB multi-bank high-performance SRAM with 2MB of onboard Flash Memory
- The board is equipped with a RAK3172 LoRa Module supporting LoRaWAN protocol for IoT-based applications 
- 1.14” TFT display for visual interactions with a resolution of 240x135 pixels
- Display Appearance: RGB, Colors: 65K/262K
- Having ST7789 display driver using SPI interface 
- Interface Type C for powering and standalone access to the LoRa module for configuration.
- Two programmable buttons for more control features
- Onboard Power status LED indicator
- Buzzer to add audio alerts or notifications of various events
- Micro SD card support for data logging and external storage
- Boot and Reset button for module
- Pico GPIOs are available as side headers for Additional hardware like sensors, actuators  interfacing

### Specifications:
- **Microcontroller**  : Pico/ Pico W/ Pico 2
- **LoRaWAN Module** : RAK3172 LPWAN module
- **Supply Voltage:** 5V
- **Operating Pin:** 3.3V
- **Display Size**: 1.14"
- **Display Resolution**: 135x240 pixel
- **Display Driver**: ST7789
- **Display Appearance**: RGB
- **Display Colors**: 65K/262K
- **Antenna port:** 1 port ,SMA

**RAK3172 LoRaWAN Module Specifications:**
- RAK3172 is based on STM32WLE5CCU6 chip
- Complies with Class A, B, & C of LoRaWAN 1.0.3 specifications, ensuring interoperability and compliance with industry standards.
- Module Available with Supported bands: EU433, CN470, IN865, EU868, AU915, US915, KR920, RU864, and AS923-1/2/3/4
- LoRaWAN activation by OTAA/ABP
- LoRa Point-to-Point (P2P) communication to build your own LoRa Network
- Easy-to-use AT command set via UART interface
- Long-range - around 15 km* with optimized antenna
  
## Getting Started with LoRaWAN for Pico
### Pinout 
<img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/pinout.png" width="" height=""> 

### Interfacing Overview
<img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/interfacing_details.png" width="578" height="392"> 

### Step 1: Setup and installation
  * Connect Pico/Pico2 Microcontroller board on expansion along with suitable Antenna you received.

    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/lorawan_pico_expansion.png" width="" height=""> 

  * We need **MicroPython** firmware .UF2 preinstalled with the corresponding Pico, if not, follow steps mentioned in the link [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) to do that.
  * Second we need **Thonny IDE** software for the programming and testing purpose. You can download and install from [here](https://thonny.org/).
  * Once everything ready, connect pico to laptop/PC with micro USB and then proceed for next step.

### Step 2: Testing and Running Demo 
  * Download this complete github which contains lib and example codes,

    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/git_download.png" width="389" height="323">

  * Open any demo example in Thonny IDE, also make sure file view is checked for easy operation which is useful for easy access of file from System and Pico board. Select micropython board as shown below,

    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/file_view.png" width="451" height="418">
    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/board_select.png"  width="" height="">

  * Upload [lib](https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/tree/main/examples/lib) folder to Pico board and save [example](https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/tree/main/examples) to try as **main.py**.

    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/upload_files.png"  width="" height="">

  * You can even run example for debugging through Thonny by clicking Green Play button as shown.

    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/run_example.png"  width="957" height="508">

  * To try P2P or LoRaWAN related examples make sure jumper setting is on RAK-PICO side as shown below,

    <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/jumper_sel.jpg" width="233" height="162">

  * Once everything all set so now you can try [examples](https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/tree/main/examples) related to P2P/Lorawan commmunication 

## RAK3172 Module Standalone
* You can access RAK3172 module directly. For this remove Pico from header and change jumper selection to USB-RAK side as shown below,
  
  <img src="https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Software/blob/main/images/rak3172_direct_access.jpg" width="316" height="276">

* Connect device to PC/laptop using Type C. Now you can follow steps mentioned [here](https://github.com/sbcshop/LoRaWAN_Breakout_Software) to use RAK3172 module standalone like breakout for changing configuration or [Firmware update](https://github.com/sbcshop/LoRaWAN_Breakout_Software/blob/main/documents/Firmware%20Update%20Procedure%20with%20WisToolBox.pdf).
  

## Resources
  * [Schematic](https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Hardware/blob/main/Design%20Data/SCH%20Lorawan%20for%20pico.pdf) 
  * [Hardware data](https://github.com/sbcshop/LoRaWAN_Pico_Expansion_Hardware)
  * [RAK3172 AT Command Reference ](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/)
  * [CH340 Driver Installation Guide](https://github.com/sbcshop/NFC_Module/blob/main/documents/CH340%20Driver%20installation%20steps.pdf)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
    
## Related Products  

  * [LoRaWAN RP2040 USB Dongle](https://shop.sb-components.co.uk/products/lorawan-rp2040-usb-dongle)
  
  * [LoRaWAN Breakout Board](https://shop.sb-components.co.uk/products/lorawan-breakout)

  * [LoRaWAN For ESP32](https://shop.sb-components.co.uk/products/lorawan-for-esp32)

  * [LoRaWAN HAT Node for Raspberry Pi](https://shop.sb-components.co.uk/products/lorawan-hat-for-raspberry-pi)
  
  * [LoRaWAN Gateway HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/lorawan-gateway-hat)
   

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
