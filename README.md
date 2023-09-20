# Tiny Weather <img src="https://github.com/loonglade/Weather/blob/main/images/temp.png" height="30px" width="100px">
 A tiny weather station using a BME280 sensor.

## Hardware
- Any microcontroller that has I2C pins (Recommended: RPI Pico or ESP32)
- USB-to-TTL adapter
- BME280 sensor
- USB power adapter

<table border="0">
  <td style="border: none;">
   <img src="https://github.com/loonglade/Weather/blob/main/images/IMG_0226.PNG" height="300px" width="550px">
  </td>
  <td style="border: none;">
   <img src="https://github.com/loonglade/Weather/blob/main/images/sensor_web.png">
  </td>
</table>

## Software
### Microcontroller
The micropython files found in the folder "<a href="https://github.com/loonglade/Weather/tree/main/mpython">mpython</a>" need to be uploaded onto the microcontroller. Make sure any other files are removed as well; especially "boot.py". I use <a href="https://thonny.org/">Thonny</a> as it is very easy to use. You need to modify <a href="https://github.com/loonglade/Weather/blob/main/mpython/main.py">main.py</a> to reflect your setup's WiFi credentials and Microcontroller's IP/Port as well as <a href="https://github.com/loonglade/Weather/blob/main/temp.py">temp.py</a> in the main directory for the IP/Port as well.
### Requirements
Open terminal > cd path/to/folder >

	pip install -r requirements.txt

### Script
	
#### 1. Create weather.sh
	nano weather.sh
#### 2. Paste these lines (edit the path to reflect yours), save and exit the file
	#!/bin/bash
	python3 /path/to/your/weather.py

#### 3. Turn script into an executable
	chmod +x weather.sh

#### 4. Execute script
	nohup ./weather.sh &
