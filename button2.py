from time import sleep
import RPi.GPIO as GPIO
import requests

input_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def handle_push():
  r = requests.post('http://127.0.0.1:1337')

last_input = None
try:
  while True:
    input = GPIO.input(input_pin)
    if input != last_input:
      if input:
        print "Button is released"
      else:
        print "Button is pushed"
        handle_push()
    last_input = input
    sleep(0.05)
except:
  GPIO.cleanup()
