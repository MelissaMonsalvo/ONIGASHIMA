############# GHOST ENCOUNTERS ###########################
label ghost_hikaru_1:

label hikaru_ghost_loveloop_unhinged:


    ##show hikaru's ghost zoooming very very slowly and distorts (use xzoom or yzoom for distortion)

    n "Huh? What is--"

    hikaru "...You came back."

    MC "Hikaru?"

    n "Who's that?"

    hikaru "You came back for me."

    hikaru "{cps=14}I missed you.{/cps}"

    n "Their voice is as soft as a lullaby."

    hikaru "I love you."

    n "..."

    mc "What?"

    hikaru "{cps=12}I lOvE yOu.{/cps}"

    hikaru "I lOvE yOu sO mUcH."

    hikaru "{cps=8}dOn’T gO AgAiN{/cps}"

    hikaru "{size=+6}{cps=6}StAY sTAY sTAY{/cps}{/size}"

    MC "Get away, you--"

    hikaru "{cps=5}{size=+8}I lOvE yOu—{/size}{/cps}"

    hikaru "{fast}{color=#111}I LOVE YOU I LOVE YOU ILOVEYOUILOVEYOUILOVE—{/color}{/fast}"

    mc "Stop it."

    hikaru "eVeRy DaY wIThOuT yOu FeLt LiKe—"

    hikaru "{size=+10}{cps=4}—hELL—{/cps}{/size}"

    hikaru "{color=#111}So sTAY{/color}"

    hikaru "{color=#000}sTAYsTAYsTAYsTAYsTAY{/color}"

    n "No—stop—"

    hikaru "{size=+12}{cps=2}I’M ALREADY INSIDE{/cps}{/size}"

    ## hikaru's ghost is at maximum zooming

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
    $ renpy.pause(1.0)

    n "..."

    n "Wait. {w}Was something—"

    hide hikaru ghost
    $ renpy.pause(0.2)

    # show hikaru's ghost moving fast across the screen
    $ renpy.pause(1.2)

    n "No. That’s nothing."

    n "You blink."

    hide hikaru ghost
    $ renpy.pause(0.2)

    # show hikatu's ghost blinking at the back fast
    $ renpy.pause(1.5)

    n "You swear something’s changed."

    n "You’d rewind, but…"

    n "You can’t."

    hide hikaru ghost
    $ renpy.pause(0.2)

    # Jumpscare position (sudden front face)
    ## screen shakes

    $ renpy.pause(0.5)

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

    hikaru "...Sshh. Don’t wake up yet."

    ## screen shakes as MC struggles

    n "You try to speak, lift your arms but can't--"

    hikaru "{cps=9}Bring back.{w=0.4} Bring back.{w=0.3} bring [persistent.player_name] back.{/cps}"

    $ renpy.pause(2.0)

    ## Fake choices appear but can't be picked : "Pull their hands away" "Kick them"
    ## giving the sense of helplessness

    MC "I-I can't do anything!!!!"

    hikaru "{size=+8}{cps=5}You're wearing their skin, aren't you?{/cps}{/size}"

    n "You can’t breathe."

    $ renpy.pause(1.5)

    ## gone again

    MC "Hahhh--!"

    n "They're gone..."

    return

    $ ghost_hikaru_3 = True

    return

label ghost_hikaru_4:


    n "You’re dreaming again..."

    n "It's that person again. You called them Hikaru."

    n "Their face looks normal this time, hair swaying under the wind."

    hikaru "...Hey."

    hikaru "I was waiting. You said you'd be back."

    mc "I am back."

    hikaru "...No."

    n "The edges of their face blur... Slowly... Slowly..."

    n "The lines slide off... Again... Again..."

    hikaru "{cps=12}Why are you wearing their face?{/cps}"

    mc "What?"

    hikaru "{cps=10}Who are you?{/cps}"

    n "Their nose flattens, then the skin peels."

    n "A hard ridge pushes forward."

    n "Beak."

    n "Mask."

    n "You can't make the edges anymore."

    hikaru "{cps=9}I know that voice, but not that look...{/cps}"

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
    show hikaru ghost at Position(xpos=0.5, ypos=0.85, xanchor=0.5, yanchor=1.0)
    $ renpy.pause(1.0)

    MC "...Hikaru?"

    n "No answer."

    n "You walk forward. Slowly."

    show hikaru ghost at Position(xpos=0.5, ypos=0.85) with move
    $ renpy.pause(2.0)

    n "It still follows you with the same pace and rythm."

    n "You try to speak again. Nothing comes out."

    $ renpy.pause(2.0)

    n "You walk faster."

    play sound "sfx/steps_dirt.ogg"
    show hikaru ghost at Position(xpos=0.5, ypos=0.85) with move
    $ renpy.pause(1.5)

    n "They're still there."

    n "You stop. So do they."

    n "You check your shadow."

    n "You can’t see it."

    n "There's a pair of wings on your shadow."

    ## show hikaru's ghost but only shadowed

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
