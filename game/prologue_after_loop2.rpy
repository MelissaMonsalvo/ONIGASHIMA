label prologue_loop2:

    ### this has the prologue after two peoples has been devoured

    n2 "HhhAahhh... {w}hhHaaaAAhh."

    n2 "It stILL fitS. {w=0.3}moRE or lEsS."

    n2 "ThiS flEsH... {w}bEnds wHeN I sMilE."

    n2 "It'LL lASt fOR onE MoRE MeAT."

    window hide
    $ renpy.pause(1.5)
    window show

    n2 "YoU waNteD a hErO? {w} LoOk... LoOk cLoSE."

    n "..."

    MC "STay quIeT iN tHeRre."

    n2 "I’M wALkINg. {w} bReAthInG. {w} SMiLing."

    n2 "ThEy alL bELiEvE mE."

    n2 "ThEy kEep cHeErInG, {w} cHeErInG fOr tHe pErSOn unDEr tHE sKiN."

    play sound "sfx/heartbeat_distorted.ogg" loop
    $ renpy.pause(0.4)

    n "...you..."

    MC "HhHHRaAAHaHhAH!"

    n2 "OnE MOre."

    play sound "sfx/gulp.ogg"
    $ renpy.pause(0.3)

    n "s...stop..."

    n2 "NnNnnooOOO."

    play sound "sfx/blood_pulse.ogg"
    show screen blood_pulse_effect

    MC "oN tHe nExT rEd mOon..."

    MC "I wiLL eaT tHe lAsT OnE."

    n "D-Don’t..."

    n2 "i WiLL fInD tHeM. ThEN yoUR ViLLaGErs."

    n2 "So mAnY mOutHs tO opEn."

    n2 "So muCh hUNgEr."

    ### laughing sfx

    window show
    centered "{color=#FF4444}{size=+5}SEVEN DAYS UNTIL THE NEXT RED MOON{/size}{/color}"

    $ renpy.pause(2.0)

    return
label loop3_arrival:

    scene bg village_day with fade
    play sound "sfx/flies_loop.ogg" loop
    show screen heat_distortion

    n2 "I cAmE dOwN tHe mOunTAiN... {w} jUsT lIkE bEfOrE."

    play sound "sfx/squishstep1.ogg"
    $ renpy.pause(0.2)
    play sound "sfx/squishstep2.ogg"
    $ renpy.pause(0.2)

    n2 "stEp. {w} dRip. {w} slOugh."

    n2 "YoUR FlEsH coMEs oFf in rIbBonS wHeN i SmiLE."

    n2 "tHe sKin wAs tOo rOTteD aNywAy~"

    show villagers_scared at center
    play sound "sfx/gasp.ogg"

    "Villager" "W-What is that?!"

    "Child" "Kyaaaaaa!!"

    ## people screaming and running

    n2 "tHeY rAn."

    n2 "nO oNe cAme tO gReeT mE tHiS tImE."

    n2 "ToO BaD. So sAD."

    n "..."

    window hide
    $ renpy.pause(2.5)

    window show

    n2 "aND I sTiLL hAvE oNe mOre of YOuR FRieNdS tO eAt."

    scene black with fade
    $ renpy.pause(2.0)


    return
