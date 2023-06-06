from interpreter import draw
from chessPictures import *

draw(square.join(square.negative()).horizontalRepeat(4).under(square.join(square.negative()).horizontalRepeat(4).verticalMirror()).verticalRepeat(2))