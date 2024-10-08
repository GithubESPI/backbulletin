import logging
from app.api.endpoints import uploads, importBulletin
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.services.storage_service import AzureBlobService


# Configurer le logger pour la production
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Ajouter la middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bulletin.groupe-espi.fr"],  # Remplacer par l'URL de ton frontend
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)

# Inclusion des routes des différents modules
app.include_router(uploads.router, prefix="", tags=["uploads"])  # Uploads sans préfixe
app.include_router(importBulletin.router, prefix="/importBulletins", tags=["importBulletins"])

azure_blob_service = AzureBlobService()  # Initialize the Azure Blob service


