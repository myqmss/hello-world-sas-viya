import saspy
import requests

# Conectar a SAS Viya
sas = saspy.SASsession(cfgname='viya')

# Nombre del archivo a subir
file_name = 'hello_world.py'

# Abrir el archivo en modo lectura binaria
with open(file_name, 'rb') as f:
    # Construir los datos para la solicitud POST
    files = {'file': (file_name, f, 'application/octet-stream')}
    
    # URL para subir el archivo a SAS Viya
    upload_url = 'https://azureuse011282.my-trials.sas.com/SASDrive/cas-shared-default-http/casProxy/upload'

    # Realizar la solicitud POST con autenticación básica
    response = requests.post(
        upload_url,
        files=files,
        auth=('mario.sanchez@myqorg.biz', 'L@contra01')
    )

# Verificar el estado de la respuesta
if response.status_code == 200:
    print(f"Script '{file_name}' subido exitosamente a SAS Viya en Azure.")
else:
    print(f"Error al subir el script '{file_name}' a SAS Viya. Código de estado: {response.status_code}")