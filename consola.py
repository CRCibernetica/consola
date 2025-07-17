from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

import time
import board
from ideaboard import IdeaBoard

# Configurar el hardware de la radio BLE
ble = BLERadio()

# Por defecto, tu dispositivo tendrá un nombre como CIRCUITPYxxxx; hagámoslo más amigable
ble.name = "IdeaBoard_BLE"

# Configurar el servicio UART. Este puerto serie virtual te permite enviar texto a través de BLE.
uart = UARTService()

# Configurar la publicidad (advertising), para que tu teléfono o PC sepa que el servicio UART está disponible en tu dispositivo
advertisement = ProvideServicesAdvertisement(uart)

while True:
  print("Anunciando servicios BLE")
  # Empezar a anunciar
  ble.start_advertising(advertisement)
  # Continuar hasta que tengamos una conexión
  while not ble.connected:
    pass
    
  # Si llegamos aquí, tenemos una conexión. ¡Dejar de anunciar!
  ble.stop_advertising()
  print("BLE conectado")
  
  last = 0
  # Hacer algo de trabajo mientras estemos conectados
  while ble.connected:
    # Intentar leer algo de texto desde el UART, ej. lo que se escribe en la aplicación
    raw_bytes = uart.readline()
    if raw_bytes:
      text = raw_bytes.decode("utf-8")
      print(f"Recibido: {text}")
    
    # Mandar texto periódicamente (como ejemplo)
    now = time.monotonic()
    if now - last > 1:
        texto = "prueba"
        uart.write(texto.encode("utf-8"))
        last = now
  
  # Ya no tenemos conexión, así que volveremos al inicio del bucle
  # y empezaremos a anunciar de nuevo
  print("BLE desconectado")