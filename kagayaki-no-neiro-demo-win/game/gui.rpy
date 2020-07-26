









init -2 python:
    gui.init(1280, 720)













define -2 gui.accent_color = '#65beb7'


define -2 gui.idle_color = '#888888'



define -2 gui.idle_small_color = '#aaaaaa'


define -2 gui.hover_color = '#65beb7'



define -2 gui.selected_color = '#ffffff'


define -2 gui.insensitive_color = '#8888887f'



define -2 gui.muted_color = '#285100'
define -2 gui.hover_muted_color = '#3d7a00'


define -2 gui.text_color = '#000000'
define -2 gui.interface_text_color = '#ffffff'





define -2 gui.text_font = "gui/fonts/M-NijimiMincho/M-NijimiMincho.otf"


define -2 gui.name_text_font = "gui/fonts/UrsaSerif/URSB____.TTF"


define -2 gui.interface_text_font = "gui/fonts/M-NijimiMincho/M-NijimiMincho.otf"

translate japanese python:

    gui.text_font = "gui/fonts/M-NijimiMincho/M-NijimiMincho.otf"

    gui.name_text_font = "gui/fonts/SoukouMincho-Font/SoukouMincho.ttf"

    gui.interface_text_font = "gui/fonts/M-NijimiMincho/M-NijimiMincho.otf"
    gui.text_size = 28


define -2 gui.text_size = 24
define -2 gui.text_bold = False
define -2 gui.text_line_spacing = 10


define -2 gui.name_text_size = 30

define -2 gui.name_text_bold = False
define -2 gui.name_text_outlines = [ (4, "#fff1", 0, 0), (3, "#fff1", 0, 0),  (2, "#fff2", 0, 0) ]


define -2 gui.interface_text_size = 22


define -2 gui.label_text_size = 24


define -2 gui.notify_text_size = 16


define -2 gui.title_text_size = 50





define -2 gui.main_menu_background = "images/bg/small-river.png"
define -2 gui.game_menu_background = "gui/game_menu.png"








define -2 gui.textbox_height = 195



define -2 gui.textbox_yalign = 1.0




define -2 gui.name_xpos = 240
define -2 gui.name_ypos = 0



define -2 gui.name_xalign = 0.5
define -2 gui.name_xoffset = -390
define -2 gui.name_yalign = -0.38
define -2 gui.name_yanchor = 0.0
define -2 gui.name_ypos = -0.17

translate japanese python:

    gui.name_yanchor = 0.0
    gui.name_ypos = -0.16



define -2 gui.namebox_width = None
define -2 gui.namebox_height = None



define -2 gui.namebox_borders = Borders(5, 5, 5, 5)



define -2 gui.namebox_tile = False





define -2 gui.dialogue_xpos = 130
define -2 gui.dialogue_ypos = 50


define -2 gui.dialogue_width = 1000



define -2 gui.dialogue_text_xalign = 0.0








define -2 gui.button_width = None
define -2 gui.button_height = None


define -2 gui.button_borders = Borders(4, 4, 4, 4)



define -2 gui.button_tile = False


define -2 gui.button_text_font = gui.interface_text_font


define -2 gui.button_text_size = gui.interface_text_size


define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color



define -2 gui.button_text_xalign = 0.0








define -2 gui.radio_button_borders = Borders(18, 4, 4, 4)

define -2 gui.check_button_borders = Borders(18, 4, 4, 4)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(10, 4, 10, 4)

define -2 gui.quick_button_borders = Borders(10, 4, 10, 0)
define -2 gui.quick_button_text_size = 14
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color












define -2 gui.choice_button_width = 790
define -2 gui.choice_button_height = None
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(100, 5, 100, 5)
define -2 gui.choice_button_text_font = gui.text_font
define -2 gui.choice_button_text_size = gui.text_size
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#cccccc"
define -2 gui.choice_button_text_hover_color = "#ffffff"









define -2 gui.slot_button_width = 276
define -2 gui.slot_button_height = 206
define -2 gui.slot_button_borders = Borders(10, 10, 10, 10)
define -2 gui.slot_button_text_size = 14
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color


define -2 config.thumbnail_width = 256
define -2 config.thumbnail_height = 144


define -2 gui.file_slot_cols = 3
define -2 gui.file_slot_rows = 2

define -2 gui.slot_button_text_selected_idle_color = gui.selected_color
define -2 gui.slot_button_text_selected_hover_color = gui.hover_color








define -2 gui.navigation_xpos = 40


define -2 gui.skip_ypos = 10


define -2 gui.notify_ypos = 45


define -2 gui.choice_spacing = 22


define -2 gui.navigation_spacing = 4


define -2 gui.pref_spacing = 10


define -2 gui.pref_button_spacing = 0


define -2 gui.page_spacing = 0


define -2 gui.slot_spacing = 10


define -2 gui.main_menu_text_xalign = 1.0








define -2 gui.frame_borders = Borders(4, 4, 4, 4)


define -2 gui.confirm_frame_borders = Borders(40, 40, 40, 40)


define -2 gui.skip_frame_borders = Borders(16, 5, 50, 5)


define -2 gui.notify_frame_borders = Borders(16, 5, 40, 5)


define -2 gui.frame_tile = False











define -2 gui.bar_size = 25
define -2 gui.scrollbar_size = 12
define -2 gui.slider_size = 25


define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False


define -2 gui.bar_borders = Borders(4, 4, 4, 4)
define -2 gui.scrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.slider_borders = Borders(4, 4, 4, 4)


define -2 gui.vbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vslider_borders = Borders(4, 4, 4, 4)



define -2 gui.unscrollable = "hide"







define -2 config.history_length = 250



define -2 gui.history_height = 140



define -2 gui.history_name_xpos = 155
define -2 gui.history_name_ypos = 0
define -2 gui.history_name_width = 155
define -2 gui.history_name_xalign = 1.0


define -2 gui.history_text_xpos = 170
define -2 gui.history_text_ypos = 2
define -2 gui.history_text_width = 740
define -2 gui.history_text_xalign = 0.0







define -2 gui.nvl_borders = Borders(0, 10, 0, 20)



define -2 gui.nvl_list_length = 6



define -2 gui.nvl_height = None
define -2 gui.nvl_window_height = 700



define -2 gui.nvl_spacing = 0
define -2 gui.nvl_text_color = '#fff'



define -2 gui.nvl_name_xpos = 0.53
define -2 gui.nvl_name_ypos = 0.08
define -2 gui.nvl_name_width = 150
define -2 gui.nvl_name_xalign = 0.0

translate japanese python:
    gui.nvl_name_xalign = 1.0
    gui.nvl_name_width = 280
    gui.nvl_name_xpos = 0.63


define -2 gui.nvl_text_xpos = 450
define -2 gui.nvl_text_ypos = 0.1
define -2 gui.nvl_text_width = 590
define -2 gui.nvl_text_xalign = 0.0
define -2 gui.nvl_text_size = 30



define -2 gui.nvl_thought_xpos = 0.5
define -2 gui.nvl_thought_ypos = 0.1
define -2 gui.nvl_thought_width = 780
define -2 gui.nvl_thought_xalign = 0.5


define -2 gui.nvl_button_xpos = 450
define -2 gui.nvl_button_xalign = 0.0







define -2 gui.language = "unicode"


init -2 python:


    style.ruby_style = Style(style.default)
    style.ruby_style.size = 12
    style.ruby_style.yoffset = -25
    style.ruby_style.color = "#ffdddd"

    style.default.ruby_style = style.ruby_style





init -2 python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(40, 14, 40, 0)



    if renpy.variant("small"):
        
        
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34
        
        
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100
        
        
        gui.slider_size = 36
        
        gui.choice_button_width = 1240
        
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        
        gui.history_height = 190
        gui.history_text_width = 690
        
        gui.quick_button_text_size = 20
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 170
        
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
