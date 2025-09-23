label loop3_yamato:

    scene village day:
        zoom 0.5
    show darken

    n2 "tHeY aLL hIdE."

    n2 "nO oNe sPeAks mY nAmE."

    n2 "tHe sKiN sTaRtS tO bUbBlE. {w}It’s RoTtInG--"

    show yam normal behind darken:
        zoom 0.3
        xalign 0.65       # Start off to the right
        yalign 0
        yoffset 110       # Slightly below
        xzoom 1.0
        yzoom 1.0
        alpha 0.0

        # Step in: fade in and slide to position
        linear 0.17 alpha 1.0 xalign 0.55 yoffset 50
    stop music
    stop muzak

    yamato "{sc=7}You.{/sc}"

    n2 "..."

    n2 "oHhH~"

    n2 "GaMeY mEAt."

    yamato "Goddamnit, [persistent.player_name]. {w=0.1}Ya go to the mountains yerself and came back with this thing weain' ya?"

    yamato "{i}Oi, bastard!{/i} That ain't yer face!"

    with vpunch

    play music "Battora.mp3"

    MC "iT iS nOw~"

    yamato "{sc=3}SHUT YOUR MOUTH!{/sc}"

    play sound "sfx/shing.mp3"
    with hpunch


    n "..."

    n2 "sO yOu sTiLL hAvE tHe gUTs, huh?"

    n2 "Go oN tHeN. sHoW mE."

    show yam normal behind darken:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        alpha 1.0

        linear 0.13 zoom 0.47 yoffset -120 xalign 0.65
        linear 0.12 zoom 0.68 yoffset -250 xalign 0.7
    scene black with vpunch



    yamato "{sc=8}RAAAAAHH!!{/sc}"

    scene black
    play sound "swing.wav"
    show combo_slash_1
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "swing.wav"
    show combo_slash_2
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "swing.wav"
    show combo_slash_3
    $ renpy.pause(0.1, hard=True)

    n2 "TtKk--"

    n2 "tOo sLoW, mUtt."

    play sound "Sfx/stumble.mp3"

    scene village day:
        zoom 0.5

    show yam normal:
        zoom 0.47
        align (0.5, 0.005)


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.29 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.25 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0
    show darken
    with vpunch



    yamato "Bastard--"

    yamato "{cps=14}The hell's with {b}THAT{/b} speed?{/cps}"

    n2 "yOuR hAtReD sMEllS gOoD."

    n2 "sO dOeS yOuR gUiLt."

    show yam normal:
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.10 yoffset 54 yzoom 0.91
        linear 0.09 yoffset -28 yzoom 1.11
        linear 0.07 yoffset 12 yzoom 0.98
        linear 0.08 yoffset 0 yzoom 1.0

        pause 0.08
    with vpunch

    yamato "{glitch=8}I'LL RIP YOU APART, YOU FUCKIN--{/glitch}"

    MC "{w=0.1}...nO nEeD tO sWeAr."

    MC "tHe mOoN wILL bE rEd sOoN."

    MC "I’LL mAkE sUrE yOu dIe sCrEaMiNg."

    n "..."

    n "{cps=13}Yamato...{/cps}"

    n "...I’m sorry."

    yamato "{sc=7}COME ON!!{/sc}"

    show yam normal behind darken:
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.13 zoom 0.47 yoffset -120 xalign 0.65
        linear 0.12 zoom 0.68 yoffset -250 xalign 0.7
    scene black with vpunch


    play sound "swing.wav"
    show slash_vertical
    $ renpy.pause(0.1, hard=True)
    with vpunch

    scene village day:
        zoom 0.5

    show yam normal:
        zoom 0.47
        align (0.5, 0.005)


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.4 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.35 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0

    show darken

    yamato "{sc=6}Gh--!{/sc}"

    n2 "ThAt’s bEtTeR."

    n "{i}Yamato... You can't win against the Yamakui!{/i}"

    n "Run...! You're bleeding already!"

    show yam normal:
        zoom 0.35
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        # Subtle, uneven trembling
        linear 0.08 xoffset 138 yoffset 10
        linear 0.07 xoffset 151 yoffset -8
        linear 0.06 xoffset 147 yoffset 6
        linear 0.07 xoffset 144 yoffset 0   # Back to rest, pain

        pause 0.10

    yamato "I{w=0.1}-won't..."

    MC "TsK, tsK, tsKKKKKK...."

    MC "iS tHAt AlL?"

    yamato "..."

    n2 "nOt dEad yEt, aRe yOu?"

    play sound "sfx/spit.mp3"

    show yam normal:
        zoom 0.35
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        # Subtle, uneven trembling
        linear 0.08 xoffset 138 yoffset 10
        linear 0.07 xoffset 151 yoffset -8
        linear 0.06 xoffset 147 yoffset 6
        linear 0.07 xoffset 144 yoffset 0   # Back to rest, pain

        pause 0.10

    yamato "The fuck yer starin' for?"

    yamato "{cps=13}Why won't ya finish me already!?{/cps}"

    MC "HeHhhHhHH..."

    MC "nO."

    MC "wOuLdn’t bE fUn."

    MC "tHE rEd mOOn's NoT HeRE Yet."



    show yam normal:
        zoom 0.35
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        # Subtle, uneven trembling
        linear 0.08 xoffset 138 yoffset 10
        linear 0.07 xoffset 151 yoffset -8
        linear 0.06 xoffset 147 yoffset 6
        linear 0.07 xoffset 144 yoffset 0   # Back to rest, pain

        pause 0.10



    yamato "{i}You... {w=0.1}freak--{/i}"

    MC "{sc=1}RuN. RuN, lITttLE mUTt.{/sc}"

    MC "i’LL mAkE sUrE iT hUrTs wHeN i fInD yOu."

    yamato "Damn it... {sc=2}Damn it to hell!{/sc}"

    yamato "{sc=1}I'll be back t' kill ya, just ya wait!{/sc}"

    play sound "sfx/stumble.mp3"

    pause 0.1

    show yam normal:
        zoom 0.35
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        xzoom 1.0
        yzoom 1.0


        linear 0.09 zoom 0.38 xoffset 220
        linear 0.15 zoom 0.26 xoffset 820
        linear 0.11 zoom 0.19 xoffset 1600 alpha 0.0

    pause 0.2

    play sound "sfx/run.mp3"

    n "{cps=13}Yamato...{/cps}"

    n "...don’t come back."

    n "Don’t give it what it wants..."

    stop sound

    scene black

    pause 0.3

    stop music

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}ONE DAY UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

    with fade

    pause 0.5

    scene moon5
    with fade
    pause 0.2
    scene moon6
    with fade

    stop sound

    pause 0.5

    show darken2

    n2 "lOoK aT tHE mOOn, sPiLLiNg {w}bLoOd fOr mE."

    n2 "hHhAhhh~ {w}hHhHAhHhAha--"

    n "..."

    play sound "sfx/stretch.mp3"

    play muzak "sfx/forest night.wav"

    n2 "YouR sKiN's mElTiNg nOw."

    n2 "WhERe, {w=0.2}wheRE {w=0.2}is YoUR FriENd?"

    n2 "WheRe is MY {cps=10}mEaT?{/cps}"

    n2 "I cAn smELL hIs swEaT. {w=0.2}hIs rIbS."

    n2 "He’s cOvErInG hIs wOuNdS."

    n2 "lImPiNg aRoUnD tHe sHiNe lIkE i cAn’T sEe hIm~"

    n2 "bUt i dO."

    n2 "I wAtCh hIm sLuRp hIs dRiNk wItH tReMbLiNg hAnDs."

    n2 "I hEAr hIm sAy yOuR nAmE in hIs sLeEp."

    n "..."

    n "{sc=5}Stop it...{/sc}"

    n2 "He’s tRyInG tO hOlD oN."

    n2 "He’s trYINg to HeAL aNd i’m {i}lEtTiNg hIm~{/i}"

    n2 "dO yOu kNoW wHy?"

    n "{cps=12}No. I don't WANT to know!?{/cps}"

    n2 "BeCausE iT’s bEtTeR wHeN tHeY tHiNk tHeY hAvE a cHaNcE."

    n2 "TheY'Ll tAsTe sWeEtEr thaT WaY."

    n "{glitch=8}You... monster.. .{/glitch}"

    n2 "cOrReCT."


    scene black with fade
    $ renpy.pause(2.5)

    stop music

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

    pause 0.5

    play music "Blood Ritual.mp3"

    n2 "FiNaLlY."

    n2 "ThE rEd mOoN iS hErE."

    scene village night with in_212:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    show darken2

    n2 "tHeY aLL hIdE."

    n2 "nO oNe sPeAks mY nAmE."

    n2 "tHe sKiN sTaRtS tO bUbBlE. {w}It’s RoTtInG--"


    show yam normal behind darken2:
        zoom 0.3
        xalign 0.67
        yalign 0
        yoffset 120
        xzoom 1.0
        yzoom 1.0
        alpha 0.0

        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.19 alpha 0.7 xalign 0.62 yoffset 145
        linear 0.15 alpha 1.0 xalign 0.60 yoffset 100
        pause 0.10

        linear 0.20 xalign 0.58 yoffset 150
        linear 0.14 xalign 0.55 yoffset 50

    MC "i cAn sMeLL yOu, o'gAmEy oNe."

    yamato "..."

    MC "I sEE yOUr Limp aND YeT yOU DEciDE tO FigHT Me StIll."

    yamato "{cps=25}A real man never backs down from a duel.{/cps}"

    show yam normal behind darken2:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.10 xoffset -38 yoffset 102
        linear 0.07 xoffset 21 yoffset 60
        linear 0.06 xoffset -15 yoffset 78
        linear 0.09 xoffset 0 yoffset 50
        pause 0.10

    yamato "For [persistent.player_name]'s honor!"

    n "{i}Yamato...{/i}"

    yamato "A-And... For the others, too."

    yamato "{cps=14}I--I can’t remember their damned faces...{/cps}"

    show yam normal behind darken2:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.10 xoffset -38 yoffset 102
        linear 0.07 xoffset 21 yoffset 60
        linear 0.06 xoffset -15 yoffset 78
        linear 0.09 xoffset 0 yoffset 50
        pause 0.10

    yamato "{glitch=8}That just means ya ate 'em!{/glitch}"

    yamato "I can't bring 'em back, but I sure hell can avenge 'em!"

    n "I always thought you hated me..."

    MC "hOoOoOoO..."

    yamato "{sc=5}C'mon, Oni! Let's finish this!{/sc}"

    MC "So HonORaBLe, tHis MuTt."

    MC "So STupID."

    yamato "{sc=5}COME!{/sc}"

    n "You don’t have to do this--"

    n "Yamato, please--"

    n "{cps=13}Just run--{/cps}"

    show village night:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        linear 0.23 zoom 1.22

    show yam normal behind darken2:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        xoffset 0
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.23 zoom 0.68 xalign 0.5 yoffset 16
    scene black with vpunch

    scene black
    play sound "swing.wav"
    show slash_fx_horizontalred
    $ renpy.pause(0.1, hard=True)
    show darken2
    with hpunch




    n2 "FiRsT sWiNg~"


    n2 "I lEt hIm gRaZe mY aRm."

    play sound "swing.wav"
    show combo_slash_2red
    $ renpy.pause(0.1, hard=True)
    show darken2
    with vpunch

    MC "hHhhAhhh-- {w}iT hUrTs sO nIcE."

    yamato "Why t'hell are ya laughin'?!"

    MC "I liKE PlaYIng WiTh FooD."

    yamato "{sc=7}The hell--!{/sc}"


    play sound "swing.wav"
    show combo_slash_1red
    $ renpy.pause(0.1, hard=True)
    show darken2
    with vpunch

    n2 "He sWiNgS aGaIn."

    n2 "I lEaN bAcK."

    n2 "I tAp tHe bAcK oF hIs hAnD wItH mY fInGeRs."

    MC "BoOP."

    with vpunch

    n "{cps=14}Please stop playing with him--{/cps}"

    scene village night:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

    show yam normal:
        zoom 0.47
        align (0.5, 0.005)
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.29 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.25 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0
    show darken2
    with vpunch

    yamato "{sc=6}Ghh--!!{/sc}"

    yamato "You--"

    yamato "You’re enjoying this--"

    stop music fadeout 1.0

    n2 "iT’s a dAaaaAaAaAanCe."

    n "{i}Yamato doesn't have any hope of winning--{/i}"

    play music "Goodbye.mp3"

    yamato "{sc=5}[persistent.player_name]...{/sc}"

    yamato "We promised."

    yamato "{cps=13}Even if I die.... I’ll keep swingin'.{/cps}"

    n "..."

    scene black
    play sound "swing.wav"
    show combo_slash_3red
    $ renpy.pause(0.2, hard=True)
    with vpunch

    play sound "swing.wav"
    show combo_slash_1red
    $ renpy.pause(0.2, hard=True)
    show darken2
    with vpunch

    scene village night:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

    show yam normal:
        zoom 0.47
        align (0.5, 0.005)
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.29 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.25 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0
    show darken2
    with vpunch


    n2 "sTiLL sWiNgInG?"

    n2 "yOuR aRm iS sHaKiNg."

    n2 "yOuR wOuNdS aRe oPeN aGaIn."

    n2 "jUsT GivE Up aND DiE~"

    yamato "{sc=7}Shut up.{/sc}"

    yamato "Shut up and fight me seriously...!"

    MC "I AM fIgHtInG. {w}SerIOuSLy. {w}So YoUR MeaT iS TEndeRIzeD."

    n2 "aNd lOoK--"

    play sound "sfx/stretch.mp3"
    with flashred

    n2 "iT’s fAlLiNg oFf."

    n2 "jUsT lIkE mY sKiN."

    show yam normal behind darken2:
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Violent pain shaking, abrupt, uneven
        linear 0.05 xoffset 118 yoffset 16
        linear 0.04 xoffset 171 yoffset -22
        linear 0.05 xoffset 132 yoffset 28
        linear 0.04 xoffset 154 yoffset -17
        linear 0.05 xoffset 144 yoffset 0    # Back to original

        pause 0.12

    yamato "{sc=5}AaaAaAghhhh!!!{/sc}"

    hide yam
    with easeoutbottom
    pause 0.1
    with vpunch

    MC "ThErE iT iS."

    MC "YoU’Re fInAlLy dOnE."

    MC "StUPiD MuTT. So LOuD... So PRoUd..."

    MC "LiKe yOu cOuLd sAvE aNyOnE..."

    MC "LiKe yOu wErE sTrOnGeR tHaN mE...."

    MC "yOu wErEn’t."

    MC "yOu’rE nOt."

    MC "YoU’rE wEaKeR tHaN tHiS SkIN I'm WeARiNg."

    MC "[persistent.player_name] {w}fOuGhT mE tOo."

    MC "DIeD {i}wItH tEeTh bArEd.{/i}"

    MC "aNd yOu?"

    MC "yOu’rE oN yOuR kNeEs."

    ## CG HERE

    yamato "{cps=14}I know, {w=0.1}damn it...{/cps}"

    yamato "{cps=14}[persistent.player_name] was always, always stronger than me...{/cps}"

    n "Yamato, please run...! {i}I forgive you!{/i}"

    n2 "He CAn'T."

    MC "LoOk aT yOu~"

    MC "yOu cAn’T eVeN rUn aNyMoRe."

    n "{sc=7}DON’T--{/sc}"

    n "{sc=6}PLEASE--{/sc}"

    n "{sc=7}YAMATO--GET UP--{/sc}"

    yamato "..."

    yamato "[persistent.player_name]..."

    yamato "{cps=14}Even if I'll forget you in the end...{/cps}"

    yamato "...I’ll remember this pain {w}in hell."

    scene black
    show darken2

    stop music
    play sound "sfx/hahh.mp3"


    n2 "hHHhhHhh~"

    n2 "tHaT mAkEs iT {i}bEtTeR{/i}."

    n2 "bEcAuSe nOw yOu’LL tAsTe lIkE mEmOrIeS."

    n "{sc=7}DON’T--{/sc}"

    n "{sc=8}STOP--STOP--{/sc}"

    play sound "sfx/yamato_eaten.wav"

    yamato "{sc=6}GHHHH--HHAKK--HHHHH!!{/sc}"

    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n "{i}Yamato...{/i}"

    n "{cps=13}You took everything from me...{/cps}"

    n "And now..."

    stop music

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}A L L  {w=0.1}Y O U R  {w=0.1}F R I E N D S  {w=0.1}A R E  {w=0.1}D E A D{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    $ persistent.yamato_dies = True

    $ persistent.loop3 = True

    ## at the end of the route yamato dies

    return
