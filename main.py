import pyautogui as pg
import keyboard

REGION_BATTLE = (1746,440,158,73)


def check_battle():
    try:
        location = pg.locateOnScreen('imgs/region_battle.png', region=REGION_BATTLE)
        print(location)
    except pg.ImageNotFoundException:
        return None

def kill_monster():    
    while True:
        keyboard.wait('h')
        is_battle = check_battle()
        if is_battle is None:
            print('entrei aqui')
            pg.press('space')
            while pg.locateOnScreen('imgs/red_target.png', confidence=0.7, region=REGION_BATTLE) is not None:
                print('esperando o monstro morrer')
            print('procurando outro monstro')
        print(is_battle)

kill_monster()