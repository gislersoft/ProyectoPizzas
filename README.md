# Projeto Pizzas

# Cosas para tener en cuenta en Django

```
pip install virtualenv
virtualenv nombre_del_proyecto
pip install django
python .\Scripts\django-admin.py startproject nombre_proyecto
```
Verificar que se está en la raíz del virtual env y que este está activo.
Renombrar de nombre_proyecto a src para no tener confusiones.
Entrar a src y ejecutar:

```
python manage.py runserver (dentro del src para ejecutar servidor)
python manage.py migrate (migrar bases de datos [investigar para qué sirve esto])
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

# Proceso de Code Review

Este diagrama de procesos describe las interacciones que ocurren entre el desarrollador, git, github, jenkins y su par programador encargado de verificar el código.

![ProcesoDesarrollo](https://user-images.githubusercontent.com/9287467/64791593-8e61b480-d53d-11e9-99a6-6998478d6550.png)
