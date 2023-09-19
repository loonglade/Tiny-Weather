from machine import Pin, SoftI2C
import network, time, socket
from bme280 import BME280

SSID = "TELUS4051"
PW = "2asfminxz3"

# Initialize the BME280 sensor
try:
    i2c = SoftI2C(sda=Pin(14), scl=Pin(15))
    bme = BME280(i2c=i2c)
except Exception as e:
    print("Error initializing BME280 sensor: ", e)

# Initialize the network connection
try:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    while not sta_if.isconnected():
        sta_if.connect(SSID, PW)
        time.sleep(1)
    print('network config:', sta_if.ifconfig())
    print('Connection successful')
except Exception as e:
    print("error connecting to wifi: ", e)

# Define the function that will handle incoming client requests
def handle_request(conn):
    try:
        request = conn.recv(1024)
        print('Content = %s' % str(request))
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'
        response += '<html><body>'
        response += '<h1>BME280 Sensor Readings</h1>'
        response += "<p>Temperature: {} °C</p>".format(bme.temperature())
        response += '<p>Pressure: {} hPa</p>'.format(bme.pressure())
        response += '<p>Humidity: {} %</p>'.format(bme.humidity())
        response += '</body></html>'
        conn.send(response)
        conn.close()
    except Exception as e:
        print("Error handling request: ", e)

# Create a socket and bind it to port 80 (the default HTTP port)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('192.168.1.103', 8000))
    s.listen(5)

    print('Web server running on 192.168.1.103:8000')

    # Listen for incoming client requests and handle them with the handle_request function
    while True:
        conn, addr = s.accept()
        handle_request(conn)
        
except KeyboardInterrupt:
    print("Shutting down the server...")
    s.close()
except Exception as e:
    print("Error starting server: ", e)
