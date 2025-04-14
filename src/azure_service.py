from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

# 🔐 Suas credenciais do Azure
API_KEY = "SUA_CHAVE_AQUI"
ENDPOINT = "SUA_URL_DO_ENDPOINT"

# Cria o cliente de Computer Vision
client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

def recognize_text_from_image(image_path):
    with open(image_path, "rb") as image_stream:
        read_response = client.read_in_stream(image_stream, raw=True)

    # Recupera o ID da operação
    operation_location = read_response.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]

    # Aguarda o processamento assíncrono
    while True:
        result = client.get_read_result(operation_id)
        if result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Extrai o texto
    if result.status == OperationStatusCodes.succeeded:
        text = ""
        for page in result.analyze_result.read_results:
            for line in page.lines:
                text += line.text + "\n"
        return text
    else:
        return "Erro ao processar a imagem."
