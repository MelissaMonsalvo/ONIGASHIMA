label LI_intro_noyamato:

    scene village day:
        zoom 0.5
    with dissolve

    n "But of course, you don’t get far."

    show shi happy at shiori_skipp:
        xalign 0.44
    with dissolve
    pause 0.6
    stop sound
    pause 0.3
    show hik normal at hikaru_zoom, right
    with dissolve

    n "Because Shiori and Hikaru, your childhood friends find you."

    n "You grew up together, trained together, sat under the same tree together, and chased each other on the paddy fields."

    n "There were always four sets of muddy shoes by the door."

    n "Wait, four?"

    show yam normal at yamato_zoom, left:
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
    pause 0.3
    hide yam
    with dissolve

    n "...Wasn’t there one more?"

    n2 "The loud one."

    n "..."

    n2 "All muscle, gamey."

    show shi happyblush
    with dissolve

    shiori "Ehehe~ [persistent.player_name]-samaaa~!"

    shiori "You came back~! You didn’t explode or get squashed or turned into dough!"

    MC annoyed2 "Oi, rude. I’m tougher than I look."

    show hik happy
    with dissolve

    hikaru "Welcome home, [persistent.player_name]-san."

    n "There should be someone grumbling now, that you left to fight the Yamakui all by yourself..."

    n2 "That one stopped moving halfway down the throat."

    n "..."

    shiori "Ne ne~ Did Yamakui look like the legends? Big and scary? Lots of fangs? Or was it kinda cute~?"

    MC smug2 "I think it looked like it needed stabbing."

    show shi annoyed at shakey:
        xalign 0.44

    shiori "Muuuu, why are you so stingy, [persistent.player_name]???"

    show hik sad
    with dissolve

    hikaru "..."

    n "Silence falls when Shiori stops talking."

    n "Someone should have said something by now..."

    show shi happyblush at bounci:
        xalign 0.44

    shiori "You must be starving, [persistent.player_name]-sama. Shiori's gonna make alllll~ the food you want!"

    MC smugcl2 "{cps=35}How 'bout {/cps}{cps=5}venison?{/cps}"

    show shi surprised
    with dissolve

    shiori "Eh...? I don't think I have... {w}that...."

    show hik angry
    with dissolve

    hikaru "..."

    pause 0.5

    MC surprised2 "What is it?"

    hikaru "{w=0.5}...Do you feel like something’s missing?"

    MC nervous2 "Huh?"

    show hik angry
    with dissolve

    hikaru "I don’t know. I keep thinking there should be..."

    hikaru "{w=0.5}...four of us."

    MC sad2 "..."

    n "You-{w=0.1}I... {w}don’t know what to say."

    hikaru "...Forget it."

    show shi worried at shakey:
        xalign 0.44

    shiori "Ah, mou... Let's go eat before Hikaru is making odd theories again!"

    MC normal2 "Yeah, agreed."

    scene black
    show darken2
    with fade

    n "The fourth voice still doesn’t come."

    n "The armor clinks in your hand as you carry around with you behind Shiori and Hikaru."

    n "..."

    n "{cps=10}You wonder what venison tastes like, again.{/cps}"

    jump beforesecondloop
