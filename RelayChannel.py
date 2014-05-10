import RPi.GPIO as GPIO
from apscheduler.scheduler import Scheduler


class RelayChannel:
    def __init__(self, gpioPin, scheduler=None):
        if str(gpioPin).isdigit():
            if scheduler is None:
                scheduler = Scheduler()
            self.scheduler = scheduler
            self.pin = gpioPin
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
        else:
            raise Exception('Invalid pin: ' + str(gpioPin))

    def on(self):
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def status(self):
        return GPIO.input(self.pin)

    def turnOnDailyAt(self, hour, minute):
        self.scheduler.add_cron_job(self.on, hour=hour, minute=minute)

    def turnOffDailyAt(self, hour, minute):
        self.scheduler.add_cron_job(self.off, hour=hour, minute=minute)

    def shutdown(self):
        self.scheduler.shutdown(wait=False)

    if __name__ == "__main__":
        import time
        import RelayChannel

        toTest = RelayChannel.RelayChannel(11)
        toTest.off()
        print
        "status: " + str(toTest.status())
        time.sleep(2)
        toTest.on()
        print
        "status: " + str(toTest.status())
