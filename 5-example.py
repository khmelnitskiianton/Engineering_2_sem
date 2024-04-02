import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN, )

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

try:
    while(True):
            for x in range(256):
                signal = num2dac(x)
                volt = float(x)/256*3.3
                time.sleep(0.01)
                compVal = GPIO.input(comp)
                if compVal == 1:
                    print("ADC: val = {:^3} -> {}, input volt = {:.2f}".format(x, signal, volt))
                    break
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print("END")