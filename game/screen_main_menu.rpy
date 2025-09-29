## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform mc_slidein:
    xalign 1.3
    yalign 0.5
    zoom 0.45
    xoffset 300
    linear 0.7 xalign 0.9

transform fadein0:
    alpha 0.0
    pause 0.2
    linear 0.5 alpha 1.0

transform fadein1:
    alpha 0.0
    pause 0.8
    linear 0.5 alpha 1.0

transform fadein2:
    alpha 0.0
    pause 1.4
    linear 0.5 alpha 1.0



screen press_anything_to_continue():
    if not persistent.loop1:
        add "MOON/moon1.jpg"
    else:
        add "MOON/moon6.jpg"
    button:
        xysize (config.screen_width, config.screen_height)
        background None

        text "Press Enter to Continue":
            font NOTO_JP
            xalign 0.5
            yalign 0.55
            outlines [(4, "#000000", 0, 0)]

            at ts_text_fade()

        action Return()



screen main_menu():
    style_prefix "mm"

    ## This ensures that any other menu screen is replaced.
    on "show" action Function(restore_all_volumes) ### DO NOT DELETE
    tag menu

    on "show" action Function(play_menu_music)


    if not persistent.loop1:
        $ tt_color = BLACK
        $ tt_out = BLACK
    else:
        $ tt_color = WHITE
        $ tt_out = RED




    if not persistent.loop1:
        add "MOON/moon1.jpg"
    else:
        add "MOON/moon6.jpg"

    # Yamato
    if persistent.yamato_dies:
        add "gui/Main Menu/yamato_idle.webp" xpos -100 ypos 0 zoom 0.2 at fadein0
    else:
        add "gui/Main Menu/yamato_static.webp" xpos 400 ypos 0 zoom 0.2 at fadein0

    # Hikaru
    if persistent.hikaru_dies:
        add "gui/Main Menu/hikaru_idle.webp" xpos 700 ypos 100 zoom 0.2 at fadein1
    else:
        add "gui/Main Menu/hikaru_static.webp" xpos 900 ypos 100 zoom 0.2 at fadein1

    # Shiori
    if persistent.shiori_dies:
        add "gui/Main Menu/shiori_idle.webp" xpos 500 ypos 200 zoom 0.2 at fadein2
    else:
        add "gui/Main Menu/shiori_static.webp" xpos 660 ypos 200 zoom 0.2 at fadein2

    # MC sliding in (after others for maximum impact)
    if not persistent.loop1:
        add 'mc_mm_loop1' at mc_slidein
    elif persistent.loop1 and not persistent.loop2:
        add 'mc_mm_loop2' at mc_slidein
    elif persistent.loop1 and persistent.loop2:
        add 'mc_mm_loop3' at mc_slidein
    else:
        add 'mc_mm_loop1' at mc_slidein

    fixed:
        xysize (config.screen_width, config.screen_height)

        vbox:
            at ts_enterX(-80, 1.0)


            spacing -40

            pos (40, 40)

            add "logo" xpos 40 ypos -30
            null height 80

            button:
                text _("START"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

                action Start()

            button:
                text _("LOAD"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

                action ShowMenu("load")

            button:
                text _("SETTINGS"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

                action Show("preferences")

            button:
                text _("CONTROLS"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

                action ShowMenu("help")

            button:
                text _("EXTRAS"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

                action ShowMenu("extras")

            button:
                text _("CREDITS"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

                action ShowMenu("credits")

            button:
                text _("QUIT TO DESKTOP"):
                    hover_color tt_color
                    idle_outlines [(2, tt_out, 0, 0)]
                    hover_outlines ([(2, RED, 0, 0)] if persistent.loop1 else [(0, BLACK, 0, 0)])

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
    font NOTO_JP_BOLD
    color WHITE

    #idle_outlines [(1, BLACK, 0, 0)]
    #hover_outlines [(0, BLACK, 0, 0)]

    size 35
    bold False
    italic False
    kerning 5


screen content_warning():
    vbox:
        at ts_fadein()

        align (0.5, 0.5)
        xsize 1100

        text "Content Warning":
            font NOTO_JP_BOLD
            color BLACK
            size 50
            xalign 0.5

        null height 100

        text "This game contains depictions of violence, gore, mild profanity, alcohol, drugs, smoking, and possibly severe frightening and intense scenes.\nIf you feel uncomfortable at any point, please take a break from playing.":
            font NOTO_JP
            color BLACK
            size 50
            xalign 0.5

        null height 50
        hbox:
            xsize 800
            xalign 0.5

            button:
                text _("I understand."):
                    align (0.5, 0.5)
                    font NOTO_JP_BOLD
                    color BLACK
                    hover_color (WHITE if persistent.loop1 else BLACK)

                xysize (280, 120)
                background None
                hover_background Transform("long_btn_hover_no_frame", xysize=(280, 120))

                action Hide(), Return()

            button:
                text _("Leave."):
                    align (0.5, 0.5)
                    font NOTO_JP_BOLD
                    color BLACK
                    hover_color (WHITE if persistent.loop1 else BLACK)

                xysize (280, 120)
                background None
                hover_background Transform("long_btn_hover_no_frame", xysize=(280, 120))

                action Quit(confirm=False)




screen seizure():
    vbox:
        at ts_fadein()

        align (0.5, 0.5)
        xsize 1100

        text "Photosensitivity Seizure Warning":
            font NOTO_JP_BOLD
            color BLACK
            size 50
            xalign 0.5

        null height 100

        text "Some individuals may experience epileptic seizures when exposed to certain visual images, including light patterns or flashing light.":
            font NOTO_JP
            color BLACK
            size 50
            xalign 0.5


label splashscreen:
    $ _window_hide()
    scene gm bg1 with fade

    call screen content_warning()

    # Show first image instantly, with fade
    #scene expression "splashscreen/seizure.jpg" with fade
    show screen seizure()

    # Block all input for 3 seconds WHILE first image is shown
    $ renpy.pause(1.0, hard=True)
    # Show first image a bit longer (adjust this to your liking)
    $ renpy.pause(1.5)   # This CAN be clicked/fast-forwarded, or set to 0 if you want exactly 3 sec

    hide screen seizure
    pause 0.3
    # Show the rest of the splash images, clickable as normal
    scene expression "splashscreen/ss1.jpg" with fade
    $ renpy.pause(0.7)

    scene expression "splashscreen/ss2.jpg" with fade
    $ renpy.pause(0.7)

    scene expression "splashscreen/ss3.jpg" with fade
    $ renpy.pause(0.7)

    scene expression "splashscreen/ss3a.jpg" with fade
    $ renpy.pause(0.7)

    scene expression "splashscreen/ss4.jpg" with fade
    $ renpy.pause(0.7)

    scene expression "splashscreen/ss4a.jpg" with fade
    $ renpy.pause(0.7)

    scene expression "splashscreen/ss5.jpg" with fade
    $ renpy.pause(0.7)

    scene black with fade
    call screen press_anything_to_continue()
    return
