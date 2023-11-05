import datetime
import os
import pickle
import zipfile


class BackupController:

    def __init__(self, folder_path, destination_path):
        """
        Inicializa un objeto BackupController con las rutas de la carpeta fuente y la carpeta de destino.

        Args:
        folder_path (str): Ruta de la carpeta que se desea respaldar.
        destination_path (str): Ruta donde se almacenarán los archivos de respaldo.

        Returns:
        None
        """
        self.folder_path = folder_path
        self.destination_path = destination_path

    def create_zip(self):
        """
        Crea un archivo ZIP que contiene el contenido de una carpeta y lo almacena en una ubicación de destino.

        Args:
        None

        Returns:
        None
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

        Args:
        None

        Returns:
        None
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
        Carga las rutas de carpetas almacenadas previamente en un archivo pickle.

        Args:
        None

        Returns:
        dict: Un diccionario que contiene las rutas de carpetas cargadas desde el archivo pickle.
        Si el archivo no se encuentra, retorna None.
        """
        try:
            user_path = os.path.expanduser("~")
            with open(f"{user_path}\\Documents\\BackupMaker\\paths.pkl", "rb") as file:
                paths = pickle.load(file)
                return paths
        except FileNotFoundError:
            paths = {
                "folder_path": "",
                "destination_path": ""
            }

            return paths
