## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    style_prefix "help"

    tag menu

    default device = "keyboard"

    

    if not persistent.loop1:
        $ skin = btn_skin_yellow
        $ tt_color = BLACK
    else:
        $ skin = btn_skin_red
        $ tt_color = WHITE

    add gui.game_menu_background

    fixed:
        xysize (config.screen_width, config.screen_height)

        add "gm navline"

        label _("CONTROLS")

        vbox:
            button:
                text _("Keyboard"):
                    hover_color (tt_color if device == "keyboard" else BLACK)
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("device", "keyboard")

            button:
                text _("Mouse"):
                    hover_color (tt_color if device == "mouse" else BLACK)
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("device", "mouse")

            button:
                text _("Gamepad"):
                    hover_color (tt_color if device == "gamepad" else BLACK)
                    selected_color tt_color

                background skin["idle"]
                hover_background skin["hover"]
                selected_background skin["sel_idle"]
                selected_hover_background skin["sel_hover"]

                action SetScreenVariable("device", "gamepad")


        ### VIEWPORT ###

        viewport:
            style_prefix "help_vp"

            xysize GM_VP_SIZE
            pos GM_VP_POS

            draggable True pagekeys True mousewheel True
            scrollbars "vertical" yinitial 0.0
            has vbox:
                spacing 30



            if device == "keyboard":
                use keyboard_help()
            elif device == "mouse":
                use mouse_help()
            elif device == "gamepad":
                use gamepad_help()
    

    ## NAV ## ## Use SAVE/LOAD ref
    frame:
        at ts_enterX(80)


        style_prefix "help_gm"
    
        hbox:
            if device == "gamepad":
                button:
                    text _("CALIBRATE") hover_color tt_color

                    action GamepadCalibrate()

            button:
                text _("BACK") hover_color tt_color

                action Return()


style help_label:
    is sl_label

style help_label_text:
    is sl_label_text

style help_vbox:
    xsize 375
    spacing GM_SPACING
    pos (40, 306)

style help_button:
    xysize (422, 102)

style help_text:
    size 40
    color BLACK
    font NOTO_JP
    xpos 100
    yalign 0.5
    

style help_gm_frame:
    ysize 95
    xminimum GM_XMIN_FRAME
    anchor (1.0, 1.0)
    pos (1920, 1060)
    background Frame("gui/game menu/btn_backgroud.png", 20, 10)
    padding GM_LONG_BTN_PADDING

style help_gm_hbox:
    is ni_hbox

style help_gm_button:
    is ni_button

style help_gm_text:
    is ni_text


screen keyboard_help():
    style_prefix "help_tab"

    hbox:
        label _("Enter")
        
        frame:
            text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        
        frame:
            text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        
        frame:
            text _("Navigate the interface.")

    hbox:
        label _("Escape")
        
        frame:
            text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        
        frame:
            text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        
        frame:
            text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        
        frame:
            text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        
        frame:
            text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        
        frame:
            text _("Hides the user interface.")

    hbox:
        label "S"
        
        frame:
            text _("Takes a screenshot.")

    hbox:
        label "V"
        
        frame:
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        
        frame:
            text _("Opens the accessibility menu.")


screen mouse_help():
    style_prefix "help_tab"

    hbox:
        label _("Left Click")
        
        frame:
            text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        
        frame:
            text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        
        frame:
            text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        
        frame:
            text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        
        frame:
            text _("Rolls forward to later dialogue.")


screen gamepad_help():
    style_prefix "help_tab"

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        
        frame:
            text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        
        frame:
            text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        
        frame:
            text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        
        frame:
            text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        
        frame:
            text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        
        frame:
            text _("Hides the user interface.")



style help_tab_hbox:
    xfill True
    spacing 10


style help_tab_label_text:
    font NOTO_JP_BOLD
    color BLACK
    size 40
    text_align 0.0
    xsize 250

style help_tab_frame:
    xsize 625
    xalign 1.0
    background None

style help_tab_text:
    font NOTO_JP
    color BLACK
    size 40

    text_align 0.0
    xalign 0.0