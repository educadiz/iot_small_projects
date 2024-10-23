#   Autor: Eduardo Cadiz
#   Codigo para testes com servo motor E_Sky mod.: EK2 - 0508
#

from machine import Pin, PWM
from time import sleep

Rled = Pin (2,Pin.OUT)  # LED Vermelho (RED)
Bled = Pin (16,Pin.OUT) # LED Azul (BLUE)
angle = 0

# controles do servo motor: 
pin_pwm = Pin(18,Pin.OUT)
servo_pwm = PWM(pin_pwm) 
servo_pwm.freq(50)  

def move_servo(angle):
    duty = (angle / 180) * 102 + 26
    servo_pwm.duty(int(duty))

# Funcoes atribuidas aos pinos / botoes:
def gpio12_callback(Pin):
    global angle
    angle += 45
    Rled.on()
    sleep(0.25)   
    Rled.off()
    move_servo(angle)

def gpio14_callback(pin): 
    global angle
    angle -= 45
    Bled.on()
    sleep(0.25)
    Bled.off()
    move_servo(angle)
    
Rbutton = 12
gpio12 = Pin(Rbutton, Pin.IN)
gpio12.irq(trigger = Pin.IRQ_FALLING, handler = gpio12_callback)
    
Bbutton = 14
gpio14 = Pin(Bbutton, Pin.IN)
gpio14.irq(trigger = Pin.IRQ_FALLING, handler = gpio14_callback)

# Inicializa
print("\nInicializando ...")
Rled.off()
Bled.off()
move_servo(angle)

# Loop principal:
while True:
    print("Posicionando ..",end="\r")
    sleep(1)



    
    
    