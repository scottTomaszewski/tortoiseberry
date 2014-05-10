import RPi.GPIO as GPIO
from apscheduler.scheduler import Scheduler


class RelayChannel:
    def __init__(self, gpio_pin, scheduler=None):
        if str(gpio_pin).isdigit():
            if scheduler is None:
                scheduler = Scheduler()
            self.scheduler = scheduler
            self.pin = gpio_pin
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
        else:
            raise Exception('Invalid pin: ' + str(gpio_pin))

    def on(self):
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def status(self):
        return GPIO.input(self.pin)

    def turn_on_daily_at(self, hour, minute):
        self.scheduler.add_cron_job(self.on, hour=hour, minute=minute)

    def turn_off_daily_at(self, hour, minute):
        self.scheduler.add_cron_job(self.off, hour=hour, minute=minute)

    def shutdown(self):
        self.scheduler.shutdown(wait=False)

    if __name__ == "__main__":
        import time
        import RelayChannel

        toTest = RelayChannel.RelayChannel(11)
        toTest.off()
        print "status: " + str(toTest.status())
        time.sleep(2)
        toTest.on()
        print "status: " + str(toTest.status())
