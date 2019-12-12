# Proyecto Pizzas 🍕

Este es el repositorio principal del proyecto de pizzas, en este readme encontrarás toda la ayuda recopilada por el equipo para el proceso de desarrollo.


# Proyecto en Taiga

Este es el link de acceso al kanban board del proyecto: https://tree.taiga.io/project/josealejolibreros-superpizzas/backlog

Recuerda agregar los criterios de aceptación a las  historias de usuario.

# Indice

* 📌[Dominio y Tenants](#dominioytenants)
* 📌[Prácticas Ágiles](#prácticas-ágiles)
* 📌[Instalación](#instalación)
* 📌[Preguntas frecuentes sobre Django](#preguntas-frecuentes-sobre-django)
* 📌[Proceso de Code Review](#proceso-de-code-review)
* 📌[Comandos Básicos de GIT](#comandos-básicos-de-git)
* 📌[Preguntas frecuentes sobre GitHub](#preguntas-frecuentes-sobre-github)

## Dominio y Tenants

* **Franquicia:** El tenant "La cuenta" Ejemplos de franquicias: Pizza Hut, Jennos Pizza, Dominos Pizza etc.
* **Usuarios:** Los que se loguean al sistema y pueden tener los siguientes roles: Administrador, Digitar y Cliente.
* **Superusuario:** El superusuario se encarga de administrar todas las franquicias y tiene acceso a vistas especiales.

![tenants](https://user-images.githubusercontent.com/9287467/64831865-3064b980-d59d-11e9-874f-61fac23907ab.png)

## Prácticas Ágiles

* Daily Meetings
* Kanban Board
* Retrospectiva
* Planning
* Continuous Integration / Continuos Deployment
* Par programador (Code Review)
* DevOps
* Team Leader Rotation

## Instalación

Ubicarse en la carpeta raíz del repositorio

1) Instalar los requerimientos pip3 install -r requirements.txt

2) Crear una base de datos para el proyecto y actualizar la configuración de BD en env/secrets.env

3) Sincronizar la base de datos: python manage.py migrate

4) Ejecutar el comando: python manage.py initial_franchise para crear el tenant publico:

Los datos de acceso por defecto son: email="admin@admin.co", password="superpizzas"


## Preguntas frecuentes sobre Django

```
pip install virtualenv
virtualenv nombre_del_proyecto
```
o
```
python -m venv nombre_del_entorno
```

En `nombre_del_entorno/Scripts` se encuentran scripts llamados `activate` con diferentes extensiones.
Estos scripts sirven para activar el entorno virtual. En PyCharm, se puede seleccionar el entorno virtual para el proyecto, para que el IDE lo active automáticamente al abrir el proyecto, e incluso el mismo PyCharm puede crear entornos virtuales para el proyecto.
En caso de necesitar desactivar el entorno virtual, usar el comando `deactivate`

```
pip install django
python .\Scripts\django-admin.py startproject nombre_proyecto
```
Verificar que se está en la raíz del virtual env y que este está activo.
Renombrar de nombre_proyecto a src para no tener confusiones.
Entrar a src y ejecutar:

```
python manage.py runserver (dentro del src para ejecutar servidor)
python manage.py migrate (migrar bases de datos)
python manage.py makemigrations
```

En settings.py se puede cambiar el idioma en la opción LANGUAGES

```
python manage.py createsuperuser
python manage.py startapp nombre_app (crear nueva app)
```

* En **setting.py** se debe inscribir la nueva aplicación en installed apps
* El comando **models** se usa para crear las tablas de las bases de datos (buscar en la documentación para los tipos de campos que se pueden crear)
* Usar python **manage.py makemigrations** al cambiar un models y luego migrate
* Debe registrarse el modelo en **admin.py** de la aplicación para que aparezca en la página de admins
* En views se configura qué html carga la aplicación, en urls debe configurarse esa vista (debe importarse la vista en las urls)
* En **settings.py** está la opción templates. Ahí debe agregarse un directorio en dirs para guardar los html
* En la aplicación se crea el **forms.py** para los formularios a renderizar (formularios que no son basados en un modelo, por ejemplo, un formulario de contacto)
* En views se debe importar el form y crear un diccionario para el "contexto". Lo que va entre comillas es lo que se pone en el html para renderizar
* **python manage.py** collectstatic para recoger archivos estáticos

## Proceso de Code Review

Este diagrama de procesos describe las interacciones que ocurren entre el desarrollador, git, github, jenkins y su par programador encargado de verificar el código.

![ProcesoDesarrollo](https://user-images.githubusercontent.com/9287467/64791593-8e61b480-d53d-11e9-99a6-6998478d6550.png)

## Comandos Básicos de GIT

- `git clone <URL_DEL_REPOSITORIO>` --> Clona el repositorio
- `git pull origin master` --> Sincroniza el repositorio local con la rama MASTER del repositorio ORIGIN
- `git add <ARCHIVO>` --> Marca el archivo modificado como parte de un commit
- `git reset HEAD <ARCHIVO>` --> Quita el archivo del STAGING 
- `git push <REPOSITORIO_REMOTO> <BRANCH>` --> Envia cambios a la rama BRANCH del REPOSITORIO_REMOTO
- `git commit -m "MENSAJE_DESCRIPTIVO_DEL_COMMIT" ` --> Crea el COMMIT con los cambios marcados en el STAGING y pone el mensaje descriptivo 
- `git branch ` --> Muestra las ramas del repositorio local

## Preguntas frecuentes sobre GitHub

* [¿Qué es un Pull Request?](#qué-es-un-pull-request)
* [¿Qué debo hacer si mi Pull Request falló?](#qué-debo-hacer-si-mi-pull-request-falló)
* [¿Qué debo hacer si mi Pull Request pasó?](#qué-debo-hacer-si-mi-pull-request-pasó)
* [¿Qué debo hacer si mi Pull Request tiene conflictos?](#qué-debo-hacer-si-mi-pull-request-tiene-conflictos)
* [¿Porqué toma tanto tiempo Jenkins en actualizar mi Pull Request?](#porqué-toma-tanto-tiempo-Jenkins-en-actualizar-mi-pull-request)
* [¿Porqué Jenkins no ha empezado el build de mi Pull Request?](#porqué-jenkins-no-ha-empezado-el-build-de-mi-pull-request)

### ¿Qué es un Pull Request?

Un Pull Request (PR) es un intento de mezclar una rama dentro de la rama principal u otra rama, este proceso se realiza desde la interfaz web de github, se debe tener en cuente desde que rama se está haciendo el PR y a que rama se está intentando mezclar.

### ¿Qué debo hacer si mi Pull Request falló?

En el caso de que el PR tenga un comentario de Jenkins explicando que el build ha fallado debemos revisar el log en Jenkins, en este caso el comentario contiene una URL al servidor de Jenkins dando click en este link debemos realizar los siguientes pasos:

1. Introducir las credenciales de Jenkins.
2. Dar click en la opción "Console Log".

### ¿Qué debo hacer si mi Pull Request pasó?

En este caso falta que un "Par programador" (Code Reviewer) apruebe los cambios ya que para poder mezclar un Pull Request se requiere dos aprobaciones la de Jenkins y la de un Code Reviewer.

### ¿Qué debo hacer si mi Pull Request tiene conflictos?

Esto es de lo más normal en el proceso de desarrollo, los conflictos ocurren cuando dos o más programadores han realizado cambios a un mismo archivo en tiempos diferentes, git es muy inteligenete y verifica si puede hacer un "Merge" de líneas de manera autómatica sin embargo hay momentos en que las líneas de código "colisionan" y git no sabe cómo resolver esta "colisión" en este momento se produce un conflicto. Para resolver un conflicto se pude utilizar la interfaz web de GitHub si aún no se es muy experto manejando git, un conflicto se vé así:

```
int a = 3;
<<<<<<< HEAD
b = a + 1;
=======
b = a + 2;
>>>>>>> branch-a
```

Git agrega tres marcas:

1. Esta marca `<<<<<<<` explica donde inicia el conflicto.
1. Esta marca ======= explica donde termina el código del commit A involucrado en el conflicto y marca el inicio del commit B involucrado en el conflicto.
1. Esta marca `>>>>>>>` explica donde termina el conflicto del commit B.

Estas marcas se **DEBEN** borrar **NUNCA** deben irse en un commit, git las pone ahí para que el desarrollador "manualmente" las elimine y resuelva el conflicto. En el ejemplo anterior la línea que debe ir es `b = b + 2` a el criterio de quien está resolviendo el conflicto, el resultado debe ser después de borrar las marcas:

```
int a = 3;
b = a + 2;
```

Cuando esto ocurre en la interfaz web de github se marca el conflicto cómo resuelto, si se está usando la línea de comandos se debe hacer un `git add archivo` marcando que el archivo en cuestión ya tiene todos los conflictos resueltos, un **ERROR** muy común es olvidar resolver otros conflictos en el archivo **NO OLVIDES** resolverlos todos antes de marcar el archivo cómo resuelto.

### ¿Porqué toma tanto tiempo Jenkins en actualizar mi Pull Request?

Jenkins require tiempo para detectar el nuevo pull request actualmente tenemos un servidor de jenkins que no está en la nube, entonces obtamos por utilizar la estrategía de "Polling" que consiste en que Jenkins cada dos minutos está revisando el repositorio por algún cambio, si utilizaramos los github webhooks podriamos reducir esos 2 minutos. Sin embargo hay varios tiempos que hay que tener en cuenta la siguiente fórmula muestra todos los tiempos involucrados desde que se hace un Pull Request hasta que se termina un Build:  

> Tiempo Total = Tiempo Polling + Tiempo del Build

### ¿Porqué Jenkins no ha empezado el build de mi Pull Request?

Jenkins hace "Polling" del repositorio en busca de cambios algunas causas pueden ser: 

1. El servidor de jenkins está apagado o no tiene acceso a internet.
2. Ya se corrieron las pruebas anteriormente, en este caso agregando el comentario `ok to test` le vuelve a decir a Jenkins que intente un nuevo build.



