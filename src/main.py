from azure_service import recognize_text_from_image
from utils import validar_caminho_imagem, formatar_texto_extraido, exibir_banner

def main():
    image_path = "assets/example_image.jpg"

    exibir_banner()
    validar_caminho_imagem(image_path)

    texto = recognize_text_from_image(image_path)
    texto_formatado = formatar_texto_extraido(texto)

    print("\nTexto extraído:")
    print(texto_formatado)

if __name__ == "__main__":
    main()
