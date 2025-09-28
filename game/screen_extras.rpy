### EXTRAS SCREEN ############################################################
##
## Gallery
##


############################################################
### EXTRAS SCREEN ###
############################################################
screen extras():
    style_prefix "extras"
    tag menu

    default tab = "gallery"
    default selected_song = None

    if current_route == "route1":
        $ skin = btn_skin_yellow
        $ tt_color = BLACK
    elif current_route == "route2":
        $ skin = btn_skin_red
        $ tt_color = WHITE
        

    add gui.game_menu_background

    fixed:
        xysize (config.screen_width, config.screen_height)

        add "gm navline"

        label _("{}".format(tab.upper()))


        ### SIDE NAV ###
        vbox:
            button:
                text "Gallery":
                    hover_color tt_color
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("tab", "gallery")

            
            button:
                text "Music":
                    hover_color tt_color
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]
                
                action SetScreenVariable("tab", "music")
    

        ### VIEWPORT ###
        viewport:
            style_prefix "extras_vp"

            xysize GM_VP_SIZE
            pos GM_VP_POS

            draggable True pagekeys True mousewheel True
            scrollbars "vertical" yinitial 0.0
            has vbox:
                spacing 30

            if tab == "gallery":
                use extras_gallery()
            elif tab == "music":
                use extras_music(selected_song)


    ## NAV ## ## Use SAVE/LOAD ref
    frame:
        at ts_enterX(80)


        style_prefix "help_gm"
    
        hbox:
            if tab == "music":
                button:
                    text _("PLAY"):
                        hover_color tt_color

                    sensitive selected_song is not None and mr.is_unlocked(selected_song)

                    
                    action mr.Play(selected_song)

                button:
                    text _("STOP") hover_color tt_color

                    sensitive selected_song

                    action mr.Stop()

            button:
                text _("BACK") hover_color tt_color

                action Return()


    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "Main Menu.mp3")




############################################################
### EXTRAS STYLES ###
############################################################
style extras_label:
    is sl_label

style extras_label_text:
    is sl_label_text

style extras_vbox:
    xsize 375
    spacing GM_SPACING
    pos (40, 306)

style extras_button:
    xysize (422, 102)

style extras_text:
    is help_text

