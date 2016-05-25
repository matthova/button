import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def printFunction(channel):
  print("Button 1 pressed!")
  print("Note how the bouncetime affects the button press")
  r = requests.post('http://127.0.0.1:1337')
  
GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)

while True:
  pass

GPIO.cleanup()
