import pyautogui
import time
import os
from mpmath import mp

# Define a precisão para 100.000 casas decimais
mp.dps = 100000  # Define a precisão em número de casas decimais
pi = str(mp.pi)[2:]  # Obtém π sem o "3." inicial

# Mapeamento de botões (1-8)
mapa_teclas = {
    '1': 'up', '2': 'down', '3': 'left', '4': 'right',
    '5': 'up', '6': 's', '7': 'z', '8': 'x', '9': 'up', '0': 'down'
}

# Caminho do arquivo que armazena o progresso
PROGRESSO_FILE = "progresso.txt"

# Função para ler o progresso salvo
def carregar_progresso():
    if os.path.exists(PROGRESSO_FILE):
        with open(PROGRESSO_FILE, "r") as f:
            try:
                return int(f.read().strip())  # Lê e converte para inteiro
            except ValueError:
                return 0  # Se houver erro ao ler, começa do zero
    return 0  # Se o arquivo não existir, começa do zero

# Função para salvar o progresso
def salvar_progresso(indice):
    with open(PROGRESSO_FILE, "w") as f:
        f.write(str(indice))  # Salva o índice atual

# Função para segurar teclas por 0.8s (pode ajustar)
def segurar_tecla(tecla, digito, duracao=0.8):
    pyautogui.keyDown(tecla)  # Pressiona a tecla
    time.sleep(duracao)       # Mantém pressionado por X segundos
    pyautogui.keyUp(tecla)    # Solta a tecla
    time.sleep(0.01)          # Pequeno intervalo entre ações
    print(f"Número: {digito} -> Tecla: {tecla}")  # Exibe apenas o número e a tecla

# Lê o último ponto salvo
indice_inicio = carregar_progresso()

# Espera antes de começar (tempo para abrir o emulador)
time.sleep(5)

# Continua de onde parou
for i in range(indice_inicio, len(pi)):
    digito = pi[i]
    if digito in mapa_teclas:
        tecla = mapa_teclas[digito]
        segurar_tecla(tecla, digito)
    
    # Salva o progresso a cada iteração
    salvar_progresso(i + 1)
