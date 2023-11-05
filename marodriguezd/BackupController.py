import datetime
import os
import pickle
import zipfile


class BackupController:

    def __init__(self, folder_path, destination_path):
        self.folder_path = folder_path
        self.destination_path = destination_path

    def create_zip(self):
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
        folder_name = self.folder_path.split("/")[-1]
        if not folder_name:
            folder_name = "Backup"

        # Genera el nombre del archivo ZIP basado en la fecha y hora actual
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        zip_name = f"{folder_name}_Backup_{timestamp}.zip"
        zip_path = os.path.join(self.destination_path, zip_name)

        # Crea un archivo ZIP de la carpeta y su contenido
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.folder_path)
                    zipf.write(file_path, rel_path)

    def save_paths(self):
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
            "folder_path": self.folder_path,
            "destination_path": self.destination_path
        }

        user_path = os.path.expanduser("~")
        backup_folder = os.path.join(user_path, "Documents", "BackupMaker")
        os.makedirs(backup_folder, exist_ok=True)

        with open(f"{user_path}\\Documents\\BackupMaker\\paths.pkl", "wb") as file:
            pickle.dump(paths, file)

    def load_paths(self):
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
                return paths
                """entry_folder_path.delete(0, tk.END)
                entry_destination_path.delete(0, tk.END)
                entry_folder_path.insert(0, paths["folder_path"])
                entry_destination_path.insert(0, paths["destination_path"])"""
        except FileNotFoundError:
            pass
