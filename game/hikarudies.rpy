label LI_intro_nohikaru:

    scene village day:
        zoom 0.5
    with dissolve

    n "But of course, you don’t get far."

    show shi normal at shiori_skipp:
        xalign 0.44
    with dissolve
    pause 0.6
    stop sound
    show yam normal at yamato_zoom, left
    with dissolve
    pause 0.3

    n "Because Shiori and Yamato find you."

    n "Your childhood friends. {w}Two of them?"

    show hik normal at hikaru_zoom, right:

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
    hide hik

    n "{w=0.3}...Weren’t there more? {glitch}You cared for them more than the others...{/glitch} {w}didn't you?"

    n "Yes, you remember the rice paddies, muddy ankles, chasing cats and sparring...."

    n "Didn't one of you never talk much?"

    n "Who was it?"

    n2 "{blur}The mushy one.{/blur}"

    n "..."

    show shi happyblush
    with dissolve

    shiori "Ehehe~ [persistent.player_name]-samaaa~!"

    shiori "You came back~! I was so sure you'd get squished into pancake mochi~!"

    MC annoyed2 "Oi, rude. I’m not that easy to mash."

    show yam annoyed
    with dissolve

    yamato "Hnh. Coulda fooled me, dumbass. Leavin’ us without a word, ya promised ya'd bring me along!"

    MC smugcl2 "C’mon, you know how it is. Oni Slayer tradition."

    yamato "Tradition is for corpses."

    show shi annoyed at shakey:
        xalign 0.44

    shiori "Mou~ Yamato-kun is just mad he didn’t get to do anything cool~"

    yamato "Tch. I stayed behind t’guard the goddamn village."

    show shi smug
    with dissolve

    shiori "Did you now? Aren't you just sulky [persistent.player_name] didn't bring you along?"

    n "There should be someone cutting into this conversation right now, someone who observes, someone who is–"

    n2 "–Tender "

    n "...What?"

    n2 "{cps=25}Soft around the ribs.{/cps}"

    n "..."

    show shi happy
    with dissolve

    shiori "Ne ne~ [persistent.player_name]-sama! You have to tell us what Yamakui looked like! Did it have fangs? Big claws? Did it talk?"

    MC nervous2 "Uh... Big. Yeah. Bloody. And...."

    hide shi happy
    show shi yansm:
        zoom 0.26
        yalign -0.60
        yoffset 0
        xalign 0.44
        parallel:
            easein 0.4 zoom 0.34 yalign -0.1
            easeout 0.4 zoom 0.26 yalign -0.60

    shiori "{sc=1}Beau~tiful?{/sc}"

    n2 "Hah."

    MC surprised2 "...What?"

    show yam angry
    with dissolve

    yamato "Oi, cut it out."

    show shi happy
    with dissolve

    shiori "What~? I’m just sayin’! Maybe Yamakui-sama's got a pretty face!"

    yamato "Damn Oni's got teeth, that's what."

    n "They bicker again, but something is missing. {i}Someone{/i} is missing."

    n "There was four of you. {i}You’re sure of it.{/i}"

    n "{w=0.3}...Right?"

    MC normal2 "Yeah, whatever they looked like now, it doesn't matter now."

    show yam annoyed
    with dissolve

    yamato "Tch. Ain’t like I’m complainin’. Ya came back in one piece."

    show shi surprised
    with dissolve

    shiori "Especially not clean like that~ {w}Not even a scratch on you!"

    show yam smug
    with dissolve

    yamato "Almost like ya ain’t fought anything at all, eh?"

    MC happycl2 "Ehh, just got lucky that's all!"

    yamato "What, damned Oni bonked their head on a stone and dropped dead?"

    MC nervous2 "{k=-1}Something like that, yeah...!{/k}"


    n "Yamato and Shiori says nothing else, but their smile fade as yours does."
    scene black
    show darken2
    with fade

    n "You look down at the armor."

    n "You thought you cleaned it better."

    jump beforesecondloop
