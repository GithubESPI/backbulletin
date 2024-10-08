import logging
from fastapi import HTTPException
from azure.storage.blob import BlobServiceClient
import os

logger = logging.getLogger(__name__)

class AzureBlobService:
    def __init__(self):
        # Charger la chaîne de connexion et le nom du conteneur depuis les variables d'environnement
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = os.getenv("AZURE_BLOB_CONTAINER")
        
        if not self.connection_string or not self.container_name:
            logger.error("Azure storage configuration is missing.")
            raise ValueError("Azure storage configuration is missing.")
        
        # Initialiser le client BlobService
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def download_template(self, blob_name: str, temp_template_path: str):
        try:
            # Logs avant de commencer le téléchargement
            logger.info(f"Attempting to download blob {blob_name} to {temp_template_path}")

            # Récupérer le client du conteneur
            container_client = self.blob_service_client.get_container_client(self.container_name)
            # Récupérer le client du blob
            blob_client = container_client.get_blob_client(blob_name)
            # Télécharger le fichier dans le chemin spécifié
            with open(temp_template_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())

            # Log de succès après téléchargement
            logger.info(f"File downloaded successfully from Azure Blob: {blob_name} to {temp_template_path}")

        except Exception as e:
            # Log de l'erreur et levée d'une exception HTTP
            logger.error(f"Error while downloading blob {blob_name}: {str(e)}")
            raise HTTPException(status_code=500, detail="Error downloading template")
