# Google Drive Inventory

## Contexto
Se solicitó crear un script de python, el cual le permita a un usuario loguearse a su cuenta de google drive, con el fin de poder obtener sus archivos almacenados. Estos archivos deben almacenarse en una base de datos y una vez ahí ver cuales de ellos son de acceso público y cuales de acceso privado. A todos los archivos que sean de acceso público se los debe modificar para que sean de acceso privado y al hacer esto, debe envíarsele al dueño de dicho archivo un mail indicando dicha modificación.

## Aclaraciones
- El archivo "client_secrets.json" y "credentials_module.json" fueron eliminados del repositorio para no tener problemas con github, por lo tanto se deben seguir los pasos que se encuentran debajo para poder descargar las credenciales. Igualmente se deja el archivo "settings.yaml" que ya tiene la configuración para que no sea necesario autenticarse cada vez una vez que ya están las credenciales cargadas.
- La funcionalidad que permite enviar un mail al owner de un archivo que fue modificado no pudo ser implementada, debido a errores de conexión utilizando "smtplib".
- No está testeado que funcione la dockerización

# Utilizando Google Drive API

Para poder utilizar la api de google drive, lo primero que hay que hacer es:
1) ingresar a https://console.cloud.google.com/welcome?project=prueba-427220 (Google Cloud Platform).
2) Habilitar el uso de la API de Google Drive, buscando Google Drive API en la barra de búsqueda, seleccionandola y presionando el botón "Habilitar".
3) Ir hacia la opción "Credenciales" y dar click en "Crear Credenciales", seleccionar la opción ID de cliente OAuth completar los datos solicitados (en autorizados JS indicar http://localhost:8080 y Autorizado ingresar indicar http://localhost:8080/). Dar click en "Aceptar".
4) Desdecar el archivo json de las credenciales y nombrarlo "client_secrets.json" una vez hecho esto se debe modificar los campos 'client_id' y 'client_secrets' del archivo settings.yml y poner los valores de los campos con mismo nombre del archivo 'client_secrets.json', esto con el fin de que se cree el archivo 'credentials_module.json' donde se almacenaran los datos de inicio de sesion.

## Nota:
- Se deben instalar todas las dependencias necesarias para poder ejecutar el script, las mismas se encuentran en el archivo requierements.txt y se instalan ejecutando el siguiente comando:
```sh
    pip install -r requirements.txt
```

- También en el archivo .env se deben ingresar todos los datos requeridos, esto con el fin de que la DB funcione correctamente.

## Para realizar este proyecto se utilizo virtualenv
```sh
    pip install virtualenv #instala virtualenv
    virtualenv -p python3 nombre_entorno #crea un nuevo entorno virtual
```

# Links de interes
https://pypi.org/project/python-dotenv/ -> dotenv
https://www.w3schools.com/python/python_mysql_update.asp --> W3Schools
https://developers.google.com/drive/api/reference/rest/v3?hl=es-419 --> Google Drive API
https://developers.google.com/drive/api/quickstart/python?hl=es-419 --> configuración de google api para python