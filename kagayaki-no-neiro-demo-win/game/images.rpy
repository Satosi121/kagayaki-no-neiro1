


transform _ku:
    align (0.5, 1.0)
image ku:
    'kulumu/kulumu-idle.png'
    _ku
image ku darken:
    darken('kulumu/kulumu-idle.png')
    _ku
image ku zawarudo:
    zawarudo('kulumu/kulumu-surprised2.png')
    _ku

transform _ku_nsei:
    anchor (0.6, 1.0)
    pos (0.5, 1.0)
image ku nsei:
    'kulumu/kulumu-nsei2.png'
    _ku_nsei
image ku nsei darken:
    darken('kulumu/kulumu-nsei2.png')
    _ku_nsei

transform _ku_openm:
    anchor (0.426, 1.0)
    pos (0.5, 1.0)
image ku openm:
    'kulumu/kulumu-caradeemoji2.png'
    _ku_openm
image ku openm darken:
    darken('kulumu/kulumu-caradeemoji2.png')
    _ku_openm

transform _ku_surprised1:
    anchor (0.42, 1.0)
    pos (0.5, 1.0)
image ku surprised1:
    'kulumu/kulumu-surprised2.png'
    _ku_surprised1
image ku surprised1 darken:
    darken('kulumu/kulumu-surprised2.png')
    _ku_surprised1

transform _ku_hazu:
    anchor (0.426, 1.0)
    pos (0.5, 1.0)
image ku hazu:
    'kulumu/kulumu-hazukashii2.png'
    _ku_hazu
image ku hazu darken:
    darken('kulumu/kulumu-hazukashii2.png')
    _ku_hazu


transform _ku_idle:
    anchor (0.5, 1.0)
    pos (0.5, 1.0)
image ku idle:
    'kulumu/kulumu-idle2.png'
    _ku_idle
image ku idle darken:
    darken('kulumu/kulumu-idle2.png')
    _ku_idle

transform _ku_thonk:
    anchor (0.5, 1.0)
    pos (0.5, 1.0)
image ku thonk:
    'kulumu/reallymakesuthink.png'
    _ku_thonk
image ku thonk darken:
    darken('kulumu/reallymakesuthink.png')
    _ku_thonk

transform _ku_tired:
    anchor (0.5, 1.0)
    pos (0.5, 1.0)
image ku tired:
    'kulumu/ku-tired.png'
    _ku_tired
image ku tired darken:
    darken('kulumu/ku-tired.png')
    _ku_tired

transform _ku_isleep:
    anchor (0.5, 1.0)
    pos (0.5, 1.0)
image ku isleep:
    'kulumu/kulumu-cansado1.png'
    _ku_isleep
image ku isleep darken:
    darken('kulumu/kulumu-cansado1.png')
    _ku_isleep



transform _ae:
    align (0.5, 1.0)
image ae:
    'ifr/ifr-idle.png'
    _ae
image ae darken:
    darken('ifr/ifr-idle.png')
    _ae
image ae black:
    darken('ifr/ifr-idle.png', 1.0)
    _ae

transform _ae_odoroi:
    anchor (0.35, 1.0)
    pos (0.5, 1.0)
image ae odoroi:
    'ifr/ifr-odoroita.png'
    _ae_odoroi
image ae odoroi darken:
    darken('ifr/ifr-odoroita.png')
    _ae_odoroi

transform _ae_stance:
    anchor (0.68, 1.0)
    pos (0.5, 1.0)
image ae stance:
    'ifr/ifr-stance.png'
    _ae_stance
image ae stance darken:
    darken('ifr/ifr-stance.png')
    _ae_stance

transform _ae_attack:
    anchor (0.7, 1.0)
    pos (0.5, 1.0)
image ae attack:
    'ifr/ifr-attack.png'
    _ae_attack

transform _ae_ears:
    align (0.5, 1.0)
image ae ears:
    'ifr/cover-ears.png'
    _ae_ears
image ae ears darken:
    darken('ifr/cover-ears.png')
    _ae_ears

transform _ae_hurt:
    align (0.5, 1.0)
image ae hurt:
    'ifr/ifr-hurt.png'
    _ae_hurt
image ae hurt darken:
    darken('ifr/ifr-hurt.png')
    _ae_hurt



image main_menu_title:
    anchor (1.0, 1.0)
    pos (1280-40, 720-40)
    "vfx/title-1.png"
    pause 2.0
    "vfx/title-2.png" with Dissolve(2.0, alpha=True)
    pause 3.0
    "vfx/title-1.png" with Dissolve(2.0, alpha=True)

image c_dark = '#0005'
image c_black = '#000'
image c_white = '#fff'
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define za_warudo = ImageDissolve("vfx/zawarudo.png", 0.6)


image bg death_forest = 'bg/death-forest.png'
image bg death_forest darken:
    darken('bg/death-forest.png')
image bg haikyo = 'bg/haikyo.png'
image bg haikyo darken:
    darken('bg/haikyo.png')
image bg haikyo zawarudo:
    zawarudo('bg/haikyo.png')

image bg bedroom = 'bg/abandoned-bedroom.png'
image bg bedroom darken:
    darken('bg/abandoned-bedroom.png', 0.1)

image bg small_river = 'bg/small-river.png'
image bg small_river darken:
    darken('bg/small-river.png', 0.1)

image bg val_tree = 'bg/vallouro-tree.png'


image cg ruins = 'cg/cg-bons.png'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
