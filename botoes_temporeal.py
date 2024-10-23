#   Author: Eduardo Cadiz
#   Dispositivo: ESP32 - WROOM - 32D
#   This code monitors the activities on 2 pins by pressing 2 buttons.
#   The monitoring is in the background. It will increment and decrement values ​​on an X axis
#   as the buttons are pressed.
#

from machine import Pin
from time import sleep

Rled = Pin (2,Pin.OUT)  # LED Vermelho (RED)
Bled = Pin (16,Pin.OUT) # LED Azul (BLUE)
eixo_x = 0.0

# Funcoes atribuidas aos pinos / botoes:
def gpio12_callback(pin): # Negativo
    global eixo_x
    Rled.on()
    sleep(0.30)   
    Rled.off()
    eixo_x -= 0.5
    print("\t\tEixo X:",eixo_x,end="\r")   
     
def gpio14_callback(pin): # Positivo
    global eixo_x
    Bled.on()
    sleep(0.30)
    Bled.off()
    eixo_x += 0.5 
    print("\t\tEixo X:",eixo_x,end="\r")
    
# Monitors the buttons connected to pins 12 and 14:
# IRQ_FALLING > Monitors when pressed (PUSH)
# IRQ_RISING > Monitors when rising (PULL) after pressing
 
Rbutton = 12
gpio12 = Pin(Rbutton, Pin.IN)
#gpio12.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = gpio12_callback)
gpio12.irq(trigger = Pin.IRQ_FALLING, handler = gpio12_callback)
    
Bbutton = 14
gpio14 = Pin(Bbutton, Pin.IN)
#gpio14.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = gpio14_callback)
gpio14.irq(trigger = Pin.IRQ_FALLING, handler = gpio14_callback)

# Inicializa
print("\nInicializando ...")
Rled.off()
Bled.off()
print("Pos. Inicial Eixo X:",eixo_x,"\n")
# Loop principal:
while True:
    print("Posicionando:",end="\r")
    sleep(1)



    
    
    