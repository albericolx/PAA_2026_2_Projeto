import os
import subprocess

def gerar_pdf():
    diretorio = os.path.dirname(os.path.abspath(__file__))
    arquivo_html = os.path.join(diretorio, "artigo_sbc_template.html")
    arquivo_pdf = os.path.join(diretorio, "artigo_sbc_tema6_motoboy.pdf")
    
    # Caminhos comuns do Microsoft Edge e Google Chrome no Windows
    caminhos_navegadores = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    
    navegador_encontrado = None
    for cam in caminhos_navegadores:
        if os.path.exists(cam):
            navegador_encontrado = cam
            break
            
    if not navegador_encontrado:
        print("Navegador Edge/Chrome não encontrado nos caminhos padrão.")
        return False
        
    print(f"Utilizando: {navegador_encontrado}")
    print(f"Gerando PDF a partir de: {arquivo_html}")
    
    cmd = [
        navegador_encontrado,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={arquivo_pdf}",
        "--no-pdf-header-footer",
        arquivo_html
    ]
    
    try:
        resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if os.path.exists(arquivo_pdf):
            print(f"SUCESSO! PDF oficial gerado em: {arquivo_pdf}")
            return True
        else:
            print("Falha ao gerar o arquivo PDF.")
            return False
    except Exception as e:
        print(f"Erro ao executar: {e}")
        return False

if __name__ == "__main__":
    gerar_pdf()
