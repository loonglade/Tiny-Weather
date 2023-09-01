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
The files found in the folder "<a href="https://github.com/loonglade/Weather/tree/main/mpython">mpython</a>" need to be uploaded onto the microcontroller. Make sure any other files are removed as well; especially "boot.py". I use <a href="https://thonny.org/">Thonny</a> as it is very easy to use.
