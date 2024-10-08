import logging
from app.api.endpoints import apprenants, groupes, absences, uploads, importBulletin, codeRepertoire
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
app.include_router(apprenants.router, prefix="/apprenants", tags=["apprenants"])
app.include_router(groupes.router, prefix="/groupes", tags=["groupes"])
app.include_router(absences.router, prefix="/absences", tags=["absences"])
app.include_router(uploads.router, prefix="", tags=["uploads"])  # Uploads sans préfixe
app.include_router(importBulletin.router, prefix="/importBulletins", tags=["importBulletins"])
app.include_router(codeRepertoire.router, prefix="/codeRepertoire", tags=["codeRepertoire"])

azure_blob_service = AzureBlobService()  # Initialize the Azure Blob service

@app.get("/generate-pdf")
def generate_pdf(template_name: str):
    try:
        template_data = azure_blob_service.download_blob(template_name)
        return {"message": "PDF generated successfully"}
    except Exception as e:
        logger.error(f"Error generating PDF: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while generating the PDF")
