import pyautogui as pg
import actions
import constants
import time
import json
from pynput.keyboard import Listener
from pynput import keyboard
import threading





def kill_monster():
    while actions.check_battle() is None:
        print('matando monstros')
        if event_th.is_set():
            return
        is_battle = pg.locateOnScreen('imgs/region_battle.PNG', confidence=0.4, region=constants.REGION_BATTLE)
        if is_battle is None:
            print('Imagem não encontrada. Pressionando a tecla space...')
            pg.press('space')
            try:
                while pg.locateOnScreen('imgs/red_target.png', confidence=0.4, region=constants.REGION_BATTLE) is not None:
                    if event_th.is_set():
                        return
                    print('esperando o monstro morrer')
                    pg.sleep(1)
            except pg.ImageNotFoundException:
                print('target não encontrada. Procurando outro monstro...')
        else:
            print('Imagem encontrada:', is_battle)

        # Adicione um pequeno atraso entre as iterações para evitar consumo excessivo de recursos
        pg.sleep(1)




def get_loot():
    # Lista de coordenadas (x, y)
    coordinates = [(866, 372), (959, 370), (947, 449), (958, 531), (868, 529),
                   (790, 530), (796, 452), (787, 374)]

    # Itera sobre as coordenadas e clica com o botão direito
    for coord in coordinates:
        x, y = coord
        pg.click(x, y, button='right')
        time.sleep(0.5)  # Aguarda meio segundo entre cliques (pode ajustar conforme necessário)

def go_to_flag(path, wait):
    flag = pg.locateOnScreen(path, confidence=0.7, region=constants.REGION_MAP)
    if flag:
        x, y=pg.center(flag)
        if event_th.is_set():
            return
        pg.moveTo(x, y)
        pg.click()
        pg.sleep(wait)

def check_player_position():
    return pg.locateOnScreen('imgs/point_player.png', confidence=0.8, region=constants.REGION_MAP)

def run():
    event_th.is_set()
    with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    for item in data:
        if event_th.is_set():
            return
        kill_monster()
        if event_th.is_set():
            return
        pg.sleep(1)
        get_loot()
        if event_th.is_set():
            return
        go_to_flag(item['path'], item['wait'])
        if event_th.is_set():
            return
        if check_player_position():
            kill_monster()
            if event_th.is_set():
                return
            pg.sleep(1)
            get_loot()
            if event_th.is_set():
                return
            go_to_flag(item['path'],item['wait'])
        actions.hole_down(item['down_hole'])
        if event_th.is_set():
            return
        actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.png', 440, 0 )
        actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_3.png', 130, 130)




def key_code(key):
    print('Key ->', key)
    if key == keyboard.Key.esc:
        event_th.set()
        return False
    if key == keyboard.Key.delete:
        th_run.start()

global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)


with Listener(on_press=key_code) as listener:
    listener.join()






