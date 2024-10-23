#   Author: Eduardo Cadiz
#   Device: ESP32 - WROOM - 32D
#   This code implements an emergency stop when you press the button.
#   We will monitor one of the GPIO ports and this one will be called GPIO_CALLBACK
#

from machine import Pin
from time import sleep

Rled = Pin (2,Pin.OUT)
Bled = Pin (16, Pin OUT)

def gpio12_callback(pin):
    print("Botao Vermelho.")
    Rled.on()
    sleep(2)
    Rled.off()

def gpio14_callback(pin):
    print("Botao Azul.")
    Bled.on()
    sleep(2)
    Bled.off()
    
# Monitora o pino 12: 
Rbutton = 12
gpio12 = Pin(Rbutton, Pin.IN)
gpio12.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = gpio12_callback)

Bbutton = 14
gpio14 = Pin(Bbutton, Pin.IN)
gpio14.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = gpio14_callback)


print("\nInicializando ... \n")

# Loop principal:
while True: 
       print("Executando...",end="\r")



    
    
    