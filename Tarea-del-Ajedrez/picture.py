from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(self.img[::-1])

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for line in self.img:
      new_line = ''
      for c in line:
        new_line += self._invColor(c)
      negative.append(new_line)
    
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joined = []
    for i in range(len(self.img)):
      joined.append(self.img[i] + p.img[i])
    return Picture(joined)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p encima de la
        figura actual """
    return Picture(p.img + self.img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p debajo de la
        figura actual """
    return Picture(self.img + p.img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    hrepeat = []
    for i in range(len(self.img)):
      hrepeat.append(self.img[i] * n)
    return Picture(hrepeat)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual debajo
        la cantidad de veces que indique el valor de n """
    return Picture(self.img * n)
  
  def AddBackground(self):
    """Agrega fondo color LIGHTGRAY a las piezas de ajedrez"""
    backgrounded = []
    for line in self.img:
      backgrounded.append(line.replace(" ","_"))
    
    return Picture(backgrounded)
  
  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotated = []
    for i in range(len(self.img[0])):
      line = ''
      for j in reversed(range(len(self.img))):
        line += self.img[j][i]
      rotated.append(line)

