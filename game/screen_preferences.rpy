### PREFERENCES SCREEN ############################################################
##
## Define preferences screen.
##

############################################################
### PYTHON ###
############################################################



############################################################
### PREF SCREEN ###
############################################################
screen preferences():
    style_prefix "pref"

    tag menu

    default tab = "general"

    if current_route == "route1":
        $ skin = btn_skin_yellow
        $ tt_color = BLACK
    elif current_route == "route2":
        $ skin = btn_skin_red
        $ tt_color = WHITE


    ###---------###

    add gui.game_menu_background

    fixed:
        xysize (config.screen_width, config.screen_height)

        label _("SETTINGS")


        ### SIDE NAV ###
        add "gm navline"

        vbox:
            button:
                text _("General"):
                    hover_color tt_color
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("tab", "general")


            button:
                text _("Audio"):
                    hover_color tt_color
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("tab", "audio")


            button:
                text _("Dialogue"):
                    hover_color tt_color
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("tab", "dialogue")


            button:
                text _("Accessibility"):
                    hover_color tt_color
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("tab", "accessibility")



        ### VIEWPORT ###

        viewport:
            style_prefix "pref_vp"

            xysize GM_VP_SIZE
            pos GM_VP_POS

            draggable True pagekeys True mousewheel True
            scrollbars "vertical" yinitial 0.0
                

            ### SCREENS ###
            if tab == "general":
                use pref_general()
            elif tab == "audio":
                use pref_audio()
            elif tab == "dialogue":
                use pref_dialogue()
            elif tab == "accessibility":
                use pref_access()

        
        ## NAV ## ## Use CONTROLS ref
        frame:
            at ts_enterX(80)

            style_prefix "help_gm"

            hbox:

                button:
                    text _("REVERT ALL") hover_color tt_color

                    action Return()


                button:
                    text _("BACK") hover_color tt_color

                    action Return()

############################################################
### STYLES ###
############################################################
style pref_label:
    is sl_label

style pref_label_text:
    is sl_label_text

style pref_button:
    xysize (422, 102)

style pref_text:
    is help_text

style pref_vbox:
    is help_vbox


############################################################
### PREF TAB ###
############################################################
screen pref_general():
    style_prefix "pref_tab"

    hbox:
        vbox:
            frame:
                xsize 500
                text _("Display")

            frame:
                xsize 500
                text _("Skip: Unseen Text")

            frame:
                xsize 500
                text _("Skip: After Choices")

            frame:
                xsize 500
                text _("Skip: Transitions")




        vbox:
            ## DISPLAY ##
            style_prefix "pref_tab2"

            frame:
                xsize 500
                hbox:

                    imagebutton auto "gui/settings/btn_left_arrow_%s.png":
                        xalign 0.0

                        action Preference("display", "toggle")

                    text ("Fullscreen" if preferences.fullscreen else "Windowed") align (0.5, 0.5)

                    imagebutton auto "gui/settings/btn_right_arrow_%s.png":
                        xalign 1.0
                        action Preference("display", "toggle")


            ## SKIP ##
    

            frame:
                xsize 500
                hbox:

                    imagebutton auto "gui/settings/btn_left_arrow_%s.png":
                        action Preference("skip", "toggle")

                    text ("ON" if preferences.skip_unseen else "OFF") align (0.5, 0.5)

                    imagebutton auto "gui/settings/btn_right_arrow_%s.png":
                        xalign 1.0

                        action Preference("skip", "toggle")




            frame:
                xsize 500
                hbox:

                    imagebutton auto "gui/settings/btn_left_arrow_%s.png":
                        xalign 0.0

                        action Preference("after choices", "toggle")

                    text ("ON" if preferences.skip_after_choices else "OFF") align (0.5, 0.5)

                    imagebutton auto "gui/settings/btn_right_arrow_%s.png":
                        xalign 1.0

                        action Preference("after choices", "toggle")



            frame:
                xsize 500
                hbox:

                    imagebutton auto "gui/settings/btn_left_arrow_%s.png":
                        xalign 0.0

                        action Preference("transitions", "toggle")

                    text ("ON" if preferences.transitions != 2 else "OFF") align (0.5, 0.5)

                    imagebutton auto "gui/settings/btn_right_arrow_%s.png":
                        xalign 1.0

                        action Preference("transitions", "toggle")


screen pref_audio():
    style_prefix "pref_tab"

    hbox:
        vbox:
            frame:
                text _("Music")
            frame:
                text _("Sound")
            if config.has_voice:
                frame:
                    text _("Volume")


        $ bar_skin = bar_skin_yellow if (current_route=="route1") else bar_skin_red

        vbox:
            style_prefix "pref_tab2"
            ### MUSIC ###
            frame:
                xsize 635
                xoffset -50

                hbox:
                    spacing -5

                    $ mvol = int(preferences.get_mixer("music") * 100)
                    text "[mvol]" xalign 0.0

                    bar value Preference("music volume") alt "change music volume":
                        style "bar"
                        xalign 1.0
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        ysize 68
                        thumb None
                        


            ### SOUND ###
            frame:
                xsize 635
                xoffset -50

                hbox:
                    spacing -5

                    $ svol = int(preferences.get_mixer("sfx") * 100)
                    text "[svol]" xalign 0.0

                    bar value Preference("sound volume") alt "change sound volume":
                        style "bar"
                        xalign 1.0
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        ysize 68
                        thumb None
                        


            ### VOICE ###
            if config.has_voice:
                frame:
                    xsize 635
                    xoffset -50

                    hbox:
                        spacing -5

                        $ vvol = int(preferences.get_mixer("voice") * 100)
                        text "[vvol]" xalign 0.0

                        bar value Preference("voice volume") alt "change voice volume":
                            style "bar"
                            xalign 1.0
                            left_bar bar_skin
                            right_bar "gui/game menu/right.png"
                            ysize 68
                            thumb None
                            


screen pref_dialogue():
    style_prefix "pref_tab"

    hbox:
        vbox:
            frame:
                text _("Dialogue Speed")

            frame:
                text _("Dialogue Size")

            frame:
                text _("Line Spacing")

            frame:
                text _("Auto-Delay Time")

            #text _("Textbox Opacity")
            frame:
                text _("Typeface")

        $ bar_skin = bar_skin_yellow if (current_route=="route1") else bar_skin_red

        vbox:
            style_prefix "pref_tab2"
            frame:
                xsize 635
                xoffset -50
                hbox:
                    spacing -5
                    
                    $ spd = int(preferences.text_cps)
                    text "[spd]" xalign 0.0
                    
                    bar value Preference("text speed") alt "Change dialogue text speed":
                        style "bar"
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        thumb None
                        ysize 68
                        xalign 1.0

        
            frame:
                xsize 635
                xoffset -50
                hbox:
                    spacing -5
                    
                    text "[persistent.dialogue_text_size]" xalign 0.0

                    bar value FieldValue(persistent, "dialogue_text_size", step=5, min=25, max=45) alt "Change dialogue text size":
                        style "bar"
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        thumb None
                        ysize 68
                        xalign 1.0

            frame:
                xsize 635
                xoffset -50
                hbox:
                    spacing -5
                    
                    text "[persistent.dialogue_line_spacing]" xalign 0.0

                    bar value FieldValue(persistent, "dialogue_line_spacing", max_is_zero=False, step=0.5, min=2, max=80) alt "Change dialogue line spacing":
                        style "bar"
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        thumb None
                        ysize 68
                        xalign 1.0

            frame:
                xsize 635
                xoffset -50
                hbox:
                    spacing -5
                    
                    $ afm = int(preferences.afm_time)
                    text "[afm]" xalign 0.0

                    bar value Preference("auto-forward time") alt "Change auto-delay time":
                        style "bar"
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        thumb None
                        ysize 68
                        xalign 1.0

            ### TYPEFACE ###
            frame:
                xsize 500
                hbox:
                    imagebutton auto "gui/settings/btn_left_arrow_%s.png":
                        xalign 0.0

                        action [
                                SetVariable("font_index", (font_index - 1) % len(fonts)),
                                Function(update_dialogue_font)
                            ]

                    text "{}".format(fonts[font_index]) align (0.5, 0.5)

                    imagebutton auto "gui/settings/btn_right_arrow_%s.png":
                        xalign 1.0
                        
                        action [
                                SetVariable("font_index", (font_index + 1) % len(fonts)),
                                Function(update_dialogue_font)
                            ] 

        

screen pref_access():
    style_prefix "pref_tab"
    hbox:
        vbox:
            frame:
                text _("Self-Voicing")

        vbox:
            style_prefix "pref_tab2"
            frame:
                xsize 500
                hbox:
                    imagebutton auto "gui/settings/btn_left_arrow_%s.png":
                        xalign 0.0

                        action Preference("self voicing", "toggle")

                    text ("ON" if _preferences.self_voicing else "OFF") align (0.5, 0.5)

                    imagebutton auto "gui/settings/btn_right_arrow_%s.png":
                        xalign 1.0
                        
                        action Preference("self voicing", "toggle")

############################################################
### PREF TAB STYLES ###
############################################################
style pref_tab_hbox:
    xfill True

style pref_tab_vbox:
    spacing 30
    xsize 400


style pref_tab_text:
    font NOTO_JP
    size 40
    color BLACK

style pref_tab_frame:
    xsize 500
    background None
    #ysize 70


### PREF 2 ##
style pref_tab2_frame:
    is pref_tab_frame

style pref_tab2_hbox:
    #xminimum 485
    #xmaximum 630
    xfill True
    xalign 1.0


style pref_tab2_vbox:
    spacing 30

style pref_tab2_text:
    is pref_tab_text
    xsize 320
    




