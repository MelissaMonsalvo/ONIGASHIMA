label LI_intro_noshiori:

    n "But of course, you don't get far."

    show yam normal at yamato_zoom, left
    with dissolve
    pause 0.3
    show hik normal at hikaru_zoom, right
    with dissolve

    n "Because Yamato and Hikaru find you, they are your childhood friends–"

    n "Wait a second."

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xoffset -40
        yzoom 1.0
        xzoom 1.0
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.04 alpha 0.1 xoffset 12
        linear 0.04 alpha 1.0 xoffset 0
        linear 0.05 alpha 0.25 xoffset -14
        linear 0.04 alpha 1.0 xoffset 0
        repeat 3

        parallel:
            linear 0.07 alpha 0.1
            linear 0.12 alpha 0.0
        parallel:
            linear 0.09 xoffset 25
            linear 0.10 xoffset -22
            linear 0.05 xoffset 0
    pause 0.5
    hide shi

    n "Wasn’t there {glitch}someone else?{/glitch}"

    n "You remember the rice paddies, the muddy sandals, the laughters and the paper effigies–"

    n "Someone used to hang up those paper effigies."

    n "There were four of you. Weren’t there {glitch}four?{/glitch}"

    play sound "sfx/walk grass.mp3"

    show yam annoyed
    with dissolve

    yamato "Tch. Look who finally shows up."

    show hik happy
    with dissolve

    hikaru "Welcome home, [persistent.player_name]-san."

    MC smug2 "Oi. That how you greet a hero?"

    yamato "Hero my ass. Ya ran off alone, idiot."

    MC smugcl2 "C’mon, tradition is tradition. Oni Slayer always goes solo."

    yamato "Fuckin' tradition..."

    n "Wait... {w}There should be another voice now, someone who usually teases Yamato..."

    n "No, wait... {w}Not Hikaru... {w}Hikaru's a quiet person."

    n "..."

    show hik worried
    with dissolve

    hikaru "...Didn’t you forget something, [persistent.player_name]?"

    MC surprised2 "Huh? What, like a souvenir? I brought the armor, didn’t I?"

    hikaru "...I see."

    n "Hikaru’s voice lowers, eyes drifting slowly to the armor."

    show hik angry
    with dissolve

    hikaru "...It's rather small for something like the Yamakui, isn’t it?"

    MC nervous2 "...What?"

    show yam serious
    with dissolve

    yamato "Oi. What’s that supposed t' mean?"

    hikaru "...Forget it."

    n "The silence stretches again."

    n "Someone should occupy this space right there."

    n "Someone should've said something to fill the quiet."

    n "But no one else is there but the three of you."

    n2 "...She is {w}D E A D."

    show hik angry behind darken:

        zoom 0.231
        yoffset 460

        linear 0.4 xzoom -1 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
    pause 0.2
    hide hik with dissolve

    play sound "sfx/walk grass.mp3"
    pause 0.4
    stop sound fadeout 1.0

    n "Hikaru shrugs, turns and walks away."

    MC sad2 "...Hikaru?"

    show yam annoyed
    with dissolve

    yamato "Tch, whatever."


    hide yam with dissolve

    play sound "sfx/walk grass.mp3"
    pause 0.4
    stop sound fadeout 1.0


    n "Yamato follows. The empty space between you seems larger now."

    scene black
    show darken2
    with fade

    n "You look down at the armor, it feels heavier. Your fingers ache from holding it."

    n "You thought you cleaned it better."

    n2 "But we both know this is not mine."

    jump beforesecondloop
