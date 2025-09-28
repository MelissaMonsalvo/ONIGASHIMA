init python:
    renpy.music.register_channel("muzak", "music")

define mc2 = Character("[name]")

init:
    $ wiperight2 = CropMove(0.07, "wiperight")
    $ wipeleft2 = CropMove(0.07, "wipeleft")
    $ wipeup2 = CropMove(0.07, "wipeup")
    $ wipedown2 = CropMove(0.07, "wipedown")

init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)


# AFTER LOAD STUFF
default loopflag = 1  # Use this to track which playthrough (set at start of game/loop)

default should_block_label = None
default block_scheduled = False

# Use a normal store variable, not config
default current_route = "route1"

init python:
    def update_route():
        if persistent.route2:
            store.current_route = "route2"
        else:
            store.current_route = "route1"

init python:
    # True name we want to force
    true_name_target = "Yamakui"
    name_input_index = 0
    name_display = ""

    def _fake_type_char():
        global name_input_index
        global name_display
        if name_input_index < len(true_name_target):
            name_display += true_name_target[name_input_index]
            name_input_index += 1

# screen fake_name_input():
#     frame:
#         xalign 0.5
#         yalign 0.5
#         background None
#         has vbox
#         spacing 30

#         text "Say your name" size 40 color "#CCCCCC" xalign 0.5

#         text "> [name_display]|" size 40 color "#FFFFFF" xalign 0.5

#     key "K_RETURN" action Return()
#     key "K_BACKSPACE" action NullAction()

#     # Capture most key presses (alphanumeric)
#     for key in ("a","b","c","d","e","f","g","h","i","j","k",
#                 "l","m","n","o","p","q","r","s","t","u","v",
#                 "w","x","y","z",
#                 "K_a","K_b","K_c","K_d","K_e","K_f","K_g","K_h",
#                 "K_i","K_j","K_k","K_l","K_m","K_n","K_o","K_p",
#                 "K_q","K_r","K_s","K_t","K_u","K_v","K_w","K_x",
#                 "K_y","K_z", "K_SPACE"):
#         key key action Function(_fake_type_char)

screen fake_name_input():
    fixed:
        xysize (config.screen_width, config.screen_height)

        add "gui/menu_background.jpg"

        add "gui/name_input_background.png" ypos 188

        text "Say your name":
            pos (55, 200)
            font "NotoSerifJP-VariableFont_wght.ttf"
            bold False
            italic False
            size 80
        frame:
            xysize (1350, 135)
            pos (300, 430)
            background None
            text "> [name_display]|": #size 40 color "#FFFFFF" xalign 0.5
                align (0.5, 0.5)
                size 100
                font "NotoSerifJP-VariableFont_wght.ttf"
                bold False
                italic False
                color '#cc0000'
            ### CONFIRM/REVERT ###
        frame:
            style_prefix "ni"
            hbox:
                button:
                    text "CONFIRM"
                    action Confirm("Choose this name?", Return(), Hide())
                button:
                    text "CLEAR"
                    action SetVariable("persistent.player_name", "")


    key "K_RETURN" action Return()
    key "K_BACKSPACE" action NullAction()

    # Capture most key presses (alphanumeric)
    for key in ("a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z",
                "K_a","K_b","K_c","K_d","K_e","K_f","K_g","K_h",
                "K_i","K_j","K_k","K_l","K_m","K_n","K_o","K_p",
                "K_q","K_r","K_s","K_t","K_u","K_v","K_w","K_x",
                "K_y","K_z", "K_SPACE"):
        key key action Function(_fake_type_char)

label start:
    if persistent.shiori_dies:
        $ shiori_alive = False
    else:
        if persistent.hikaru_dies:
            $ hikaru_alive = False
        else:
            if persistent.yamato_dies:
                $ yamato_alive = False
    #jump map
    #call screen name_input
    #call screen fake_name_input
    $ ysword = False
    $ hmask = True
    $ hsword = False
    #jump map
    #jump loop3_hikaru
    #jump get_player_name
    #jump prologue_loop1
    #jump prologue_loop2
    $ _prev_music_volume = _preferences.volumes["music"]
    if persistent.trueendingunlocked:
        $ current_route = "route1"
        $ loopflag = 5
        $ persistent.route1 = True
        $ persistent.route2 = False
        $ update_route()
        jump prologue_trueend
    if persistent.loop8:
        $ current_route = "route2"
        $ loopflag = 4
        jump prologue_loop8
    if persistent.loop7:
        $ current_route = "route2"
        $ loopflag = 4
        jump prologue_loop7
    if persistent.loop6:
        $ current_route = "route2"
        $ loopflag = 4
        jump prologue_loop6
    if persistent.loop5:
        $ current_route = "route2"
        $ loopflag = 4
        jump prologue_loop5
    if persistent.loop4:
        $ current_route = "route2"
        $ loopflag = 4
        jump prologue_loop4
    if persistent.loop3:
        $ current_route = "route2"
        $ loopflag = 4
        jump prologue_loop3
    if persistent.loop2:
        $ current_route = "route2"
        $ current_loop = 2
        $ loopflag = 3
        $ persistent.route1 = True
        $ persistent.route2 = False
        $ update_route()
        jump prologue_loop2
    if persistent.loop1:
        $ current_route = "route2"
        $ loopflag = 2
        $ current_loop = 2
        jump prologue_loop1
    else:
        $ loopflag = 1
        $ current_loop = 1
        jump prologue
