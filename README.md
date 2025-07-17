# Consola BLE UART Web

Este repositorio contiene el código para una aplicación web de consola serie que se comunica a través de Bluetooth Low Energy (BLE) utilizando el servicio Nordic UART. También incluye un script de ejemplo en CircuitPython para la placa [CRCibernetica Ideaboard](https://www.crcibernetica.com/ideaboard/).

## Descripción

El proyecto consiste en dos partes principales:

1.  **`index.html`**: Una aplicación web de una sola página que funciona como una terminal o consola. Permite buscar, conectar y comunicarse con dispositivos BLE que exponen el servicio UART. La interfaz está diseñada para ser responsiva y funcionar tanto en computadoras de escritorio como en dispositivos móviles a través de navegadores compatibles con Web Bluetooth (como Google Chrome).
2.  **`consola.py`**: Un script de CircuitPython diseñado para la placa Ideaboard. Este script configura la placa como un periférico BLE, anuncia el servicio UART y permite el intercambio de texto bidireccional con un cliente conectado, como la aplicación web proporcionada.

## Requisitos

### Hardware

* Una placa de desarrollo compatible con CircuitPython y BLE, como la **CRCibernetica Ideaboard**.
* Una computadora o dispositivo móvil con Bluetooth.

## Instrucciones de Uso

### 1. Configurar la Placa (Ideaboard)

1.  **Instala CircuitPython con BLE**: Usa este [instalador](https://crcibernetica.github.io/ideaboard-experimental/). 
1.  **Carga el Código**: Copia el archivo `consola.py` y ejecutar el programa.

### 2. Usar la Aplicación Web

1.  **Navega al Web App**: [Consola BLE UART](https://crcibernetica.github.io/consola/)
2.  **Habilita Bluetooth**: Asegúrate de que el Bluetooth de tu computadora o dispositivo móvil esté encendido.
3.  **Conectar**: Haz clic en el botón **"Conectar"**. Se abrirá una ventana del navegador que mostrará los dispositivos BLE cercanos.
4.  **Selecciona el Dispositivo**: Busca y selecciona "IdeaBoard_BLE" de la lista y haz clic en "Emparejar".
5.  **Comunica**: Una vez conectado, el indicador de estado cambiará a verde ("Conectado"). Ahora puedes:
    * Escribir mensajes en el campo de entrada y presionar **"Enviar"** para mandarlos a la placa.
    * Ver los mensajes enviados desde la placa en la ventana de la terminal. El script `consola.py` está programado para enviar la palabra "prueba" cada segundo.