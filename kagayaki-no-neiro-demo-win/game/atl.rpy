

transform right1:
    pos (0.9, 1.0)

transform left1:
    pos (0.1, 1.0)

transform right2:
    pos (0.8, 1.0)

transform left2:
    pos (0.2, 1.0)

transform right3:
    pos (0.7, 1.0)

transform left3:
    pos (0.3, 1.0)

transform right4:
    pos (0.6, 1.0)

transform left4:
    pos (0.4, 1.0)


transform shaking(trans):
    trans
    choice:
        xoffset 2
    choice:
        xoffset -2
    pause 0.02
    repeat

transform darken(name, d=0.2):
    im.MatrixColor(name, im.matrix.brightness(-d))

transform zawarudo(name):
    im.MatrixColor(name, im.matrix.invert())
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
