from chessPictures import *
from interpreter import draw

fila1 = knight.join(knight.negative())
fila2 = knight.negative().join(knight)

tablero = fila1.up(fila2)

draw(tablero)