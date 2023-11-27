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

### Installation
	git clone https://github.com/loonglade/Tiny-Weather.git
 	cd Tiny-Weather
  	./setup.sh

#### <img src="https://www.file-extensions.org/imgs/app-icon/128/10409/bitcoin-core-icon.png" width="20" height="20"> Donations </img>
If this project is useful, consider donating. Any amount helps.
bitcoin:bc1q6nu6347k3n077sscjntk949namnulrrpshz4j4
