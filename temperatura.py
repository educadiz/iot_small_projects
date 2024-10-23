#Autor: Eduardo Cadiz
#Projeto: Teste verificação de temperatura e umidade com sensor DHT22

from machine import Pin
from time import sleep
import dht

sensor =  dht.DHT22(Pin(13))# Objeto sensor DHT
temp_referencia = 25.5      # Temperatura de referência para comparação
intervalo = 1.0             # Intervalo de tempo de leitura do sensor

while True:
    try:
        sleep(intervalo)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        lverm = machine.Pin(25, machine.Pin.OUT)
        lverd = machine.Pin(26, machine.Pin.OUT)   
    except OSError as e:
        print("Falha de leitura do sensor!")
    if (temp >= temp_referencia):
        lverd.off()     
        lverm.on()  
    else:
        lverm.off()
        lverd.on()
    if (temp > 0):
        print("Temperatura atual: %+2.2f Celsius" %temp)
    else:
        print("Temperatura atual: %-2.2f Celsius" %temp)
    print("Humidade: %2.2f" %hum), 
    
    
      
    
        