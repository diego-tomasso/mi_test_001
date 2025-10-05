from io import BytesIO
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload

from usuario import Usuario
from persistencia_pickle import leer_usuarios, guardar_usuarios

# === Configuración
CREDENTIALS_PATH = "/home/diego/.google-keys/bitacora-doc-app-b5d503f32903.json"
FILE_ID = "1DISOmid_-jkRhlQv3U1o3AB2GYmFD8Y4"

# === Autenticación con la API de Drive
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH, scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=creds)

# === 1. Descargar archivo desde Drive a un buffer en memoria
buffer = BytesIO()
request = drive_service.files().get_media(fileId=FILE_ID)
downloader = MediaIoBaseDownload(buffer, request)

done = False
while not done:
    _, done = downloader.next_chunk()

buffer.seek(0)  # volvemos al inicio del buffer

# === 2. Leer lista de usuarios
try:
    usuarios = leer_usuarios(buffer)
except EOFError:
    usuarios = []

print(f"Usuarios cargados: {len(usuarios)}")

# === 3. Crear un nuevo usuario
nuevo_usuario = Usuario(
    nombre="Testeo Pickle", id=999, telefono="12345678", mail="test@ejemplo.com"
)
usuarios.append(nuevo_usuario)
print(f"Usuario agregado: {nuevo_usuario}")

# === 4. Serializar nuevamente a un nuevo buffer
nuevo_buffer = BytesIO()
guardar_usuarios(usuarios, nuevo_buffer)
nuevo_buffer.seek(0)

# === 5. Subir el buffer a Drive sobre el mismo archivo
media = MediaIoBaseUpload(
    nuevo_buffer, mimetype="application/octet-stream", resumable=True
)

update = drive_service.files().update(fileId=FILE_ID, media_body=media).execute()

print("Archivo actualizado en Drive.")
