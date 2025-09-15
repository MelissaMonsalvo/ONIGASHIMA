init python:
    renpy.music.register_channel("muzak", "music")

define mc2 = Character("[name]")

# =========================
# ROUTE FLAGS
# =========================
default persistent.route1 = True
default persistent.route2 = False

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

screen fake_name_input():
    frame:
        xalign 0.5
        yalign 0.5
        background None
        has vbox
        spacing 30

        text "Say your name" size 40 color "#CCCCCC" xalign 0.5

        text "> [name_display]|" size 40 color "#FFFFFF" xalign 0.5

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
    if persistent.trueendingunlocked:
        $ persistent.route1 = True
        $ persistent.route2 = False
        $ update_route()
        jump prologue_trueend
    if persistent.loop8:
        jump prologue_loop8
    if persistent.loop7:
        jump prologue_loop7
    if persistent.loop6:
        jump prologue_loop6
    if persistent.loop5:
        jump prologue_loop5
    if persistent.loop4:
        jump prologue_loop4
    if persistent.loop3:
        jump prologue_loop3
    if persistent.loop2:
        $ persistent.route1 = True
        $ persistent.route2 = False
        $ update_route()
        jump prologue_loop2
    if persistent.loop1:
        jump prologue_loop1
    else:
        jump prologue
