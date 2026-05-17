from colors import *

class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    return Picture([fila[::-1] for fila in self.img])

  def horizontalMirror(self):
    return Picture(self.img[::-1])

  def negative(self):
    nueva = []
    for fila in self.img:
      nueva.append("".join(self._invColor(c) for c in fila))
    return Picture(nueva)

  def join(self, p):
    nueva = []
    for i in range(len(self.img)):
      nueva.append(self.img[i] + p.img[i])
    return Picture(nueva)
  
  

  def up(self, p):
    return Picture(p.img + self.img)

  def under(self, p):
    return Picture(self.img + p.img)

  def horizontalRepeat(self, n):
    res = self
    for _ in range(n - 1):
      res = res.join(self)
    return res

  def verticalRepeat(self, n):
    res = self
    for _ in range(n - 1):
      res = res.under(self)
    return res

  def rotate(self):
    nueva = []
    for i in range(len(self.img[0])):
      fila = ""
      for j in range(len(self.img)-1, -1, -1):
        fila += self.img[j][i]
      nueva.append(fila)
    return Picture(nueva)
  def overlay(self, p):
    nueva = []
    for i in range(len(self.img)):
        fila = ""
        for j in range(len(self.img[i])):
            if p.img[i][j] == " ":
                fila += self.img[i][j]
            else:
                fila += p.img[i][j]
        nueva.append(fila)
    return Picture(nueva)