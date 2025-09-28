## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu



screen press_anything_to_continue():
    add "mm_background"
    button:
        xysize (config.screen_width, config.screen_height)
        background None

        text "Press Enter to Continue":
            font NOTO_JP
            xpos 10
            yalign 0.55
            outlines [(2, "#000000", 0, 0)]

            at ts_text_fade()

        action Return()



screen main_menu():
    style_prefix "mm"

    ## This ensures that any other menu screen is replaced.
    on "show" action Function(restore_all_volumes) ### DO NOT DELETE
    tag menu


    if current_route == "route1":
        $ tt_color = BLACK
    elif current_route == "route2":
        $ tt_color = WHITE


    add "mm_background"

    fixed:
        xysize (config.screen_width, config.screen_height)

        vbox:
            at ts_enterX(-80, 1.0)

            
            spacing -20

            pos (40, 40)

            add "logo"
            null height 20

            button:
                text _("START") hover_color tt_color
                action Start()

            button:
                text _("LOAD") hover_color tt_color
                action ShowMenu("load")

            button:
                text _("SETTINGS") hover_color tt_color
                action Show("preferences")

            button:
                text _("CONTROLS") hover_color tt_color
                action ShowMenu("help")

            button:
                text _("EXTRAS") hover_color tt_color
                action ShowMenu("extras")

            button:
                text _("CREDITS") hover_color tt_color
                action ShowMenu("credits") 

            button:
                text _("QUIT TO DESKTOP") hover_color tt_color
                action Quit()

############################################################
### MAIN MENU STYLES ###
############################################################
style mm_button:
    xysize (600, 120)
    background None
    hover_background "long_btn_hover"
    padding LONG_BTN_PADDING

style mm_text:
    font NOTO_JP
    color WHITE
    
    #idle_outlines [(1, BLACK, 0, 0)]
    #hover_outlines [(0, BLACK, 0, 0)]

    size 40
    bold False
    italic False

label splashscreen:
    call screen press_anything_to_continue()
    return
