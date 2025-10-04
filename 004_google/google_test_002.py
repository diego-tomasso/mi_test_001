# google_test_002.py

# ----------------------------
# IMPORTS
# ----------------------------
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from pathlib import Path

# ----------------------------
# RUTA AL ARCHIVO DE CREDENCIALES
# ----------------------------
# Usamos Path para que sea multiplataforma
KEY_PATH = Path.home() / ".google-keys" / "bitacora-doc-app-b5d503f32903.json"

# ----------------------------
# SCOPES QUE VAMOS A USAR
# ----------------------------
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]

# ----------------------------
# ID DE LA CARPETA EN DRIVE
# ----------------------------
# Esta es la carpeta que compartiste con el service account
FOLDER_ID = "186DgvkFKhYyisHAzjDumNjL6Ic8zeOkF"

# ----------------------------
# TITULO DEL DOCUMENTO A CREAR
# ----------------------------
DOC_TITLE = "primer test"

# ----------------------------
# AUTENTICACIÓN CON LA KEY
# ----------------------------
creds = Credentials.from_service_account_file(filename=str(KEY_PATH), scopes=SCOPES)

# ----------------------------
# CONSTRUIMOS EL SERVICIO DE GOOGLE DRIVE
# ----------------------------
drive_service = build("drive", "v3", credentials=creds)

# ----------------------------
# CREAMOS UN NUEVO DOCUMENTO dE GOOGLE DOCS
# DENTRO DE LA CARPETA COMPARTIDA
# ----------------------------
file_metadata = {
    "name": DOC_TITLE,
    "mimeType": "application/vnd.google-apps.document",
    "parents": [FOLDER_ID],
}

new_file = drive_service.files().create(body=file_metadata, fields="id, name").execute()

# ----------------------------
# MOSTRAMOS RESULTADO
# ----------------------------
print(f"Documento creado: {new_file['name']}")
print(f"ID del documento: {new_file['id']}")
print(f"Link: https://docs.google.com/document/d/{new_file['id']}/edit")
