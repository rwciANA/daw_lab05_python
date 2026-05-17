from chessPictures import *
from interpreter import draw

cuadro1=square
cuadro2=square.join(cuadro1.negative())
cuadro3=square.join(cuadro2.negative())
cuadro4= square.join(cuadro3.negative())

cuadro5=square.join(cuadro4.negative())

cuadro6=square.join(cuadro5.negative())
cuadro7=square.join(cuadro6.negative())
cuadro8=square.join(cuadro7.negative())
draw(cuadro8)














