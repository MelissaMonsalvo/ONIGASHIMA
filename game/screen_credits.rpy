### CREDITS SCREEN ############################################################
##
## tiredge.
##

############################################################
### PYTHON ###
############################################################
init python:
    CREDITS_LIST = {
        "AzureXTwilight": ["Writer / Main Programmer / Lead", "azurextwilight.itch.io"],
        "Akua": ["Sprite Artist & Monster Colorist / Character & Mask Design / Cover & Banner", "akua-kourin.itch.io"],
        "Pauline Reinacher": ["CG Artist / Monster & Oni Design / Monster Sketch & Lineart", "pollyrein.itch.io"],
        "Otoke Neko": ["UI / Programmer / Itch Page", "otojang.itch.io"],
        "Mel": ["Programmer", "melomell.itch.io"],
        "ChrisD": ["Programmer", "eddyc.itch.io"],
        "Captain Sho": ["Logo Designer", "shiogames.itch.io"],
        "CyborgNekoSica": ["Background Artist", "cyborgnekosica.itch.io"],
        "FreeSound.org, Pixabay": ["SFX", ""],
        "FreePix.com": ["Extra Art", ""],
        "Dova Syndrome": ["Music", "https://dova-s.jp/EN/_mobile/"],
        "H/Mix Gallery": ["Music", "http://www.hmix.net/"],
        "Hashimamiweb": ["Music", "https://hashimamiweb.com/"],
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

                if sm:
                    textbutton "Link":
                        text_font NOTO_JP_BOLD
                        text_underline True
                        xalign 1.0
                        action Confirm("Open this link?", OpenURL(sm), Hide())

            null height 20

    if not persistent.loop1:
        $ tt_color = BLACK
    else:
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
