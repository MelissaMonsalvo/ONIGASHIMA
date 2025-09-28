label loop3_epilogue:

    scene bg village_day with fade
    play music "bgm/peaceful_but_wrong.ogg" fadein 2.0

    stop sound fadeout 2.0
    hide screen red_moon_effect
    hide screen blood_pulse_effect

    show screen slight_blur

    n2 "tHe sUn rIsEs."

    n2 "tHe cHiLdReN lAugH aGaIn."

    n2 "tHe mArKeTs bReAtHe."

    n2 "tHe vIlLaGe iS aLiVe."

    play sound "sfx/bells_ring.ogg"
    $ renpy.pause(0.4)

    n2 "nO oNe rEmEmBeRs."

    n2 "[player_name]? {w}WhO’s tHaT?"

    n2 "sOmE sTrAy. sOmE lOsT nAmE."

    n2 "eVeN tHe gRaVeStOnEs aRe bLaNk nOw."

    play sound "sfx/wind_through_grass.ogg"
    $ renpy.pause(0.3)

    n2 "i pReTeNd tO sMiLe wHeN i bUy fLoWeRs."

    n2 "i pReTeNd tO pRaY aT tHe sHrInE."

    n2 "aNd wHeN tHe mOoN tUrNs fUlL–"

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

    n2 "mAyBe oNe dAy–"

    n2 "a sLaYeR wILL rIsE aGaIn."

    play sound "sfx/sword_unsheath.ogg"
    $ renpy.pause(0.3)

    n2 "bUt mAyBe–"

    n2 "tHeRe iSn’T aNyOnE lEfT wHo rEmEmBeRs hOw."

    show text "{color=#ff0000}{size=+10}tHeY aRe pReY{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    show text "{color=#880000}{size=+8}aNd i aM tHe pReDaToR{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    n "..."

    n "..."

    n "...{fast}"

    window hide
    $ renpy.pause(2.0)

    n2 "...i dOn’T hEaR yOu aNyMoRe."

    play sound "sfx/fade_echo.ogg"

    n2 "tHe sOuL iS gOnE."

    n2 "yOu hAd nO mOrE tEtHeRs."

    n2 "nO oNe lEfT tO lOvE."

    n2 "nO oNe lEfT tO rEmEmBeR."

    scene black with fade
    play sound "sfx/gulp.ogg"
    $ renpy.pause(1.5)

    stop music fadeout 3.0

    return
label loop4_start:

    scene black with fade
    stop music fadeout 3.0
    stop sound fadeout 3.0
    $ renpy.pause(2.0)

    play sound "sfx/ambient_lowrumble.ogg" loop
    play music "bgm/endless_stillness.ogg" fadein 2.0

    n2 "i dOn’T wEaR tHe sKiN aNyMoRe."

    n2 "iT sLiPpEd oFf a fEw mOoNs aGo."

    n2 "tOo wEt. tOo sOuR."

    n2 "[player_name] iS gOnE."

    n2 "nO sOuL. nO vOiCe."

    n2 "iN tHe dEn. uNdEr tHe sToNeS. iT’s qUiEt."

    play sound "sfx/distant_heartbeat.ogg"
    $ renpy.pause(0.4)

    n2 "i wAiT fOr tHe mOoN."

    scene bg village_empty with slow_dissolve
    show screen fog_overlay

    n2 "i gO dOwN tO tHe vIlLaGe."

    n2 "iT’s dIfFeReNt eVeRy tImE."

    n2 "nEw fAcEs. nEw sMeLlS. sAmE tAsTe."

    n2 "sAlT. bOnE. sIlEnCe."

    play sound "sfx/chew_dry.ogg"
    $ renpy.pause(0.3)

    n2 "eAt. {w}SwAlLoW. {w}SlEeP."

    play sound "sfx/yawn_low.ogg"

    n2 "i sTaRt tO yAwN."

    n2 "tHe fEaR iS fAiNt nOw."

    n2 "tHe cRiEs sOuNd rEhEaRsEd."

    n2 "sOmEtImEs i lEt tHeM rUn lOnGeR."

    n2 "tHe cHaSe fEeLs hOlLoW."

    scene black with fade
    $ renpy.pause(1.5)

    n2 "mAyBe iT’s tHe mEaT."

    n2 "mAyBe iT’s mE."

    n2 "iT aLL tAsTeS tHe sAmE nOw."

    show text "{color=#aa0000}{size=+10}lOoP 4{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    show text "{color=#990000}{size=+8}tHe mEaT dOeSn’t sCrEaM rIgHt{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    return
label loop5_start:

    scene black with fade
    stop music fadeout 2.5
    stop sound fadeout 2.5
    $ renpy.pause(1.5)

    play sound "sfx/low_rumble_soft.ogg" loop
    play music "bgm/stale_cycle.ogg" fadein 3.0

    n2 "sTiLL hErE."

    n2 "lOoP fIvE."

    n2 "tHe mOoN rIsEs. tHe vIlLaGe gRoWs. tHe hUnGeR sTaYs."

    n2 "sAmE pAtTeRn. sAmE pAtH."

    n2 "nEw sMeLl. sAmE eNd."

    scene bg mountain_cave_dark with fade
    show screen dust_motes

    n2 "i sLeEp lEsS tHeSe dAyS."

    n2 "i lIsTeN mOrE."

    n2 "nO vOiCe."

    n2 "nO qUeStIoNs."

    play sound "sfx/distant_echo.ogg"

    n2 "yOu uSeD tO sAy sO mUcH."

    n2 "aNNoyInG. sOft. {w}aLiVe."

    n2 "nOW yOu’Re–"

    n2 "..."

    play sound "sfx/wind_whistle.ogg"

    scene bg village_empty with slow_dissolve

    n2 "i dOn’T sPiT jOkEs aNyMoRe."

    n2 "nO oNe’s hErE tO sNaRk bAcK."

    n2 "eAt. {w}SlOw. {w}SwAlLoW. {w}rEpEaT."

    n2 "i tRy tO mAkE tHeM bEg lOuDeR."

    n2 "i tRy tO mAkE mYsElF lAuGh."

    play sound "sfx/laugh_choked.ogg"

    n2 "iT dOeSn’T sOuNd rIgHt."

    scene black with fade
    $ renpy.pause(1.5)

    show text "{color=#880000}{size=+10}lOoP 5{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    show text "{color=#660000}{size=+8}tHe sIlEnCe iS a lOuD tHiNg{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    return
label loop6_start:

    scene black with fade
    stop music fadeout 2.0
    stop sound fadeout 2.0
    $ renpy.pause(2.0)

    play sound "sfx/static_low.ogg" loop
    play music "bgm/broken_mirror.ogg" fadein 2.5

    n2 "..."

    n2 "lOoP. {w}SiX."

    n2 "I wOkE uP tOdAy."

    n2 "i sAiD:"

    n2 "\"It’s dArk.\""

    play sound "sfx/breath_sharp.ogg"

    n2 "...yOu uSeD tO sAy tHaT."

    n2 "\"It’s dark. We’re here again?\""

    n2 "hHhAHa."

    n2 "iT sOuNdS fUnNy wHeN i sAy iT."

    scene bg mountain_cave_dark with fade
    show screen static_overlay

    n2 "\"sToP sTaBbInG iT. yOu sAvEd tHe vIlLaGe.\""

    n2 "ThAt wAs a gOoD oNe."

    play sound "sfx/voice_mimic_fail.ogg"

    n2 "...I dOn’T rEmEmBeR hOw yOu sOuNd."

    n2 "i’M mAkInG iT uP."

    n2 "bUt iF i dOn’T tAlK tO sOmEtHiNg, i’LL–"

    n2 "..."

    play sound "sfx/heartbeat_faint.ogg"

    n2 "tHe mEaT iSn’t lAuGhInG."

    n2 "tHe mEaT dIeS fAsT nOw."

    n2 "tHe mEaT dOeSn’T sAy nAmEs. tHe mEaT dOeSn’T sAy yOuRs."

    scene bg shrine_field_night with slow_dissolve
    show screen red_moon_effect
    show screen blood_pulse_effect

    n2 "tHe mOoN iS fUlL aGaIn."

    n2 "i wEnT dOwN."

    n2 "a cHiLd sCrEaMeD."

    play sound "sfx/wet_crunch2.ogg"
    $ renpy.pause(0.4)
    play sound "sfx/gulp.ogg"
    $ renpy.pause(0.3)

    n2 "i aTe."

    n2 "i aSkEd:"

    n2 "\"dO yOu rEmEmBeR [player_name]?\""

    play sound "sfx/wind_whistle.ogg"

    n2 "tHe mEaT dIdN’t aNsWeR."

    n2 "oF cOuRsE iT dIdN’t."

    scene black with fade
    $ renpy.pause(2.0)

    n2 "nOtHiNg dOeS."

    n2 "nOt eVeN mE."

    show text "{color=#660000}{size=+10}lOoP 6{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    show text "{color=#440000}{size=+8}i’M sTiLl hUnGrY{/size}{/color}" with dissolve
    $ renpy.pause(2.5)
    hide text

    return
label loop7_start:

    scene black with fade
    stop music fadeout 2.0
    stop sound fadeout 2.0
    $ renpy.pause(1.5)

    play music "bgm/broken_prayer.ogg" fadein 3.0
    play sound "sfx/faint_rattle.ogg" loop

    n2 "..."

    n2 "iT hUrTs."

    n2 "nOt mY bOnEs."

    n2 "nOt mY tEeTh."

    n2 "iT hUrTs {i}iNsIdE.{/i}"

    n2 "tHe qUiEt– {w}iT sCrAtChEs."

    n2 "tHe lOoPs– {w}iT rOtS."

    scene bg forest_clearing_dead with slow_dissolve
    show screen blood_fog_overlay

    n2 "tHe mEaT tAsTeS lIkE mUd."

    n2 "tHe bLoOd tAsTeS lIkE sAlT."

    n2 "tHe vOiCe iN mY hEaD– {w}iSn’T yOu."

    n2 "...wHeRe aRe yOu."

    play sound "sfx/breath_ragged.ogg"
    $ renpy.pause(1.0)

    n2 "...pLeAsE."

    n2 "i dOn’T wAnT tO bE tHiS."

    n2 "i dOn’T wAnT tO eAt."

    n2 "i dOn’T wAnT tO bE aLoNe."

    play sound "sfx/heartbeat_soft.ogg"
    $ renpy.pause(0.8)

    n2 "...lEt mE rEsT."

    ## repent repent

label loop8_start:

    scene black with fade
    play sound "sfx/growl_low.ogg" loop
    play music "bgm/sick_decay.ogg" fadein 2.0

    n2 "..."

    n2 "tHe bLoOd iS wEt"

    n2 "i fOrgOt mY nAmE."

    n2 "I. I. I. I. I. i. i. i. i–"

    n2 "sKrTchSkRkGh–"

    n2 "tHeY dOn’T sCrEaM rIgHt aNyMoRe."

    n2 "eAt."

    n2 "eAt."

    n2 "eAt–"

    n2 "EATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEATEAT"

    show text "{color=#ff0000}{size=+15}lOoP 8{/size}{/color}" with hpunch
    $ renpy.pause(3.0)
    hide text

    return
