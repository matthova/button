import RPi.GPIO as GPIO # Import GPIO library
import time

try:
    inputPin = 23
    GPIO.setmode(GPIO.BOARD)     # Use board pin numbering
    GPIO.setup(inputPin, GPIO.OUT) # Setup GPIO Pin 7 to OUT	
    
    prev_input = 0
    while True:
      #take a reading
      input = GPIO.input(inputPin)
      #if the last reading was low and this one high, print
      if ((not prev_input) and input):
        print("Button pressed")
      #update previous input
      prev_input = input
      #slight pause to debounce
      time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()               # Clean up the hardware drivers
