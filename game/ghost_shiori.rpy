############# GHOST ENCOUNTERS ###########################
label ghost_shiori_1:

    scene bg empty_room_dark with fade
    ## refelection and ghosts are in the ghosts folder

    n "You see yourself."

    # MC in front of glass/water reflection
    MC "..."

    window hide
    $ renpy.pause(0.5)

    # blinks animation
    show black_screen at c_show_13
    $ renpy.pause(1)

    ## then shiori’s ghost appears behind them
    show ghost_shiori normal at c_show_14
    MC "...?"

    $ renpy.pause(1.0)

    ## MC Blinks again
    scene black with fade
    #show black_screen at c_show_13
    n "...!"

    hide ghost_shiori with dissolve

    $ renpy.pause(1.0)
    ## shiori's ghost dissapears

    window show
    n "There’s only the puddle now."

    $ ghost_shiori_1 = True

    return

label ghost_shiori_2:

    scene shire night with fade

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

    scene shrine night with fade
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
    show ghost_shiori normal at c_show_25 

    n "A-Aah, she's coming at you!"

    $ renpy.pause(1.0)

    # Blink flicker

    n "Wait, she's just staring...."
    #shiori blink animation

    n "Does she know you?"

    # Move closer
    show ghost_shiori normal at c_show_26 

    $ renpy.pause(1.0)

    # Disappear just before

    stop sound fadeout 1.0
    stop music fadeout 2.0

    n "She's gone..."

    $ ghost_shiori_3 = True
    return

label ghost_shiori_4:

    #scene bg shrine_empty with fade
    scene shrine night with fade

    n "No one is here."

    n "Someone is supposed to be here..."

    $ renpy.pause(2.0)

    stop music fadeout 1.0

    # Blackout
    #scene black with fade
    show black_screen with fade

    $ renpy.pause(2.5)

    # Whisper
    scene circle_ghost
    hide black_screen
    #play voice "sfx/whisper_staywithme.ogg"
    centered "S T A Y  W I T H  M E"

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

    return

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

    # Instead of the room, there’s a flickering room with the sound of a rattling doorknob.
    # Each click to “open” makes the rattling more frantic.
    # Shiori’s ghost sprite is shown with low opacity

    # shrine only for temporary
    scene shrine night with fade

    MC "I'm locked in."

    call screen ghost_shiori_5_open1()

    ## you click "open" image button

    ## rattling intensifies

    ## shiori's ghost appears with low opacity
    show ghost_shiori normal at c_show_28

    MC "Let me out!"

    call screen ghost_shiori_5_open2()

    ## you click "open" image button

    ## rattling intensifies

    ## shiori's ghost image creeps in

    show ghost_shiori normal at c_show_29

    MC "LET ME OUT!!!"

    ## you click "open" image button
    call screen ghost_shiori_5_open3()

    ## rattling intensifies

    ## shiori's ghost image creeps in
    show ghost_shiori normal at c_show_30

    MC "YoU ArE DEaD, I Ate YOu!"

    ## bam, everything stops
    #play sound bam
    #stop sound ratling
    hide ghost_shiori

    "..."

    $ ghost_shiori_5 = True
    return
