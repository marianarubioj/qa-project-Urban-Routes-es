# **PROYECTO URBAN ROUTES ES**

Mariana Rubio Jaramillo. Cohorte 14

## **Descripción del proyecto.**

Urban Routes es una aplicación que crea rutas y calcula la duración y precio del viaje para diferentes tipos de transporte. 
Contiene dos campos para las direcciones: "Desde" y "Hasta". Además, cuenta con tres modos ("Óptimo", "Flash" y "Personal"), así como íconos para los tipos de 
transporte (automóvil del usuario, a pie, taxi, bicicleta, scooter o compartir un automóvil). Al pedir un taxi, muestran los distintos tipos de tarifa para taxi (Laboral,
 sueño, relajante, hablador, comfort y glamuroso), donde cada uno tiene diferentes requisitos del pedido. Al pedir un taxi, es obligatorio ingresar un número de
teléfono, la cual, es la validada por un código de verificación y el método de pago puede ser en efectivo o con tarjeta bancaria. 
 
En este caso se comprobarán las funcionalidades de Urban Routes al pedir un taxi por medio de la tarifa "Comfort".

## **Tecnologías y técnicas utilizadas.**

- GitHub
- Pycharm
- Lenguaje python
- Paquete Pytest
- Paquete selenium
- from selenium.webdriver.common.by import By
- from selenium.webdriver.support.wait import WebDriverWait
- from selenium.webdriver.support import expected_conditions as EC
- from selenium.webdriver.chrome.service import Service
- from selenium.webdriver.chrome.options import Options
- from selenium import webdriver
- import json 
- import time 
- from selenium.common import WebDriverException

## **Reglas**

El localizador de cada botón y campo debe ser único. Igual que el nombre de los métodos. También hay que utilizar las esperas inteligentes de Selenium para que las pruebas tengan
tiempo de realizarse. Además, hay que tener en cuenta la conexión al git y clonar el repositorio con SSH para trabajar en el proyecto de forma local. 
Cuando ya se haya terminado de trabajar con el proyecto, se debe empujar al git por medio de comandos de commit

### **locators.py**

En este archivo está almacenada la clase LocatorsUrbanRoutesPage, la cual, contiene los localizadores para cada campo y/botón.
Llama a "from selenium.webdriver.common.by import By"
 

### **methods.py**

En este archivo está la clase MethodsUrbanRoutesPage, la cual, contiene los métodos.
Llama a import code, import data, from locators import LocatorsUrbanRoutesPage, from selenium.webdriver.common.by import By, 
from selenium.webdriver.support.wait import WebDriverWait, from selenium.webdriver.support import expected_conditions as 

### **data.py**

En este archivo estan almacenadas los cuerpos que se solicitan por medio del get y el url de urban routes.

### **main.py**

En este archivo están almacenadas las pruebas para pedir un taxi por medio de la tarifa "Comfort".
Llama a import data, from methods import MethodsUrbanRoutesPage, from selenium import webdriver , from selenium.webdriver.chrome.service import Service, 
from selenium.webdriver.chrome.options import Options, from locators import LocatorsUrbanRoutesPage

### **code.py**
En este archivo está el código que devuelve un número de confirmación de teléfono y lo devuelve como un string.

## **Pasos para realizar las pruebas pertinentes al pedir un taxi por medio de la tarifa comfort**

Es muy importante descargar los paquetes selenium y pytest. Además tener en cuenta las funciones de selenium, las cuales, están especificadas en REGLAS; de esta forma, 
se podrán usar comandos como el By, el WaitDriverWait, entre otras.

### 1. Configurar la dirección

- Hacer clic a “Desde”
- Escribir la dirección "Desde"
- Hacer clic a “Hasta”
- Escribir la dirección “Hasta”
- Hacer click al botón “Pedir un taxi”.               

### 2. Seleccionar la tarifa Comfort.

- Hacer click a “Comfort”.


### 3. Rellenar el número de teléfono.

- Hacer click al botón “Número de teléfono”.                                                                                              
- Hacer click al texto “Número de teléfono”.      
- Escribir el número “phone_number”.                
- Hacer click al botón “siguiente”.                       
	(abre la ventana emergente para introducir el código del SMS)
- Introducir el código del SMS.                            
- Hacer click al botón “confirmar”.

### 4. Agregar una tarjeta de crédito.

- Hacer click a “Método de pago”.                  
- Hacer click a “Agregar tarjeta”                      
- Hacer click al “numero de tarjeta”                 
- Escribir el numero de tarjeta “234 5678 9100’”.      
- Hacer click al código.                                      
- Escribir el código “111”.                                   
- Hacer click en la pantalla.                               
- Hacer click al botón “Agregar”-.                      
- Hacer click al botón X.                                 

### 5. Escribir un mensaje para el controlador.

- Hacer click a “Mensaje para el conductor”.   
- Escribir “Traiga un aperitivo”.              

### 6. Pedir una manta y pañuelos.

- Hacer click al botón de “Manta y pañuelos”. 

### 7. Pedir 2 helados

- Hacer click al botón “+” del texto Helado.   

### 8. Aparece el modal para buscar un taxi.

- Hacer click al botón para buscar un taxi.

### 9. Información del conductor en el modal 
 - Esperar a que aparezca la información del conductor en el modal. 


