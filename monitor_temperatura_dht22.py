#
#   Author: Eduardo Cadiz
#   Dispositivo: ESP32 - WROOM - 32D
#   Project: DHT22 Temperature Verification and SMTP Email Notification
#   Rev. Date: Apr. 28 2024

from machine import Pin
import umail
import network
import dht
import ntptime
import utime
import uos

def email_notification(temp_sensor,hum_sensor,log_time):
    # Email details
    sender_email = 'example@gmail.com'              # here you use the sender email ( device )
    sender_name = 'Temperature Monitor'             # here you use the sender name
    sender_app_password = '1234 abcd 4321 dcba'     # here you use the sender password (device)
    recipient_email ='eduardo.cadiz.ndb@gmail.com'  # here you use the recipient mail
    email_subject ='IoT Serial Number 0001 - Abnormal Operation Alert'
    email_content_line1 ='IoT Temperature ' + str(temp_sensor) +'C \n'
    email_content_line2 ='IoT Humidity ' + str(hum_sensor) +'% \n'
    email_content_line3 ='IoT Reading Local Time ' + log_time
   # Send the email
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)  # Gmail's SSL port
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    smtp.write(email_content_line1)
    smtp.write(email_content_line2)
    smtp.write(email_content_line3)
    smtp.send()
    smtp.quit()     
    return ("Email was sent succesfull. \n")

def connect_wifi(ssid, password,connected):
    #Connect to WIFI Network (Data Network)
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)  
    if connected:
        station.disconnect()
        print("Data Network Disconnected. \n")
        return (False)       
    while station.isconnected() == False:
        pass
    print("Data Connection Successfull. \n") 
    print(station.ifconfig())
    return (True)
    
def local_time_set():
    #Setting UTC time
    ntptime.settime()
    return utime.localtime()

def write_log_file(log_file_data):
    #Write Log File
    log_file = "tempmonitor_log.txt"
    with open(log_file,'a') as log:
        log.write(log_file_data +'\n')

def file_size(log_file):
    #Check Log File Size
    return uos.stat(log_file)[6]
    

print("Initializing IoT \n")

IoT_Serial_Number = "001"       # IoT Identification
sensor =  dht.DHT22(Pin(13))    # Temperature Sensor Initializing
temp_reference = 30.0           # Reference Temperature Trigger
interval = 45                   # Sensor Reading Interval Time (in seconds)
alarm = False                   # Alarm
cicle = 0                       # Sensor reading cycle
avc = 5                         # Abnormality Cycles (Abnormal Verification Cicle)
connected = False               # Set Data Network Off
ssid = 'GeoJetson'              # Network Wifi SSID
password = 'Jetson@2260'        #'Network WiFi password

connected = connect_wifi(ssid, password,connected)
current_time = local_time_set()
current_time = ("%d-%02d-%02d %02d:%02d:%02d" % current_time[:6])
connected = connect_wifi(ssid, password,connected)

while True:
    try:
        utime.sleep(interval)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        Rled = Pin(25, Pin.OUT)
        Gled = Pin(26, Pin.OUT)   
    except OSError as e:
        print("Sensor failure. \n")
        
    if (temp >= temp_reference):
        alarm = True
        Rled.on()     
        Gled.off()
        cicle +=1
        if (cicle >= avc):
            print("\n")
            connected = connect_wifi(ssid, password,connected)
            current_time = local_time_set()
            current_time = ("%d-%02d-%02d %02d:%02d:%02d" % current_time[:6])
            print ("Time Log.: " + current_time + "\n")
            print(email_notification (temp,hum,current_time))
            connected = connect_wifi(ssid, password,connected)           
            cicle = 0 
    else:
        Rled.off()
        Gled.on() 
        alarm = False
        cicle = 0  
    if (temp > 0):
        print(f"Temp.: {temp}C | Humidity: {hum}%",end="\r")
    else:
        print(f"Temp.: -{temp}C | Humidity: {hum}%",end="\r")
        
    logFileData = "IoT S/N:" + IoT_Serial_Number + " Time(UTC):" + current_time + " Temp.:" + str(temp) + " Hum.:" + str(hum) + "\n ----"
    if file_size("tempmonitor_log.txt") >= 100000:  
        with open("tempmonitor_log.txt", 'w') as log:
            log.write("")  
    write_log_file(logFileData)    
    
      
    
        