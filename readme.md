# Instalación del proyecto de "Prueba técnica ADEN" con Odoo 16
### Requisitos
* Tener instalado docker y docker-compose

### Pasos
1. Ejecución
En la raiz del proyecto donde se encuentra docker-compose.yaml, ejecute:
    ~~~~
    docker-compose up -d
    ~~~~

    
2. Ingresa a Odoo
    * Ingresa a localhost:<WEB_PORT> (En el puerto usted definira si quiere acceder a la pagina web o a la base de datos port:80 para bd y port:8085 para pagina web)
    * Si es la primera vez que ingresa al sistema complete el formulario de creación de la base de datos.


3. Consulta a la API:
    * Si usted desea hacer una consulta a la api para saber cuantos Students hay en x Program ingrese la siguiente url: http://localhost:8085/edu_hub/program/<int:program_id>/students
