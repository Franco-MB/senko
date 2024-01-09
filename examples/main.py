from machine import Pin
import time
import senko

OTA = senko.Senko(user="Franco-MB", repo="senko", working_dir="examples", files=["main.py"])

led = Pin(2, Pin.OUT)

while(True):

  led.on()
  print('Led OFF')
  time.sleep_ms(5000)

  led.off()
  print('Led ON')
  time.sleep_ms(5000)
  '''
  # Verifique se a versão mais recente está disponível
  if OTA.fetch():
    print("Nova versão disponível")
    machine.reset()
  '''
