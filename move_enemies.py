## l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## a = list(map(lambda x: [x[0], x[1] + 5, x[1]], l))
## a.assert.equals([[1, 7, 2], [4, 10, 5], [7, 13, 8]])
from pygame import Rect

def move_enemies(enemies: list, current_position, enemy_direcction):
    new_enemies_list = []
    new_enemies_list = list(map(lambda x: Rect(x.left + enemy_direcction, x.top, x.width, x.height), enemies))
    # print (new_enemies_list)
    return new_enemies_list

def move_enemies_down(enemies: list):
    new_enemies_list = []
    new_enemies_list = list(map(lambda x: Rect(x.left, x.top+1, x.width, x.height), enemies))
    # print (new_enemies_list)
    return new_enemies_list