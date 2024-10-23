# 7-segment display activation
# ESP32 - WROOM 32D
# The display used has its segments activated by low voltage level
# ELD-512GWA display
# Turn off: 1 / Turn on: 0

from machine import Pin
from time import sleep

dot = Pin(2,Pin.OUT)
a = Pin(4,Pin.OUT)
b = Pin(16,Pin.OUT)
c = Pin(17,Pin.OUT)
d = Pin(18,Pin.OUT)
e = Pin(21,Pin.OUT)
f = Pin(22,Pin.OUT)
g = Pin(5,Pin.OUT)

segments = [a,b,c,d,e,f,g,dot]

v0 = [a,b,c,d,e,f]
v1 = [b,c]
v2 = [a,b,d,e,g]
v3 = [a,b,c,d,g]
v4 = [b,c,g,f]
v5 = [a,c,d,g,f]
v6 = [a,c,d,e,g,f]
v7 = [a,b,c]
v8 = [a,b,c,d,e,f,g]
v9 = [a,b,c,g,f]

numbers = [v0,v1,v2,v3,v4,v5,v6,v7,v8,v9]

def turn_all_off():
    global segments
    for j in segments:
        j.on()
        
turn_all_off()

while True:
    turn_on=[]
    for num in range(10):
        turn_on = (numbers[num])
        for i in turn_on:
            i.off()
        sleep(1)
        turn_all_off()
    sleep(1)   
        
        
    