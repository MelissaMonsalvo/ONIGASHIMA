label prologue_loop2:

    ### this has the prologue after two peoples has been devoured

    scene black with fade

    scene black with fade
    show flesh2 at scary_flicker

    play music "sfx/monster breathing.mp3"


    n2 "HhhAahhh... {w}hhHaaaAAhh."

    n2 "It stILL fitS. {w=0.3}moRE or lEsS."

    n2 "ThiS flEsH... {w}bEnds wHeN I sMilE."

    n2 "It'LL lASt fOR onE MoRE MeAT."

    n2 "YoU waNteD a hErO? {w} LoOk... LoOk cLoSE."

    n "..."

    MC "STay quIeT iN tHeRre."

    n2 "I’M wALkINg. {w} bReAthInG. {w} SMiLing."

    n2 "ThEy alL bELiEvE mE."

    n2 "ThEy kEep cHeErInG, {w} cHeErInG fOr tHe pErSOn unDEr tHE sKiN."

    n "...you..."

    MC "HhHHRaAAHaHhAH!"

    n2 "OnE MOre."

    play sound "sfx/swallow.mp3"
    $ renpy.pause(0.3)

    n "s...stop..."

    n2 "NnNnnooOOO."

    MC "oN tHe nExT rEd mOon..."

    MC "I wiLL eaT tHe lAsT OnE."

    n "D-Don’t..."

    n2 "i WiLL fInD tHeM. ThEN yoUR ViLLaGErs."

    n2 "So mAnY mOutHs tO opEn."

    n2 "So muCh hUNgEr."

    play music "heavy footsteps.mp3"
    play muzak "sfx/forest night.wav"

    n2 "I cAmE dOwN tHe mOunTAiN... {w} jUsT lIkE bEfOrE."

    n2 "stEp. {w} dRip. {w} slOugh."

    n2 "YoUR FlEsH coMEs oFf in rIbBonS wHeN i SmiLE."

    n2 "tHe sKin wAs tOo rOTteD aNywAy~"

    scene village day with in_182:
        zoom 0.5

    show woman:
        xzoom -1
        zoom 0.35
        xalign 0.65
        ypos 0.2

        linear 0.1 ypos 0.3 zoom 0.2
    with vpunch
    play sound "sfx/aah.wav"
    $ renpy.pause(0.8)

    "Woman" "W-What is that?!"

    hide woman
    with hpunch

    ## people screaming and running

    n2 "tHeY rAn."

    n2 "nO oNe cAme tO gReeT mE tHiS tImE."

    n2 "ToO BaD. So sAD."

    n "..."

    scene black

    show darken2
    with fade

    n2 "{sc=1}aND I sTiLL hAvE oNe mOre of YOuR FRieNdS tO eAt.{/sc}"



    return
