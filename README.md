# Instalación de API

Ubicarse al incio del proyecto en terminal y correr lo siguiente:

## Configuración previa

### Creación de un virtual enviroment
```bash
python -m venv venv
```

*Nota:* En el caso de que ocurra un error, posiblemente se tenga que instalar primero **python3-venv** o **python-venv** o lo que sea que te diga la consola xd (asegurarse que la version sea para python 3).

### Conectarse al venv

```bash
source venv/bin/activate.fish
```

*Nota:* Si estas en fish shell se usa la extensión **.fish** del activate, si estas en **bash** no poner ninguna extensión y si estás en otro shell, averigua!.

### Instalación de paquetes

```bash
pip install -r requirements.txt
```

*Nota:* Recuerda tener instalado pip.

## Preparación para correr la API por primera vez

### Generando las migraciones de los modelos

```bash
python manage.py migrate
```

### Creación de superusuario (Opcional)

```bash
python manage.py createsuperuser
```

Te pedirá username, email y pass. Esto se crea para poder accede al admin y si lo haces debes crearte un perfil dentro del admin para que puedas usarlo en el frontend.

Este parte es opcional porque puedes crearte el usuario desde el frontend o desde la misma API **(no podrás entrar al admin con esto)**.

### Corriendo el servidor

```bash
python manage.py runserver
```

Con esto debería correr normal la API.