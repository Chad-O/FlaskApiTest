# bSalestest
#Carpeta API:

main.py: Contiene la llamada a la base de datos y la ruta del app.

wsgi.py: Funciona como una "interfaz" para el main.py de modo que no se interactúa directamente con la definición de la ruta.

Procfile: Permite a gunicorn determinar qué archivo utilizar. Se desplegó en Heroku.

#Ruta:

https://bsalesapi.herokuapp.com/flights/#/passengers

Donde # es el número del vuelo, de 1 a 4.

##Para montar el api localmente:
  
  -Ingresar a la carpeta api por consola y correr: " pip install -r requirements.txt"
  -En Consola correr: ".\env\Scripts\Activate"
  -Correr el archivo main
