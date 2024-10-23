import machine
import math
import time

# Pinos de conexão do NTC
pin_ntc = 34

# Função para ler a temperatura do NTC
def read_ntc_temperature(pin):
    adc = machine.ADC(pin)
    adc_value = adc.read()
    
    # Converter a leitura ADC em tensão
    voltage = adc_value * 3.3 / 4095  # 3.3V é a tensão de referência do ESP32
    
    # Calcular a resistência do NTC usando um divisor de tensão
    R2 = 10000  # Resistência do resistor fixo (em ohms)
    R1 = (3.3 * R2) / voltage - R2
    
    # Calcular a temperatura usando a equação de Steinhart-Hart
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    kelvin = 1 / (A + B * math.log(R1) + C * math.pow(math.log(R1), 3))
    celsius = kelvin - 273.15
    
    return celsius

# Loop principal
while True:
    temperature = read_ntc_temperature(pin_ntc)
    print("Temperatura: {:.2f}°C".format(temperature))
    time.sleep(1)  # Espera 1 segundo antes de ler novamente
