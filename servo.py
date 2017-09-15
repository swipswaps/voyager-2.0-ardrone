import RPi.GPIO as GPIO
from time import sleep


class Servo():

    def connect(pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        pwm=GPIO.PWM(pin, 50)
        pwm.start(0)


    def set_angle(angle):
    	duty = angle / 18 + 2
    	GPIO.output(self.pin, True)
    	pwm.ChangeDutyCycle(duty)
    	sleep(0.5)
    	GPIO.output(self.pin, False)
    	pwm.ChangeDutyCycle(0)

    def stop():
        pwm.stop()
        GPIO.cleanup()