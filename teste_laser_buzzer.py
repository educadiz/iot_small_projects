# Autor: Edurdo Cadiz 
# Circuito teste ESP32
# Teste com Buzzer e sensor laser
#
# Buzzer modelo DY-012 pinos: gnd / vcc (3.3v) / signal
# Precisa informar a frequencia do som atraves do pino PWM


from machine import Pin, PWM
from time import sleep

Led_R = Pin(15,Pin.OUT)
Led_Y = Pin(4,Pin.OUT)
buzzer = Pin(16,Pin.OUT)
buzzer_pwm = PWM(buzzer)
laser = Pin(19,Pin.IN)

flag = 1

def play_buzzer(frequency):
    buzzer_pwm.freq(frequency)
    buzzer_pwm.duty(50)
    
while True:
    
    flag = laser.value()
    
    if (flag == 1):
        Led_R.on()
        Led_Y.off()
        play_buzzer(440)
        
    else:
        
        Led_R.off()
        Led_Y.on()
        buzzer_pwm.duty(0)
        
    sleep(0.30)    