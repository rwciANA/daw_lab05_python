from chessPictures import *
from interpreter import draw

blanco = square
negro = square.negative()


fila1 = blanco.join(negro).horizontalRepeat(4)
fila2 = fila1.negative()

def fila_con_piezas(fondo1, fondo2):
    return fondo1.overlay(rock) \
        .join(fondo2.overlay(knight)) \
        .join(fondo1.overlay(bishop)) \
        .join(fondo2.overlay(queen)) \
        .join(fondo1.overlay(king)) \
        .join(fondo2.overlay(bishop)) \
        .join(fondo1.overlay(knight)) \
        .join(fondo2.overlay(rock))

fila_piezas_blancas = fila_con_piezas(blanco, negro)
fila_piezas_negras = fila_piezas_blancas.negative()

def fila_peones(fondo1, fondo2, pieza):
    return fondo1.overlay(pieza) \
        .join(fondo2.overlay(pieza)) \
        .join(fondo1.overlay(pieza)) \
        .join(fondo2.overlay(pieza)) \
        .join(fondo1.overlay(pieza)) \
        .join(fondo2.overlay(pieza)) \
        .join(fondo1.overlay(pieza)) \
        .join(fondo2.overlay(pieza))

try:
    fila_peones_blancos = fila_peones(blanco, negro, pawn)
except:
    fila_peones_blancos = fila1

fila_peones_negros = fila_peones_blancos.negative()

# final tavlero
tablero = fila_piezas_negras \
    .under(fila_peones_negros) \
    .under(fila1) \
    .under(fila2) \
    .under(fila1) \
    .under(fila2) \
    .under(fila_peones_blancos) \
    .under(fila_piezas_blancas)

draw(tablero)