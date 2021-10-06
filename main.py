import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)


while True:
    
    d.measure()
    print("Temperatura={} Umidade={}".format(d.temperature(), d.humidity()))
    if d.temperature() > 31 or d.humidity() > 70:
        r.value(1)
    else:
        r.value(0)
        
    time.sleep(2)
