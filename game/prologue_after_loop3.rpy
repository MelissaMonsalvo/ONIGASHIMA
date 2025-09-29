label prologue_loop3:
    $ save_name = "Devoured"

    ### this has the prologue after everyone has devoured

    scene black
    show darken2
    with dissolve

    play music "Narukami.mp3"

    n2 "tHe rED MoOn iS GoNE."

    n2 "tHe cHiLdReN lAugH aGaIn."

    n2 "tHe vIlLaGe iS aLiVe."


    n2 "nO oNe rEmEmBeRs YoU."

    n2 "[persistent.player_name]? {w}WhO’s tHaT?"


    n2 "BeCAuSE I deVOuReD WhAT iS LeFt Of YOu."

    n2 "aNd wHeN tHe mOoN tUrNs fUlL–"

    n2 "i tEAr aNoThEr oNe aPaRt."

    scene moon7
    show darken2
    with fade



    n2 "tHe mOnThs pAsS."

    n2 "tHe cAtChEs gEt sLoWeR."

    n2 "tHe mEaT gEtS tHiN."


    n2 "mAyBe oNe dAy–"

    n2 "a sLaYeR wILL rIsE aGaIn."


    n2 "bUt mAyBe–"

    n2 "tHeRe iSn’T aNyOnE lEfT wHo WaNTs tO."

    scene black
    show darken2
    with fade

    show text "{color=#ff0000}{size=+10}B E C A U S E  I  A T E  T H E M  A L L {/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    n "..."

    n "..."

    n "...{fast}"


    n2 "RiGht?"

    n2 "[persistent.player_name]?"

    n2 "...."

    n2 "...."

    n2 "I fOrgOT."

    n2 "I CaN'T heAR YoU AnYmOrE."

    stop music fadeout 3.0

    $ persistent.loop4 = True

    scene black

    pause 0.1

    show text "{color=#ff0000}{size=+10}I WANT TO START AGAIN {/size}{/color}"

    with dissolve

    pause 0.1

    return

label prologue_loop4:

    play music "sfx/forest night.wav"

    n2 "[persistent.player_name] iS gOnE."

    n2 "iT’s qUiEt."

    scene moon4
    show darken2
    with fade

    n2 "i wAiT fOr tHe mOoN."

    scene moon7
    show darken2
    with fade

    n2 "i gO dOwN tO tHe vIlLaGe."

    n2 "iT’s dIfFeReNt eVeRy tImE."

    n2 "nEw fAcEs."


    n2 "nEw sMeLlS."

    n2 "sAmE tAsTe."

    n2 "SaMe FeAR."


    n2 "eAt. {w}SwAlLoW. {w}SlEeP."

    n2 "YaAaAaaaaAAaAaAaaaaWN~"

    n2 "So DuLl."

    n2 "sOmEtImEs i lEt tHeM rUn lOnGeR, fOR FuN."

    n2 "bUT tHe cHaSe fEeLs hOlLoW."

    scene black with fade
    show darken2
    $ renpy.pause(1.5)

    n2 "iT aLL tAsTeS tHe sAmE nOw."

    n2 "mAyBe iT’s tHe mEaT."

    n2 "mAyBe iT’s mE..."

    n2 "Or THe AbSeNCE oF yOU."

    stop music fadeout 3.0

    $ persistent.loop5 = True

    scene black

    pause 0.1

    show text "{color=#ff0000}{size=+10}I wANT To STaRT AgaIN {/size}{/color}"

    with dissolve

    pause 0.1

    return

label prologue_loop5:

    play music "sfx/forest night.wav"

    scene black
    show darken2
    with fade

    n2 "sTiLL hErE."

    scene moon7
    show darken2
    with fade

    n2 "tHe mOoN rIsEs."

    n2 "tHe vIlLaGe gRoWs."

    n2 "tHe hUnGeR sTaYs."

    n2 "sAmE pAtTeRn."

    scene flesh:
        matrixcolor BrightnessMatrix(-0.5)

        parallel:
            linear 1.2 zoom 1.02 blur 2
            linear 1.2 zoom 1.0 blur 1
            repeat

        parallel:
            linear 0.1 matrixcolor BrightnessMatrix(-1)
            linear 0.1 matrixcolor BrightnessMatrix(-0.5)
            pause 2.0
            repeat

        parallel:
            linear 0.05 xoffset -5 yoffset 3
            linear 0.05 xoffset 5 yoffset -2
            linear 0.05 xoffset 0 yoffset 0
            pause 1.5
            repeat

        parallel:
            linear 0.2 blur 6
            linear 0.4 blur 2
            pause 3.0
            repeat
    show darken2
    with fade

    play sound "sfx/monstermunch.mp3"

    n2 "EaT. EaT. EateATEateATeaTeateAt–"


    n2 "i sLeEp lEsS tHeSe dAyS."

    n2 "i lIsTeN mOrE."

    stop sound fadeout 0.5

    n2 "To SiLEnCe."


    n2 "yOu uSeD tO sAy sO mUcH."

    n2 "aNNoyInG. sOft. {w}aLiVe."

    n2 "nOW yOu’Re–"

    n2 "..."


    n2 "i dOn’T WaNT tO sPiT jOkEs aNyMoRe."

    n2 "nO oNe’s hErE tO sNaRk bAcK."

    n2 "eAt. {w}EaAAaat. {w}SlOw. {w}SwAlLoW. {w}rEpEaT."

    n2 "i tRy tO mAkE tHeM bEg lOuDeR."

    n2 "mAkE mYsElF lAuGh."

    n2 "iT dOeSn’T sOuNd rIgHt."

    n2 "HoLLoW."

    scene black
    with fade

    n2 "BoRedBorEDbOredBOoooooooooooooooOOOOOOOred."

    scene black

    pause 0.1

    show text "{color=#ff0000}{size=+10}STaRT AgaIN {/size}{/color}"

    with dissolve

    pause 0.1

    $ persistent.loop6 = True

    return

label prologue_loop6:

    scene black
    with fade

    play music "sfx/forest night.wav"

    n2 "I wOkE uP tOdAy."

    n2 "i sAiD:"

    n2 "\"It’s dark...\""


    n2 "...yOu uSeD tO sAy tHaT."

    n2 "\"It’s dark. We’re here again?\""

    n2 "hHhAHa."

    n2 "iT sOuNdS fUnNy wHeN i sAy iT."


    n2 "\"Stop stabbing it. You saved the village.\""

    n2 "ThAt wAs a gOoD oNe."

    n2 "DrAMatIC."


    n2 "...I dOn’T rEmEmBeR hOw yOu sOuNd."

    n2 "i’M mAkInG iT uP."

    n2 "bUt iF i dOn’T tAlK tO sOmEtHiNg, i’LL–"

    n2 "..."

    n2 "tHe mEaT dIeS SoooOoOo fAsT nOw."

    n2 "tHe mEaT dOeSn’T sAy mUcH, NoT LiKE yOU."

    n2 "tHe mOoN iS fUlL aGaIn."

    n2 "i wEnT dOwN."

    play sound "sfx/aah.wav"

    with sshake

    scene flesh
    show darken
    with fade

    n2 "i aTe."

    n2 "i aSkEd:"

    n2 "\"dO yOu rEmEmBeR [persistent.player_name]?\""

    n2 "tHe mEaT dIdN’t aNsWeR ME."

    scene black with fade
    $ renpy.pause(2.0)

    n2 "nOtHiNg dOeS AnYMOrE."

    scene black

    pause 0.1

    show text "{color=#ff0000}{size=+10}AgaIN {/size}{/color}"

    with dissolve

    pause 0.1

    $ persistent.loop7 = True

    return


label prologue_loop7:

    scene black
    with fade

    stop music

    n2 "..."

    n2 "iT hUrTs."

    n2 "HuRTsHurtsHuRTs."

    n2 "BuT I'M nOt BLEeDiNG?"

    n2 "Ah."

    n2 "iT hUrTs {i}iNsIdE.{/i}"

    n2 "tHe mEaT tAsTeS lIkE mUd NoW."

    n2 "tHe vOiCe iN mY hEaD {w}iSn’T yOu."

    n2 "...wHeRe aRe yOu."

    n2 "..."

    n2 "i dOn’T wAnT tO bE tHiS."

    n2 "i dOn’T wAnT tO eAt."

    n2 "i dOn’T wAnT tO bE aLoNe."

    n2 "...."

    scene black

    pause 0.1

    show text "{color=#ff0000}{size=+10}SsstttttttttaaaaRRRRRttttttt AgggAaaAAAIiiiINNN {/size}{/color}"

    with dissolve

    pause 0.1

    $ persistent.loop8 = True

    return


label prologue_loop8:

    scene black
    with fade

    stop music

    n2 "[persistent.player_name]."

    n2 "yOu wErE..."

    n2 "...tHe oNlY vOiCe tHaT mAdE mE lAuGh."

    n2 "i cAn’T bE aLoNe."

    n2 "i cAn’T hEaR mYsElF tHiNk ANyMOrE."

    n2 "tHe sIlEnCe iS sCrEaMiNg iN mY EaRS."

    n2 "I’M... {w}i’m gOnNa–"

    pause 1.0

    n2 "...KaMi-sAmA."

    n2 "cAn yOu hEaR mE?"

    n2 "wOuLd yOu bRiNg tHeM bAcK?"

    n2 "jUsT oNe mOrE ChAnCE."

    n2 "TO tAlK."

    n2 "i dOn’T wAnT tO bE tHiS."

    n2 "i’LL rEpEnT."

    n2 "i’LL sToP."

    n2 "i’LL sToP–i’LL sToP–"

    menu:

        "Repent":
            $ persistent.trueendingunlocked = True


            ### EVERYTHING IS HARD RESET
            $ persistent.shiori_dies = False
            $ persistent.yamato_dies = False
            $ persistent.hikaru_dies = False

            $ persistent.loop1 = False
            $ persistent.loop2 = False
            $ persistent.loop3 = False

            $ persistent.loop2_shiori_ghost1 = False
            $ persistent.loop2_shiori_ghost2 = False
            $ persistent.loop2_shiori_ghost3 = False
            $ persistent.loop2_shiori_ghost4 = False
            $ persistent.loop2_shiori_ghost5 = False

            $ persistent.loop2_yamato_ghost1 = False
            $ persistent.loop2_yamato_ghost2 = False
            $ persistent.loop2_yamato_ghost3 = False
            $ persistent.loop2_yamato_ghost4 = False
            $ persistent.loop2_yamato_ghost5 = False

            $ persistent.loop2_hikaru_ghost1 = False
            $ persistent.loop2_hikaru_ghost2 = False
            $ persistent.loop2_hikaru_ghost3 = False
            $ persistent.loop2_hikaru_ghost4 = False
            $ persistent.loop2_hikaru_ghost5 = False

            if persistent.first_playthrough == True:
                $ persistent.first_playthrough = False

            n2 "...ThE nExT TiME..."
            n2 "I wOn'T eAt aNyoNE."
            n2 "Won'T eVeN TAlK to ANYone."
            n2 "...ProMIsE..."
            n2 "LeT's StART CleAN."
            $ delete_all_saves()
            $ renpy.full_restart()
            return
            ## after this, you are kicked to main menu and everyone are alive again
        "Continue":
            n2 "..."

            n2 "...."

            n2 "....."

            n2 "i fOrgOt mY nAmE."

            n2 "I. I. I. I. I. i. i. i. i–"

            n2 "sKrTchSkRkGh–"

            n2 "eAt."

            n2 "eAt."

            n2 "eAt–"

            n2 "EATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEAT"

            return
