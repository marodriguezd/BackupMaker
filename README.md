# BackupMaker

**BackupMaker** es una aplicación de Python que te permite realizar copias de seguridad de tus carpetas de forma sencilla y con una interfaz gráfica. Puedes seleccionar la carpeta de origen y la carpeta de destino donde se guardarán tus copias de seguridad. Además, la aplicación generará automáticamente nombres únicos para los archivos ZIP de las copias de seguridad.

## Características

- Interfaz gráfica amigable para el usuario.
- Selección de carpeta de origen y carpeta de destino.
- Nombres únicos para los archivos ZIP de copias de seguridad basados en la fecha y hora de creación.
- Posibilidad de guardar las rutas seleccionadas para su uso posterior.
- Gestión automática de directorios para almacenar la información de las rutas guardadas.

## Uso

1. **Seleccionar Carpeta de Origen**: Haciendo clic en el botón "Seleccionar Carpeta de Origen", puedes elegir la carpeta que deseas respaldar.

2. **Seleccionar Ruta de Destino**: Haciendo clic en el botón "Seleccionar Ruta de Destino", puedes elegir la carpeta donde se guardarán las copias de seguridad.

3. **Realizar Copia de Seguridad**: Haciendo clic en "Realizar Copia de Seguridad", se generará un archivo ZIP en la carpeta de destino, con un nombre único basado en la fecha y hora de creación, que contiene el contenido de la carpeta de origen.

4. **Guardar Rutas**: Haciendo clic en "Guardar Rutas", las rutas de la carpeta de origen y de destino se guardarán para su uso posterior.

5. **Cargar Rutas Guardadas**: Al iniciar la aplicación, las rutas previamente guardadas se cargarán automáticamente si existen.

## Requisitos

- Python 3.x
- Módulos requeridos: `os`, `zipfile`, `datetime`, `re`, `tkinter`, `pickle`

## Compilar el Código

Para compilar este código en un ejecutable independiente, puedes utilizar PyInstaller. Asegúrate de instalar PyInstaller antes de usarlo.

```
pip install pyinstaller
```

Luego, puedes compilar el código de la siguiente manera:

```
pyinstaller --onefile --noconsole .\BackupMaker.py
```

Esto creará una carpeta con el ejecutable en la subcarpeta `dist`.

## Nota

En sistemas Windows, puede aparecer brevemente una ventana de consola al ejecutar el programa, pero desaparecerá rápidamente.

¡Disfruta de tus copias de seguridad fáciles y automáticas con BackupMaker!
