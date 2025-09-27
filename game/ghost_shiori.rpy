############# GHOST ENCOUNTERS ###########################
label ghost_shiori_1:

    play music "Friends.mp3"

    scene black
    with fade
    n "It's too dark to see anything...."

    # MC in front of glass/water reflection
    MC shocked "..."


    show ghost_shiori normal:
        zoom 0.3
        xalign 0.5

        block:
            linear 0.3 matrixcolor BrightnessMatrix(-0.2)
            linear 0.3 matrixcolor BrightnessMatrix(-0.5)
            linear 0.3 matrixcolor BrightnessMatrix(0.0)
            linear 0.3 matrixcolor BrightnessMatrix(-0.4)
            linear 0.3 matrixcolor BrightnessMatrix(0.2)
            linear 0.3 matrixcolor BrightnessMatrix(-0.6)
            linear 0.3 matrixcolor BrightnessMatrix(-0.05)
            repeat
    MC "...?"

    $ renpy.pause(0.3)

    n "There's{nw}"
    play sound "sfx/jumpscare.mp3"

    show ghost_shiori normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 0

        # Sudden jumpscare: zoom in fast, move up to focus on face
        linear 0.13 zoom 1.26 yoffset -290 xoffset -500

    n "...!"

    hide ghost_shiori with dissolve

    $ renpy.pause(1.0)
    ## shiori's ghost dissapears

    n "What was that?"

    $ ghost_shiori_1 = True

    return

label ghost_shiori_2:

    play music "Friends.mp3"

    scene shrine day with fade:
        zoom 0.5

    #blinking
    show black_screen zorder 5 with fade
    $ renpy.pause(0.3)
    hide black_screen zorder 5 with fade
    $ renpy.pause(0.3)

    #blinking ghost appear
    show black_screen zorder 5 with fade
    show ghost_shiori normal zorder 4 at c_show_22
    $ renpy.pause(0.3)
    hide black_screen zorder 5 with fade
    $ renpy.pause(0.3)

    #blinking ghost appear still
    show black_screen zorder 5 with fade
    $ renpy.pause(0.3)
    hide black_screen zorder 5 with fade
    $ renpy.pause(0.3)

    #blinking ghost disappear
    show black_screen zorder 5 with fade
    hide ghost_shiori normal zorder 1 with fade
    hide black_screen zorder 5 with fade
    $ renpy.pause(0.3)

    #MC sleeping then eye opens (renpy eye blink pov dissolve) , suddenly shiori crawls into view, staring at you too long.
    # You don't know that you have to click, panic. So like, disable clicking for some uncomfortable seconds

    # Simulate first-person waking up with blinking
    #show placeholder with in_eye
    #$ renpy.pause(0.2)
    #show placeholder with out_eye
    #$ renpy.pause(0.2)
    #show placeholder with in_eye
    #$ renpy.pause(0.2)
    #show placeholder with out_eye
    #$ renpy.pause(0.2)

    # Silence, no dialogue yet
    window hide
    $ renpy.pause(1.5)

    # Eyes slowly open, fade in Shiori crawling from below
    show black_screen zorder 5 with fade
    $ renpy.pause(0.3)
    hide black_screen zorder 5 with fade
    # show shiori ghost crawling >> ATL
    show ghost_shiori normal zorder 4 at c_show_23

    #play sound "sfx/crawl_scrape.ogg"
    #$ renpy.pause(2.0)

    # Shiori stares—clicking disabled here
    $ renpy.pause(6.5, hard=True)

    # SOME WHISPERING SFX

    # Only now allow input
    window show

    n "...Was that....?"

    n "...."

    hide ghost_shiori normal with dissolve
    #stop sound fadeout 1.5

    $ ghost_shiori_2 = True

    return

screen force_mouse_move_ghost_shiori_3():
    on "show":
        action MouseMove(config.screen_width/4 * 3., config.screen_height/2, duration=7)
    timer 7.5 action Return()

label ghost_shiori_3:

    play music "Friends.mp3"

    scene shrine night with fade:
        zoom 0.5
    pause(0.2)
    call screen force_mouse_move_ghost_shiori_3
    show ghost_shiori normal at c_show_24

    # ​Shiori's ghost is hidden from view in the shrine, we code force mouse move to her ghost location,
    #then she appears, blink, moves closer, and before she becomes too close, dissapears
    # Say she is at the right edge of the screen then slowly creeps in

    # Hide Shiori initially at alpha 0?
    #show shiori ghost :
    #    alpha 0.0

    # Show a screen to force mouse move?

    # Once mouse is at position, Shiori appears
    #show shiori ghost at right_edge_hidden:
        #linear 0.5 alpha 1.0

    MC "Hmm?"

    # She creeps in
    show ghost_shiori normal:
        zoom 0.15
        xalign 0.5
        yalign 0.6

    n "A-Aah, she's coming at you!"

    $ renpy.pause(1.0)

    # Blink flicker

    n "Wait, she's just staring...."
    #shiori blink animation

    n "Does she know you?"

    # Move closer
    play sound "sfx/shighost.mp3"
    show ghost_shiori attack:
        zoom 0.15
        xalign 0.5
        yalign 0.6

        # Staggering, irregular zoom-in
        linear 0.01 zoom 0.22 xalign 0.49 yalign 0.52
        linear 0.02 zoom 0.28 xalign 0.5 yalign 0.48
        linear 0.03 zoom 0.33 xalign 0.43 yalign 0.44
        linear 0.05 zoom 0.41 xalign 0.47 yalign 0.4
        linear 0.08 zoom 0.50 xalign 0.4 yalign 0.3 xoffset -300
        linear 0.13 zoom 0.62 xalign 0.3 yalign 0 xoffset -500
    $ renpy.pause(1.0)
    hide ghost_shiori

    # Disappear just before

    stop sound fadeout 1.0
    stop music fadeout 2.0

    n "She's gone..."

    $ ghost_shiori_3 = True
    return

label ghost_shiori_4:

    stop music

    #scene bg shrine_empty with fade
    scene shrine night with fade:
        zoom 0.5

    n "No one is here."

    n "Someone is supposed to be here..."

    $ renpy.pause(2.0)

    stop music fadeout 1.0

    # Blackout
    #scene black with fade
    show black_screen with fade

    $ renpy.pause(2.5)
    centered "S T A Y  W I T H  M E"

    # Whisper
    hide black_screen
    #play voice "sfx/whisper_staywithme.ogg"


    # Flicker screen effect ATL

    $ renpy.pause(2)

    #flicker after 2 sec
    show black_screen at c_show_27

    #10s flicker then hide
    $ renpy.pause(10)
    hide black_screen
    #hide screen shrine_flicker

    stop sound fadeout 1.0

    window show
    n "..."


    $ ghost_shiori_4 = True
    return

screen ghost_shiori_5_open1():
    imagebutton:
        xalign 0.1 yalign 0.2
        idle "images/button_open.png"
        #action play sound ratling
        action Return()

screen ghost_shiori_5_open2():
    imagebutton:
        xalign 0.1 yalign 0.2
        idle "images/button_open.png"
        #action play sound ratling
        action Return()

screen ghost_shiori_5_open3():
    imagebutton:
        xalign 0.1 yalign 0.2
        idle "images/button_open.png"
        #action play sound ratling
        action Return()

label ghost_shiori_5:

    play music "heavy breathing.mp3"

    # Instead of the room, there’s a flickering room with the sound of a rattling doorknob.
    # Each click to “open” makes the rattling more frantic.
    # Shiori’s ghost sprite is shown with low opacity

    # shrine only for temporary
    scene shrine night with fade:
        zoom 0.7
        xalign 0.5
        yalign 0.6

    MC shocked2 "I'm locked in...!?"

    call screen ghost_shiori_5_open1()

    ## you click "open" image button

    play sound "sfx/rattle.mp3"
    with sshake

    ## rattling intensifies

    ## shiori's ghost appears with low opacity
    show ghost_shiori normal at c_show_28

    MC angry2 "Let me out!"
    with sshake

    call screen ghost_shiori_5_open2()

    ## you click "open" image button

    play sound "sfx/rattle.mp3"
    with sshake

    ## rattling intensifies

    ## shiori's ghost image creeps in

    show ghost_shiori normal at c_show_29

    MC "LET ME OUT!!!"

    ## you click "open" image button
    call screen ghost_shiori_5_open3()

    ## rattling intensifies
    play sound "sfx/rattle.mp3"
    with sshake

    ## shiori's ghost image creeps in
    show ghost_shiori normal at c_show_30

    MC angry2 "YoU ArE DEaD, I Ate YOu!"

    scene black

    play sound "sfx/prang.mp3"
    with sshake

    ## bam, everything stops
    #play sound bam
    #stop sound ratling
    hide ghost_shiori

    "..."

    $ ghost_shiori_5 = True
    return
