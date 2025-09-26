### NAME INPUT ############################################################
##
##

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

                exclude "*$#!{}()-@+=/^%"

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


############################################################
### STYLES ###
############################################################
style ni_frame:
    #xysize (895, 95)
    xminimum 895
    ysize 95

    anchor (1.0, 1.0)
    pos (1920, 1060)

    background Frame("gui/game menu/btn_backgroud.png", 20, 10)

style ni_hbox:
    xalign 1.0
    yalign 0.5

style ni_button:
    xysize (430, 58)

    background Frame("gui/game menu/btn_idle_background.png", 20, 10)
    hover_background Frame("gui/game menu/btn_hover_background.png", 20, 10)
    insensitive_background Frame("gui/game menu/btn_insensitive_background.png", 20, 10)

style ni_text:
    font "NotoSerifJP-VariableFont_wght.ttf"
    bold False
    italic False
    size 30
    yalign 0.5
    xoffset 30

    color "#000"

