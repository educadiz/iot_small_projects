#
# Este codigo implementa uma parada de emergencia quando aperta o push-button.
# Iremos monitorar uma das portas GPIO e este sera chamada de GPIO_CALLBACK
#

from machine import Pin
from time import sleep

led_onboard = Pin (2,Pin.OUT)
executando = True

def gpio_callback(pin):
    global executando
    executando = False
    
# Monitora o pino 12: 
gpio_pin = 12
gpio = Pin(gpio_pin, Pin.IN)
gpio.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = gpio_callback)

print("\nInicializando ... \n")

# Loop principal:
while executando: 
    led_onboard.off()
    sleep(.50)
    led_onboard.on()
    sleep(0.50)
    print("Executando...",end="\r")
print("\n\nParei!")
led_onboard.off()
    
    
    
    