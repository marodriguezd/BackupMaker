import os
import zipfile
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import pickle


def create_zip(folder_path, destination_path):
    """
    Crea un archivo ZIP que contiene el contenido de una carpeta y lo almacena en una ubicación de destino.

    Args:
    folder_path (str): Ruta de la carpeta que se desea comprimir en el archivo ZIP.
    destination_path (str): Ruta donde se almacenará el archivo ZIP resultante.

    Returns:
    None

    Example:
    create_zip("/ruta/a/la/carpeta", "/ruta/para/almacenar/backup")

    Esta función toma como entrada una ruta de carpeta y una ruta de destino. Genera un archivo ZIP con el contenido de
    la carpeta especificada y lo guarda en la ruta de destino.

    Si el nombre de la carpeta está vacío, se establece por defecto como "Backup". El archivo ZIP se nombra utilizando
    la fecha y hora actuales en el formato "NombreDeCarpeta_Backup_AAAA-MM-DD_HHMM.zip".

    La función recorre la carpeta y sus subdirectorios, añadiendo cada archivo al archivo ZIP con su ruta relativa.

    Nota: Esta función requiere que los módulos 'os' y 'zipfile' estén importados.
    """
    # Extrae el nombre de la propia ruta
    folder_name = folder_path.split("/")[-1]
    if not folder_name:
        folder_name = "Backup"

    # Genera el nombre del archivo ZIP basado en la fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    zip_name = f"{folder_name}_Backup_{timestamp}.zip"
    zip_path = os.path.join(destination_path, zip_name)

    # Crea un archivo ZIP de la carpeta y su contenido
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, rel_path)


def save_paths():
    """
    Guarda las rutas de carpetas especificadas por el usuario en un archivo pickle en una ubicación predefinida.

    Esta función recopila las rutas de carpetas especificadas por el usuario, que se almacenan en un diccionario 'paths'
    con las claves 'folder_path' y 'destination_path'. Luego, crea una carpeta de respaldo predeterminada en la carpeta
    'Documentos' del directorio de usuario. A continuación, guarda el diccionario de rutas en un archivo pickle en la
    ubicación predefinida.

    Args:
    None

    Returns:
    None

    Example:
    save_paths()

    Nota: Esta función requiere que los módulos 'os' y 'pickle' estén importados.
    """
    paths = {
        "folder_path": entry_folder_path.get(),
        "destination_path": entry_destination_path.get()
    }

    user_path = os.path.expanduser("~")
    backup_folder = os.path.join(user_path, "Documents", "BackupMaker")
    os.makedirs(backup_folder, exist_ok=True)

    with open(f"{user_path}\\Documents\\BackupMaker\\paths.pkl", "wb") as file:
        pickle.dump(paths, file)


def load_paths():
    """
    Carga las rutas de carpetas almacenadas previamente en un archivo pickle y las muestra en campos de entrada en la
    interfaz de usuario.

    Esta función intenta cargar las rutas de carpetas desde un archivo pickle previamente almacenado en una ubicación
    específica. Si el archivo se encuentra, las rutas se recuperan y se insertan en los campos de entrada
    'entry_folder_path' y 'entry_destination_path' de la interfaz de usuario.

    Si el archivo no se encuentra (FileNotFoundError), la función no realiza ninguna acción.

    Args:
    None

    Returns:
    None

    Example:
    load_paths()

    Nota: Esta función requiere que los módulos 'os' y 'pickle' estén importados. Los campos de entrada
    'entry_folder_path' y 'entry_destination_path' deben estar definidos en la interfaz de usuario para que esta función
    funcione correctamente.
    """
    try:
        user_path = os.path.expanduser("~")
        with open(f"{user_path}\\Documents\\BackupMaker\\paths.pkl", "rb") as file:
            paths = pickle.load(file)
            entry_folder_path.delete(0, tk.END)
            entry_destination_path.delete(0, tk.END)
            entry_folder_path.insert(0, paths["folder_path"])
            entry_destination_path.insert(0, paths["destination_path"])
    except FileNotFoundError:
        pass


def select_folder_path():
    """
    Abre un cuadro de diálogo para que el usuario seleccione una carpeta de origen y muestra la ruta en un campo de entrada.

    Esta función utiliza un cuadro de diálogo proporcionado por el módulo 'filedialog' de tkinter para permitir al
    usuario seleccionar una carpeta de origen. La ruta de la carpeta seleccionada se almacena en la variable
    'folder_path'. Luego, esta ruta se inserta en un campo de entrada 'entry_folder_path' en la interfaz de usuario.

    Args:
    None

    Returns:
    None

    Example:
    Se debe llamar a esta función al hacer clic en un botón u otro evento en la interfaz de usuario.

    Nota: Para que esta función funcione correctamente, los módulos 'filedialog' y 'tkinter' deben estar importados, y
    un campo de entrada 'entry_folder_path' debe estar definido en la interfaz de usuario.
    """
    folder_path = filedialog.askdirectory(title="Seleccionar carpeta de origen")
    entry_folder_path.delete(0, tk.END)
    entry_folder_path.insert(0, folder_path)


def select_destination_path():
    """
    Abre un cuadro de diálogo para que el usuario seleccione una carpeta de destino para la copia de seguridad y
    muestra la ruta en un campo de entrada.

    Esta función utiliza un cuadro de diálogo proporcionado por el módulo 'filedialog' de tkinter para permitir al
    usuario seleccionar una carpeta de destino para la copia de seguridad. La ruta de la carpeta seleccionada se
    almacena en la variable 'destination_path'. Luego, esta ruta se inserta en un campo de entrada
    'entry_destination_path' en la interfaz de usuario.

    Args:
    None

    Returns:
    None

    Example:
    Se debe llamar a esta función al hacer clic en un botón u otro evento en la interfaz de usuario.

    Nota: Para que esta función funcione correctamente, los módulos 'filedialog' y 'tkinter' deben estar importados, y
    un campo de entrada 'entry_destination_path' debe estar definido en la interfaz de usuario.
    """
    destination_path = filedialog.askdirectory(title="Seleccionar destino de copia de seguridad")
    entry_destination_path.delete(0, tk.END)
    entry_destination_path.insert(0, destination_path)


def backup():
    """
    Realiza una copia de seguridad comprimiendo una carpeta de origen en una ubicación de destino.

    Esta función obtiene las rutas de la carpeta de origen y de destino desde los campos de entrada 'entry_folder_path'
    y 'entry_destination_path' en la interfaz de usuario. Luego, utiliza la función 'create_zip' para comprimir la
    carpeta de origen y su contenido en un archivo ZIP, que se guarda en la carpeta de destino.

    Args:
    None

    Returns:
    None

    Example:
    Se debe llamar a esta función al hacer clic en un botón u otro evento en la interfaz de usuario.

    Nota: Para que esta función funcione correctamente, se deben definir los campos de entrada 'entry_folder_path' y
    'entry_destination_path' en la interfaz de usuario, y la función 'create_zip' debe estar disponible en el mismo
    contexto.
    """
    folder_path = entry_folder_path.get()
    destination_path = entry_destination_path.get()
    create_zip(folder_path, destination_path)


if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Copia de Seguridad")

    # Crear y configurar etiquetas y entradas de texto
    label_folder = tk.Label(root, text="Ruta de origen:")
    label_folder.grid(row=0, column=0, padx=10, pady=10)
    entry_folder_path = tk.Entry(root, width=40)
    entry_folder_path.grid(row=0, column=1, padx=10, pady=10)

    label_destination = tk.Label(root, text="Ruta de destino:")
    label_destination.grid(row=1, column=0, padx=10, pady=10)
    entry_destination_path = tk.Entry(root, width=40)
    entry_destination_path.grid(row=1, column=1, padx=10, pady=10)

    # Crear botones para seleccionar carpetas y realizar la copia de seguridad
    button_select_folder = tk.Button(root, text="Seleccionar Carpeta de Origen", command=select_folder_path)
    button_select_folder.grid(row=0, column=2, padx=10, pady=10)

    button_select_destination = tk.Button(root, text="Seleccionar Ruta de Destino", command=select_destination_path)
    button_select_destination.grid(row=1, column=2, padx=10, pady=10)

    button_backup = tk.Button(root, text="Realizar Copia de Seguridad", command=backup)
    button_backup.grid(row=2, column=1, padx=10, pady=20)

    # Crear botón para guardar rutas
    button_save_paths = tk.Button(root, text="Guardar Rutas", command=save_paths)
    button_save_paths.grid(row=2, column=2, padx=10, pady=10)

    # Obtener el tamaño de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (screen_width - root.winfo_reqwidth()) / 2
    y = (screen_height - root.winfo_reqheight()) / 2

    # Establecer la geometría para centrar la ventana en la pantalla
    root.geometry("+%d+%d" % (x, y))

    # Cargar las rutas guardadas si existen
    load_paths()

    # Iniciar el bucle de la interfaz gráfica
    root.mainloop()
