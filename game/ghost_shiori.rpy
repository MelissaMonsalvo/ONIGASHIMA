############# GHOST ENCOUNTERS ###########################
label ghost_shiori_1:

    ## refelection and ghosts are in the ghosts folder

    n "You see yourself."

    # MC in front of glass/water reflection
    MC "..."

    window hide
    $ renpy.pause(1.0)

    # blinks animation

    ## then shiori’s ghost appears behind them

    MC "...?"

    $ renpy.pause(1.0)

    ## MC Blinks again

    n "...!"

    $ renpy.pause(1.0)


    ## shiori's ghost dissapears


    window show
    n "There’s only the puddle now."

    $ ghost_shiori_1 = True

    return

label ghost_shiori_2:


    #MC sleeping then eye opens (renpy eye blink pov dissolve) , suddenly shiori crawls into view, staring at you too long.
    # You don't know that you have to click, panic. So like, disable clicking for some uncomfortable seconds

    # Simulate first-person waking up with blinking
    show placeholder with in_eye
    $ renpy.pause(0.2)
    show placeholder with out_eye
    $ renpy.pause(0.2)
    show placeholder with in_eye
    $ renpy.pause(0.2)
    show placeholder with out_eye
    $ renpy.pause(0.2)

    # Silence, no dialogue yet
    window hide
    $ renpy.pause(1.5)

    # Eyes slowly open, fade in Shiori crawling from below
    # show shiori ghost >> ATL

    #play sound "sfx/crawl_scrape.ogg"
    #$ renpy.pause(2.0)

    # Shiori stares—clicking disabled here
    $ renpy.pause(6.5, hard=True)

    # SOME WHISPERING SFX

    # Only now allow input
    window show

    n "...Was that....?"

    n "...."

    #hide shiori ghost with dissolve
    #stop sound fadeout 1.5

    $ ghost_shiori_2 = True
    return


label ghost_shiori_3:

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

    n "A-Aah, she's coming at you!"

    $ renpy.pause(1.0)

    # Blink flicker

    n "Wait, she's just staring...."

    n "Does she know you?"

    # Move closer

    $ renpy.pause(1.0)

    # Disappear just before

    stop sound fadeout 1.0
    stop music fadeout 2.0

    n "She's gone..."

    $ ghost_shiori_3 = True
    return

label ghost_shiori_4:

    #scene bg shrine_empty with fade

    n "No one is here."

    n "Someone is supposed to be here..."

    $ renpy.pause(2.0)

    stop music fadeout 1.0

    # Blackout
    scene black with fade

    $ renpy.pause(2.5)

    # Whisper
    scene circle_ghost
    #play voice "sfx/whisper_staywithme.ogg"
    centered "S T A Y  W I T H  M E"

    # Flicker screen effect ATL

    $ renpy.pause(3.5)

    hide screen shrine_flicker
    stop sound fadeout 1.0

    window show
    n "..."

    return

    $ ghost_shiori_4 = True
    return

label ghost_shiori_5:

    # Instead of the room, there’s a flickering room with the sound of a rattling doorknob.
    # Each click to “open” makes the rattling more frantic.
    # Shiori’s ghost sprite is shown with low opacity

    MC "I'm locked in."

    ## you click "open" image button

    ## rattling intensifies

    ## shiori's ghost appears with low opacity

    MC "Let me out!"

    ## you click "open" image button

    ## rattling intensifies

    ## shiori's ghost image creeps in

    MC "LET ME OUT!!!"

    ## you click "open" image button

    ## rattling intensifies

    ## shiori's ghost image creeps in

    MC "YoU ArE DEaD, I Ate YOu!"

    ## bam, everything stops

    $ ghost_shiori_5 = True
    return
