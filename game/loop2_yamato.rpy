label loop2_yamato:
    scene black
    with fade

    pause 0.2

    scene white_bg
    with out_182

    show petals_dense
    show petals_scatter

    n2 "...I spent most of my days with the gamey one."

    n2 "No choice but to go for gamey meat..."

    scene black
    with fade

    pause 0.3



    scene shrine night with in_212:
        zoom 0.5
        xalign 0.5

        pause 0.1
        linear 2 zoom 0.7
    pause 0.5
    show yam eldritch1:
        zoom 0.4
        xanchor 0.5
        xalign 1.15
        yalign -0.04
        xzoom 1.0
        yzoom 1.14
        yoffset -22
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.33 zoom 0.35 yzoom 1.03 xalign 0.65 yoffset -10
        linear 0.17 zoom 0.3 yzoom 1.0 xalign 0.6 yoffset 0



    play music "noinomai.mp3"

    n "You can feel the voices crawling up your spine... Someone praying at the shrine."

    n "Not to the kami-sama, but to something more ancient and sinister.. Blasphemous at its core."

    n "And it draws you right to it, your blood feeling right at home."

    n "You're familiar with the voice. Of course it's Yamato."


    show yam eldritch:
        zoom 0.3
        xanchor 0.5
        xalign 0.6
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        # Seizure-like rapid shaking and twitching
        linear 0.06 xoffset -24 yoffset -8
        linear 0.05 xoffset 17 yoffset 10
        linear 0.04 xoffset -15 yoffset -14
        linear 0.04 xoffset 12 yoffset 15
        linear 0.05 xoffset -8 yoffset -11
        linear 0.04 xoffset 9 yoffset 12
        linear 0.03 xoffset -6 yoffset -9
        linear 0.03 xoffset 4 yoffset 8
        linear 0.04 xoffset 0 yoffset 0    # Stop, reset to neutral

        pause 0.09



    n "He’s... bent forward at a wrong angle. Spine curled like a beast crawling toward a scent."

    n "He's clutching his stomach."

    n "His skin ripples, something is moving underneath. A worm-like creature, crawling under the surface."

    yamato "{sc}...rggna...{/sc}"

    show screen black_flicker
    with Pause(0.45)  # 0.05*8 + buffer for full duration (optional)
    hide screen black_flicker

    n2 "GhhhhhH."

    show screen black_flicker
    with Pause(0.45)  # 0.05*8 + buffer for full duration (optional)
    hide screen black_flicker
    scene black

    show screen eyessss


    $ phrase = "大地の主よ、目覚めよ、目覚めよ"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.045    # <<<<<< REDUCE SPACING FOR CENTERED LOOK
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    # Show each letter with classic script, using as to assign tags
    show expression Text("大", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as wrb1
    show expression Text("地", style="jojo_bigtext") at wriggle_zoomout(0.10, start_x+spacing*1, y_center, 2.1) as wrb2
    show expression Text("の", style="jojo_bigtext") at wriggle_zoomout(0.20, start_x+spacing*2, y_center, 2.1) as wrb3
    show expression Text("主", style="jojo_bigtext") at wriggle_zoomout(0.30, start_x+spacing*3, y_center, 2.1) as wrb4
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(0.40, start_x+spacing*4, y_center, 2.1) as wrb5
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.50, start_x+spacing*5, y_center, 2.1) as wrb6
    show expression Text("目", style="jojo_bigtext") at wriggle_zoomout(0.60, start_x+spacing*6, y_center, 2.1) as wrb7
    show expression Text("覚", style="jojo_bigtext") at wriggle_zoomout(0.70, start_x+spacing*7, y_center, 2.1) as wrb8
    show expression Text("め", style="jojo_bigtext") at wriggle_zoomout(0.80, start_x+spacing*8, y_center, 2.1) as wrb9
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*9, y_center, 2.1) as wrb10
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(1.00, start_x+spacing*10, y_center, 2.1) as wrb11
    show expression Text("目", style="jojo_bigtext") at wriggle_zoomout(1.10, start_x+spacing*11, y_center, 2.1) as wrb12
    show expression Text("覚", style="jojo_bigtext") at wriggle_zoomout(1.20, start_x+spacing*12, y_center, 2.1) as wrb13
    show expression Text("め", style="jojo_bigtext") at wriggle_zoomout(1.30, start_x+spacing*13, y_center, 2.1) as wrb14
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(1.40, start_x+spacing*14, y_center, 2.1) as wrb15



    yamato "{cps=30}{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}Master of the earth,{/sc}{/outlinecolor}{/color}{/size}{w=0.2}{fast}{size=+1}{color=#ff0000}{sc=6} awake,{/sc}{/color}{/size}{w=0.5}{fast}{size=+1}{color=#ff0000}{sc=6} awake...{/sc}{/color}{/size}{/cps}"

    $ renpy.pause(2.6)

    hide wrb1
    hide wrb2
    hide wrb3
    hide wrb4
    hide wrb5
    hide wrb6
    hide wrb7
    hide wrb8
    hide wrb9
    hide wrb10
    hide wrb11
    hide wrb12
    hide wrb13
    hide wrb14
    hide wrb15

    show screen eyessss onlayer background

    show yam normal:
        zoom 0.4
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.5 zoom 0.3




    $ phrase = "我に力を、炎を授けたまえ。"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.052   # good for 13 chars, adjust if needed for your font
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    show expression Text("我", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as ch1
    show expression Text("に", style="jojo_bigtext") at wriggle_zoomout(0.09, start_x+spacing*1, y_center, 2.1) as ch2
    show expression Text("力", style="jojo_bigtext") at wriggle_zoomout(0.18, start_x+spacing*2, y_center, 2.1) as ch3
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.27, start_x+spacing*3, y_center, 2.1) as ch4
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.36, start_x+spacing*4, y_center, 2.1) as ch5
    show expression Text("炎", style="jojo_bigtext") at wriggle_zoomout(0.45, start_x+spacing*5, y_center, 2.1) as ch6
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.54, start_x+spacing*6, y_center, 2.1) as ch7
    show expression Text("授", style="jojo_bigtext") at wriggle_zoomout(0.63, start_x+spacing*7, y_center, 2.1) as ch8
    show expression Text("け", style="jojo_bigtext") at wriggle_zoomout(0.72, start_x+spacing*8, y_center, 2.1) as ch9
    show expression Text("た", style="jojo_bigtext") at wriggle_zoomout(0.81, start_x+spacing*9, y_center, 2.1) as ch10
    show expression Text("ま", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*10, y_center, 2.1) as ch11
    show expression Text("え", style="jojo_bigtext") at wriggle_zoomout(0.99, start_x+spacing*11, y_center, 2.1) as ch12
    show expression Text("。", style="jojo_bigtext") at wriggle_zoomout(1.08, start_x+spacing*12, y_center, 2.1) as ch13

    $ renpy.pause(2.6)

    yamato "{cps=30}{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}Grant me strength,{/sc}{/outlinecolor}{/color}{/size}{w=0.2}{fast}{size=+1}{color=#ff0000}{sc=6} grant me{/sc}{/color}{/size}{w=0.5}{fast}{size=+1}{color=#ff0000}{sc=6} flame...{/sc}{/color}{/size}{/cps}"

    hide ch1
    hide ch2
    hide ch3
    hide ch4
    hide ch5
    hide ch6
    hide ch7
    hide ch8
    hide ch9
    hide ch10
    hide ch11
    hide ch12
    hide ch13
    hide screen eyessss

    scene shrine night with in_212:
        zoom 0.5
        xalign 0.5

        pause 0.1
        linear 0.1 zoom 0.7
    show yam eldritch:
        zoom 0.4
        xanchor 0.5
        xalign 1.15
        yalign -0.04
        xzoom 1.0
        yzoom 1.14
        yoffset -22

        linear 0.33 zoom 0.35 yzoom 1.03 xalign 0.65 yoffset -10
        linear 0.17 zoom 0.3 yzoom 1.0 xalign 0.6 yoffset 0

    n "Yamato lifts his head,{w=0.2} you can see his eyes are {sc=6}rolled white.{/sc}"

    n "Blood starts to drip from his mouth that doesn’t stop moving,{w=0.2} even when he’s no longer making sound."

    n2 "{i}Don't have claws on your own, so you ask for another.{/i}"

    show yam eldritch:
        zoom 0.3
        xanchor 0.5
        xalign 0.6
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

        # Jagged, twitchy, seizure-like convulsions
        linear 0.05 xoffset -20 yoffset 11
        linear 0.04 xoffset 17 yoffset -15
        linear 0.04 xoffset -13 yoffset 12
        linear 0.03 xoffset 15 yoffset -10
        linear 0.04 xoffset -9 yoffset 8
        linear 0.03 xoffset 6 yoffset -7
        linear 0.03 xoffset -4 yoffset 5
        linear 0.04 xoffset 0 yoffset 0   # Back to neutral

        pause 0.09

    n "You take a step back, eyes still glued to Yamato's {sc=4}twitchy{/sc} figure."

    yamato "Heh."

    show yam eldritch2:
        zoom 0.3
        xanchor 0.5
        xalign 0.6
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

        # Jagged, twitchy, seizure-like convulsions
        linear 0.05 xoffset -20 yoffset 11
        linear 0.04 xoffset 17 yoffset -15
        linear 0.04 xoffset -13 yoffset 12
        linear 0.03 xoffset 15 yoffset -10
        linear 0.04 xoffset -9 yoffset 8
        linear 0.03 xoffset 6 yoffset -7
        linear 0.03 xoffset -4 yoffset 5
        linear 0.04 xoffset 0 yoffset 0   # Back to neutral

        pause 0.09

    yamato "{i}You came t’watch, huh?{/i}"

    yamato "Maybe now you’ll see what I become."

    show yam eldritch2:
        zoom 0.3
        xanchor 0.5
        xalign 0.6
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

        # Jagged, twitchy, seizure-like convulsions
        linear 0.05 xoffset -20 yoffset 11
        linear 0.04 xoffset 17 yoffset -15
        linear 0.04 xoffset -13 yoffset 12
        linear 0.03 xoffset 15 yoffset -10
        linear 0.04 xoffset -9 yoffset 8
        linear 0.03 xoffset 6 yoffset -7
        linear 0.03 xoffset -4 yoffset 5
        linear 0.04 xoffset 0 yoffset 0   # Back to neutral

        pause 0.09

    yamato "When I pray t’something that can beat ya."

    n2 "Yamato."

    n2 "{cps=8}Yamato. {w=0.2}Yamato. {w=0.1}Yamato...{/cps}"

    n2 "{w=0.3}Little mutt crawling to the hole.{w=0.3}"

    n2 "Wants new teeth, ha?"

    play sound "sfx/firecrackle.mp3"
    show red_flash_slow onlayer screens
    show darken2
    with flashred

    n "{glitch=8}The altar catches fire,{w=0.2} then everything is enveloped in smoke...{/glitch}"

    if persistent.shiori_dies:

        hikaru "{sc=6}YAMATO!{/sc}"

        show hik normal behind darken2:
            zoom 0.31
            xanchor 0.5
            xalign 1.15
            yalign -0.20
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.13 xalign 0.9
            linear 0.10 xalign 0.7
            linear 0.10 xalign 0.8
        show yam eldritch1 behind darken2:
            zoom 0.3
            xanchor 0.5
            xalign 0.6
            yalign -0.04
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.09 xalign 0.57
            linear 0.08 xalign 0.2


        n "Hikaru rushes in, Sai in hand."

        yamato "...!"

        show hik normal:
            zoom 0.31
            xanchor 0.5
            xalign 0.8
            yalign -0.20
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.06 xoffset -18
            linear 0.06 xoffset 19
            linear 0.05 xoffset -13
            linear 0.05 xoffset 9
            linear 0.06 xoffset 0

        pause 0.05

        hikaru "Yamato... What are you doing!?"

        yamato "Tch... Look at ya screamin’ like it matters now."

        yamato "{cps=50}Ya people always looked at [persistent.player_name] like they were gonna save us, but no, they returned as {i}a monster.{/i}{/cps}"

        hikaru "What!?"

        MC smug2 "He's gone insane because of his jealousy."

        hikaru "Yamato, this isn’t you {i}at all–{/i}"

        show yam eldritch1:
            zoom 0.3
            xanchor 0.5
            xalign 0.2
            yalign -0.04
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.06 xoffset -13 yoffset 7
            linear 0.04 xoffset 17 yoffset -6
            linear 0.05 xoffset -10 yoffset 9
            linear 0.03 xoffset 6 yoffset -8
            linear 0.04 xoffset 0 yoffset 0

        pause 0.08

        yamato "I trained twice as {i}hard{/i}. I've bled myself {i}stupid{/i} for this place. And what do I get?"

        hikaru "So you–"

        hikaru "You thought summoning something worse was the answer?"

        yamato "{sc=1}I asked for power.{/sc}"

        yamato "And I fuckin’ {i}got it.{/i}"

        show yam eldritch1:
            zoom 0.3
            xanchor 0.5
            xalign 0.2
            yalign -0.04
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.06 xoffset -13 yoffset 7
            linear 0.04 xoffset 17 yoffset -6
            linear 0.05 xoffset -10 yoffset 9
            linear 0.03 xoffset 6 yoffset -8
            linear 0.04 xoffset 0 yoffset 0

        pause 0.08

        yamato "{sc=2}Th' damn Yamakui is still alive, so I'll have the power to kill it!{/sc}"

        hikaru "Yamato, please–"

        play sound "sfx/quake.mp3"
        with sshake

        n "{glitch=7}The ground shudders.{w=0.2} and Hikaru stumbles backwards.{/glitch}"

        hikaru "{sc=7}What did you CALL!?{/sc}"

        show yam eldritch1:
            zoom 0.3
            xanchor 0.5
            xalign 0.2
            yalign -0.04
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.06 xoffset -13 yoffset 7
            linear 0.04 xoffset 17 yoffset -6
            linear 0.05 xoffset -10 yoffset 9
            linear 0.03 xoffset 6 yoffset -8
            linear 0.04 xoffset 0 yoffset 0

            pause 0.08


            linear 0.02 xoffset -180 xzoom 1.17 yzoom 0.87
            linear 0.01 xoffset -260 xzoom 1.11 yzoom 0.93
            linear 0.01 xoffset -1000 xzoom 1.0 yzoom 1.0



        hikaru "Yamato–!!"

    elif persistent.hikaru_dies:

        show yam normal:
            zoom 0.3
            xanchor 0.5
            xalign 0.2
            yalign -0.04
            xzoom 1.0
            yzoom 1.0
            yoffset 0


            linear 0.06 xoffset -13 yoffset 7
            linear 0.04 xoffset 17 yoffset -6
            linear 0.05 xoffset -10 yoffset 9
            linear 0.03 xoffset 6 yoffset -8
            linear 0.04 xoffset 0 yoffset 0

            pause 0.08


            linear 0.10 xoffset -180 xzoom 1.17 yzoom 0.87
            linear 0.08 xoffset -260 xzoom 1.11 yzoom 0.93
            linear 0.10 xoffset -370 xzoom 1.0 yzoom 1.0
        n "He's gone..."


        scene shrine night with in_212:
            zoom 0.5

        show shi normal:
            zoom 0.8
            xalign 0.1
            yoffset -20
            xoffset -150
        with dissolve

        shiori "...Yamato-kun?"

        n "Her voice cracks as she steps closer.{w=0.3} She’s trying not to cry."

        shiori "{i}[persistent.player_name]...? What was that just now?{/i}"

        shiori "W-What’s going on?"

        MC normal2 "...He’s gone, Shiori."

        shiori "{sc=5}That wasn’t a kami, was it?{/sc}"

        shiori "The prayers... The chanting's all wrong..."

        MC sadcl2 "He’s beyond saving now."

        shiori "..."

        shiori "{cps=15}Stupid, stupid Yamato...{/cps}"

        shiori "{i}Always acting like he's the only one who suffers...{/i} {w=0.2}always pretending he's strong..."

        shiori "But he just needed someone to hug him. Someone to tell him it’s okay."

        n "Her lips tremble...{w=0.2} then curl up in a slow, bitter smile."

        shiori "Everything can be fixed."

        shiori "Right? I mean... {w=0.2} if you just love someone enough..."

        shiori "{sc=6}Even the Yamakui... {w=0.2} it just needs someone to see it as it really is.{/sc}"

        shiori "{i}Maybe it’s angry because it’s lonely, and because we’re all so mean to it.{/i}"

        shiori "But if we just... {w=0.2} sat down...{w=0.2}  maybe lit some incense... {w=0.2} and just talked..."

        shiori "It’d understand."

        shiori "It’d stop, {glitch=7}right?{/glitch}"

        MC yan2 "..."

        shiori "{cps=13}If only I was given the chance to talk to it...{/cps}"

        shiori "Because love always wins, doesn’t it?"

        n2 "Ha."

        n2 "She’s gone too."

        n2 "{i}Split her open and see what 'love' looks like inside.{/i}"

    else:

        n2 "He called it."

        n2 "{w=0.2}Now let’s see if he can contain it."

    scene black with fade

    stop music

    scene black

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

    n "The sky is fully red now,{w=0.2} it's just mere hours before the red moon is full."

    play music "Blood Ritual.mp3"

    show yam glitched:
        zoom 0.23
        xalign 0.5
        yalign 0.2
        yoffset 400
        xoffset 0
        alpha 0.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Fade in and crawl forward in jagged, irregular movements
        linear 0.18 zoom 0.26 xoffset -30 yoffset 428 alpha 0.3
        linear 0.15 zoom 0.29 xoffset 24 yoffset 410 alpha 0.6
        linear 0.13 zoom 0.31 xoffset -18 yoffset 402 alpha 0.7
        linear 0.14 zoom 0.34 xoffset 16 yoffset 394 alpha 0.86
        linear 0.13 zoom 0.37 xoffset -12 yoffset 400 alpha 1.0
        linear 0.18 zoom 0.4 xoffset 100 yoffset 300         # End fully centered, at zoom 0.4
    show moon7 glitched behind yam:
        zoom 1.0
        linear 2 zoom 1.3


    n "And of course, you saw the man {sc=5}practically crawling{/sc} towards you."

    n "Limbs jerking,{w=0.2} all bent up with one hand dragging behind,{w=0.2} flopping."

    n2 "Look, look who is crawling back."

    hide yam

    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Subtle, weird, not comical twitching
        linear 0.07 xoffset -19 yoffset 410
        linear 0.06 xoffset 13 yoffset 396
        linear 0.05 xoffset -11 yoffset 402
        linear 0.05 xoffset 8 yoffset 393
        linear 0.06 xoffset 100 yoffset 300   # Back to normal

        pause 0.10

    yamato "{cps=12}...tonight.{/cps}"

    n "His voice folds in on itself,{w=0.2} another voice is speaking from behind him...{w=0.2} or from inside him."
    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Subtle, weird, not comical twitching
        linear 0.07 xoffset -19 yoffset 410
        linear 0.06 xoffset 13 yoffset 396
        linear 0.05 xoffset -11 yoffset 402
        linear 0.05 xoffset 8 yoffset 393
        linear 0.06 xoffset 100 yoffset 300   # Back to normal

        pause 0.10
    play sound "sfx/glitch.wav"

    yamato "{sc=6}T-tonight–{w=0.2}t–{w=0.2}tonight–{/sc}"

    yamato "{glitch=8}...Red moon...{/glitch}"

    yamato "{i}I will–{/i}"
    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Subtle, weird, not comical twitching
        linear 0.07 xoffset -19 yoffset 410
        linear 0.06 xoffset 13 yoffset 396
        linear 0.05 xoffset -11 yoffset 402
        linear 0.05 xoffset 8 yoffset 393
        linear 0.06 xoffset 100 yoffset 300   # Back to normal

        pause 0.10
    play sound "sfx/glitch.wav"

    yamato "Tear {w=0.2}you–"

    yamato "Tear–"

    yamato "{sc=7}{w=0.2}YOU–{/sc}"

    MC evil2 "Growl all you want, {i}mutt.{/i}"
    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Subtle, weird, not comical twitching
        linear 0.07 xoffset -19 yoffset 410
        linear 0.06 xoffset 13 yoffset 396
        linear 0.05 xoffset -11 yoffset 402
        linear 0.05 xoffset 8 yoffset 393
        linear 0.06 xoffset 100 yoffset 300   # Back to normal

        pause 0.10
    play sound "sfx/glitch.wav"

    yamato "No more {w=0.2}GODS."

    yamato "{color=#ff002e}Y A M A K U I.{/color}"

    yamato "{sc=6}K-k-k-k-KILL.{/sc}"

    yamato "{sc=8}TONIGHT–{/sc}"
    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Subtle, weird, not comical twitching
        linear 0.07 xoffset -19 yoffset 410
        linear 0.06 xoffset 13 yoffset 396
        linear 0.05 xoffset -11 yoffset 402
        linear 0.05 xoffset 8 yoffset 393
        linear 0.06 xoffset 100 yoffset 300   # Back to normal

        pause 0.10
    play sound "sfx/glitch.wav"

    yamato "{size=+10}{color=#ff2200}{b}TONIIIIIIIIIIIIIIIIIIIIIGHT–{/b}{/color}{/size}"

    n "He lunges–"

    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        easein 0.05 zoom 0.6 yoffset 180 xoffset 140   # Lurches up and forward

    scene black with vpunch


    # Optional: Play sound effects in sync
    scene black
    play sound "sfx/screech.wav"
    show slash_fx_horizontalred
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "sfx/screech.wav"
    show combo_slash_2red
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "sfx/screech.wav"
    show combo_slash_1red
    $ renpy.pause(0.1, hard=True)

    show darken2

    n "{sc=2}His sword makes a screaming sound.{/sc}"

    n "I’ve never heard metal scream.{w=0.2} I–I don’t know what that was."

    yamato "{sc=2}Oni.{/sc}"

    yamato "{color=#ff002e}Time to die!{/color}"

    n "That is no longer Yamato's voice anymore..."

    n "No. Yamato, stop. Please–{w=0.1}just–{w=0.1}stop this–"

    n "That’s not you talking!"

    n "You’re still in there! {sc=2}Please!{/sc}"

    yamato "The master of the earth has blessed me!"

    n "Yamato raises his sword at an unexpected speed, and zig-zagged towards you."

    scene black
    play sound "sfx/screech.wav"
    show combo_slash_3red
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "sfx/screech.wav"
    show combo_slash_1red
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "sfx/screech.wav"
    show slash_x2red
    $ renpy.pause(0.1, hard=True)
    show darken2


    n "You draw your own weapon the moment he strikes."

    n "The impact is enough to crack the ground you're standing on."

    n2 "FASTER."

    n2 "TEAR HIM."

    n "No, please, this is wrong...!"

    n "Yamato used to spar with me under this same moonlight."

    n "We used to laugh. He used to swear when I tackled him down."

    n "Now he’s... he’s–"

    yamato "{glitch=12}ThE ReD MoON wiLL be YoUR FuNeRAl–{/glitch}"

    # Optional: Play sound effects in sync
    scene black
    play sound "sfx/screech.wav"
    show slash_fx_horizontalred
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "sfx/screech.wav"
    show combo_slash_2red
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "sfx/screech.wav"
    show combo_slash_1red
    $ renpy.pause(0.1, hard=True)
    show darken2

    n "You block, parry, twirl–"

    n "The blade in your hands splits Yamato’s in two, but it was only an afterimage."

    n2 "{i}Still too slow–!{/i}"

    show yam glitched:
        zoom 0.23
        xalign 0.5
        yalign 0.2
        yoffset 400
        xoffset 0
        alpha 0.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Fade in and crawl forward in jagged, irregular movements
        linear 0.08 zoom 0.26 xoffset -30 yoffset 428 alpha 0.3
        linear 0.01 zoom 0.29 xoffset 24 yoffset 410 alpha 0.6
        linear 0.01 zoom 0.31 xoffset -18 yoffset 402 alpha 0.7
        linear 0.01 zoom 0.34 xoffset 16 yoffset 394 alpha 0.86
        linear 0.02 zoom 0.37 xoffset -12 yoffset 400 alpha 1.0
        linear 0.01 zoom 0.4 xoffset 100 yoffset 300         # End fully centered, at zoom 0.4
    show moon7 glitched behind yam:
        zoom 1.0
        linear 0.1 zoom 1.3
    with sshake

    yamato "...Nnn–!"

    n "He retches,{w=0.2} out come string of black, twitching, writhing things."

    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Subtle, weird, not comical twitching
        linear 0.07 xoffset -19 yoffset 410
        linear 0.06 xoffset 13 yoffset 396
        linear 0.05 xoffset -11 yoffset 402
        linear 0.05 xoffset 8 yoffset 393
        linear 0.06 xoffset 100 yoffset 300   # Back to normal

        pause 0.10
    play sound "sfx/glitch.wav"

    yamato "{sc=6}Still–still ain’t done–!{/sc}"

    yamato "I’ll break ya in pieces. One piece for the friend I can't remember, and another for [persistent.player_name]–"

    play sound "sfx/fall.mp3"

    hide yam

    show moon7 glitched:
        linear 0.2 zoom 2
        xalign 0.5
        yalign 0.5
        rotate 0
        linear 0.3 rotate 180
    pause 0.1
    scene black

    n "{cps=14}Everything stops.{/cps}"

    n "He’s kneeling now,{w=0.2} fists clenched so tight,{w=0.2} muttering, mumbling, that same chant again."

    n "Asking for power, for blessing..."

    scene black

    with dissolve

    show screen eyessss


    $ phrase = "大地の主よ、目覚めよ、目覚めよ"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.045    # <<<<<< REDUCE SPACING FOR CENTERED LOOK
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    # Show each letter with classic script, using as to assign tags
    show expression Text("大", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as wrb1
    show expression Text("地", style="jojo_bigtext") at wriggle_zoomout(0.10, start_x+spacing*1, y_center, 2.1) as wrb2
    show expression Text("の", style="jojo_bigtext") at wriggle_zoomout(0.20, start_x+spacing*2, y_center, 2.1) as wrb3
    show expression Text("主", style="jojo_bigtext") at wriggle_zoomout(0.30, start_x+spacing*3, y_center, 2.1) as wrb4
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(0.40, start_x+spacing*4, y_center, 2.1) as wrb5
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.50, start_x+spacing*5, y_center, 2.1) as wrb6
    show expression Text("目", style="jojo_bigtext") at wriggle_zoomout(0.60, start_x+spacing*6, y_center, 2.1) as wrb7
    show expression Text("覚", style="jojo_bigtext") at wriggle_zoomout(0.70, start_x+spacing*7, y_center, 2.1) as wrb8
    show expression Text("め", style="jojo_bigtext") at wriggle_zoomout(0.80, start_x+spacing*8, y_center, 2.1) as wrb9
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*9, y_center, 2.1) as wrb10
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(1.00, start_x+spacing*10, y_center, 2.1) as wrb11
    show expression Text("目", style="jojo_bigtext") at wriggle_zoomout(1.10, start_x+spacing*11, y_center, 2.1) as wrb12
    show expression Text("覚", style="jojo_bigtext") at wriggle_zoomout(1.20, start_x+spacing*12, y_center, 2.1) as wrb13
    show expression Text("め", style="jojo_bigtext") at wriggle_zoomout(1.30, start_x+spacing*13, y_center, 2.1) as wrb14
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(1.40, start_x+spacing*14, y_center, 2.1) as wrb15



    yamato "{cps=30}{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}Master of the earth,{/sc}{/outlinecolor}{/color}{/size}{w=0.2}{fast}{size=+1}{color=#ff0000}{sc=6} awake,{/sc}{/color}{/size}{w=0.5}{fast}{size=+1}{color=#ff0000}{sc=6} awake...{/sc}{/color}{/size}{/cps}"

    n "–No...."

    $ renpy.pause(2.6)

    hide wrb1
    hide wrb2
    hide wrb3
    hide wrb4
    hide wrb5
    hide wrb6
    hide wrb7
    hide wrb8
    hide wrb9
    hide wrb10
    hide wrb11
    hide wrb12
    hide wrb13
    hide wrb14
    hide wrb15

    show screen eyessss onlayer background

    show yam normal:
        zoom 0.4
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.5 zoom 0.3

    n2 "Again, again."



    $ phrase = "我に力を、炎を授けたまえ。"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.052   # good for 13 chars, adjust if needed for your font
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    show expression Text("我", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as ch1
    show expression Text("に", style="jojo_bigtext") at wriggle_zoomout(0.09, start_x+spacing*1, y_center, 2.1) as ch2
    show expression Text("力", style="jojo_bigtext") at wriggle_zoomout(0.18, start_x+spacing*2, y_center, 2.1) as ch3
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.27, start_x+spacing*3, y_center, 2.1) as ch4
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.36, start_x+spacing*4, y_center, 2.1) as ch5
    show expression Text("炎", style="jojo_bigtext") at wriggle_zoomout(0.45, start_x+spacing*5, y_center, 2.1) as ch6
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.54, start_x+spacing*6, y_center, 2.1) as ch7
    show expression Text("授", style="jojo_bigtext") at wriggle_zoomout(0.63, start_x+spacing*7, y_center, 2.1) as ch8
    show expression Text("け", style="jojo_bigtext") at wriggle_zoomout(0.72, start_x+spacing*8, y_center, 2.1) as ch9
    show expression Text("た", style="jojo_bigtext") at wriggle_zoomout(0.81, start_x+spacing*9, y_center, 2.1) as ch10
    show expression Text("ま", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*10, y_center, 2.1) as ch11
    show expression Text("え", style="jojo_bigtext") at wriggle_zoomout(0.99, start_x+spacing*11, y_center, 2.1) as ch12
    show expression Text("。", style="jojo_bigtext") at wriggle_zoomout(1.08, start_x+spacing*12, y_center, 2.1) as ch13

    $ renpy.pause(2.6)

    yamato "{cps=30}{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}Grant me strength,{/sc}{/outlinecolor}{/color}{/size}{w=0.2}{fast}{size=+1}{color=#ff0000}{sc=6} grant me{/sc}{/color}{/size}{w=0.5}{fast}{size=+1}{color=#ff0000}{sc=6} flame...{/sc}{/color}{/size}{/cps}"

    hide ch1
    hide ch2
    hide ch3
    hide ch4
    hide ch5
    hide ch6
    hide ch7
    hide ch8
    hide ch9
    hide ch10
    hide ch11
    hide ch12
    hide ch13


    n "He keeps chanting it, again and again and again–"

    n2 "{i}Ahhh, little mutt prays so sweetly.{/i}"

    n2 "Didn’t know he was feeding me."

    n "You take one step forward."


    scene black
    with dissolve

    show screen eyessss

    $ phrase = "よめ覚目、よめ覚目、よ主の地大"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.045
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as rev1
    show expression Text("め", style="jojo_bigtext") at wriggle_zoomout(0.10, start_x+spacing*1, y_center, 2.1) as rev2
    show expression Text("覚", style="jojo_bigtext") at wriggle_zoomout(0.20, start_x+spacing*2, y_center, 2.1) as rev3
    show expression Text("目", style="jojo_bigtext") at wriggle_zoomout(0.30, start_x+spacing*3, y_center, 2.1) as rev4
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.40, start_x+spacing*4, y_center, 2.1) as rev5
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(0.50, start_x+spacing*5, y_center, 2.1) as rev6
    show expression Text("め", style="jojo_bigtext") at wriggle_zoomout(0.60, start_x+spacing*6, y_center, 2.1) as rev7
    show expression Text("覚", style="jojo_bigtext") at wriggle_zoomout(0.70, start_x+spacing*7, y_center, 2.1) as rev8
    show expression Text("目", style="jojo_bigtext") at wriggle_zoomout(0.80, start_x+spacing*8, y_center, 2.1) as rev9
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*9, y_center, 2.1) as rev10
    show expression Text("よ", style="jojo_bigtext") at wriggle_zoomout(1.00, start_x+spacing*10, y_center, 2.1) as rev11
    show expression Text("主", style="jojo_bigtext") at wriggle_zoomout(1.10, start_x+spacing*11, y_center, 2.1) as rev12
    show expression Text("の", style="jojo_bigtext") at wriggle_zoomout(1.20, start_x+spacing*12, y_center, 2.1) as rev13
    show expression Text("地", style="jojo_bigtext") at wriggle_zoomout(1.30, start_x+spacing*13, y_center, 2.1) as rev14
    show expression Text("大", style="jojo_bigtext") at wriggle_zoomout(1.40, start_x+spacing*14, y_center, 2.1) as rev15

    MC yan2 "{cps=30}{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}.ekawa ,ekawa ,htrae eht fo retsaM{/sc}{/outlinecolor}{/color}{/size}{/cps}"

    $ renpy.pause(2.6)

    hide rev1
    hide rev2
    hide rev3
    hide rev4
    hide rev5
    hide rev6
    hide rev7
    hide rev8
    hide rev9
    hide rev10
    hide rev11
    hide rev12
    hide rev13
    hide rev14
    hide rev15



    $ phrase = "。えまたけ授を炎、を力に我"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.052
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    show expression Text("。", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as revc1
    show expression Text("え", style="jojo_bigtext") at wriggle_zoomout(0.09, start_x+spacing*1, y_center, 2.1) as revc2
    show expression Text("ま", style="jojo_bigtext") at wriggle_zoomout(0.18, start_x+spacing*2, y_center, 2.1) as revc3
    show expression Text("た", style="jojo_bigtext") at wriggle_zoomout(0.27, start_x+spacing*3, y_center, 2.1) as revc4
    show expression Text("け", style="jojo_bigtext") at wriggle_zoomout(0.36, start_x+spacing*4, y_center, 2.1) as revc5
    show expression Text("授", style="jojo_bigtext") at wriggle_zoomout(0.45, start_x+spacing*5, y_center, 2.1) as revc6
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.54, start_x+spacing*6, y_center, 2.1) as revc7
    show expression Text("炎", style="jojo_bigtext") at wriggle_zoomout(0.63, start_x+spacing*7, y_center, 2.1) as revc8
    show expression Text("、", style="jojo_bigtext") at wriggle_zoomout(0.72, start_x+spacing*8, y_center, 2.1) as revc9
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.81, start_x+spacing*9, y_center, 2.1) as revc10
    show expression Text("力", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*10, y_center, 2.1) as revc11
    show expression Text("に", style="jojo_bigtext") at wriggle_zoomout(0.99, start_x+spacing*11, y_center, 2.1) as revc12
    show expression Text("我", style="jojo_bigtext") at wriggle_zoomout(1.08, start_x+spacing*12, y_center, 2.1) as revc13

    MC yan2 "{cps=30}{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}.emalf em tnarG ,htgnerts em tnarG{/sc}{/outlinecolor}{/color}{/size}{/cps}"

    $ renpy.pause(2.6)

    hide revc1
    hide revc2
    hide revc3
    hide revc4
    hide revc5
    hide revc6
    hide revc7
    hide revc8
    hide revc9
    hide revc10
    hide revc11
    hide revc12
    hide revc13

    hide screen eyessss

    pause 0.2




    show yam glitched:
        zoom 0.4
        xalign 0.5
        yalign 0.2
        yoffset 300
        xoffset 100
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Sudden leap backward and up, zoom out for shock effect
        linear 0.12 zoom 0.32 yoffset 180 xoffset 0       # Leap up and back
        linear 0.10 zoom 0.25 yoffset 90 xoffset 25      # Further out, more shock

        pause 0.06
    show moon7 glitched behind yam:
        zoom 1.3


    yamato "What...{w=0.2} what the fuck are you saying..."

    MC evil2 "Your prayers, don't they go something like this?"

    yamato "You’re... saying it backwards–"

    MC evil2  "Yamato-kun..."

    MC evil2 "Who do you think the master of the earth is?"

    show yam glitched:
        zoom 0.25
        xalign 0.5
        yalign 0.2
        yoffset 90
        xoffset 25
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.07 xoffset -60 yoffset 66
        linear 0.06 xoffset 55 yoffset 105
        linear 0.05 xoffset -35 yoffset 81
        linear 0.06 xoffset 30 yoffset 97
        linear 0.05 xoffset 25 yoffset 90

        pause 0.08

    yamato "{sc=8}No–!{/sc}"

    show yam glitched:
        zoom 0.25
        xalign 0.5
        yalign 0.2
        yoffset 90
        xoffset 25
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.07 xoffset -60 yoffset 66
        linear 0.06 xoffset 55 yoffset 105
        linear 0.05 xoffset -35 yoffset 81
        linear 0.06 xoffset 30 yoffset 97
        linear 0.05 xoffset 25 yoffset 90

        pause 0.08

    yamato "{sc=7}No–!{/sc}"

    show yam glitched:
        zoom 0.25
        xalign 0.5
        yalign 0.2
        yoffset 90
        xoffset 25
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Extreme violent jerk: very abrupt, wide, unsettling
        linear 0.05 xoffset -170 yoffset 50
        linear 0.04 xoffset 200 yoffset 130
        linear 0.04 xoffset -120 yoffset 35
        linear 0.04 xoffset 105 yoffset 150
        linear 0.04 xoffset -80 yoffset 110
        linear 0.03 xoffset 40 yoffset 95
        linear 0.04 xoffset 25 yoffset 90   # Back to neutral

        pause 0.10

    yamato "{glitch=8}NOOOOOOOO–!{/glitch}"

    yamato "{sc=8}YOU’RE–{/sc}"

    MC evil2 "{size=+4}{color=#aa0000}Mountains. Earth. Same thing.{/color}{/size}"

    MC evil2 "The mountains belong to me, Yamato."

    n "Yamato scrambles back immediately as realization slaps him in the face."

    show yam glitched:
        zoom 0.25
        xalign 0.5
        yalign 0.2
        yoffset 90
        xoffset 25
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Extreme violent jerk: very abrupt, wide, unsettling
        linear 0.05 xoffset -170 yoffset 50
        linear 0.04 xoffset 200 yoffset 130
        linear 0.04 xoffset -120 yoffset 35
        linear 0.04 xoffset 105 yoffset 150
        linear 0.04 xoffset -80 yoffset 110
        linear 0.03 xoffset 40 yoffset 95
        linear 0.04 xoffset 25 yoffset 90   # Back to neutral

        pause 0.10

    yamato "{sc=8}GHhhAAAGhghh–{/sc}"

    MC evil2 "I gave you teeth, claws, power, eeeeverything you wanted."

    MC evil2 "But it'll never be as strong as mine."

    n "His fingers snap sideways as they claw at his own chest."



    show yam glitched:
        zoom 0.25
        xalign 0.5
        yalign 0.2
        yoffset 90
        xoffset 25
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.07 xoffset -60 yoffset 66
        linear 0.06 xoffset 55 yoffset 105
        linear 0.05 xoffset -35 yoffset 81
        linear 0.06 xoffset 30 yoffset 97
        linear 0.05 xoffset 25 yoffset 90

        pause 0.08

    yamato "{glitch=8}I WASN'T TRYING TO–{/glitch}"

    MC yansm2 "But you prayed to me."

    MC evil2 "ME."

    MC evil2 "{cps=10}Yamakui.{/cps}"


    show moon7 glitched behind yam:
        zoom 1.3
        # Optionally, add center shift if you ever use xalign/yalign/xoffset/yoffset
        linear 0.1 zoom 1.7
    show yam glitched:
        zoom 0.25
        xalign 0.5
        yalign 0.2
        yoffset 90
        xoffset 25
        alpha 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Lunge forward (zoom in, center, reduce offset)
        linear 0.01 zoom 0.65 xoffset 0 yoffset 0
    pause 0.3

    scene black

    with sshake

    stop music

    play sound "sfx/yamato_eaten.wav"

    pause 0.5

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


    n "You step over what used to be Yamato."

    n2 "{i}Charred is better than rotting.{/i}"

    n "Your foot lands beside his cheek."

    n "The one that used to sneer at you, call you dumbass, and taught you how to–"

    n2 "No. He taught YOU."

    n2 "He's nothing to me."

    play sound "sfx/tearflesh.wav"
    with flashred

    n2 "{cps=7}O N L Y   M E A T.{/cps}"


    n "I–"

    play sound "sfx/swallow.mp3"
    with flashred
    n2 "JjJJuIiiiiiICe"


    n "The texture hits first, then the feeling of tendons snapping. It feels chewy in your mouth."

    play sound "sfx/tearflesh.wav"
    with flashred

    n2 "Mmmmgh–hhhnnnHH."

    n "Please stop."

    n "Stop. He's my friend. My friend. My best friend–"

    n2 "A friend? Really?"

    n2 "He was so ready to tear this face apart."

    n "I am going to puke, urk–"

    play sound "sfx/slurrp.mp3"
    $ renpy.pause(0.2)

    n2 "GLLLRHkkk... HHhhhehhehh..."

    n "I can’t–I can’t watch this–"

    n2 "LOOK. LOOK. {w=0.2}SEE."

    n2 "There are no gods to pray to."

    n2 "Your kami-sama have turned their backs on you."

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}YAMATO IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}O N E M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    n2 "HUngRy HunGRy HuNGrY."

    n2 "StARt AgAIn."

    pause 0.5
    $ persistent.yamato_dies = True

    $ persistent.loop2 = True

    $ MainMenu(confirm=False)()

    $ renpy.full_restart()


    return
