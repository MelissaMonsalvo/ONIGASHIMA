### NAME INPUT ############################################################
##
##
## Names players cannot use
define EXCLUDE_NAMES = ["yamakui", "hikaru", "shiori", "yamato", "fuck", "bitch", "ass" ]
screen name_input():
    fixed:
        xysize (config.screen_width, config.screen_height)
            
        add "gui/menu_background.jpg"

        add "gui/name_input_background.png" ypos 188


        text "Say your name out loud":
            pos (55, 200)

            font "NotoSerifJP-VariableFont_wght.ttf"
            bold False
            italic False

            size 80

        frame:
            xysize (1350, 135)
            pos (300, 430)
            background None

            input value VariableInputValue("persistent.player_name", returnable=True):
                id "input"

                align (0.5, 0.5)

                length 8
                size 100
                font "NotoSerifJP-VariableFont_wght.ttf"
                bold False
                italic False

                caret Transform("#cc0000", xysize=(3, 100), ypos=35)

                exclude "*$#!{}()-@+=/^%"

        if persistent.player_name.lower().replace(" ", "") in EXCLUDE_NAMES:
            text "You cannot choose this name." color RED size 25 xalign 0.5 yalign 0.6 yoffset 80

        ### CONFIRM/REVERT ###
        frame:
            style_prefix "ni"

            hbox:
                button:
                    text "CONFIRM"

                    sensitive (persistent.player_name.lower().replace(" ", "") not in EXCLUDE_NAMES)

                    action Confirm("Choose this name?", Return(), Hide())


                button:
                    text "CLEAR"

                    action SetVariable("persistent.player_name", "")


############################################################
### STYLES ###
############################################################
style ni_frame:
    #xysize (895, 95)
    xminimum GM_XMIN_FRAME
    ysize 95

    anchor (1.0, 1.0)
    pos (1920, 1060)

    background Frame("gui/game menu/btn_backgroud.png", 20, 10)
    padding GM_LONG_BTN_PADDING

style ni_hbox:
    xalign 1.0
    yalign 0.5

style ni_button:
    xysize GM_BUTTON_SIZE

    background Frame("gui/game menu/btn_idle_background.png", 20, 10)
    hover_background "gm_btn_hover"
    insensitive_background Frame("gui/game menu/btn_insensitive_background.png", 20, 10)

style ni_text:
    font "NotoSerifJP-VariableFont_wght.ttf"
    bold False
    italic False
    size 30
    yalign 0.5
    xoffset 30

    color "#000"

