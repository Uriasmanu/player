import pyautogui
import time
from mpmath import mp

# Define a precisão para 100.000 casas decimaisaz
mp.dps = 100000  # Define a precisão em número de casas decimais
pi = str(mp.pi)[2:]  # Obtém π sem o "3." inicial

# Mapeamento de botões (1-8)
mapa_teclas = {
    '1': 'up', '2': 'down', '3': 'left', '4': 'right',
    '5': 'up', '6': 's', '7': 'z', '8': 'x','9': 'up', '0': 'down'
}

# Função para segurar teclas por 0.05s (pode ajustar)
def segurar_tecla(tecla, digito, duracao=0.8):
    pyautogui.keyDown(tecla)  # Pressiona a tecla
    time.sleep(duracao)       # Mantém pressionado por X segundos
    pyautogui.keyUp(tecla)    # Solta a tecla
    time.sleep(0.01)          # Pequeno intervalo entre ações
    print(f"Número: {digito} -> Tecla: {tecla}")  # Exibe apenas o número e a tecla

# Espera antes de começar (tempo para abrir o emulador)
time.sleep(5)

for digito in pi:
    if digito in mapa_teclas:
        tecla = mapa_teclas[digito]
        segurar_tecla(tecla, digito)
