import RPi.GPIO as GPIO

ext_mic_en_pin=12

GPIO.setmode(GPIO.BCM)

GPIO.setup(ext_mic_en_pin, GPIO.OUT)

GPIO.output(ext_mic_en_pin,1)
