from chessPictures import *
from interpreter import draw

blanco = square
negro = square.negative()

def poner(fondo, pieza):
    return fondo.overlay(pieza)

# ===== FILA 8 =====
fila8 = poner(blanco, rock.negative()) \
    .join(poner(negro, knight.negative())) \
    .join(poner(blanco, bishop.negative())) \
    .join(poner(negro, queen.negative())) \
    .join(poner(blanco, king.negative())) \
    .join(poner(negro, bishop.negative())) \
    .join(poner(blanco, knight.negative())) \
    .join(poner(negro, rock.negative()))

# ===== FILA 7 =====
fila7 = poner(negro, pawn.negative()) \
    .join(poner(blanco, pawn.negative())) \
    .join(poner(negro, pawn.negative())) \
    .join(poner(blanco, pawn.negative())) \
    .join(blanco) \
    .join(poner(blanco, pawn.negative())) \
    .join(poner(negro, pawn.negative())) \
    .join(poner(blanco, pawn.negative()))

# ===== FILA 6 (caballo en c6) =====
fila6 = blanco \
    .join(negro) \
    .join(poner(blanco, knight.negative())) \
    .join(negro) \
    .join(poner(blanco, pawn.negative())) \
    .join(negro) \
    .join(blanco) \
    .join(negro)

# ===== FILA 5 (peón en e5) =====
fila5 = negro.join(blanco).join(negro).join(blanco) \
    .join(poner(negro, pawn.negative())) \
    .join(blanco).join(negro).join(blanco)

# ===== FILA 4 (peones en d4 y e4) =====
fila4 = blanco.join(negro) \
    .join(blanco) \
    .join(poner(negro, pawn)) \
    .join(poner(blanco, pawn)) \
    .join(negro).join(blanco).join(negro)

# ===== FILA 3 (caballo en f3) =====
fila3 = negro.join(blanco).join(negro).join(blanco) \
    .join(negro) \
    .join(poner(blanco, knight)) \
    .join(negro).join(blanco)

# ===== FILA 2 (peones blancos, d2 vacío) =====
fila2_p = poner(blanco, pawn) \
    .join(poner(negro, pawn)) \
    .join(poner(blanco, pawn)) \
    .join(negro) \
    .join(negro) \
    .join(poner(negro, pawn)) \
    .join(poner(blanco, pawn)) \
    .join(poner(negro, pawn))

# ===== FILA 1 =====
fila1_p = poner(negro, rock) \
    .join(poner(blanco, knight)) \
    .join(poner(negro, bishop)) \
    .join(poner(blanco, queen)) \
    .join(poner(negro, king)) \
    .join(poner(blanco, bishop)) \
    .join(blanco) \
    .join(poner(blanco, rock))

# ===== TABLERO =====
tablero = fila8 \
    .under(fila7) \
    .under(fila6) \
    .under(fila5) \
    .under(fila4) \
    .under(fila3) \
    .under(fila2_p) \
    .under(fila1_p)

draw(tablero)