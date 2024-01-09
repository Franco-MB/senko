from machine import Pin
import time
import senko

OTA = senko.Senko(user="Franco-MB", repo="senko", working_dir="examples", files=["main.py"])

# Verifique se a versão mais recente está disponível
def version():
  global OTA
  if OTA.fetch():
    print("Nova versão disponível")
    machine.reset()


led = Pin(2, Pin.OUT)

while(True):

  led.on()
  print('Led OFF')
  time.sleep_ms(100)

  led.off()
  print('Led ON')
  time.sleep_ms(100)

  version()

