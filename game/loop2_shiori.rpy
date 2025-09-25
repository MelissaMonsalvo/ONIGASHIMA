label loop2_shiori:

    ## SHIORI'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS OR DEFAULT ROUTE IF YOU DIDN'T UNLOCK YAMATO AND HIKARU

    scene shrine night with in_182:
        zoom 0.5

    show shi blush:
        zoom 0.8
        xalign 0.1
        yoffset -20
        xoffset -150
    with dissolve

    play music "Dark.mp3"

    n "Night falls."

    n "Shiori's head leans against your shoulder like it’s always belonged there."

    shiori "...I used to do this, you know?"

    shiori "When we were kids."

    shiori "When I got scared. You’d let me lean on you, even if you complained that I made your shoulder stiff."

    shiori "But you always felt warm, [persistent.player_name]."

    MC nervous2 "Yeah...?"

    shiori "Mmhm."


    scene black
    with out_eye

    n "You close your eyes and the world stops spinning."

    shiori "...It’s strange though."

    stop music

    shiori "I can’t...{w=0.1} hear your heartbeat."

    MC panic2 "...!"

    scene shrine night with in_eye:
        zoom 0.5

    show shi yan:
        zoom 0.8
        xalign 0.1
        yoffset -20
        xoffset -150
    show darken
    with vpunch

    play music "spooky.mp3"

    n "She lifts her head just a little and stares at you with a knowing smile."

    n2 "Hee--{w=0.3}heeH--{w=0.3}hhhh--{w=0.3}KCH--KKHahHhahhh--"

    n "Your hand clenches,{w=0.2} you want to move, to push Shiori away,{w=0.3} but you can't."

    n "If you do,{w=0.2} then--"

    n2 "{b}{cps=2}CaaaAAANNN’T.{/cps}{/b}"

    n2 "Tear.{w=0.2} Yet."

    show shi yansm
    with dissolve

    shiori "...You’re really quiet tonight, [persistent.player_name]-sama."

    shiori "That’s okay.{w=0.2} I don’t mind."

    shiori "We can stay this way until you don't feel lonely anymore~"

    show shi yansm:
        zoom 0.8
        xalign 0.1
        yoffset -20
        xoffset -150

        linear 0.5 zoom 0.85 xoffset -200 yoffset -40

    n "She’s curling in closer{w=0.2} and presses her head even more to your shoulder."

    shiori "You're cold now, you know?{w=0.2} Like, {i}literally.{/i}"

    shiori "{sc=1}As cold as a corpse.{/sc}"

    MC nervous2 "Shiori-chan... {w=0.2}You're... {w=0.2}freaking me out, heh..."

    show shi yan
    with dissolve

    shiori "{glitch=5}Really?{/glitch} I think I'm the one who feels afraid."

    show shi yansm

    with dissolve

    shiori "But I'll try not to, so you'd feel better."

    stop music

    scene black
    with fade

    shiori "...{w=0.5}Yamakui-sama."

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

    scene black
    with fade

    play muzak "sfx/rain.mp3"

    n "It's raining today, you're drenched in mud and dirt, and--"

    n "--is that blood? Whose blood?"

    scene shrine night with in_182:
        zoom 0.5

    n "Shiori’s already waiting."

    show shi yansmbl:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0
    with dissolve

    shiori "You're such a mess again, [persistent.player_name]-sama~"

    shiori "Come here. I’ll clean you up."

    MC annoyed2 "I’m fine."

    shiori "Aww, just let Shiori take care of you. {w}Please?"

    scene shrine night:
        zoom 0.5
        xalign 0.5
        linear 0.55 zoom 0.66

    show shi yansm:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0
        linear 0.4 zoom 0.45

    n "She prepares warm water and lifts the cloth with both hands, with a smile."

    n "The cloth touches your cheek..."

    play sound "sfx/stretch.mp3"
    show darken2
    with flashred

    n "...and peels the skin away."

    show shi yan
    with dissolve

    shiori "Oops~"

    shiori "That wasn’t dirt, huh?"

    play sound "sfx/stretch.mp3"
    with flashred
    show darken2

    n "She wipes again...{w=0.2} and a piece of muscle {sc=5}sloughs{/sc} off."

    $ _prev_music_volume = _preferences.volumes["music"]

    $ decrease_music_volume(0.5)
    $ renpy.block_rollback()

    n "..."

    n "..."

    n "{cps=13}Wait.{/cps}"

    n "{i}...That’s... that’s not...{/i}"

    $ decrease_music_volume(0.5)
    $ renpy.block_rollback()

    n "That was {sc=2}mine.{/sc}"

    n "My muscle, my skin, my--"

    n "{glitch=10}...You're wearing my face...{/glitch}"

    n2 "{cps=20}YOU'RE GETTING IT NOW, LITTLE GHOST~{/cps}"

    n2 "{cps=20}TOOK YOU LONG ENOUGH--{w=0.1}KkkkhHrrA--{w=01}Hahha--{/cps}"

    n2 "{cps=20}Your face fit SO WELL.{/cps}"

    n "N-No, that can't be...!"

    n "That was...{w=0.2} the fight...{w=0.3} The final battle...?"

    stop muzak
    $ restore_music_volume()
    $ restore_music_volume()

    n "I killed you. I remember killing you! I stabbed you...!"

    pause 0.5

    play music "noinomai.mp3"

    n2 "YOU. {w}DIED."

    n2 "I needed your skin."

    n2 "You’re still here because I didn’t finish {cps=10}aaalllll{/cps} of you."

    n "...."

    n "{sc=7}NO--{/sc}{nw}"

    show shiyansm behind darken2
    with dissolve

    shiori "{i}Hmm~{/i}"

    shiori "Let’s take this part too."

    n "Shiori,{w=0.2} stop,{w=0.2} run.{w=0.2} Get away from me--!"

    play sound "sfx/stretch.mp3"
    with flashred
    show darken2

    shiori "There, better."

    shiori "You always try to hide, [persistent.player_name]-sama...{w=0.3} but I think you’re more beautiful like this."

    n "{glitch=9}Shiori-chan, what are you saying!?{/glitch}"

    MC normal3 "Mm."

    n "I can't move,{w=0.2} my mouth won't say anything, but it's smiling--"

    n "{cps=14}Why are you smiling!?{/cps}"

    n2 "...Because the Red Moon’s coming."

    n2 "{cps=10}Better make more room inside.{/cps}"

    n "{sc=3}No, I refuse to be controlled like this!!!{/sc}"

    n "{sc=3}I’m still ME!{/sc}"

    n "{sc=3}I can still fight--! These are my muscles, so I can--{/sc}"

    call screen multi_click_button(total_clicks=7, next_label="after_many_clicks")
    return

label after_many_clicks:

    n "I--"

    n "I almost--"

    n "{cps=13}I’m taking it back. This body--of mine--{/cps}"

    pause 1.0

    n "..."

    n2 "{cps=20}...Heh. HahahaHahRHRAHhahaahH!{/cps}"

    n2 "{cps=20}You thought...{/cps}"

    n2 "{cps=20}You thought you still have {i}control?{/i}{/cps}"

    n2 "{cps=20}T O O L A T E{/cps}"

    n "No--"

    show shi happyblush
    with dissolve

    shiori "Aaaand done! Good as new."

    shiori "Oops, but you're not actually [persistent.player_name], are you?"

    MC yan3 "..."

    shiori "Don't worry, Yamakui-sama. Even if you can't go out like this..."

    shiori "You can stay with Shiori-chan until the red moon comes!"

    show shi happyblush:
        zoom 0.45
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0

        linear 10 zoom 0.8 yoffset -400
    pause 0.4
    scene black
    with out_eye


    n "She spreads her arm and hugged you--{w}me--{w}what--"

    n "What is happening?"

    n2 "Hush."

    n2 "Go to sleep, {w=0.1}ghost."
    n "..."
    n "..."

    n "...!!!"

    n "Where are we...!?"

    scene shrine day:
        zoom 0.5
    with in_eye

    play sound "sfx/suzu.wav"

    show shi yansmbl:
        zoom 0.27
        xanchor 0.5
        xalign 0.32
        yalign -0.1
        yoffset 26
        yzoom 1.0
        xzoom 1.0

        easein 0.19 zoom 0.31 xalign 0.36 yoffset -18
        easeout 0.15 zoom 0.29 xalign 0.355 yoffset 30

        easein 0.14 zoom 0.33 xalign 0.39 yoffset 10
        easeout 0.13 zoom 0.3 xalign 0.38 yoffset 20

        linear 0.18 zoom 0.35 xalign 0.4 yoffset 0



    shiori "Oh~ Good morning, [persistent.player_name]-sama..."

    n "Why is she limping?"

    MC normal2 "What's up with you?"

    show shi blush
    with dissolve

    shiori "I stubbed my toe real bad. Clumsy ol' me~"

    n2 "HUNGRY."

    n2 "Hungryhungryhungry--"

    n2 "I want it. {w=0.1}I want {i}her.{/i}"

    n2 "GIVE IT TO ME--{nw}"

    n "No, stop, stop putting those thoughts in my head!"

    show shi yansmbl
    with dissolve

    shiori "Hehe..."

    shiori "You're looking at me funny, [persistent.player_name]-sama."

    shiori "Is it because of the blood?"

    n "{sc=1}Run, run away,{/sc} Shiori-chan...!"

    n "Tonight is--"

    stop music
    stop muzak

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THE TIME TO FEED{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    pause 0.5

    scene black

    n "Ah, I passed out again..."

    n "Did Shiori-chan knocked me out, or did you--"
    scene shrine night:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.5
    with in_eye

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

    play music "Blood Ritual.mp3"

    shiori "{sc=5}It's time, Yamakui-sama~{/sc}"

    shiori "I brought tonight’s offering."

    n2 "I smell it."

    n2 "I smell it{w=0.1} I smell it{w=0.1} {sc=7}I SMELL IT--{/sc}"

    n "She kneels in front of the altar and unfolds the cloth she's been carrying."

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show bone:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
        yzoom -1.0
    with dissolve

    n "{cps=13}Three tiny bones rest inside...{w=0.2} those look too small for an anima--{/cps}{nw}"

    n "Oh....{w=0.3} no."

    n "{glitch=8}Those are her--{/glitch}"

    hide frame2
    hide bone
    with dissolve

    show shi yanbl
    with dissolve

    shiori "I thought love should hurt sometimes."

    shiori "{i}If I can’t stay beside you forever...{w=0.2} I’ll just give you parts of me instead.{/i}"

    show shi yansmbl
    with dissolve

    shiori "{cps=15}Bit by bit. Until we’re always together~{/cps}"

    n "No. No, this isn’t--"

    n "This isn't the Shiori-chan I know.{w=0.2} This can’t be--"

    n "She--{w=0.2}she was always scared of blood--"

    show shi yan
    with dissolve

    shiori "You won’t leave me, nee Yamakui-sama?"

    MC yansm3 "{w=0.2}...Never."

    n "She doesn’t know what she’s saying--"

    shiori "Tonight, I want you to eat well."

    show shi yansmbl
    with dissolve

    shiori "{glitch=1}So you stay strong~{/glitch}"

    n "Shiori chan--"

    MC yansm3 "--Thank you."

    n "{i}What... What the hell is happening?{/i}"

    n "This isn’t what I died for."

    n "{sc=2}This isn’t the village I tried to save.{/sc}"

    n "{cps=12}Am I going insane, or is everyone is insane from the start?{/cps}"

    shiori "Yamakui-sama, everyone said that you're evil."

    shiori "But I know that you only eat to survive..."

    shiori "If I love you enough...{w=0.2} you’ll let me stay by your side, right?"

    show shi yan

    with dissolve

    shiori "Shiori's so alone, you know?"

    shiori "I know that [persistent.player_name] and Hikaru has something special going on, but they won't confess to each other."

    shiori "Yamato-kun only cares about being the best."

    show shi yansm
    with dissolve

    shiori "So let me be with you forever, so Shiori won't get lonely~"


    pause 1.0

    n2 "Yes..."

    n2 "F O R E V E R."

    MC "Come closer, then."

    play muzak "sfx/shiori_eaten.mp3"

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

    shiori "{sc=4}Ngh...{/sc}"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    play sound "sfx/swallow.mp3"

    shiori "...I love..."


    play sound "sfx/squelch.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    stop sound


    play sound "sfx/splurt.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve



    stop muzak
    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve
    n2 "slrrrp."

    pause 0.5

    n "...Why...."

    play sound "sfx/slurrp.mp3"
    pause 0.5
    n2  "glk. glk. glk."
    pause 0.5

    scene black

    stop sound
    stop music
    stop muzak

    n "..."

    n "I should’ve stayed dead."



    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}I LOVE YOU TOO, SHIORI{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}O N E M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound



    $ persistent.shiori_dies = True

    $ persistent.loop2 = True

    ## at the end of the route shiori dies

    return
