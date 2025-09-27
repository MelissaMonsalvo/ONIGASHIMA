### EXIT GAME SCREEN ############################################################
##
## Custom exit screen. 
##

############################################################
### EXIT SCREEN ###
############################################################
screen exit_game():

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "screen overlay"

    ## TEXT COLOR CHANGE ##

    if current_route == "route1":
        $ tt_color = BLACK
    elif current_route == "route2":
        $ tt_color = WHITE


    frame:
        at ts_enterY(80)

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Exit this tale?"):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                button:
                    text _("Yes") hover_color tt_color
                    
                    action Quit(confirm=False)
                    

                button:
                    text _("No") hover_color tt_color
                    action Hide()

    ## Right-click and escape answer "no".
    key "game_menu" action Hide()

