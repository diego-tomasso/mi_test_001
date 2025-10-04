from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Ruta al archivo JSON con tus credenciales
SERVICE_ACCOUNT_FILE = "/home/diego/.google-keys/bitacora-doc-app-b5d503f32903.json"

# Definimos los permisos necesarios para Google Docs
SCOPES = ["https://www.googleapis.com/auth/documents"]

# ID del documento que vos creaste a mano
DOCUMENT_ID = "1raF87fvWlR8k80nI8suNdmgZVPfNQJljtiYc36pncd0"

# Autenticamos con la cuenta de servicio
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Creamos el cliente de la API de Google Docs
docs_service = build("docs", "v1", credentials=creds)

# Obtenemos el contenido del documento para saber su longitud
doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()
end_index = doc["body"]["content"][-1]["endIndex"]  # indice final

# Armamos el texto a insertar
texto = input("Ingresa el texto a agregar al final del doc: ")

# Insertamos texto al final
requests = [
    {
        "insertText": {
            "location": {
                # antes del último carácter (usualmente un salto de línea)
                "index": end_index
                - 1
            },
            "text": texto + "\n",
        }
    }
]

# Ejecutamos la modificación
docs_service.documents().batchUpdate(
    documentId=DOCUMENT_ID, body={"requests": requests}
).execute()

print("Texto agregado correctamente al documento.")
