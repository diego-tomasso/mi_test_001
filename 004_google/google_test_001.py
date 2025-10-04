from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from pathlib import Path

# Ruta a tus credenciales
json_path = Path.home() / ".google-keys" / "bitacora-doc-app-b5d503f32903.json"

# Scopes necesarios para Google Docs
SCOPES = ["https://www.googleapis.com/auth/documents"]

# Autenticación
creds = Credentials.from_service_account_file(str(json_path), scopes=SCOPES)
docs_service = build("docs", "v1", credentials=creds)

# Crear un nuevo documento
doc = (
    docs_service.documents()
    .create(
        body={
            "title": "primera prueba",
            "mimeType": "application/vnd.google-apps.document",
            "parents": ["186DgvkFKhYyisHAzjDumNjL6Ic8zeOkF"],
        }
    )
    .execute()
)
document_id = doc.get("documentId")

# Agregar contenido
requests = [
    {
        "insertText": {
            "location": {"index": 1},
            "text": "¡Hola, decime qué se siente? tener en casa a tu papá!\n",
        }
    }
]

docs_service.documents().batchUpdate(
    documentId=document_id, body={"requests": requests}
).execute()

print(f"Documento creado: https://docs.google.com/document/d/{document_id}/edit")
