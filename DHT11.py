#!/usr/bin/env python
import threading

import pigpio


class DHT11Sensor:
    """
    Orginal Source:
    http://www.raspberrypi.org/forums/viewtopic.php?p=515575#p515575

    A class to read relative humidity and temperature from the
    DHT11 sensor.  The sensor is also known as the AM2302.

    The sensor can be powered from the Pi 3V3 or the Pi 5V rail.

    Powering from the 3V3 rail is simpler and safer.  You may need
    to power from 5V if the sensor is connected via a long cable.

    For 3V3 operation connect pin 1 to 3V3 and pin 4 to ground.

    Connect pin 2 to a gpio.

    For 5V operation connect pin 1 to 5V and pin 4 to ground.

    The following pin 2 connection works for me.  Use at YOUR OWN RISK.

    5V--5K_resistor--+--10K_resistor--Ground
                     |
    DHT11 pin 2 -----+
                     |
    gpio ------------+
    """

    def __init__(self, gpio):
        """
        Instantiate with the gpio to which the DHT11 output pin is connected.
        """
        self.gpio = gpio
        self.bad_checksum = 0
        self.bad_timeout = 0
        self.accumulating = False
        self.relative_humidity = -999
        self.temp = -999
        self.tov = None
        self.tick = 0

        # reset in trigger
        self.bit = -3  # header bits
        self.hum_high_byte = 0
        self.hum_low_byte = 0
        self.temp_high_byte = 0
        self.temp_low_byte = 0
        self.checksum = 0

        pigpio.set_mode(gpio, pigpio.INPUT)
        pigpio.set_pull_up_down(gpio, pigpio.PUD_UP)
        self.cb = pigpio.callback(gpio, pigpio.EITHER_EDGE, self._cb)
        self.auto_update()

    def _cb(self, gpio, level, tick):
        """
        Accumulate the 40 data bits.  Format into 5 bytes, humidity high,
        humidity low, temperature high, temperature low, checksum.
        """
        if self.accumulating:
            if level == 0:
                diff = pigpio.tickDiff(self.tick, tick)

                # edge length determines if bit is 1 or 0
                if diff >= 50:
                    val = 1
                else:
                    val = 0

                if self.bit >= 32:  # in checksum byte
                    self.checksum = (self.checksum << 1) + val
                    if self.bit >= 39:
                        # 40 bits received
                        self.accumulating = False
                        pigpio.set_watchdog(self.gpio, 0)
                        total = self.hum_high_byte + self.hum_low_byte + self.temp_high_byte + self.temp_low_byte

                        if (total & 255) == self.checksum:  # is checksum ok
                            self.relative_humidity = self.adjust_humidity()
                            self.temp = self.adjust_temperature()
                            self.tov = time.time()
                        else:
                            self.bad_checksum += 1

                elif self.bit >= 24:  # in temp low byte
                    self.temp_low_byte = (self.temp_low_byte << 1) + val
                elif self.bit >= 16:  # in temp high byte
                    self.temp_high_byte = (self.temp_high_byte << 1) + val
                elif self.bit >= 8:  # in humidity low byte
                    self.hum_low_byte = (self.hum_low_byte << 1) + val
                elif self.bit >= 0:  # in humidity high byte
                    self.hum_high_byte = (self.hum_high_byte << 1) + val
                else:  # header bits
                    pass
                self.bit += 1

            elif level == 1:
                self.tick = tick
                if self.bit == -3:  # correct for first reading
                    self.bit = -2

            else:  # level == pigpio.TIMEOUT:
                # time out if less than 40 bits received
                self.accumulating = False
                pigpio.set_watchdog(self.gpio, 0)
                self.bad_timeout += 1

        else:  # perhaps a repeated watchdog
            if level == pigpio.TIMEOUT:
                pigpio.set_watchdog(self.gpio, 0)

    def temperature(self):
        """Return current temperature."""
        return self.temp

    def temperature_f(self):
        return int(float(9.0 / 5.0 * self.temperature() + 32))

    def humidity(self):
        """Return current relative humidity."""
        return self.relative_humidity

    def staleness(self):
        """Return time since measurement made."""
        if self.tov is not None:
            return time.time() - self.tov
        else:
            return -999

    def bad_checksum(self):
        """Return count of messages received with bad checksums."""
        return self.bad_checksum

    def timed_out(self):
        """Return count of messages which have timed out."""
        return self.bad_timeout

    def trigger(self):
        """Trigger a new relative humidity and temperature reading."""
        pigpio.write(self.gpio, 1)
        time.sleep(0.009)
        self.bit = -3  # header bits
        self.hum_high_byte = 0
        self.hum_low_byte = 0
        self.temp_high_byte = 0
        self.temp_low_byte = 0
        self.checksum = 0
        self.accumulating = True
        pigpio.write(self.gpio, 0)
        time.sleep(0.017)
        pigpio.set_mode(self.gpio, pigpio.INPUT)
        pigpio.set_watchdog(self.gpio, 50)

    def cancel(self):
        """Cancel the DHT11 sensor."""
        self.cb.cancel()

    def adjust_temperature(self):
        return self.temp_high_byte

    def adjust_humidity(self):
        return self.hum_high_byte

    def auto_update(self):
        self.trigger()
        threading.Timer(5, self.auto_update).start()


if __name__ == "__main__":
    import time
    import pigpio
    import DHT11

    pigpio.start()
    s = DHT11.DHT11Sensor(4)
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
