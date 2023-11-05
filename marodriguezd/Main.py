import tkinter as tk
from tkinter import filedialog
from BackupController import BackupController


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

    bm = BackupController(folder_path, destination_path)
    bm.create_zip()


def save_paths():
    bm = BackupController(entry_folder_path.get(), entry_destination_path.get())
    bm.save_paths()


def load_paths():
    bm = BackupController("", "")
    paths = bm.load_paths()

    entry_folder_path.delete(0, tk.END)
    entry_destination_path.delete(0, tk.END)
    entry_folder_path.insert(0, paths["folder_path"])
    entry_destination_path.insert(0, paths["destination_path"])


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
