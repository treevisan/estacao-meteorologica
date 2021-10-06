from wifi_lib import conecta
import urequests
print("Conectando...")
station = conecta("Sapo Cururu", "Romeu2020")
if not station.isconnected():
    print("Não conectado")
else:
    print("Conectado!")
    print("Acessando o site...")
    resposta = urequests.get("https://api.thingspeak.com/update?api_key=LTDSZ98CEWW3YE8Q&field1=0")
    print("Página acessada:")
    print(resposta.text)
    station.disconnect()
    
