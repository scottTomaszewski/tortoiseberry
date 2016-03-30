#!/usr/bin/env python
import time
import pigpio
import DHT11

class DHT22Sensor(DHT11.DHT11Sensor):
    def adjust_temperature(self):
        if self.temp_high_byte & 128:  # negative temperature
            multiplier = -0.1
            self.temp_high_byte = self.temp_high_byte & 127
        else:
            multiplier = 0.1
        return ((self.temp_high_byte << 8) + self.temp_low_byte) * multiplier

    def adjust_humidity(self):
        return ((self.hum_high_byte << 8) + self.hum_low_byte) * 0.1


if __name__ == "__main__":
    import time
    import pigpio
    import DHT22

    pigpio.start()
    s = DHT22.DHT22Sensor(14)
    r = 0

    while True:
        r += 1
        s.trigger()
        time.sleep(0.2)
        print("{} RH={}% T={}C staleness={:3.2f}s bad CS={} timed out={}"
              .format(r, s.humidity(), s.temperature(), s.staleness(),
                      s.bad_checksum(), s.timed_out()))
        time.sleep(1.75)
    s.cancel()
    pigpio.stop()
