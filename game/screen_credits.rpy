### CREDITS SCREEN ############################################################
##
## tiredge.
##

############################################################
### PYTHON ###
############################################################
init python:
    CREDITS_LIST = {
        "AzureXTwilight": ["Writer / Main Programmer / Lead", "SOCIALS HERE"],
        "Akua": ["Sprite Artist & Monster Colorist / Character & Mask Design / Cover & Banner", "SOCIALS HERE"],
        "Pauline Reinacher": ["CG Artist / Monster & Oni Design / Monster Sketch & Lineart", "SOCIALS HERE"],
        "Otoke Neko": ["UI / Programmer / Itch Page", "SOCIALS HERE"],
        "Mel": ["Programmer", "SOCIALS HERE"],
        "ChrisD": ["Programmer", "SOCIALS HERE"],
        "Captain Sho": ["Logo Designer", "SOCIALS HERE"],
        "CyborgNekoSica": ["Background Artist", "SOCIALS HERE"],
        "FreeSound.org, Pixabay": ["SFX", ""],
        "FreePix.com": ["Extra Art", ""],
    }

############################################################
### SCREEN ###
############################################################
screen credits():
    tag menu
    add gui.game_menu_background

    style_prefix "credits"

    label "CREDITS"

    viewport:
        style_prefix "credits_vp"
        
        xysize (1327, 590)
        pos (286, 320)
        xfill False
        yfill False

        draggable True mousewheel True pagekeys True
        scrollbars "vertical" yinitial 0.0

        has vbox

        for name, data in CREDITS_LIST.items():
            $ role = data[0]
            $ sm = data[1]

            frame:
                background None
                padding (0, 0)
                xysize (1280, 200)

                text "{}  -  {}". format(name, role):
                    xalign 0.0
                    font NOTO_JP_BOLD
                    xsize 400
                    text_align 0.0

                text "{}".format(sm):
                    xalign 1.0

            null height 20

    if current_route == "route1":
        $ tt_color = BLACK
    elif current_route == "route2":
        $ tt_color = WHITE
    ## NAV ## ## Use SAVE/LOAD ref
    frame:
        at ts_enterX(80)


        style_prefix "help_gm"
    
        hbox:

            button:
                text _("BACK") hover_color tt_color

                action Return()


############################################################
### STYLES ###
############################################################
style credits_label:
    is sl_label

style credits_label_text:
    is sl_label_text



style credits_vp_text:
    font NOTO_JP
    color BLACK
    size 30
