import threading, rumps, requests, time

class TemperatureApp(rumps.App):
    def __init__(self):
        super(TemperatureApp, self).__init__("Fetching temperature...", icon="weather.png")
        self.temperature = None
        threading.Timer(0, self.fetch_temperature).start()

    @rumps.timer(5)
    def update_temperature(self, _):
        if self.temperature is not None:
            self.title = f"{self.temperature}°C"
        else:
            self.title = "Loading..."

    def fetch_temperature(self):
        while True:
            try:
                response = requests.get('http://192.168.1.103:8000/', timeout=5)
                if response.status_code == 200:
                    temperature = response.content.decode().split('Temperature: ')[1].split(' °')[0]
                    self.temperature = temperature
                    print(f"Temperature fetched: {self.temperature}°C")
                else:
                    print(f"Failed to fetch temperature. Status code: {response.status_code}")
                time.sleep(5)
            except requests.ConnectionError:
                print("Could not connect to the device. Retrying in 5 seconds.")
                self.temperature = None
                time.sleep(5)
            except Exception as e:
                print(f"An error occurred: {e}")
                self.temperature = None
                time.sleep(5)


if __name__ == '__main__':
    TemperatureApp().run()
