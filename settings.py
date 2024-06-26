import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)

ANIM_TIME_INTERVAL = 150 #miliseconds

TILE_SIZE = 50
FIELD_SIZE = FIELD_W , FIELD_H = 10 , 15
"""
oznacza to samo co:
FIELD_W = 10
FIELD_H = 20
FIELD_SIZE = (FIELD_W, FIELD_H) - krotka
"""
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

"""
FIELD_RES_X = FIELD_W * TILE_SIZE
FIELD_RES_Y = FIELD_H * TILE_SIZE
FIELD_RES = (FIELD_RES_X, FIELD_RES_Y)
"""
INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}