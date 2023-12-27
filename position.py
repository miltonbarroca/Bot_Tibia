import pyautogui

# Aguarde alguns segundos para posicionar o cursor
pyautogui.confirm("Posicione o cursor na extremidade superior esquerda e pressione OK.")

# Obtenha as coordenadas (x, y) do cursor
x1, y1 = pyautogui.position()

# Aguarde novamente para posicionar o cursor na extremidade inferior direita
pyautogui.confirm("Posicione o cursor na extremidade inferior direita e pressione OK.")

# Obtenha as coordenadas (x, y) do cursor novamente
x2, y2 = pyautogui.position()

# Calcule as dimensões (width, height)
width = x2 - x1
height = y2 - y1

print(f"Coordenadas (x, y): ({x1}, {y1})")
print(f"Dimensões (width, height): ({width}, {height})")
