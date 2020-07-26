













define config.name = _("Kagayaki no Neiro")




define gui.show_name = False
define config.default_fullscreen = True



define config.version = "demo"





define gui.about = _p("""Demo version

This demo was made during the NaNoRenO 2018.

Credits:

- Music: {a=https://www.youtube.com/user/happy30}Happy30{/a}

- Story: Hajime Suzuki

- Art and Translation: {a=https://twitter.com/yomieda}Ana Yomieda{/a}

- Programming: {a=http://tumeo.space/}William Tumeo{/a}

Sponsored by Ana Yomieda and Novastrike Media.
""")






define build.name = "kagayaki-no-neiro"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5




define config.sample_sound = 'sfx/several-swings.ogg'







define config.main_menu_music = "music/bgm.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.end_splash_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 24





default preferences.afm_time = 15
















define config.save_directory = "kagayaki-no-neiro-demo"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**.import', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpym', None)
    build.classify('addons/', None)
    build.classify('devel/', None)
    build.classify('**.godot', None)
    build.classify('icon.png', None)


    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.rpymc", "scripts")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.ogg", "audio")
    build.classify("game/gui/fonts/**", "fonts")




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
