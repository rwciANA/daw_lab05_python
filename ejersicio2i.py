from chessPictures import *
from interpreter import draw

blanco = square
negro = square.negative()

fila1 = blanco.join(negro).horizontalRepeat(4)
fila2 = fila1.negative()

def poner(fondo, pieza):
    return fondo.overlay(pieza)


fila8 = poner(blanco, rock.negative()) \
    .join(poner(negro, knight.negative())) \
    .join(poner(blanco, bishop.negative())) \
    .join(poner(negro, queen.negative())) \
    .join(poner(blanco, king.negative())) \
    .join(poner(negro, bishop.negative())) \
    .join(poner(blanco, knight.negative())) \
    .join(poner(negro, rock.negative()))


fila7 = poner(negro, pawn.negative()) \
    .join(poner(blanco, pawn.negative())) \
    .join(poner(negro, pawn.negative())) \
    .join(poner(blanco, pawn.negative())) \
    .join(blanco) \
    .join(poner(blanco, pawn.negative())) \
    .join(poner(negro, pawn.negative())) \
    .join(poner(blanco, pawn.negative()))


fila6 = blanco \
    .join(negro) \
    .join(poner(blanco, knight.negative())) \
    .join(negro) \
    .join(poner(blanco, pawn.negative())) \
    .join(negro) \
    .join(blanco) \
    .join(negro)


fila5 = negro.join(blanco).join(negro).join(blanco) \
    .join(poner(negro, pawn.negative())) \
    .join(blanco).join(negro).join(blanco)


fila4 = blanco.join(negro) \
    .join(poner(blanco, bishop)) \
    .join(negro) \
    .join(poner(blanco, pawn)) \
    .join(negro).join(blanco).join(negro)

fila3 = negro.join(blanco).join(negro).join(blanco) \
    .join(negro) \
    .join(poner(blanco, knight)) \
    .join(negro).join(blanco)


fila2_p = poner(blanco, pawn) \
    .join(poner(negro, pawn)) \
    .join(poner(blanco, pawn)) \
    .join(poner(negro, pawn)) \
    .join(negro) \
    .join(poner(negro, pawn)) \
    .join(poner(blanco, pawn)) \
    .join(poner(negro, pawn))


fila1_p = poner(negro, rock) \
    .join(poner(blanco, knight)) \
    .join(poner(negro, bishop)) \
    .join(poner(blanco, queen)) \
    .join(poner(negro, king)) \
    .join(blanco) \
    .join(blanco) \
    .join(poner(blanco, rock))

tablero = fila8 \
    .under(fila7) \
    .under(fila6) \
    .under(fila5) \
    .under(fila4) \
    .under(fila3) \
    .under(fila2_p) \
    .under(fila1_p)

draw(tablero)