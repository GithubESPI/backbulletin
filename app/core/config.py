from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # Nom du projet
    PROJECT_NAME: str = "Upload de Bulletins"
    
    # Répertoires de base
    BASE_DIR: str = os.getcwd()
    DOCUMENTS_DIR: str = os.path.join(os.getenv('USERPROFILE', os.getenv('HOME')), 'Documents')
    OUTPUT_DIR: str = os.path.join(DOCUMENTS_DIR, "outputs")
    
    # Fichier de modèle
    TEMPLATE_FILE: str = os.path.join(BASE_DIR, "template", "modeleM1S1.docx")

    # Azure Blob Storage settings, loaded from environment variables
    AZURE_STORAGE_CONNECTION_STRING: str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_BLOB_CONTAINER: str = os.getenv('AZURE_BLOB_CONTAINER')
    
    DOWNLOAD_DIR: str = os.path.join(os.getenv('USERPROFILE', os.getenv('HOME')), 'Downloads')

    # Templates fetched from Azure Blob Storage
    M1_S1_MAPI_TEMPLATE: str = "MAPI-2023-2024/M1-S1-MAPI.xlsx"
    M1_S1_MAGI_TEMPLATE: str = "MAGI-2023-2024/M1-S1-MAGI.xlsx"
    M1_S1_MEFIM_TEMPLATE: str = "MEFIM-2023-2024/M1-S1-MEFIM.xlsx"
    
    M1_S1_MAPI_TEMPLATE_NOT_EMPTY: str = "MAPI-2023-2024/M1-S1-MAPI.xlsx"
    M1_S1_MAGI_TEMPLATE_NOT_EMPTY: str = "MAGI-2023-2024/M1-S1-MAGI.xlsx"
    M1_S1_MEFIM_TEMPLATE_NOT_EMPTY: str = "MEFIM-2023-2024/M1-S1-MEFIM.xlsx"
    
    M1_S1_MAPI_TEMPLATE_WORD: str = "modele/modeleM1S1.docx"
    M1_S1_MAGI_TEMPLATE_WORD: str = "modele/modeleM1S1.docx"
    M1_S1_MEFIM_TEMPLATE_WORD: str = "modele/modeleM1S1.docx"

    M1_S2_MAPI_TEMPLATE: str = "MAPI-2023-2024/M1-S2-MAPI.xlsx"
    M1_S2_MAGI_TEMPLATE: str = "MAGI-2023-2024/M1-S2-MAGI.xlsx"
    M1_S2_MEFIM_TEMPLATE: str = "MEFIM-2023-2024/M1-S2-MEFIM.xlsx"
    
    M1_S2_MAPI_TEMPLATE_NOT_EMPTY: str = "MAPI-2023-2024/M1-S2-MAPI.xlsx"
    M1_S2_MAGI_TEMPLATE_NOT_EMPTY: str = "MAGI-2023-2024/M1-S2-MAGI.xlsx"
    M1_S2_MEFIM_TEMPLATE_NOT_EMPTY: str = "MEFIM-2023-2024/M1-S2-MEFIM.xlsx"
    
    M1_S2_MAPI_TEMPLATE_WORD: str = "modele/modeleM1S2.docx"
    M1_S2_MAGI_TEMPLATE_WORD: str = "modele/modeleM1S2.docx"
    M1_S2_MEFIM_TEMPLATE_WORD: str = "modele/modeleM1S2.docx"

    M2_S3_MAPI_TEMPLATE: str = "MAPI-2023-2024/M2-S3-MAPI.xlsx"
    M2_S3_MAGI_TEMPLATE: str = "MAGI-2023-2024/M2-S3-MAGI.xlsx"
    M2_S3_MEFIM_TEMPLATE: str = "MEFIM-2023-2024/M2-S3-MEFIM.xlsx"
    
    M2_S3_MAPI_TEMPLATE_NOT_EMPTY: str = "MAPI-2023-2024/M2-S3-MAPI.xlsx"
    M2_S3_MAGI_TEMPLATE_NOT_EMPTY: str = "MAGI-2023-2024/M2-S3-MAGI.xlsx"
    M2_S3_MEFIM_TEMPLATE_NOT_EMPTY: str = "MEFIM-2023-2024/M2-S3-MEFIM.xlsx"
    
    M2_S3_MAPI_TEMPLATE_WORD: str = "modele/modeleM2S3MAPI.docx"
    M2_S3_MAGI_TEMPLATE_WORD: str = "modele/modeleM2S3.docx"
    M2_S3_MEFIM_TEMPLATE_WORD: str = "modele/modeleM2S3.docx"

    M2_S4_MAPI_TEMPLATE: str = "MAPI-2023-2024/M2-S4-MAPI.xlsx"
    M2_S4_MAGI_TEMPLATE: str = "MAGI-2023-2024/M2-S4-MAGI.xlsx"
    M2_S4_MEFIM_TEMPLATE: str = "MEFIM-2023-2024/M2-S4-MEFIM.xlsx"
    
    M2_S4_MAPI_TEMPLATE_NOT_EMPTY: str = "MAPI-2023-2024/M2-S4-MAPI.xlsx"
    M2_S4_MAGI_TEMPLATE_NOT_EMPTY: str = "MAGI-2023-2024/M2-S4-MAGI.xlsx"
    M2_S4_MEFIM_TEMPLATE_NOT_EMPTY: str = "MEFIM-2023-2024/M2-S4-MEFIM.xlsx"
    
    M2_S4_MAPI_TEMPLATE_WORD: str = "modele/modeleM2S4.docx"
    M2_S4_MAGI_TEMPLATE_WORD: str = "modele/modeleM2S4.docx"
    M2_S4_MEFIM_TEMPLATE_WORD: str = "modele/modeleM2S4.docx"
    

    # ECTS
    ECTS_JSON_PATH: str = "json/ects.json"

    # ECTS
    ECTS_JSON_PATH: str = os.path.join(BASE_DIR, "json", "ects.json")

    RELEVANT_GROUPS: list = [
        "N-M1 MAPI ALT 1", "P-M1 MAPI ALT 2", "L-M1 MAPI ALT 2", "MP-M1 MAPI ALT",
        "P-M1 MAPI ALT 5", "L-M1 MAPI ALT 1", "P-M1 MAPI ALT 1", "P-M1 MAPI ALT 3",
        "B-M1 MAPI ALT 1", "M-M1 MAPI ALT 1", "LI-M1 MAPI ALT", "N-M1 MAPI ALT 2",
        "M-M1 MAPI ALT 2", "P-M1 MAPI ALT 4", "B-M1 MAPI ALT 2", "MP-M1 MAPI ALT",
        "L-M1 MAPI ALT 3", "P-M1 MAGI ALT 1", "N-M1 MAGI ALT", "M-M1 MAGI ALT",
        "LI-M1 MAGI ALT", "B-M1 MAGI ALT", "MP-M1 MAGI ALT", "L-M1 MAGI ALT",
        "P-M1 MAGI ALT 2", "LI-M1 MAGI ALT", "P-M1 MAGI ALT 2", "M-M1 MIFIM ALT",
        "N-M1 MIFIM ALT", "P-M1 MIFIM ALT 1", "P-M1 MIFIM ALT 2", "P-M1 MIFIM ALT 3",
        "LI-M1 MIFIM ALT", "B-M1 MIFIM ALT", "MP-M1 MIFIM ALT", "L-M1 MIFIM ALT"
    ]
    RELEVANT_GROUPS_M2: list = [
        "L-M2 MAPI ALT 1", "N-M2 MAGI ALT", "P-M2 MAPI ALT 3", "B-M2 MAGI ALT",
        "P-M2 MAPI ALT 5", "N-M2 MAPI ALT 2", "B-M2 MAPI ALT 1", "P-M2 MAGI ALT 2",
        "M-M2 MAPI ALT 2", "P-M2 MAPI ALT 1", "M-M2 MAPI ALT 1", "L-M2 MAPI ALT 2",
        "P-M2 MAPI ALT 2", "P-M2 MAPI ALT 4", "N-M2 MAPI ALT 1", "L-M2 MAGI ALT",
        "P-M2 MAGI ALT 1", "M-M2 MAGI ALT", "LI-M2 MAPI ALT", "M-M2 MAPI ALT 3",
        "M-M2 2ESI ALT", "N-M2 2ESI ALT", "N-M2 MIFIM ALT", "P-M2 2ESI ALT",
        "P-M2 MIFIM ALT 1", "P-M2 MIFIM ALT 2", "P-M2 MIFIM ALT 3", "M-M2 MIFIM ALT",
        "MP-M2 MAGI ALT", "MP-M2 MAPI ALT 1", "MP-M2 MAPI ALT 2", "B-M2 2ESI ALT",
        "B-M2 MIFIM ALT", "B-M2 MAPI ALT 2", "L-M2 MIFIM ALT", "L-M2 2ESI ALT",
        "P-M2 MAPI RP", "P-M2 MIFIM RP", "P-M2 MAGI RP", "CA-M2 MIFIM TP", "CA-M2 MAPI TP", "N-M2 MAGI ALT 1"
    ]

    # External API settings
    YPAERO_BASE_URL: str
    YPAERO_API_TOKEN: str

    class Config:
        # Load environment variables from a .env file located at the project root
        env_file = ".env"

# Instantiate the settings to be imported and used elsewhere
settings = Settings()
