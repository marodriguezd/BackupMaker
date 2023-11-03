import os
import zipfile
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
import pickle


def create_zip(folder_path, destination_path):
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


def select_folder_path():
    folder_path = filedialog.askdirectory(title="Seleccionar carpeta de origen")
    entry_folder_path.delete(0, tk.END)
    entry_folder_path.insert(0, folder_path)


def select_destination_path():
    destination_path = filedialog.askdirectory(title="Seleccionar destino de copia de seguridad")
    entry_destination_path.delete(0, tk.END)
    entry_destination_path.insert(0, destination_path)


def backup():
    folder_path = entry_folder_path.get()
    destination_path = entry_destination_path.get()
    create_zip(folder_path, destination_path)


def save_paths():
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
