### PAUSE MENU ############################################################
##
## Menu that appears when you press esc.
##

init python:
    _game_menu_screen = "pause_menu"

############################################################
### PAUSE MENU SCREEN ###
############################################################
screen pause_menu():
    tag menu
    
    style_prefix "pm"
    default tt_color = BLACK

    ## TEXT COLOR CHANGE ##

    if current_route == "route1":
        $ tt_color = BLACK
    elif current_route == "route2":
        $ tt_color = WHITE


    add "screen overlay"
    fixed:
        xysize (config.screen_width, config.screen_height)

        at ts_enterX(-80)


        add "gui/pause_menu_background.webp"


        vbox:
            ypos 170
            xpos 5
            spacing -5

            button:
                text _("RESUME") hover_color tt_color
                action Return()

            button:
                text _("HISTORY") hover_color tt_color
                action ShowMenu("history")

            button:
                text _("SETTINGS") hover_color tt_color
                action ShowMenu("preferences")

            button:
                text _("SAVE") hover_color tt_color
                action ShowMenu("save")

            button:
                text _("LOAD") hover_color tt_color
                action ShowMenu("load")

            button:
                text _("CONTROLS") hover_color tt_color
                action ShowMenu("help")

            button:
                text _("RETURN TO TITLE") hover_color tt_color
                action MainMenu()



############################################################
### PAUSE MENU STYLES ###
############################################################
style pm_button:
    xysize (745, 120)
    background None
    hover_background "long_btn_hover"
    padding LONG_BTN_PADDING

style pm_text:
    size 40
    color WHITE
    font NOTO_JP
    bold False
    italic False

