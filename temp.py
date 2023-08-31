import threading, rumps, requests, time

class TemperatureApp(rumps.App):
    def __init__(self):
        super(TemperatureApp, self).__init__("Fetching temperature...", icon="weather.png")
        self.temperature = None
        threading.Timer(0, self.fetch_temperature).start()

    @rumps.timer(5)
    def update_temperature(self, _):
        if self.temperature is not None:
            self.title = f"{self.temperature}°"

    def fetch_temperature(self):
        try:
            response = requests.get('http://192.168.1.103:8000/') # Change to whatever IP:Port you've set your board to
            temperature = response.content.decode().split('Temperature: ')[1].split(' °')[0]
            self.temperature = temperature
        except Exception as e:
            print(f"Error fetching temperature: {e}")
            # Sleep for 5 seconds before retrying
            time.sleep(5)
        # Schedule the next fetch in 60 seconds
        threading.Timer(5, self.fetch_temperature).start()


if __name__ == '__main__':
    TemperatureApp().run()
