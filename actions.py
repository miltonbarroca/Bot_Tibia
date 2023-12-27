import pyautogui as pg
import constants

def hole_down(should_down):
    if should_down:
        box = pg.locateOnScreen('imgs/hole_down.png', confidence=0.8)
        if box:
            x, y = pg.center(box)
            pg.moveTo(x,y)
            pg.click()
            pg.sleep(5)

def hole_up(img_anchor, plus_x,plus_y):
    box = pg.locateOnScreen(img_anchor, confidence=0.8)
    if box:
        x,y = pg.center(box)
        pg.moveTo(x + plus_x,y + plus_y, 1) 
        pg.press('F4')
        pg.click()

def check_battle():
    try:
        # Tente localizar a imagem
        result = pg.locateOnScreen('imgs/region_battle.PNG', region=constants.REGION_BATTLE)
        return result  # Retorna a posição da imagem se for encontrada
    except pg.ImageNotFoundException:
        # Se a exceção for lançada, a imagem não foi encontrada
        print("Imagem não encontrada.")
        return None