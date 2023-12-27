import pyautogui as pg
import keyboard
import actions
import constants
import time
import json





def kill_monster():
    while actions.check_battle() is None:
        print('matando monstros')
        is_battle = pg.locateOnScreen('imgs/red_target.png', confidence=0.4, region=constants.REGION_BATTLE)
        if is_battle is None:
            print('Imagem não encontrada. Pressionando a tecla space...')
            pg.press('space')
            try:
                while pg.locateOnScreen('imgs/red_target.png', confidence=0.4, region=constants.REGION_BATTLE) is not None:
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
    x, y=pg.center(flag)
    pg.moveTo(x, y)
    pg.click()

def check_player_position():
    return pg.locateOnScreen('imgs/point_player.png', confidence=0.8, region=constants.REGION_MAP)

def run():
    with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    for item in data:
        kill_monster()
        get_loot()
        go_to_flag(item['path'], item['wait'])
        if check_player_position():
            kill_monster()
            get_loot()
            go_to_flag(item['path'],item['wait'])
        actions.hole_down(item['down_hole'])
        actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.png', 440, 0 )
        actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_3.png', 130, 130)





