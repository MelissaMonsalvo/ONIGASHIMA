############# GHOST ENCOUNTERS ###########################
label ghost_hikaru_1:

label hikaru_ghost_loveloop_unhinged:


    ##show hikaru's ghost zoooming very very slowly and distorts (use xzoom or yzoom for distortion)
    #show ghost_hikaru_idle at show_1
    #show ghost_hikaru_idle at Glitch(_fps=12., color_range1="c00a", color_range2="f00", glitch_strength=.5)
    #show ghost_hikaru_idle at show_1
    show ghost_hikaru idle at c_show_3

    n "Huh? What is--"

    hikaru "...You came back."

    MC "Hikaru?"

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

    MC "Get away, you--"

    show ghost_hikaru idle at c_show_6

    hikaru "{cps=5}{size=+8}I lOvE yOu—{/size}{/cps}"

    hikaru "{cps=16}{color=#111}I LOVE YOU I LOVE YOU ILOVEYOUILOVEYOUILOVE—{/color}{/cps}"

    MC "Stop it."

    hikaru "eVeRy DaY wIThOuT yOu FeLt LiKe—"

    hikaru "{size=+10}{cps=4}—hELL—{/cps}{/size}"

    show ghost_hikaru idle at c_show_2

    hikaru "{color=#111}So sTAY{/color}"

    hikaru "{color=#000}sTAYsTAYsTAYsTAYsTAY{/color}"

    n "No—stop—"

    hikaru "{size=+12}{cps=2}I’M ALREADY INSIDE{/cps}{/size}"

    ## hikaru's ghost is at maximum zooming
    show ghost_hikaru idle at c_show_4

    $ renpy.pause(1.5)

    ## hikaru's ghost is gone

    n "No one is there."

    return


    $ ghost_hikaru_1 = True

    return

label ghost_hikaru_2:

    $ config.rollback_enabled = False
    scene bg empty_room_dark with fade
    play music "bgm/lowhum.ogg" fadein 2.0

    n "You step inside."

    n "Empty. {w}Still. {w}No windows open."

    # show hikaru's ghost at far corner
    show ghost_hikaru idle at c_show_7

    $ renpy.pause(1.0)

    n "..."

    n "Wait. {w}Was something—"

    #hide hikaru ghost
    hide ghost_hikaru

    $ renpy.pause(0.2)

    # show hikaru's ghost moving fast across the screen
    show ghost_hikaru idle at c_show_8

    n "No. That’s nothing."

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
    show ghost_hikaru idle at c_show_9 with vpunch

    ## screen shakes

    #$ renpy.pause(0.5)

    ## dissapears

    stop music fadeout 2.0

    n "..."

    n "Nothing's there."

    $ config.rollback_enabled = True

    $ ghost_hikaru_2 = True

    return

label ghost_hikaru_3:


    n "You’re dreaming..."

    $ renpy.pause(1.5)

    MC "Ghkk--!"

    play sound "sfx/soft_choke.ogg"

    n "There are hands around your throat."

    ## show hikaru's ghost above you (top down view)
    show ghost_hikaru idle at c_show_10

    hikaru "...Sshh. Don’t wake up yet."

    ## screen shakes as MC struggles
    show ghost_hikaru idle with vpunch

    n "You try to speak, lift your arms but can't--"

    hikaru "{cps=9}Bring back.{w=0.4} Bring back.{w=0.3} bring [persistent.player_name] back.{/cps}"

    $ renpy.pause(2.0)

    ## Fake choices appear but can't be picked : "Pull their hands away" "Kick them"
    ## giving the sense of helplessness
    menu:
        MC "What should i do?"

        "Pull their hands away" :
            "Nothing happend."
            menu:
                MC "What should i do?"
                "Pull their hands away" :
                    "Nothing happend."
                    jump ghost_hikaru_3_next
                "Kick them":
                    "Nothing happend."
                    jump ghost_hikaru_3_next
        "Kick them":
            "Nothing happend."
            menu:
                MC "What should i do?"
                "Pull their hands away" :
                    "Nothing happend."
                    jump ghost_hikaru_3_next
                "Kick them":
                    "Nothing happend."
                    jump ghost_hikaru_3_next

    label ghost_hikaru_3_next:

    MC "I-I can't do anything!!!!"

    hikaru "{size=+8}{cps=5}You're wearing their skin, aren't you?{/cps}{/size}"

    n "You can’t breathe."

    $ renpy.pause(1.5)

    ## gone again
    show ghost_hikaru idle at c_show_11

    MC "Hahhh--!"

    n "They're gone..."

    return

    $ ghost_hikaru_3 = True

    return

label ghost_hikaru_4:

    show normal_hikaru normal at c_show_15

    n "You’re dreaming again..."

    n "It's that person again. You called them Hikaru."

    n "Their face looks normal this time, hair swaying under the wind."

    hikaru "...Hey."

    hikaru "I was waiting. You said you'd be back."

    MC "I am back."

    hikaru "...No."

    n "The edges of their face blur... Slowly... Slowly..."

    n "The lines slide off... Again... Again..."

    hikaru "{cps=12}Why are you wearing their face?{/cps}"

    MC "What?"

    hikaru "{cps=10}Who are you?{/cps}"

    n "Their nose flattens, then the skin peels."

    n "A hard ridge pushes forward."

    n "Beak."

    n "Mask."

    n "You can't make the edges anymore."

    hikaru "{cps=9}I know that voice, but not that look...{/cps}"

    show normal_hikaru normal at c_show_16
    show ghost_hikaru attack at c_show_17
    ## hikaru's normal sprite dissolves to their ghost sprite slowly
    ## you can check dissolve.rpy for the transition you like

    n "Their mouth stretches wide, then clamps shut as their bones starts to warp."

    hikaru "{cps=8}You’re not them. {/cps}{w=0.3}{cps=5}You’re nOt Them—{/cps}"

    n "The serene face you knew is gone."

    hikaru "{size=+8}{cps=6}Give [persistent.player_name] BACK.{/cps}{/size}"

    hikaru "{size=+12}{cps=4}GIVE—[persistent.player_name] —BACK—{/cps}{/size}"

    play sound "sfx/screech.ogg"

    n "..."

    n "You wake up with your ears still ringing."

    $ ghost_hikaru_4 = True

    return

label ghost_hikaru_5:

    play sound "sfx/footsteps_slow.ogg"

    n "You’re walking home."

    n "You don’t know why it’s this path again."

    n "The sun dipped quickly, so you didn’t notice until it was gone."

    play sound "sfx/second_steps.ogg"

    n "..."

    n "You hear it."

    n "A second pair of footsteps"

    n "Every time your heel hits the stone, something echoes behind it."

    $ renpy.pause(2.0)

    n "You stop walking."

    MC "...?"

    stop sound fadeout 1.0
    $ renpy.pause(1.0)

    n "It stops too."

    MC  "Hello...?"

    n "Silence."

    n "You turn around."

    n "No one."

    $ renpy.pause(1.0)

    n "You turn back."

    play sound "sfx/air_cut.ogg"
    show ghost_hikaru idle at c_show_18
    $ renpy.pause(1.0)

    MC "...Hikaru?"

    n "No answer."

    n "You walk forward. Slowly."

    #show hikaru ghost at Position(xpos=0.5, ypos=0.85) with move
    show ghost_hikaru idle at c_show_19
    $ renpy.pause(2.0)

    n "It still follows you with the same pace and rythm."

    n "You try to speak again. Nothing comes out."

    $ renpy.pause(2.0)

    n "You walk faster."

    play sound "sfx/steps_dirt.ogg"
    #show hikaru ghost at Position(xpos=0.5, ypos=0.85) with move
    show ghost_hikaru idle at c_show_20
    $ renpy.pause(1.5)

    n "They're still there."

    n "You stop. So do they."

    n "You check your shadow."

    n "You can’t see it."

    n "There's a pair of wings on your shadow."

    ## show hikaru's ghost but only shadowed
    hide ghost_hikaru with fade
    show ghost_hikaru normal at c_show_21:
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))


    $ renpy.pause(2.0)

    play sound "sfx/heartbeat_slow.ogg"
    scene black with fade
    $ renpy.pause(2.0)

    n "..."

    scene black

    centered "I A M A L W A Y S W I T H Y O U "

    $ renpy.pause(3.0)


    $ ghost_hikaru_5 = True

    return
