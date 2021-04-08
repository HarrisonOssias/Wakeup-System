import RPI.GPIO as GPIO
import time

pump = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(pump, GPIO.OUT)

def pumping(pin):
    GPIO.output(pin, GPIO.HIGH)
    print('on')
    time.sleep(2)
    GPIO.output(pin, GPIO.LOW)
    print('off')


if __name__ == '__main__':
    pumping(pump)
    GPIO.cleanup()
