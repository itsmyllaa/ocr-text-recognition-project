import os

def validar_caminho_imagem(caminho):
    """Verifica se o arquivo da imagem existe."""
    if not os.path.isfile(caminho):
        raise FileNotFoundError(f"Imagem não encontrada: {caminho}")
    return True

def formatar_texto_extraido(texto):
    """Limpa e organiza o texto extraído."""
    linhas = texto.split('\n')
    linhas_limpa = [linha.strip() for linha in linhas if linha.strip()]
    return '\n'.join(linhas_limpa)

def exibir_banner():
    """Só pra deixar o terminal mais bonito 💅"""
    print("="*40)
    print("     🔍 OCR COM AZURE - RECONHECIMENTO DE TEXTO")
    print("="*40)
