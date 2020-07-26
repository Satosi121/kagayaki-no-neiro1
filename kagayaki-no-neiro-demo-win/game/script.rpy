

label start:

    stop music fadeout 1.0


    call _01forest


    call _02ruins
    call _03ruins


    call _04bedroom

    call demo_info
    return


label splashscreen:

    scene bg small_river
    show main_menu_title
    $ renpy.pause(7.0, hard=not config.debug)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
