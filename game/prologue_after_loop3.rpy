label prologue_loop3:

    ### this has the prologue after everyone has devoured

    n2 "tHe rED MoOn iS GoNE."

    n2 "tHe cHiLdReN lAugH aGaIn."

    n2 "tHe vIlLaGe iS aLiVe."

    play sound "sfx/bells_ring.ogg"
    $ renpy.pause(0.4)

    n2 "nO oNe rEmEmBeRs YoU."

    n2 "[persistent.player_name]? {w}WhO’s tHaT?"

    play sound "sfx/wind_through_grass.ogg"
    $ renpy.pause(0.3)

    n2 "BeCAuSE I deVOuReD WhAT iS LeFt Of YOu."

    n2 "aNd wHeN tHe mOoN tUrNs fUlL--"

    n2 "i tEAr aNoThEr oNe aPaRt."

    play sound "sfx/fleshtear_burst.ogg"
    $ renpy.pause(0.3)

    play sound "sfx/wet_snap.ogg"
    $ renpy.pause(0.3)

    n2 "tHe mOnThs pAsS."

    n2 "tHe cAtChEs gEt sLoWeR."

    n2 "tHe mEaT gEtS tHiN."

    play sound "sfx/gurgle_mouth.ogg"
    $ renpy.pause(0.3)

    n2 "mAyBe oNe dAy--"

    n2 "a sLaYeR wILL rIsE aGaIn."

    play sound "sfx/sword_unsheath.ogg"
    $ renpy.pause(0.3)

    n2 "bUt mAyBe--"

    n2 "tHeRe iSn’T aNyOnE lEfT wHo WaNTs tO."

    show text "{color=#ff0000}{size=+10}B E C A U S E  I  A T E  T H E M  A L L {/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    n "..."

    n "..."

    n "...{fast}"

    window hide
    $ renpy.pause(2.0)

    n2 "RiGht?"

    n2 "[persistent.player_name]?"

    n2 "...."

    n2 "...."

    n2 "I fOrgOT."

    n2 "I CaN'T heAR YoU AnYmOrE."

    scene black with fade
    play sound "sfx/gulp.ogg"
    $ renpy.pause(1.5)

    stop music fadeout 3.0

    $ persistent.loop4 = True

    return

label prologue_loop4:

    n2 "[persistent.player_name] iS gOnE."

    n2 "iT’s qUiEt."

    play sound "sfx/distant_heartbeat.ogg"
    $ renpy.pause(0.4)

    n2 "i wAiT fOr tHe mOoN."

    scene bg village_empty with slow_dissolve
    show screen fog_overlay

    n2 "i gO dOwN tO tHe vIlLaGe."

    n2 "iT’s dIfFeReNt eVeRy tImE."

    n2 "nEw fAcEs."

    n "nEw sMeLlS."

    n "sAmE tAsTe."

    n "SaMe FeAR."

    play sound "sfx/chew_dry.ogg"
    $ renpy.pause(0.3)

    n2 "eAt. {w}SwAlLoW. {w}SlEeP."

    play sound "sfx/yawn_low.ogg"

    n2 "YaAaAaaaaAAaAaAaaaaWN~"

    n2 "So DuLl."

    n2 "sOmEtImEs i lEt tHeM rUn lOnGeR, fOR FuN."

    n2 "bUT tHe cHaSe fEeLs hOlLoW."

    scene black with fade
    $ renpy.pause(1.5)

    n2 "iT aLL tAsTeS tHe sAmE nOw."

    n2 "mAyBe iT’s tHe mEaT."

    n2 "mAyBe iT’s mE..."

    n2 "Or THe AbSeNCE oF yOU."

    stop music fadeout 3.0

    $ persistent.loop5 = True

    return

label prologue_loop5:

    n2 "sTiLL hErE."

    n2 "tHe mOoN rIsEs."

    n2 "tHe vIlLaGe gRoWs."

    n2 "tHe hUnGeR sTaYs."

    n2 "sAmE pAtTeRn."

    n2 "EaT. EaT. EateATEateATeaTeateAt--"

    scene bg mountain_cave_dark with fade
    show screen dust_motes

    n2 "i sLeEp lEsS tHeSe dAyS."

    n2 "i lIsTeN mOrE."

    n2 "To SiLEnCe."

    play sound "sfx/distant_echo.ogg"

    n2 "yOu uSeD tO sAy sO mUcH."

    n2 "aNNoyInG. sOft. {w}aLiVe."

    n2 "nOW yOu’Re--"

    n2 "..."

    play sound "sfx/wind_whistle.ogg"

    n2 "i dOn’T WaNT tO sPiT jOkEs aNyMoRe."

    n2 "nO oNe’s hErE tO sNaRk bAcK."

    n2 "eAt. {w}EaAAaat. {w}SlOw. {w}SwAlLoW. {w}rEpEaT."

    n2 "i tRy tO mAkE tHeM bEg lOuDeR."

    n2 "mAkE mYsElF lAuGh."

    play sound "sfx/laugh_choked.ogg"

    n2 "iT dOeSn’T sOuNd rIgHt."

    n2 "HoLLoW."

    n2 "BoRedBorEDbOredBOoooooooooooooooOOOOOOOred."

    $ persistent.loop6 = True

    return

label prologue_loop6:
    n2 "I wOkE uP tOdAy."

    n2 "i sAiD:"

    MC "\"It’s dark...\""

    play sound "sfx/breath_sharp.ogg"

    n2 "...yOu uSeD tO sAy tHaT."

    MC "\"It’s dark. We’re here again?\""

    n2 "hHhAHa."

    n2 "iT sOuNdS fUnNy wHeN i sAy iT."

    scene bg mountain_cave_dark with fade
    show screen static_overlay

    MC "\"Stop stabbing it. You saved the village.\""

    n2 "ThAt wAs a gOoD oNe."

    n2 "DrAMatIC."

    play sound "sfx/voice_mimic_fail.ogg"

    n2 "...I dOn’T rEmEmBeR hOw yOu sOuNd."

    n2 "i’M mAkInG iT uP."

    n2 "bUt iF i dOn’T tAlK tO sOmEtHiNg, i’LL--"

    n2 "..."

    n2 "tHe mEaT dIeS SoooOoOo fAsT nOw."

    n2 "tHe mEaT dOn’T sAy mUcH, NoT LiKE yOU."

    n2 "tHe mOoN iS fUlL aGaIn."

    n2 "i wEnT dOwN."

    ## woman scream

    play sound "sfx/wet_crunch2.ogg"
    $ renpy.pause(0.4)
    play sound "sfx/gulp.ogg"
    $ renpy.pause(0.3)

    n2 "i aTe."

    n2 "i aSkEd:"

    MC "\"dO yOu rEmEmBeR [persistent.player_name]?\""

    play sound "sfx/wind_whistle.ogg"

    n2 "tHe mEaT dIdN’t aNsWeR ME."

    scene black with fade
    $ renpy.pause(2.0)

    n2 "nOtHiNg dOeS AnYMOrE."

    $ persistent.loop7 = True

    return

label prologue_loop7:

    n2 "..."

    n2 "iT hUrTs."

    n2 "HuRTsHurtsHuRTs."

    n2 "BuT I'M nOt BLEeDiNG?"

    n2 "Ah."

    n2 "iT hUrTs {i}iNsIdE.{/i}"

    scene bg forest_clearing_dead with slow_dissolve
    show screen blood_fog_overlay

    n2 "tHe mEaT tAsTeS lIkE mUd NoW."

    n2 "tHe vOiCe iN mY hEaD {w}iSn’T yOu."

    n2 "...wHeRe aRe yOu."

    play sound "sfx/breath_ragged.ogg"
    $ renpy.pause(1.0)

    n2 "..."

    n2 "i dOn’T wAnT tO bE tHiS."

    n2 "i dOn’T wAnT tO eAt."

    n2 "i dOn’T wAnT tO bE aLoNe."

    play sound "sfx/heartbeat_soft.ogg"
    $ renpy.pause(0.8)

    n2 "...."

    $ persistent.loop8 = True

    return


label prologue_loop8:

    n2 "[persistent.player_name]."

    n2 "yOu wErE..."

    play sound "sfx/breath_shudder.ogg"

    n2 "...tHe oNlY vOiCe tHaT mAdE mE lAuGh."

    play sound "sfx/crack_voice.ogg"

    n2 "i cAn’T bE aLoNe."

    n2 "i cAn’T hEaR mYsElF tHiNk ANyMOrE."

    n2 "tHe sIlEnCe iS sCrEaMiNg iN mY EaRS."

    n2 "I’M... {w}i’m gOnNa—"

    pause 1.0

    n2 "...KaMi-sAmA."

    n2 "cAn yOu hEaR mE?"

    n2 "wOuLd yOu bRiNg tHeM bAcK?"

    n2 "jUsT oNe mOrE ChAnCE."

    n2 "TO tAlK."

    n2 "i dOn’T wAnT tO bE tHiS."

    n2 "i’LL rEpEnT."

    n2 "i’LL sToP."

    n2 "i’LL sToP—i’LL sToP—"

    menu:
        "Repent?"

        "YEs":
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

            n "Repent! Repent!"
            return
            ## after this, you are kicked to main menu and everyone are alive again
        "NO.":
            n2 "..."

            n2 "...."

            n2 "....."

            n2 "i fOrgOt mY nAmE."

            n2 "I. I. I. I. I. i. i. i. i--"

            n2 "sKrTchSkRkGh--"

            n2 "eAt."

            n2 "eAt."

            n2 "eAt--"

            n2 "EATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEAT"

            return
