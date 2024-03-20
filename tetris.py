from settings import *
from tetromino import Tetromino
import math

class Tetris:
    def __init__(self, app):
        self.app = app
        self.tetromino = Tetromino(self)


    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),1)
    def update(self):
        self.tetromino.update()

    def draw(self):
        self.draw_grid()