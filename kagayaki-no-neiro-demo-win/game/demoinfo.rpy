

define tu = Character(_(' Tumeo '), color='#3b1066')
define tunv = Character(_('Tumeo'), kind=nvl, color='#3b1066')
define jo = Character(_('Jordi'), kind=nvl, color='#fff')
define ha = Character(_('Hajime'), kind=nvl, color='#fff')
define an = Character(_('Yomieda'), color='#fff')

label demo_info:

    scene bg small_river darken with fade

    tu "Hi, I'm William Tumeo the programmer. This is the end of the demo. Thanks for playing!"
    an "Hi! this is the artist. Thank you so much for playing our game!"
    an "The original script ended up being huge, so we didn't manage to put it all up in time for Nanoreno2018. We will keep working on it, though!"
    nvl clear
    nv "I'd like to give some special thanks to:" with dissolve
    ha "for all the hard work and overall for just being who he is."
    jo "for being the real MVP and saving us with the soundtrack at the last minute."
    nv "And last, but not least:"
    tunv "for bearing with my art nitpicking throughout the whole thing."
    nvl clear
    with dissolve
    menu:
        "Back to Title Screen":
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
