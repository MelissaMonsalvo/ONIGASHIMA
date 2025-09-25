label loop3_shiori:

    scene village day:
        zoom 0.5
    show darken

    play sound "Sfx/walk grass.mp3"
    show shi happy behind darken:
        zoom 0.023
        xanchor 0.05
        xalign 0.63
        yalign 0
        yoffset 450
        xoffset 0
    with dissolve
    pause 0.3
    show shi happy behind darken:
        zoom 0.1
        xanchor 0.05
        xalign 0.63
        yalign 0
        yoffset 400
        xoffset 0
    with dissolve
    pause 0.3
    show shi happyblush behind darken:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 200
        xoffset -40
    with dissolve
    stop sound
    stop music
    stop muzak

    shiori "[persistent.player_name]-samaaaaa~"

    play music "Tense.ogg"

    n2 "..."

    n2 "ThAt's tHE stRiNgy oNe."

    n2 "STrAnGE. {w} sHe’S smILiNg."

    show shi happyblush behind darken:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 200
        xoffset -40

        linear 0.13 yoffset 180 zoom 0.315
        linear 0.09 yoffset 120 zoom 0.28
        linear 0.10 yoffset 100 zoom 0.307
        linear 0.08 yoffset 200 zoom 0.3

        pause 0.08

    shiori "Ahaha~ I knew it, I knew you'd come back~!"

    n "Shiori?"

    n "Why do you speak like that to the Yamakui...?"

    show shi yansmbl
    with dissolve

    shiori "Aaaah~ You look soooo different now~"

    shiori "Did you cut your hair? Your face? Your whole, um... body?"

    n2 "sHE DoEs NOT cAre."

    shiori "Let’s meet at the shrine when the red moon comes, okay~?"

    shiori "I have something special to show you, [persistent.player_name]-sama."

    n2 "SHe sMeLLs rEADY."


    show shi yansmbl behind darken:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 200
        xoffset -40

        linear 0.14 xoffset 40 yoffset 100 zoom 0.2

        linear 0.12 xoffset 120 yoffset 300 zoom 0.15

        linear 0.13 xoffset 230 yoffset 300 zoom 0.1 alpha 0.0

    play sound "sfx/run.mp3"

    n2 "tHE MeAT rUns."

    scene moon1
    with fade

    stop sound

    n2 "tHe sHiNe iS nOt rEd."

    n2 "nOt yEt."

    scene moon2
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "tHe dAyS mElTs AwAY."

    scene moon3
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "LiKe thIs sKiN."

    scene moon4
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "lAstEd lOngEr tHaN i tHouGhT."

    scene moon5
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "BuT It DrAgS wHeN i wALk NoW"

    scene moon6
    with flashred
    play sound "sfx/heartbeat.mp3"
    pause 0.6
    with fade

    n2 "BuT iT’s tiMe."

    n2 "tHe mOon hUngErS. {w}i hUnGer."

    n2 "OnCe mOrE. {w} oNe moRe. {w} lAsT cOuRsE."

    n "..."

    n "There’s nothing left to hold on to."

    n2 "ThErE’s oNe mOrE."

    n2 "tHe sTrIngY oNe."

    n2 "She saId shRinE. {w} oFfErIng."

    n2 "aNd tHe sHiNe tUrnS rEd, {w} anY mOMenT nOw~"

    n "She is waiting for you."

    n "{w=0.1}...She always does."

    n "Why didn't I realize sooner?"

    n "That Shiori was always in love with--{nw}"

    stop music

    scene black

    with fade

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THE RED MOON IS HERE{/color}{/atl}{/color}"

    with fade

    pause 0.5

    scene moon6
    with fade
    pause 0.2
    scene moon7
    with fade

    stop sound

    scene black
    with fade

    pause 0.5

    n2 "It’s tImE."

    n2 "tHe mOon bUrNs dOwN to mE. {w} mE. {w} mE. {w} mEeEEEeeEe."

    scene shrine night:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.5
    with in_212

    show shi yansmbl:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.35
        xalign 0.4
        yoffset 0
    show darken2
    with dissolve

    play music "Goodbye.mp3"

    shiori "{sc=1}Aaaah~ {/sc}You’re here."

    shiori "{i}My love~ My everything~{/i}"

    n2 "..."

    n2 "ShE cAlLs mE LoVe?{w=0.1}"

    shiori "You came for me, Yamakui-sama. Even though your body is all~ {w}broken and bloody and {sc=1}peeeeling~{/sc}"

    shiori "{sc=5}Ehehe~{/sc} I’m ready, Yamakui-sama."

    MC yan3 "dO yOu eVen knOw wHAt YoU aRE ReadY For?"

    shiori "Of course I do~ You’ve been so patient."

    show shi yansmbl:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.35
        xalign 0.4
        yoffset 0

        linear 0.32 zoom 0.365 xalign 0.405 yoffset -8

        pause 0.08

    shiori "{cps=13}Waiting, waiting...{/cps}{w=0.2} and I was always watching you, you know~?"

    n "..."

    shiori "{i}Even back when you were still pretending to be someone else.{/i}"

    shiori "But I saw you. {w=0.1}Even back then."

    show shi yan:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.365
        xalign 0.405
        yoffset -8

        linear 0.28 zoom 0.373 xalign 0.408 yoffset -12

        pause 0.09

    shiori "{glitch=5}All those people ran away and called you a monster.{/glitch}"


    show shi yansmbl
    with dissolve

    shiori "But not {sc=5}me~{/sc}"

    shiori "Because love doesn’t scream when it sees the truth~"

    show shi yansmbl:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.373
        xalign 0.408
        yoffset -12

        linear 0.24 zoom 0.378 xalign 0.411 yoffset -15

        pause 0.09

    shiori "You can have me now."

    shiori "{cps=15}You’ve been hungry, haven’t you~?{/cps}"

    show shi yansmbl:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.378
        xalign 0.411
        yoffset -15

        linear 0.23 zoom 0.382 xalign 0.414 yoffset -17

        pause 0.09

    shiori "Shiori will{w=0.1} make the hunger stop."

    shiori "{i}I’ll fill the part that hurts.{/i}"

    show shi yansmbl:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.382
        xalign 0.414
        yoffset -17

        linear 0.21 zoom 0.41 xalign 0.42 yoffset -30

        pause 0.08

        linear 0.23 zoom 0.44 xalign 0.38 yoffset -41

        pause 0.11

    shiori "{sc=1}Because I {i}love{/i} you.{/sc}"

    n2 "..."

    n "{cps=12}No.{/cps}"

    MC "{i}YeS.{/i}"

    MC "{i}tO lOvE iS tO cOnSuMe.{/i}"

    shiori "Ehehe~ {w} I knew you’d choose me."

    shiori "I’ll be with you {w}always."

    n2 "i’LL sHut yOu uP. {w}kEeP yOu iNsiDe AND {w} lOve yoU {w}fRoM tHe iNsiDe oUt."

    shiori "Ne, {w=0.2}Yamakui-sama..."

    shiori "Do you remember the first time we met~?"

    n2 "..."

    shiori "It was dark, I was brought to the forest to die alone."

    shiori "I couldn't remember the priests's face, so I'm sure you ate him... {w}or her? Ah, that doesn't matter anymore."

    shiori "The rope scratched my skin, I was hurt all over."

    shiori "The priest was dragging me up the mountain, saying something about... {w}offerings, maybe?"

    n2 "..."

    shiori "But you came out."

    shiori "You never once looked at me..."

    shiori "Even though I was an easy meal, {w=0.2}even though I was bound and bleeding..."

    $ renpy.pause(0.3)

    shiori "But you ate them instead. {w=0.2}The sinner, {w=0.2}the evil person."

    n "..."

    shiori "I remember standing there and watched... {w}I think I watched you eat."

    shiori "And I thought... {w}you were {i}beautiful.{/i} You saved my life. You only eat those who did wrongdoings!"

    shiori "So I decided, right there... {w}that I would love you."

    shiori "Forever and ever."

    n2 "YoU aRe... {w}sTrAnGe."

    shiori "So are you~"

    shiori "But strange things need each other, right?"

    n2 "..."

    shiori "Eat me if you want. Or {glitch}don't.{/glitch}"

    shiori "But I’ll still love you regardless~"

    stop music

    n2 "..."

    MC happy3 "HhhHhaHhhAHaHhhHAH~"

    play music "noinomai.mp3"

    with sshake

    MC happy3 "YoU thInK i SpArEd yOu bEcAuse i cArEd?"

    shiori "..."

    MC happy3 "ChiLd mEaT tAstEs DisGuStINg."

    MC happy3 "UnRiPE."

    MC happy3 "BlAaaaaAAAaaanD."

    MC happy3 "i aTe tHe prIeSt."

    play sound "sfx/gulp.wav"
    with flashred

    MC happy3 "BeCAuSe iT TasTED BEttER."



    show shi fear:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.44
        xalign 0.38
        yoffset -41

        linear 0.12 zoom 0.31 xalign 0.45 yoffset 4

        pause 0.13

        linear 0.09 zoom 0.3 xalign 0.43 yoffset 8

        pause 0.10
    with vpunch

    shiori "..."


    shiori "{sc=5}Ah...{/sc}"

    show shi yansm:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.3
        xalign 0.43
        yoffset 8

        linear 0.08 yoffset -3 zoom 0.308
        linear 0.09 yoffset 13 zoom 0.294
        linear 0.08 yoffset 8 zoom 0.3

        pause 0.07

    shiori "Aha... haha..."

    show shi yansm:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.3
        xalign 0.43
        yoffset 8

        # Big laugh bounce
        linear 0.12 yoffset -32 zoom 0.325
        linear 0.13 yoffset 34 zoom 0.28
        linear 0.11 yoffset 8 zoom 0.3      # Back to neutral

        pause 0.10

    shiori "{i}Ahaha~{/i}"

    show shi angry
    with dissolve

    shiori "{glitch=9}Then... then it wasn’t fate?{/glitch}"

    with vpunch

    shiori "It wasn’t because you--{w}{i}cared?{/i}"

    show shi angry:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.3
        xalign 0.43
        yoffset 8

        # Small laugh bounce
        linear 0.08 yoffset -3 zoom 0.308
        linear 0.09 yoffset 13 zoom 0.294
        linear 0.08 yoffset 8 zoom 0.3    # Back to neutral

        pause 0.07

    shiori "{sc=7}I thought--I thought--{/sc}"

    shiori "{size=+7}YAMAKUI!!{/size}"

    with sshake

    n2 "sHhHhH~"

    n "Please... {w}please stop..."

    show shi fear:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.3
        xalign 0.43
        yoffset 8

        # Scared, anxious shaking
        linear 0.06 xoffset -19 yoffset 16
        linear 0.05 xoffset 15 yoffset 1
        linear 0.05 xoffset -10 yoffset 14
        linear 0.05 xoffset 8 yoffset 6
        linear 0.06 xoffset 0 yoffset 8     # Return to original

        pause 0.11

    shiori "{i}No...{/i}"

    play sound "sfx/stumble.mp3"


    scene shrine night:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.5
        linear 0.18 zoom 1.2
    show shi fear:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        xanchor 0.5
        yalign -0.1
        yzoom 1.0
        xzoom 1.0
        zoom 0.3
        xalign 0.43
        yoffset 8

        linear 0.18 zoom 0.82 xalign 0.5 yoffset -10
    pause 0.1

    scene black

    shiori "{size=+5}NO--{w}WAIT--{w=0.3}I--{/size}"

    show darken2
    with flashred



    play sound "sfx/shioriscream.mp3"

    shiori "{glitch=14}NOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/glitch}"

    pause 0.1

    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n2 "Fsshhhkkhhh--"

    n2 "GglGGhhkkk... {w}Krrsshhhhh..."

    n "Please... please..."

    n2 "GnnnrrhhH... {w}Too mUch hAir. sTuck iN tHe gUmS."

    play sound "sfx/spit.mp3"

    with vpunch

    n2 "Puh."

    play sound "sfx/slurrp.mp3"

    n "Shiori..."

    n "You don't even feel her pulse anymore."

    n "You took everything from me..."

    n "And now..."

    stop music

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}A L L  {w=0.1}Y O U R  {w=0.1}F R I E N D S  {w=0.1}A R E  {w=0.1}D E A D{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    $ renpy.pause(3.0)

    $ persistent.shiori_dies = True

    $ persistent.loop3 = True

    return
