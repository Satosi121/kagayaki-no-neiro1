

define ku = Character(_("Kulumu"), color='#ffffff')
define ku2 = Character(_("Kulumu"), color='#ffffff', what_prefix=_('('), what_suffix=_(')'))
define ae = Character(_("???"), color='#ffffff')
define ru = Character(_("Ruby"), color='#ffffff')
define na = Character(None)
define nv = nvl_narrator

init python:
    city_channels = ['city_quiet', 'city_calm', 'city_per']
    renpy.music.register_channel('city_quiet', 'music', True, file_prefix='music/bgm-city-quiet', file_suffix='.ogg')
    renpy.music.register_channel('city_calm', 'music', True, file_prefix='music/bgm-city-calm', file_suffix='.ogg')
    renpy.music.register_channel('city_per', 'music', True, file_prefix='music/bgm-city-per', file_suffix='.ogg')
    renpy.music.register_channel('ocarina', 'music', True, file_prefix='music/flute', file_suffix='.ogg')

label update_volume(chan, vol, delay):
    $ renpy.music.set_volume(vol, delay, chan)
    return

label city_volume(single_chan=None, vol=1.0, delay=0):
    python:
        for c in city_channels:
            if c == single_chan or single_chan is None:
                renpy.music.set_volume(vol, delay, c)
            else:
                renpy.music.set_volume(0.0, delay, c)
    return

label city_toggle(chan, delay=1.0):
    call city_volume (chan, 1.0, delay)
    return

label city_volume_mute(delay=0):
    call city_volume (None, 0.0, delay)
    return

label play_city(single_chan=None):
    call city_volume (single_chan, 1.0, 0)
    play city_quiet ''
    play city_calm ''
    play city_per ''
    return

label stop_city():
    stop city_quiet
    stop city_calm
    stop city_per
    return


define audio.run1 = '<from 0 to 3.0>sfx/running1.ogg'
define audio.run2 = '<from 0 to 4.0>sfx/running2.ogg'
define audio.thud = 'sfx/thud.ogg'
define audio.swing_first = 'sfx/first-swing.ogg'
define audio.swing_several = 'sfx/several-swings.ogg'
define audio.swing_last = 'sfx/last-swing.ogg'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
