from interpreter import draw
from chessPictures import *

draw(rock.join(knight.AddBackground()).join(bishop).join(queen.AddBackground()).join(king).join(bishop.AddBackground()).join(knight).join(rock.AddBackground()).negative().AddBackground()
     .under(pawn.AddBackground().join(pawn).negative().AddBackground().horizontalRepeat(4))
     .under(square.join(square.negative()).horizontalRepeat(4)
            .under(square.join(square.negative()).horizontalRepeat(4).verticalMirror()).verticalRepeat(2))
            .under(pawn.join(pawn.negative().AddBackground().negative()).AddBackground().horizontalRepeat(4))
            .under(rock.negative().AddBackground().negative().join(knight).join(bishop.negative().AddBackground().negative()).join(queen).join(king.negative().AddBackground().negative()).join(bishop).join(knight.AddBackground()).join(rock).AddBackground()))