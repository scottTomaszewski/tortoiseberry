from apscheduler.scheduler import Scheduler
import RelayChannel
import DHT11
import Weather
import pigpio
import json


class StatusPage:
    def __init__(self):
        pigpio.start()
        scheduler = Scheduler()
        self.overhead = RelayChannel.RelayChannel(11, scheduler)
        self.overhead.turn_on_daily_at('10', '0')
        self.overhead.turn_off_daily_at('22', '0')
        self.overhead.off()

        self.basking = RelayChannel.RelayChannel(13, scheduler)
        self.basking.turn_on_daily_at('12', '0')
        self.basking.turn_off_daily_at('15', '0')
        self.basking.off()

        self.top_left_dht = DHT11.DHT11_sensor(4)
        self.top_right_dht = DHT11.DHT11_sensor(14)
        self.bottom_left_dht = DHT11.DHT11_sensor(15)
        self.bottom_right_dht = DHT11.DHT11_sensor(18)
        self.weather = Weather.Weather()

    def parse(self, form):
        if 'overheadOn' in form:
            self.overhead.on()
        if 'overheadOff' in form:
            self.overhead.off()
        if 'baskingOn' in form:
            self.basking.on()
        if 'baskingOff' in form:
            self.basking.off()

    def data(self):
        data = {'uvbStatus': 'OFF' if self.overhead.status() == 1 else 'ON',
                'baskingStatus': 'OFF' if self.basking.status() == 1 else 'ON',
                'topLeftTempValue': self.top_left_dht.temperatureF(),
                'topRightTempValue': self.top_right_dht.temperatureF(),
                'bottomLeftTempValue': self.bottom_left_dht.temperatureF(),
                'bottomRightTempValue': self.bottom_right_dht.temperatureF(),
                'topLeftHumidityValue': self.top_left_dht.humidity(),
                'topRightHumidityValue': self.top_right_dht.humidity(),
                'bottomLeftHumidityValue': self.bottom_left_dht.humidity(),
                'bottomRightHumidityValue': self.bottom_right_dht.humidity(), 'weatherIcon': self.weather.icon(),
                'outsideTemp': int(self.weather.temperature()), 'outsideMinTemp': int(self.weather.temp_low()),
                'outsideMaxTemp': int(self.weather.temp_high())}

        return data

    @staticmethod
    def content():
        html = open('StatusPage.html', 'rb')
        return html.read()

    def update(self):
        return json.dumps(self.data())

    def exit(self):
        self.overhead.shutdown()
        self.basking.shutdown()
        pigpio.stop()
