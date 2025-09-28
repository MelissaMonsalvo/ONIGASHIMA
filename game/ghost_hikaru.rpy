############# GHOST ENCOUNTERS ###########################
label ghost_hikaru_1:



    ##show hikaru's ghost zoooming very very slowly and distorts (use xzoom or yzoom for distortion)
    #show ghost_hikaru_idle at show_1
    #show ghost_hikaru_idle at Glitch(_fps=12., color_range1="c00a", color_range2="f00", glitch_strength=.5)
    #show ghost_hikaru_idle at show_1
    scene forest day:
        zoom 0.5
    show ghost_hikaru idle at c_show_3 behind darken2
    show darken2
    play music "spooky.mp3"

    n "Huh? What is–"

    hikaru "...You came back."

    MC shocked "Hikaru?"

    n "Who's that?"

    hikaru "You came back for me."

    hikaru "{cps=14}I missed you.{/cps}"

    n "Their voice is as soft as a lullaby."

    hikaru "I love you."


    show ghost_hikaru idle at c_show_5

    n "..."

    MC "What?"

    hikaru "{cps=12}I lOvE yOu.{/cps}"

    hikaru "I lOvE yOu sO mUcH."

    hikaru "{cps=8}dOn’T gO AgAiN{/cps}"

    hikaru "{size=+6}{cps=6}StAY sTAY sTAY{/cps}{/size}"

    MC "Get away, you–"

    show ghost_hikaru idle at c_show_6

    hikaru "{cps=5}{size=+8}I lOvE yOu–{/size}{/cps}"

    hikaru "{cps=16}I LOVE YOU I LOVE YOU ILOVEYOUILOVEYOUILOVE–{/cps}"

    MC "Stop it."

    hikaru "eVeRy DaY wIThOuT yOu FeLt LiKe–"

    hikaru "{size=+10}{cps=4}–hELL–{/cps}{/size}"

    show ghost_hikaru idle at c_show_2

    hikaru "So sTAY wITh Me"

    hikaru "sTAYsTAYsTAYsTAYsTAY"

    n "No–stop–"

    hikaru "{size=+12}{cps=2}I’M ALREADY INSIDE{/cps}{/size}"

    play sound "sfx/screech.mp3"

    ## hikaru's ghost is at maximum zooming
    show ghost_hikaru idle at c_show_4

    $ renpy.pause(1.5)

    stop sound

    scene black
    with dissolve

    ## hikaru's ghost is gone

    n "No one is there."




    $ ghost_hikaru_1 = True

    #return

label ghost_hikaru_2:

    $ config.rollback_enabled = False
    scene shrine night:
        zoom 0.6
        xalign 0.5
        linear 0.3 zoom 0.5
    play music "Friends.mp3"

    n "You step inside."

    n "Empty. {w}Still. {w}No windows open."

    # show hikaru's ghost at far corner
    show ghost_hikaru idle at c_show_7

    $ renpy.pause(1.0)

    n "..."

    n "Wait. {w}Was something–"

    #hide hikaru ghost
    hide ghost_hikaru

    $ renpy.pause(0.2)

    # show hikaru's ghost moving fast across the screen
    show ghost_hikaru idle at c_show_8
    pause 0.1

    hide ghost_hikaru idle

    n "No. That’s nothing."

    with fade

    n "You blink."

    hide ghost_hikaru

    $ renpy.pause(0.2)

    # show hikaru's ghost blinking at the back fast
    show ghost_hikaru idle at c_show_12
    #$ renpy.pause(1.5)

    n "You swear something’s changed."

    n "You’d rewind, but…"

    n "You can’t."

    hide ghost_hikaru
    $ renpy.pause(0.2)

    # Jumpscare position (sudden front face)
    play sound "sfx/jumpscare.mp3"
    show ghost_hikaru idle at c_show_9 with vpunch

    ## screen shakes

    #$ renpy.pause(0.5)

    ## disappears

    stop music fadeout 2.0

    n "..."

    n "Nothing's there."

    $ config.rollback_enabled = True

    $ ghost_hikaru_2 = True

    #return

label ghost_hikaru_3:

    play music "Friends.mp3"

    $ haze_active = True
    show haze_effect at haze_transform
    with dissolve


    n "You’re dreaming..."

    $ renpy.pause(1.5)

    MC shocked "Ghkk–!"

    with sshake
    n "There are hands around your throat."

    ## show hikaru's ghost above you (top down view)
    show ghost_hikaru idle at c_show_10

    hikaru "...Sshh. Don’t wake up yet."

    ## screen shakes as MC struggles
    show ghost_hikaru idle with vpunch

    n "You try to speak, lift your arms but can't–"

    hikaru "{cps=9}Bring back.{w=0.4} Bring back.{w=0.3} Bring [persistent.player_name] back.{/cps}"

    $ renpy.pause(2.0)

    ## Fake choices appear but can't be picked : "Pull their hands away" "Kick them"
    ## giving the sense of helplessness
    menu:

        "Pull their hands away":
            "Nothing happend."
        "Kick them":
            "Nothing happend."
    label ghost_hikaru_3_next:

    MC hurt "I-I can't do anything!!!!"

    hikaru "{size=+8}{cps=5}You're wearing their skin, aren't you?{/cps}{/size}"

    n "You can’t breathe."

    $ renpy.pause(1.5)

    $ haze_active = False
    hide haze_effect
    with dissolve

    ## gone again
    show ghost_hikaru idle at c_show_11

    MC "Hahhh–!"

    scene black
    hide screen drunk_haze
    with sshake

    pause 0.1

    n "They're gone..."


    $ ghost_hikaru_3 = True

    #return

label ghost_hikaru_4:


    play music "Friends.mp3"

    scene white_bg

    $ haze_active = True
    show haze_effect at haze_transform
    with dissolve
    n "You’re dreaming again..."

    show hik happy:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0
    with dissolve

    n "It's that person again. You called them Hikaru."

    n "Their face looks normal this time, hair swaying in the wind."

    hikaru "...Hey."

    hikaru "I was waiting. You said you'd be back."

    MC sad "I am back."

    hikaru "...No."

    show hik happy:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.5 blur 2

    n "The edges of their face blur... {w=0.1}Slowly... {w=0.1}Slowly..."

    show hik happy:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.5 blur 10

    n "The lines slide off... {w=0.1}Again... {w=0.1}Again..."

    hikaru "{cps=12}Why are you wearing their face?{/cps}"

    MC "What?"

    hikaru "{cps=10}Who are you?{/cps}"

    hikaru "{cps=9}I know that voice, but not that look...{/cps}"

    hide hik
    show ghost_hikaru idle:
        zoom 0.32
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.5 blur 2
    with in_212

    n "Their mouth stretches wide, then clamps shut as their bones starts to warp."

    hikaru "{cps=8}You’re not them. {/cps}{w=0.3}{cps=5}You’re nOt Them–{/cps}"

    n "The serene face you knew is gone."

    play sound "sfx/screech.mp3"

    hikaru "{size=+8}{cps=6}Give [persistent.player_name] BACK.{/cps}{/size}"

    with sshake

    hikaru "{size=+12}{cps=4}GIVE–[persistent.player_name] –BACK–{/cps}{/size}"
    scene black
    with sshake

    $ haze_active = False
    hide haze_effect
    with dissolve



    n "..."

    n "You wake up with your ears still ringing."

    $ ghost_hikaru_4 = True

    return

label ghost_hikaru_5:

    show village night at walkinn:

        zoom 0.6
        xalign 0.5
        yalign 0.5



    play sound "sfx/walk grass.mp3"
    pause 0.4

    n "You’re walking home."

    n "You don’t know why it’s this path again."

    n "The sun dipped quickly, so you didn’t notice until it was gone."

    play muzak "sfx/walk grass.mp3"

    n "..."

    stop sound

    n "You hear it."
    play music "sfx/walk grass.mp3"

    n "A second pair of footsteps."

    n "Every time your heel hits the stone, something echoes behind it."

    $ renpy.pause(2.0)

    stop music
    stop muzak

    show village night:

        zoom 0.6
        xalign 0.5
        yalign 0.5

    n "You stop walking."

    MC surprised2 "...?"

    n "It stops too."

    MC  "Hello...?"

    n "Silence."

    with vpunch

    n "You turn around."

    n "No one."

    with vpunch

    n "You turn back."

    play sound "sfx/whip.mp3"
    show ghost_hikaru idle:
        zoom 0.23
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

    $ renpy.pause(1.0)

    MC "...Hikaru?"

    n "No answer."

    show village night at walkinn:

        zoom 0.6
        xalign 0.5
        yalign 0.5

    n "You walk forward. Slowly."

    play muzak "sfx/walk grass.mp3"


    #show hikaru ghost at Position(xpos=0.5, ypos=0.85) with move
    show ghost_hikaru idle:
        zoom 0.23
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.5 zoom 0.28
    $ renpy.pause(2.0)

    n "It still follows you with the same pace and rhythm."

    n "You try to speak again. Nothing comes out."

    $ renpy.pause(2.0)

    #show hikaru ghost at Position(xpos=0.5, ypos=0.85) with move
    show ghost_hikaru idle:
        zoom 0.28
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.5 zoom 0.32
    $ renpy.pause(1.5)

    play music "sfx/walk grass.mp3"

    n "They're still there."

    show village night:

        zoom 0.6
        xalign 0.5
        yalign 0.5
    show ghost_hikaru idle:
        zoom 0.32
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.5 zoom 0.32
    $ renpy.pause(1.5)

    stop sound
    stop music
    stop muzak

    n "You stop. So do they."

    scene black

    centered "{cps=10}I A M A L W A Y S W I T H Y O U {/cps}"

    $ renpy.pause(3.0)


    $ ghost_hikaru_5 = True

    return
