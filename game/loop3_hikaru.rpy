label loop3_hikaru:

    $ hmask = True

    scene village day:
        zoom 0.5
    show darken

    n2 "tHe dOOrs aRe sHuT."


    n2 "i sEe eYeS tHrOuGh thE sLatS."

    n2 "tHeY aRe WaTChIng..."

    show hik shocked behind darken:
        zoom 0.3
        xalign 0.65
        yalign 0
        yoffset 110
        xzoom 1.0
        yzoom 1.0
        alpha 0.0

        linear 0.17 alpha 1.0 xalign 0.55 yoffset 50
    stop music
    stop muzak

    hikaru "...!"

    n2 "oH."

    n2 "tHe tEnDeR mEaT."

    n "No–"

    n "Hikaru, run–"

    hikaru "{sc=5}That's [persistent.player_name]'s face...{/sc}"

    show hik rage behind darken:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        alpha 1.0

        # Violent, irregular shakes (shock)
        linear 0.06 xoffset -38 yoffset 24
        linear 0.05 xoffset 32 yoffset -11
        linear 0.04 xoffset -28 yoffset 19
        linear 0.04 xoffset 21 yoffset -15
        linear 0.05 xoffset 0 yoffset 50   # Back to original

    hikaru "{glitch=7}THAT’S–{w}that’s–{/glitch}"

    n "Don’t say it. Don’t remember. Don’t look–"

    show hik rage behind darken:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        alpha 1.0

        # Violent, irregular shakes (shock)
        linear 0.06 xoffset -38 yoffset 24
        linear 0.05 xoffset 32 yoffset -11
        linear 0.04 xoffset -28 yoffset 19
        linear 0.04 xoffset 21 yoffset -15
        linear 0.05 xoffset 0 yoffset 50   # Back to original
    play music "spooky.mp3"

    hikaru "{size=+7}WHERE IS MY LOVER?!{/size}"

    hikaru "{sc=7}WHERE IS–WHERE ARE–{/sc}"

    MC happycl3 "It'S Me, HiKARu."

    hikaru "{size=+6}YAMAKUI...!{/size}"

    hikaru "{glitch=10}How dare you wear [persistent.player_name]'s skin and mock me in that voice!{/glitch}"

    hikaru "..."

    hikaru "{i}I'll avenge you, [persistent.player_name]. Just wait...!{/i}"

    play sound "sfx/whip.mp3"

    show hik rage behind darken:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        alpha 1.0

        # Quick ninja leap left, fade out fast
        linear 0.11 xoffset -290 yoffset 8 zoom 0.22
        linear 0.07 xoffset -560 yoffset -32 zoom 0.12 alpha 0.0
    with hpunch

    n "Hikaru, no–You won't win against the Yamakui!"

    n2 "HraHhaHAHAHA!"

    n2 "ThEy lOoK sO sOFT whEn tHeY bReAK~"

    scene moon1
    with fade

    stop sound

    n2 "tHe dAys paSS."

    scene moon2
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "DrIP."

    play sound "sfx/drip.wav"

    n2 "DRiP"

    play sound "sfx/drip.wav"

    n2 "DriPdrIPDRip."

    scene moon3
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "mY fAcE fALls oFF iN sTrIpS."

    play sound "sfx/stretch.mp3"

    n2 "i wEar iT bAckwArDs sOmEtImEs. {w}fUnNy."

    n "{i}I don't care whatever you are doing to my face...{/i}"

    n "But let Hikaru go..."

    n "{cps=13}Please,{/cps} I’m begging you."

    n "You already took Shiori, {w=0.1}Yamato..."

    n "But please...{w} Just {i}this one...{/i}"

    n "{sc=5}I loved Hikaru.{/sc}"

    scene moon4
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "NnNnnNnnNn."

    n2 "I wAnT tO wAtCh tHe hOpe roT iN tHeIr mOuTh."

    n "{sc=2}Please.{/sc}"

    n "{cps=12}Please please please I’ll do anything.{/cps}"

    n "{i}Kill more. Eat more. I don’t care.{/i}"

    n "Just leave Hikaru, let me save JUST ONE."

    n "{glitch=1}Everyone else is gone and I can’t–{/glitch}"

    n2 "tEnDeR mEAt iS sWeEtEsT wHeN iT knEw yOu bEfOrE."

    n "{sc=5}NO!!{/sc}"

    n "{cps=14}PLEASE–{/cps}"

    scene moon5
    play sound "sfx/heartbeat.mp3"
    with flashred
    pause 0.3

    n2 "DoN'T WorRY, GhOSt."



    stop music

    scene black
    with fade

    n2 "{atl=0.3,drop_text~#~ 1.5, bounce_text~5}i’LL mAkE iT bEauTiFuL.{/atl}"

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

    scene village day:
        zoom 0.5
    show darken
    with in_212

    n2 "sUCh a DeAD VillAGe."

    n2 "nO oNe hAs bEen hEre iN dAys."

    play sound "sfx/whip.mp3"

    hikaru "NOW–!"

    n2 "Hkk–!"

    $ hsword = True

    scene black

    play sound "swing.wav"

    show slash_arc

    pause 1

    scene village day:
        zoom 0.5

    show hik rage:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1
        yzoom 1.0

        linear 0.08 yoffset 18

        linear 0.14 zoom 0.25 yoffset -38 xoffset 144

        pause 0.10

        linear 0.12 yoffset 0

        ease 0.015 yoffset 50
        ease 0.01 yoffset 130
    show darken
    with hpunch

    play music "Battora.mp3"

    n2 "TcH. ReLENtlESS."

    hikaru "WHY–"

    show hik rage behind darken:
        zoom 0.25
        xalign 0.4
        xoffset 144
        yoffset 130
        xzoom 1
        yzoom 1.0

        linear 0.05 xoffset 121 yoffset 180
        linear 0.04 xoffset 161 yoffset 110
        linear 0.04 xoffset 126 yoffset 146
        linear 0.05 xoffset 174 yoffset 100
        linear 0.04 xoffset 144 yoffset 130

        pause 0.10

    hikaru "WHY WON’T YOU DIE?!"

    n2 "HeHhhH... {w=0.3}HeHhhHhHHHhh..."

    n2 "tEnDeR oNe hAs tEetH."

    n2 "mAkEs mE hUnGry."

    ## some animations of Hikaru swing again

    n2 "..."

    hikaru "Ngh–"

    show hik shocked behind darken:
        zoom 0.25
        xalign 0.4
        xoffset 144
        yoffset 130
        xzoom 1
        yzoom 1.0

        linear 0.05 xoffset 121 yoffset 180
        linear 0.04 xoffset 161 yoffset 110
        linear 0.04 xoffset 126 yoffset 146
        linear 0.05 xoffset 174 yoffset 100
        linear 0.04 xoffset 144 yoffset 130

        pause 0.10

    hikaru "Have the kami-sama abandoned us!?"

    MC happy3 "{size=+5}{color=#ff0000}Y E S.{/color}{/size}"

    MC happy3 "YoUR KaMI-sAMa HaVe AbANDonED YoU."

    n2 "i'LL eAt yOu."

    n2 "oN tHe rEd mOoN."

    n "HIKARU–"

    n2 "yOu wAnT tO sAvE tHeM?"

    n2 "tOo lAtE."

    n2 "I wAnT tO tAsTe yOuR hOpE {w}wHiLe thEy dIe."

    play sound "sfx/whip.mp3"

    show hik shocked behind darken:
        zoom 0.25
        xalign 0.4
        xoffset 144
        yoffset 130
        xzoom 1
        yzoom 1.0

        linear 0.10 xoffset 440 yoffset 80 zoom 0.18
        linear 0.07 xoffset 860 yoffset 34 zoom 0.08 alpha 0.0

    n "They’re retreating..."

    n "I can’t–"

    n "I can’t watch this again–"

    pause 0.1

    play sound "sfx/heartbeat.mp3"
    with flashred

    n2 "ThEn I WiLL GOUge oUt YoUr EYeS."

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

    n2 "iT iS tImE."

    play music "Blood Ritual.mp3"

    scene village night with in_212:
        zoom 0.5
        xalign 0.5
        yalign 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    show darken2

    MC evil3 "Oh HikaRuuUuUUu~"

    scene village night:
        zoom 0.5
        xalign 0.5
        yalign 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.14 zoom 0.54 xoffset 26
        linear 0.13 zoom 0.59 xoffset -29
        linear 0.14 zoom 0.64 xoffset 19
        linear 0.15 zoom 0.69 xoffset 18


    MC evil3 "ComE Out, cOmE ouT, wheReVer yOu ARe~"



    scene black
    play sound "swing.wav"
    show slash_fx_horizontalred
    $ renpy.pause(0.1, hard=True)
    show darken2
    with hpunch

    hikaru "DIE!!"

    play sound "swing.wav"
    show combo_slash_2red
    $ renpy.pause(0.1, hard=True)
    show darken2
    with vpunch

    MC nervous3 "Khh– {w}yoU GoT mE."

    MC evil3 "BuT NoT ENouGH, BiRD."

    scene village night:
        zoom 0.67
        xalign 0.5
        yalign 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

    show hik panic:
        zoom 0.47
        align (0.5, 0.005)
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.29 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.25 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 120
        linear 0.09 yoffset 190
    show darken2
    with vpunch
    hikaru "Wh–That was a direct hit!"

    hikaru "Why are you still standing–!?"

    play music "Goodbye.mp3"

    MC sad3 "..."

    MC sad3 "Help me."

    MC sad3 "Hikaru... {w}please–"

    MC sad3 "I’m still in here–{w} they’re controlling me–"

    MC sad3 "You can still save me–"

    show hik panic behind darken2:
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 190
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Quick upward-back jolt
        linear 0.09 yoffset 110 zoom 0.22    # Sharp jump up and shrink (shock)
        linear 0.08 yoffset 150 zoom 0.25    # Bounce down
        linear 0.07 yoffset 190 zoom 0.25    # Settle back

        pause 0.09

    hikaru "...!"

    n "No! Don't! That's not me–!"

    hikaru "I..."

    hikaru "That voice–"

    hikaru "You’re lying–no, wait–"

    MC sadcl3 "I don’t want to die, Hikaru..."

    n "RUN..."

    n "{sc=2}RUN!!!{/sc}"

    n "IT’S NOT {sc=2}ME!!{/sc}"

    hikaru "...I..."

    n "{sc=1}MOVE–{/sc}"

    n2 "tOo lAtE."


    play sound "sfx/stumble.mp3"


    scene village night:
        zoom 0.67
        xalign 0.5
        yalign 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Abrupt lunge to center, very fast
        linear 0.14 zoom 1.14

    show hik madcry behind darken2:
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 190
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.14 zoom 0.66 xalign 0.5 yalign 0.0 xoffset 0 yoffset 0
    show darken2
    pause 0.1

    scene black
    play sound "sfx/stab.mp3"
    with flashred

    pause 0.5

    play sound "sfx/tearflesh.wav"

    scene cg_loop3hikaru:
        zoom 0.8
        xalign 0.5
        yalign 0.5

        linear 0.4 zoom 0.5



    hikaru "{cps=13}Ah...{/cps}"

    hikaru "{cps=13}I can't kill you while you still have that face, after all...{w=0.1}{/cps}"

    hikaru "{cps=13}Even if it's broken and rotting...{/cps}"

    n2 "..."

    hikaru "{cps=13}I still keep the scarf, you know?{w=0.1}{/cps}"

    hikaru "{sc=1}The one you gave me before you left?{/sc}"

    hikaru "{cps=13}It still feels like you're here...{w=0.1}{/cps}"

    hikaru "{sc=1}I’ll see you again, right?{/sc}"
    hikaru "...The real you?"

    n "...Hikaru..."

    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n2 "tEnDeR..."

    play sound "sfx/splurt.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n2 "mMmhhHH..."

    play sound "sfx/slurrp.mp3"

    n2 "sWaLLoW..."

    play sound "sfx/slurrp.mp3"

    n2 "SwAllOw..."


    play sound "sfx/slurrp.mp3"

    n2 "SwAllOw."

    n "You took everything from me..."

    n "And now..."

    stop music

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}N O W  {w=0.1}Y O U R  {w=0.1}L O V E R  {w=0.1}I S  {w=0.1}D E A D {w=0.1} T O O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    $ renpy.pause(3.0)


    $ persistent.hikaru_dies = True

    $ persistent.loop3 = True

    $ renpy.full_restart()

    return
