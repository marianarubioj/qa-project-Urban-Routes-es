Mariana Rubio Jaramillo. Cohorte 14

Descripción del proyecto.

Urban Grocers es una plataforma interactiva que permite al cliente comprar artículos comestibles, crear kits y solicitar un servicio de entrega. Por ende, el cliente debe registrarse para crear un nuevo usuario y asi tener su propio carrito de compra.

La plataforma tiene un menú principal para hacer pedidos, la cual, consta de varios kits que ya vienen establecidos y además, el usuario puede crear su propio kit. Dentro de estos kits, se pueden encontrar productos organizados por catalogos, precio y cantidad.

En este caso, se automatizaron las pruebas para la lista de comprobación del campo 'name' en la solicitud de un kit de productos, es decir, se deberá crear un nuevo usuario y crear un kit dentro del nuevo usuario.

Tecnologías y técnicas utilizadas.

Documentación de la API de Urban Grocers = URL + /docs/ 
GitHub
Pycharm
Lenguaje python
Librería requests
Pytest
Reglas

Configuration.py

En este archivo están almacenadas las URL y rutas de solicitud que fueron obtenidas por la documentación de API de Urban Grocers.

Data.py

En este archivo están almacenados los cuerpos de la solicitud POST.

Sender_stand_request.py

En este archivo están almanaceadas las solicitudes para crear un usuario y para crear un kit dentro del nuevo usuario.

Create_kit_name_kit_test.py

En este archivo están almacenadas las pruebas de la lista de comprobación del campo 'name'.

Pasos para ejecutar las pruebas

Creación de un nuevo usuario

Descargar el paquete requests.
Importar configuration, data y requests.
Crear un nuevo usuario con el método POST utilizando las rutas URL_SERVICE y CREATE_USER_PATH y el body del archivo data.py
Guardar el authToken.
Resultado Esta solicitud generará un nuevo usuario y un token de autenticación 'authToken'.

Creación de un kit dentro del usuario nuevo

Realizar todos los pasos de 'Creación de un nuevo usuario'.
Crear el kit con el método POST utilizando la rutas URL_SERVICE y KITS_PATH y el kit_body de data.py.
Llamar el authToken que se generó cuando se creó el nuevo usuario.
Llamar el encabezado authorization.
Resultado Esta solicitud generará un kit dentro del usuario enlazado por medio del authToken

Pruebas de la lista de comprobación del campo 'name'

Descargar pytest.

Importar data y sender_stand_request.

Escribir una función con el método GET para cambiar valores en el parámetro 'name', utilizando el kit_body de data, además, se debe copiar el diccionario del archivo data para evitar cambios en los datos del diccionario de origen.

Crear una función de prueba positiva teniendo en cuenta el kit_body, el post del kit_body y el status code.

Comprobar si el código de estado de la función de prueba positiva es 201 y que el campo 'name' esté en la respuesta y contiene un valor.

Crear una función de prueba negativa teniendo en cuenta el kit_body, el post del kit_body y el status code.

Comprobar si el código de estado de la función de prueba negativa es 400 y que el status code en el cuerpo de respuesta es 400.

Crear cada prueba en una función separada y cada uno debe tener el prefijo 'test' para que pytest la tenga en cuenta.

Resultado Las pruebas estarán automatizadas y cada prueba creará un nuevo kit dentro del usuario teniendo en cuenta el parámetro de la prueba.

Lista de comprobación por tener en cuenta

El número permitido de caracteres (1): kit_body = { "name": "a"}
El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
Se permiten espacios: kit_body = { "name": " A Aaa " }
Se permiten números: kit_body = { "name": "123" }
El parámetro no se pasa en la solicitud: kit_body = { }
Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
Reglas

Se deben tener en cuenta el headers, status_code, status_code, ok, url, request, text, json() para que las respuestas de las funciones sean correctas y las pruebas estén bien ejecutadas. Tambien, hay que tener en cuenta la conexión al git y clonar el repositorio con SSH para trabajar en el proyecto de forma local. Cuando ya se haya terminado de trabajar con el proyecto, se debe empuhar al git por medio de comandos de commit
