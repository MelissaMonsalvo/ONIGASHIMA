label prologue_trueend:

    play music "heavy breathing.mp3"

    n "{cps=18}It is dark.{/cps}"
    n "Something is caught in your throat. A {color=#ff0000}pool of blood{/color} lies at your feet."

    play sound "sfx/choke.wav"
    $ renpy.pause(0.8)

    n "Are you choking?"

    n2 "YeSSsSs~!"
    n2 "I aM, I aM! {w}cHokIng oN jOy, oN yOuR sOuNd!"
    n2 "[persistent.player_name]... yOu sPeAk aGaiN."

    n "What? I didn’t-- {w}I don’t know what you’re talking about."
    n "I don’t even... remember. Anything."
    n "Wh-who am I?"

    n2 "HhhhHHaaaahhh--sWeEt, lOsT. {w}FoRgOtTeN, wIpEd cLeAn."
    n2 "DoEsN’t MaTtEr. {w}YoU’Re hErE. {w}YoU’Re bAcK."
    n2 "tHaT’s EnOuGh."

    play sound "sfx/heartbeat_soft.ogg"
    $ renpy.pause(0.5)

    n "Back? {w}From where?"

    n2 "I bEgGeD fOr YoU."
    n2 "KaMi-sAmA lEt Me hEaR yOu AgAiN."

    n "Huh...?"
    n "Why would you want me?"

    n2 "So I dOn’T dIe oF sIlEnCe."
    n2 "So I cAn LiStEn."
    n2 "ThIs TiMe, I’ll sHuT uP. {w}OnLy YoU, [persistent.player_name]. {w}OnLy YoU cAn TalK."

    n "I don’t... I don’t even know who I am."

    n2 "YoU’Ll ReMeMbEr. {w}AnD iF nOt--{w}I'lL rEmEmBeR eNoUgH fOr Us BoTh."

    play sound "sfx/wind_cave.ogg"
    $ renpy.pause(1.0)

    n "..."

    n2 "KeEp tALkiNG, I'lL juSt LisTEn."

    n2 "ZiiIIIiiiiIIiIIip."

    n "Haah..."

    n "It’s time to return to our village."

    scene black
    with fade

    jump village_entrance
