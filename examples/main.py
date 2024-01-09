from machine import Pin
import time

led = Pin(2, Pin.OUT)

while(True):

  led.on()
  print('Led OFF')
  time.sleep_ms(100)

  led.off()
  print('Led ON')
  time.sleep_ms(100)
