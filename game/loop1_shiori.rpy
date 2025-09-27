label loop1_shiori:

    ## SHIORI'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS OR DEFAULT ROUTE IF YOU DIDN'T UNLOCK YAMATO AND HIKARU

    ## TWO DAYS BEFORE THE RED MOON


    scene shrine day:
        zoom 0.5

    n "There was no sleep to be had, so you just wander around aimlessly."

    n "And yet, somehow, your feet still brought you here."

    play music "Dark.mp3"

    play sound "sfx/suzu.mp3"

    show shi happy:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
    with dissolve

    shiori "Good morning, [persistent.player_name]-sama~"

    shiori "I was just about to prepare the shrine for the red moon, and--"

    MC normal "Shiori-chan."

    MC nervous "You still don't believe me, do you?"

    show shi fear:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
        easein 0.15 yoffset 110 xzoom 0.95 yzoom 1.05

        easeout 0.12 yoffset 70 xzoom 1.05 yzoom 0.95

        easein 0.1 yoffset 90 xzoom 0.97 yzoom 1.03
        easeout 0.1 yoffset 80 xzoom 1.0 yzoom 1.0

    shiori "I--"

    show shi yansm
    with dissolve

    shiori "[persistent.player_name]-sama. I believe you, I fully believe that you believe you've killed it, but..."

    shiori "Have you ever seen a cicada still move after its head comes off?"

    MC sad "..."

    shiori "Or a puppet that keeps dancing even when no one’s holding the strings?"

    shiori "We prepare because something always comes, [persistent.player_name]."

    show shi happyblush
    with dissolve

    shiori "That's what Hikaru and Yamato keeps telling me anyway..."



    n "None of you speak again for a while."

    n "..."

    show shi normal
    with dissolve

    shiori "Nee..."

    shiori "Could you bring me the incense box, [persistent.player_name]-sama?"

    MC normal "...Yeah."

    shiori "Thank you~"

    shiori "Now... Salt, incense, water, string~ This should keep the worst away."

    n "You just look at the ground, it feels like it's tilting below you."

    play sound "sfx/swallow.mp3"

    MC nervous "*gulp*"

    play sound "sfx/jumpscare.mp3"

    show shi yansm:

        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
        xzoom 1.0
        yzoom 1.0

        # Sudden zoom-in like a jumpscare
        easein 0.08 zoom 0.8 yoffset -20 xoffset -200

    shiori "Nee, [persistent.player_name]-sama~"

    MC shocked "...!"

    with vpunch

    n "Her breath suddenly brushes your cheek. When did she get so close?"

    MC surprised "Shiori..."

    shiori "{sc=1}You’re trembling~{/sc}"

    shiori "Nee, nee. Are you scared of me?"

    MC normal "No."

    show shi yansmbl:
        zoom 0.8
        xalign 0.3
        yalign 0
        yoffset 40
        xzoom 1.0
        yzoom 1.0



        easein 1.0 zoom 1 yoffset -200 xzoom 1.1 yzoom 1.1 xoffset -400

        pause 0.2


        easeout 0.2 zoom 0.8 yoffset -20 xoffset -200 xzoom 1.0 yzoom 1.0

    shiori "Are you {sc=3}suuuuure~?{/sc}"

    n "Her lips are right beside your ear now, the sound of her breath now echoing inside your skull."

    stop music


    play sound "sfx/bucketdrop.wav"
    show darken2
    with sshake

    n "You didn't realize that your body spasms so hard it knocks down a candle."


    MC shocked "{b}-Ah!{/b}"

    n "The flame licks your wrist. Even though it burned off your sleeves, it feels like it's your flesh that is being torn apart too."

    play sound "sfx/firecrackle.mp3"
    show red_flash_slow onlayer screens

    scene shrine day:
        zoom 0.6
        xalign 0.5
        yalign 1

        linear 0.3 zoom 0.5

    show shi yansm:
        zoom 0.8
        xalign 0.3
        yalign 0
        yoffset 40
        xzoom 1.0
        yzoom 1.0


        easeout 0.15 zoom 0.5 yoffset 80

        # Add stumble shake during the retreat
        parallel:
            linear 0.05 xoffset -20
            linear 0.05 xoffset 20
            linear 0.05 xoffset -10
            linear 0.05 xoffset 10
            linear 0.05 xoffset 0
    show darken2

    n "You pull your hand back, immediately."

    play sound "sfx/firecrackle.mp3"
    show red_flash_slow onlayer screens

    MC mad "Nngh-!"
    with sshake

    n "The wax lands on your skin-Oh."

    play music "spooky.mp3"

    n "...It's... {w}black?"

    MC mad "Why the hell is the wax black?!"

    n "It burned through the cloth, and you smell something foul. Is your flesh burning?"

    MC panic "{sc}Shiori, help--{/sc}"
    with vpunch

    n "She should be helping, or reach for something, anything, but..."

    n "She’s just watching you burn with that wide eyes of hers."

    shiori "{w=0.2}You remember the charm I gave you, right?"

    MC panic "Seriously, is this the right time to talk about this--"

    shiori "The one I hid in your sleeve before you climbed the mountain...."

    shiori "{sc=2}It's protecting you, see?{/sc}"

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show charm2:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
    with dissolve


    n "She points at the black goo melted right before your arm."

    n "Oh, so it's the charm that burned, not you. It's now charred and ash and tattered into pieces."

    shiori "{i}You're fine, see?{/i}"

    hide frame2
    hide charm2
    with dissolve

    $ haze_active = True
    show haze_effect at haze_transform
    with dissolve

    n "You feel lightheaded immediately."

    MC nervous "R-Really?"

    show shi yansmbl
    with dissolve

    shiori "Of course~"

    shiori "{glitch=1.1}You're always, {w=0.1}always within my protection.{/glitch}"

    n "You turn to leave, to clean your arm and get that blasted charm off you..."

    n "...but her hand closes around your wrist before you can move."

    shiori "{w=0.2}Um, wait--!"

    show shi worried
    with dissolve

    shiori "Wait, just one more thing. Since you've burned off the charm..."

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show wine:
        zoom 0.6
        xanchor 0.5
        xalign 0.5
        yalign 0.25
    with dissolve

    shiori "{sc=2}Drink this instead and you'll not be marked when the red moon comes.{/sc}"

    MC surprised "...What is it?"

    show shi yansmbl
    with dissolve

    shiori "{i}It's just wine~{/i}"

    n "Her hand shakes slightly as she hands you a cup, you can see a thick line runing down the outside."

    n "Your fingers feel sticky where it touches."

    n "You lift it to your mouth, something metallic fills your nose... {w=0.2}then the taste swells on your tounge."

    play sound "sfx/gulp.wav"

    n "It sticks to your palate and clots at the back of your throat as you gulp it down."

    MC normal "Hahh~"
    hide frame2
    hide wine
    with dissolve

    $ haze_active = False
    hide haze_effect
    with dissolve

    show shi happy
    with dissolve

    shiori "So? How was it?"

    MC normal "It's... {w}fine. I guess?"

    show shi surprised
    with dissolve

    shiori "That's it? Just {i}'fine'{/i}? Nothing else?"

    MC happycl "I mean... {w}It's wine, right? Wine's always good in my book."

    show shi yan
    with dissolve

    shiori "{w=0.1}...Nevermind."

    shiori "It doesn’t matter."

    MC surprised "...?"

    show shi yansm
    with dissolve


    shiori "{cps=14}{sc=6}Tomorrow is the {color=#ff002e}Red Moon{/color}, [persistent.player_name]-sama.{/sc}{/cps}"



    show shi yansm:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
        xoffset 0
        xzoom 1.0
        yzoom 1.0
        alpha 1.0

        parallel:
            linear 3.0 zoom 0.3 yoffset 100

        parallel:
            ease 0.6 xoffset -25
            ease 0.6 xoffset 25
            ease 0.6 xoffset -15
            ease 0.6 xoffset 15
            repeat 1

        linear 1.0 alpha 0.0

    shiori "{i}I... I can't wait.{/i}"

    pause 0.4

    n "There's a {i}weird glint{/i} in Shiori's eyes and the way she {sc=3}smiles{/sc} when she turns away."

    n "You’re alone now, with the cup in your hand, the {glitch=12}thick residue{/glitch} sliding down your throat..."

    n "... and the taste of {color=#ff002e}{i}iron{/i}{/color} still curling at the back of your mouth."

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


    n "The sky is almost fully {color=#ff002e}{b}red{/b}{/color} today."

    scene black
    with fade

    play music "Dark.mp3"

    n "The {glitch=8}villagers starts whispering{/glitch}, you can hear it everywhere you walk."

    $ decrease_music_volume(0.2)
    $ renpy.block_rollback()
    pause 0.2

    show oldwoman at midleft :
        zoom 0.5
        ypos 0.2
    with dissolve
    show oldman at midright:
        zoom 0.5
        ypos 0.1
    with dissolve
    show darken
    with dissolve

    "Old Woman" "{i}...If [persistent.player_name] really killed it...{/i}"

    "Old Man" "...Then nothing will happen tonight, right?"

    "Old Woman" "{sc=5}...Right?{/sc}"

    $ restore_music_volume()

    hide oldman
    hide oldwoman
    hide darken
    with dissolve

    n "Of course no one dares asking you directly, but you can feel their glances when they think you’re not looking."

    n "Everywhere you go, people walks away, and your friends are nowhere to be found."

    n "No Yamato or Hikaru around, either."

    n "Maybe they’re patrolling. {w}Maybe."

    n "But you know that Shiori will always be waiting at the same spot at the shrine."

    scene shrine day:
        zoom 0.5
    show shi yansm:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
    with in_212

    shiori "{sc=2}[persistent.player_name]-sama~{/sc}"

    shiori "{w=0.2}You came."

    MC yan "..."

    shiori "It’s almost time, you know."

    show shi yansmbl:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80



        parallel:
            linear 3.0 zoom 0.7 yoffset 20 xoffset -200

    shiori "{i}So~{/i}"

    shiori "{w=0.2}Will you stay with Shiori tonight? At the shrine?"

    shiori "It’s scary, you know~ All this talk of the Oni possibly returning..."

    shiori "{glitch=1.1}I need my big, strong Oni slayer to protect me~{/glitch}"

    n "Odd..."

    n "Her hand no longer shakes as she looks at you, as if something had changed overnight."

    shiori "{i}Nee, nee, you wouldn’t leave me alone on a night like this... Right...?{/i}"

    MC yansm "{w=0.15}Of course, Shiori."

    MC yansm "{cps=11}I'll always come for you.{/cps}"

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

    play music "Blood Ritual.mp3"

    n "The red moon comes as always. When it does, everything looks washed in blood."

    n "Everyone's holed in their own house. No one dares make a sound, not even for breathing."

    n "The athmosphere feels wrong."

    scene shrine night:
        zoom 0.5
        xalign 0.5
        yalign 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    show shi yansm:
        zoom 0.34
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 80
        xoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with in_212

    n "Shiori is already standing at the altar, when you return to the shrine as promised."

    shiori "{sc=5}~[persistent.player_name]-sama~{/sc}"

    show shi yansmbl
    with dissolve

    shiori "I'm so {i}happy{/i} you came~"

    n "Her voice turns {i}{bt=h1-s0.5-p1.0}singy-songy{/bt}{/i}, even more unhinged than the last time you saw her."

    n "What on? This {glitch=10}isn't{/glitch} the Shiori you know."

    n "Wait, {i}is she always the Shiori you knew?{/i}"

    shiori "I was wondering when it started, y'know?"

    shiori "When I started looking at you and thinking... {sc=3}you poor thing~{/sc}"

    show shi yan
    with dissolve

    shiori "{i}You risked your life for the village, and this is the thanks you get?{/i}"

    shiori "Hikaru and Yamato won't talk to you, and everyone doubts you really killed the oni..."

    shiori "They keep telling me {color=#ff002e}something is wrong with you...{/color}"

    shiori "And now that I've done everything I can to prove otherwise, I {glitch=8}failed{/glitch}."

    show shi yansmbl:
        # Starting pose
        zoom 0.34
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 80
        xoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        # Forward creep
        parallel:
            linear 2.0 zoom 0.4 yoffset 60

            # Heavy swaying steps while creeping
        parallel:
            ease 1 xoffset -25 yoffset 90
            ease 1 xoffset 25 yoffset 70


    n "She takes one excrucistingly slow step forward."

    shiori "But it’s okay~"

    shiori "{sc=1}You just wanted to be seen.{/sc}"

    shiori "{cps=12}That’s why it followed you.{/cps}"

    n "What is she talking about?"

    shiori "I forgive you, 'cause I love you [persistent.player_name]~"

    shiori "And love is stronger than any curse~"

    show shi yansmbl:
        zoom 0.4
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 70
        xoffset 25
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        parallel:
            linear 1.6 zoom 0.45 yoffset 40

        parallel:
            ease 0.8 xoffset -20 yoffset 70
            ease 0.8 xoffset 20 yoffset 50
            repeat 1

    shiori "Let me help you, [persistent.player_name]-sama."

    shiori "Let me {i}keep{/i} you, mmkay?"

    n "Her eyes shimmer under the Red Moon."

    n "Her hands are outstretched now, welcoming you."

    scene shrine night:
        zoom 0.5
        xalign 0.5
        yalign 1
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        ease 0.4 zoom 0.55

    show shi yanbl:
        zoom 0.45
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 40
        xoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        parallel:
            ease 0.4 zoom 0.5 yoffset 10 xoffset -10

    n "You move closer and place your hand against her cheek."

    shiori "...[persistent.player_name]-sama?"

    n "Wait, what?"

    scene shrine night:
        zoom 0.5
        xalign 0.5
        yalign 1
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        ease 0.4 zoom 0.6

    show shi yanbl:
        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 10
        xoffset -10
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        parallel:
            ease 0.4 zoom 0.79 yoffset -40 xoffset -200



    stop music
    play sound "sfx/hahh.mp3"

    n "You lean in, her lips are warm. Her mouth opens without hesitation."

    n "She kisses you eagerly, as if she’s waited for years for this... or maybe she has. You don't know."

    n "This... feels wrong, somehow. How did--"

    MC "Shut up."

    camera:
        linear 2.0 ypos -0.1
    n "You kiss her back, then your lips moves down, down, down...."

    n "Her breath hitches in her throat, but she doesn’t stop you."

    n "Then, your teeth close around her shoulder."

    shiori "Ah-"

    n "Are you sure this is the right time to do this? The red--"

    MC yan "{sc=7}I said shut up.{/sc}"

    shiori "W-What?"

    MC yansm "{i}Not you.{/i}"

    n "*sigh*"

    show cg_shioriloop1:
        zoom 1

        easeout 0.7 zoom 0.5

    camera:
        linear 0.5 ypos 0.0
    pause 0.2

    play muzak "sfx/shiori_eaten.mp3"

    n "You press your mouth harder. Her skin splits slowly, then her blood fills your mouth."

    shiori "{sc=4}Hh-ah... [persistent.player_name]-sa...{/sc}"

    with fade

    n "She reaches up to your back, trembling, nails raking across your back. But you {i}feel none of it.{/i}."

    MC "You said you love me, right Shiori? So I’m returning the favor."

    MC "Isn’t that what {glitch=12}love{/glitch} is?"

    shiori "...Hah."

    with fade

    n "{cps=12}W-What in the kami-sama is happening?{/cps}"

    play sound "sfx/heartbeat.mp3"

    MC "You said you wanted to save me? So I’ll take all of it."

    MC "...Of you."

    shiori "{i}Hh-If it’s you, then...{/i}"

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

    play music "sfx/monstermunch.mp3"

    n "..."

    $ renpy.pause(1.0)

    shiori "{sc=4}Ahh...{/sc}"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    play sound "sfx/slurrp.mp3"

    shiori "...mmnh..."


    play sound "sfx/squelch.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    stop sound

    n "{color=#ff002e}Y-You’re not stopping.{/color}"

    n "You finally reach the fat layer under the sk-"


    play sound "sfx/splurt.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    shiori "...ahh... [persistent.player_name]-sama..."

    n "{glitch=8}Oh Kami, oh gods, {w=0.1}someone stop this-{nw}{/glitch}"

    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n "You feel her pulse against your tongue."

    n "{sc=1}The blood tastes exactly like the wine she gave you weeks ago.{/sc}"

    n "{sc=1}You like now it as much as you liked it then--{/sc}"

    shiori "{sc=3}I'm... {w=0.5}dizzy...{/sc}"

    n "{sc=7}Stop.{/sc}"

    n "{sc=8}Stop.{/sc}"

    n "{cps=10}Please, {b}stop.{/b}{/cps}"

    n "{sc=4}[persistent.player_name]???{/sc}"

    stop muzak

    n "She’s-"

    n "{glitch=6}She’s still-{/glitch}"

    stop music


    play sound "sfx/slurrp.mp3"

    scene black
    with in_212

    n "Shiori has stopped breathing."

    n "You don't even feel her pulse anymore."

    n "All you can feel now is the blood in your mouth, the slick feelings between your fingers, and the red goo dripping from your lips to now her dangling arms."

    n "..."

    n "Who... {w}are you?"

    n "Who am I?"

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}SHIORI IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}T W O M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound


    $ persistent.shiori_dies = True

    $ persistent.loop1 = True

    $ renpy.full_restart()


    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
