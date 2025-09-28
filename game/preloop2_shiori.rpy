############# LOOP 2 WHERE ONE DIED ###########################
label loop2_shiori_mandatory1:

    play music "Shiori.mp3"

    scene village day with in_182:
        zoom 0.5

    show shi happyblush:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
    with dissolve

    shiori "[persistent.player_name]-sama~!"

    n "She’s smiling again."

    shiori "Did you sleep well~?"

    MC smug2 "Yeah, definitely!"

    shiori "That’s good~ That’s very good."

    show shi yansm
    with dissolve

    shiori "I thought you'd dream of killing the Yamakui."

    n2 "Hoo?"

    MC smugcl2 "Why would I dream of that?"

    show shi happy:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80

        linear 0.11 yoffset 40
        linear 0.10 yoffset 95
        linear 0.09 yoffset 60
        linear 0.08 yoffset 80
        pause 0.05

    shiori "Oh, woow~ You just defeated the big scary Oni and you're unfazed?"

    MC smug2 "Guess I'm awesome like that!"

    show shi yansm
    with dissolve

    shiori "Ne, [persistent.player_name]-sama?"

    shiori "Will you tell me how you killed the Yamakui?"

    n  "Why would she ask that?"

    MC yansm2 "Why."

    show shi happy
    with dissolve

    shiori "I just... I want to understand. I want to know how you get to kill the fearsome Oni~"

    shiori "{i}Where did you strike first? What's the color of its blood? Did it go down without a fight?{/i}"

    n "That voice is far too soft for someone asking something that gruesome."

    show shi yan
    with dissolve

    shiori "{k=1}Did you see its eyes when it died?{/k}"

    menu:
        "I stabbed it":
            MC evil2 "{i}I snapped it's spine in half.{/i}"
        "I decapitated it":
            MC evil2 "{i}I snapped it's spine in half.{/i}"

    n "Wait, what? That's not even what you thought of–"

    n2 "{i}I say what I want.{/i}"

    show shi worried
    with dissolve

    shiori "Ara~ That sounds...{w} painful."

    shiori "{sc=2}But are you sure it's really dead?{/sc}"

    MC yansm2 "{i}Definitely.{/i}"

    menu:
        "I burned it":
            MC evil2 "I tore the arms off..."
        "I watched it bleed out":
            MC evil2 "I tore the arms off..."

    MC yan2 "...and bent the legs backwards so it'll be on the wrong angle."

    MC happy2 "It looked like {i}a beautiful flower~{/i}"

    n "What the hell are you saying."

    n2 "{size=+8}Heh. Heh. HeHeHAHAHAHa.{/size}"

    show shi yan
    with dissolve

    shiori "...."

    shiori "And did it... {w=0.1}say anything before it died?"

    menu:
        "It cursed me":
            MC yansm2 "It didn’t say anything, Shiori. Just gurgling noises. Probably because I {glitch}stabbed it in the neck to kill it.{/glitch}"
        "It cried":
            MC yansm2 "It didn’t say anything, Shiori. Just gurgling noises. Probably because I stabbed it in the neck to kill it."

    show shi happy
    with dissolve

    shiori "{i}...I thought so.{/i}"

    n "She looks relieved now, pleased even."

    pause 0.5

    stop music
    play sound "sfx/suzu.mp3"
    show darken
    with dissolve

    show shi yansm
    with dissolve

    shiori "{sc=2}[persistent.player_name]-sama, you forgot your own story~{/sc}"

    MC surprised2 "Eh?"

    shiori "{k=1}You said you snapped its spine. Now it’s a stab in the neck?{/k}"

    show shi yansm:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80

        # LAUGH/CHUCKLE MOTION
        linear 0.10 yoffset 70
        linear 0.08 yoffset 90
        linear 0.08 yoffset 68
        linear 0.07 yoffset 85
        linear 0.07 yoffset 80
        pause 0.05

    play music "spooky.mp3"

    shiori "{i}Ehehe~ You really should keep your lies straight.{/i}"

    n2 "Slipped up.{w} But not really."

    n "What–"

    n2 "This mouth. {w}{i}So much fun.{/i}"

    show shi yansmbl:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80

        linear 0.25 zoom 0.52 xalign 0.315 yoffset 85
        pause 0.05
        linear 0.16 zoom 0.54 xalign 0.38 yoffset 78
        pause 0.03
        linear 0.20 zoom 0.56 xalign 0.35 yoffset 92
        pause 0.07
        linear 0.19 zoom 0.58 xalign 0.32 yoffset 75
        pause 0.05
        linear 0.24 zoom 0.6 xalign 0.3 yoffset 80
        pause 0.08

    shiori "{sc=2}You didn’t kill the Yamakui, didn't you~{/sc}"

    shiori "It’s still alive, {w=0.2}isn’t it?"

    n "Oh no–"

    show shi yansm:
        zoom 0.6
        xalign 0.3
        yoffset 80

        linear 0.14 zoom 0.62 xalign 0.33 yoffset 50
        pause 0.04
        linear 0.10 zoom 0.65 xalign 0.3 yoffset 35
        pause 0.03
        linear 0.12 zoom 0.67 xalign 0.25 yoffset 20
        pause 0.05
        linear 0.14 zoom 0.7 xalign 0.1 yoffset 0
    pause 0.07


    shiori "But that's okay, Shiori will keep your secrets. I won't tell anyone, {i}promise.{/i}"

    shiori "Because if you’re lying... {w=0.2}it means {sc=1}my precious Yamakui{/sc} is still breathing somewhere~"

    shiori "And if it’s still alive... {w=0.2}maybe it’s listening {i}right now?{/i}"

    n "Don’t say anything. Don’t respond. Please–"

    MC yan2 "..."


    shiori "Ne, [persistent.player_name]-sama..."

    shiori "{k=1}If you see the Yamakui again...{/k}"

    shiori "...will you tell it something for me?"

    MC yan2 "What is it?"

    show shi yansmbl:
        zoom 0.7
        xalign 0.1
        yoffset 0

        linear 0.40 zoom 0.715 yoffset 0 xoffset -25
        pause 0.08
        linear 0.42 zoom 0.73 yoffset -10 xoffset -50
        pause 0.09
        linear 0.45 zoom 0.77 yoffset -15 xoffset -100
        pause 0.07
        linear 0.55 zoom 0.8 yoffset -20 xoffset -150
        pause 0.12

    shiori "Tell it... {w}it was never a monster to me."

    n "She leans closer that you feel her {sc=2}breath{/sc} on your face."

    shiori "{w=0.2}Tell it that if it feels hungry, [persistent.player_name]-sama..."

    pause 0.2

    shiori "{sc=2}...come find me first.{/sc}"

    show shi yansmbl:
        zoom 0.8
        xalign 0.5
        yoffset -20
        xoffset -150
        xzoom 1.0
        matrixcolor None

        # CRAWL BACKWARDS SLOWLY
        linear 0.36 zoom 0.72 yoffset -13
        linear 0.36 zoom 0.6 yoffset -100
    pause 0.5
    hide shi
    with dissolve
    pause 0.5





    n "She turns around and leaves, mumbling a song you haven't heard before."

    n "Shiori...?"

    n "Has she always been like this?"

    n "Or am I the one losing grip on reality?"

    $ loop2_shiori_mandatory1 = True

    return

label loop2_shiori_mandatory2:

    play music "Shiori.mp3"

## during this scene Shiori 's sprite leans closer very slowly almost unnoticeable and her eyes follow your mouse tracking

    scene shrine day with in_182:
        zoom 0.5

    show shi normal:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
    with dissolve

    n "You see her again, waiting at the same spot, wearing the same smile."

    n "She's being normal... {w}Yesterday doesn't mean anything. {w}She was just being curious, is all...."

    shiori "[persistent.player_name]-sama~ Did you sleep well again?"

    MC normal2 "...Yeah."

    show shi happyblush
    with dissolve

    shiori "I am so happy you get enough sleep!"

    show shi happyblush:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
        yzoom 1.0

        linear 0.19 zoom 0.54 yoffset 70   # Inching forward, slightly stretching
        pause 0.06
        linear 0.16 zoom 0.57 yoffset 74 xoffset -50 # Even closer, a bit more y-stretch
        pause 0.04
        linear 0.13 zoom 0.6 yoffset 80 xoffset -100   # Final uneasy "lean", back to yoffset start


    n "She’s inching closer again."

    shiori "Ne...{w=01} Can I ask more today?"

    MC annoyed2 "...What now?"

    shiori "About the mountain. I mean, no one went there and returned alive like you did."

    shiori "What did its lair look like?"

    shiori "I always imagined something awful. Or beautiful. Maybe a bit of both~"

    MC annoyed2 "It’s just a cave filled with rotten meat and bones."

    show shi worried
    with dissolve

    shiori "Oh~? {w=0.1}That sounds horrifying. Must be {i}lonely.{/i}"

    n2 "Meat's always in storage."

    n "Shut up."

    shiori "Was it surrounded by mist?"

    shiori "Everyone says that leaving the village is impossible because there's a mist that swallows people."

    shiori "I wonder if the mist is Yamakui itself~"

    MC normal2 "No, but it hides the cliffside... And there are bodies inside it, probably those who fell."

    MC normal2 "They aren't intact, some are half-eaten."

    show shi yan
    with dissolve

    shiori "{sc=1}Ara~{/sc}"

    n2 "We don't waste."

    n "Stop."

    shiori "{i}But it doesn’t eat too often, right?{/i}"

    shiori "Otherwise it will... {w}run out of food."

    MC normal2 "Exactly."

    MC evil2 "{i}The Yamakui is a patient hunter.{/i}"

    n2 "{i}Patient enough to talk like this with prey.{/i}"

    show darken2
    with dissolve

    $ _prev_music_volume = _preferences.volumes["music"]

    $ decrease_music_volume(0.5)
    $ renpy.block_rollback()

    show shi yansm
    with dissolve

    shiori "Then, does that mean Red Moon is a {b}feast?{/b}"

    MC sadcl2 "..."

    shiori "{sc=2}Like... when it actually eats normally and not just snacking?{/sc}"

    MC yan2 "{k=1}Yes! That is when it feeds off something fresh and not rotten.{/k}"

    MC yan2 "{w}Food that has its own soul and memories."

    MC evil2 "Basically, yes, a feast."

    n "{i}What are you saying? How do you know this–{/i}"

    MC panic2 "I–I mean, that’s what I heard."

    MC panic2 "{k=2}That’s what it did. {w}Not me. {w}I mean–{/k}"

    n "{w}Why is your mouth running off by itself? Get a grip already!"



    show shi yansmbl:
        zoom 0.6
        xalign 0.3
        yalign 0
        yoffset 80
        xoffset -100
        yzoom 1.07

        # Unsettling, sharp laugh-bounce
        linear 0.10 yoffset 65 yzoom 1.11      # Quick, stiff bounce up and stretch
        pause 0.07
        linear 0.09 yoffset 95 yzoom 1.06      # Drop sharply, almost like a puppet
        pause 0.05
        linear 0.11 yoffset 73 yzoom 1.09      # Up again, not as far
        pause 0.06
        linear 0.12 yoffset 80 yzoom 1.07      # Back to start, but a little lag on yzoom
        pause 0.09



    shiori "Ehehe~"

    shiori "{i}You talk as if you’ve known it for years.{/i}"

    MC evil2 "{w}I was there, remember? I {sc=1}KILLED{/sc} it."

    MC smug2 "That's why I{i} know.{/i}"

    shiori "Mm... {w=0.2}but you talk like it’s still alive."

    MC sadcl2 "..."

    show shi normal
    with dissolve

    shiori "{i}So, the Yamakui is hungry, right?{/i}"

    show shi sad
    with dissolve

    shiori "But maybe... {w=0.2}it was lonely too?"

    n "{k=2}Don’t answer that.{/k}"

    MC annoyed2 "...I don’t think it works like that for Onis. Do they even have feelings?"

    n2 "{size=+8}Hungry, {w=0.2}hungry, {w=0.2}hungry.{/size}"

    shiori "{w}Are you sure?"

    MC normal2 "Yeah."

    show shi normal
    with dissolve

    shiori "Well~"

    shiori "Thanks for the story again today, [persistent.player_name]-sama."




    show shi normal:
        zoom 0.6
        xalign 0.3
        yalign 0
        yoffset 80
        xoffset -100
        yzoom 1.07
        xzoom 1.0


        # Backwards skip (up and away, shrinking, optional flip)
        linear 0.11 zoom 0.55 yoffset 0  # First jump away (up + shrink)
        pause 0.1
        linear 0.09 zoom 0.52 yoffset -2   # Second, further back
        pause 0.1
        linear 0.11 zoom 0.5 yoffset -3  # Final, farthest, very small

        # Flip as she turns away, then fade out
        linear 0.18 alpha 0.0



    $ restore_music_volume()
    pause 0.05
    hide darken2
    with dissolve

    n "{i}She bows then literally skips away cheerfully.{/i}"

    stop music

    scene black
    with dissolve

    n "Your throat feels dry. You are {cps=10}parched.{/cps}"

    n "{sc=2}You haven't eaten or drunk anything since–{/sc}{nw}"

    n2 "Say {b}one more{/b} word."

    n2 "And I’ll use the {i}tongue{/i} for something else."


    n "..."

    $ loop2_shiori_mandatory2 = True
    return

label loop2_shiori_mandatory3:

    scene shrine night:
        zoom 0.5
    show shi worried:
        zoom 0.5
        xalign 0.3
        yalign 0
        yoffset 80
    with hpunch

    play music "Idle.mp3"

    n "Shiori’s here again, kneeling. You don't know for how long."

    n "There's a new offering box in front of the unnamed graves."

    shiori "{i}...Kami-sama...{/i}"

    shiori "...Protect [persistent.player_name]-sama, okay? And um... everyone else.{w=0.2} {i}Please.{/i}"

    shiori "And–{w=0.2}and someone else. I think."

    shiori "There was a friend of mine who died..."

    shiori "{i}But I can't remember who...{/i}"

    $ persistent.hikaru_dead = True

    shiori "{i}There were four of us, I swear!{/i}"

    play sound "sfx/sniffle.mp3"

    if persistent.hikaru_dead:
        shiori "Me, [persistent.player_name]-sama, and Yamato-kun, and–{w=0.2}and..."
        shiori "{k=1}Who else?{/k}"
        shiori "It’s right there.{w=0.2} Like, on the tip of my tongue, you know?"
        shiori "They... they used to walk with us. {i}I think.{/i}"
        shiori "They always glared when I teased Yamato too hard.{w=0.2} Or maybe they just never smiled much?"
    if persistent.yamato_dead:
        shiori "Me, [persistent.player_name]-sama, and Hikaru-san and–{w=0.2}and..."
        shiori "{k=1}Who else?{/k}"
        shiori "It’s right there.{w=0.2} Like, on the tip of my tongue, you know?"
        shiori "They... {w=0.2}they used to teach us how to use a sword. {i}I think.{/i}"
        shiori "They were louder than me,{w=0.2} and I thought of them like an older sibling..."
    shiori "They sat under the cherry blossom tree with us!{w=0.2} Right?"

    n "Your chest aches."

    n2 "..."

    show shi sad behind darken
    with dissolve


    shiori "I keep seeing a shadow next to me when I walk,{w=0.2} and then I turn and there’s no one."

    shiori "{w=0.2}...I miss someone I don’t even know."

    shiori "Isn’t that the dumbest thing ever?"

    show screen black_flicker
    show darken
    with Pause(0.45)

    if persistent.hikaru_dead:
        show ghost_hikaru normal at c_show_28 behind shi:
            xoffset +300
        with dissolve
    if persistent.yamato_dead:
        show ghost_yamato normal at c_show_28 behind shi:
            xoffset +300
        with dissolve
    hide screen black_flicker
    hide darken
    with fade


    n "Wait, was that–"

    pause 0.5

    hide ghost_yamato
    hide ghost_hikaru
    with fade

    n "Ah, it's gone."

    shiori "{w=0.2} ...I just..."

    shiori "If you’re out there, and I forgot {i}you...{/i}"

    shiori "I’m really sorry."

    shiori "You were probably annoying sometimes,{w=0.2} and I probably yelled at you a lot, but..."

    shiori "{i}I think I loved you too.{/i}"

    shiori "So...{w=0.2} wherever you are,{w=0.2} I hope you’re in peace now."

    scene black
    with out_212

    n "If she remembered who they were–{nw}"

    n2 "{cps=20}No one cares enough to remember.{/cps}"

    $ loop2_shiori_mandatory3 = True

    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    return

label loop2_shiori_mandatory4:

    scene shrine night:
        zoom 0.5
    with fade

    show shi happy:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0
    with dissolve

    shiori "Good night, [persistent.player_name]-sama~!"

    shiori "Can't sleep?"

    n2 "I don't sleep."

    MC nervous2 "Yeah. The red moon is coming, so I–"

    show shi happy:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0

        easein 0.13 yoffset -32 yzoom 1.04 xzoom 0.96
        easeout 0.13 yoffset 0 yzoom 1.0 xzoom 1.0
        pause 0.07
        easein 0.11 yoffset -22 yzoom 1.02 xzoom 0.98
        easeout 0.11 yoffset 0 yzoom 1.0 xzoom 1.0
        pause 0.07
        easein 0.09 yoffset -12 yzoom 1.01 xzoom 0.99
        easeout 0.09 yoffset 0 yzoom 1.0 xzoom 1.0
        pause 0.08

    shiori "Nee, nee, would you want to talk with me?{w=0.2} Maybe you'd get sleepy."

    shiori "Umm... I was wondering..."

    shiori "I have more questions.{w=0.2} Don't laugh, okay?"

    MC normal2 "Yeah?"

    show shi sad
    with dissolve

    shiori "When the Yamakui wasn’t eating...{w=0.2} what did it do?"

    shiori "Did it nap in a corner{w=0.2} or {i}crawl{/i} somewhere quiet?"

    shiori "Do you think it ever looked up at the sky{w=0.2} and {cps=17}watch the stars?{/cps}"

    shiori "Did it ever just...{w=0.2} wonder what it's like {glitch=12}outside{/glitch} the mountain?"

    n "The yamakui is not a {sc=1}dog.{/sc}"

    MC annoyed2 "What the hell, Shiori?"

    show shi shocked:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0

        linear 0.04 xoffset -14
        linear 0.04 xoffset 16
        linear 0.04 xoffset -13
        linear 0.04 xoffset 12
        linear 0.03 xoffset -10
        linear 0.03 xoffset 8
        linear 0.03 xoffset 0
        pause 0.05

    shiori "I-I mean!{w=0.2} It's been alone all this time, right?"

    show shi sad
    with dissolve

    shiori "{cps=15}That must’ve been scary.{/cps}"

    shiori "But also kind of...{w=0.3} I dunno.{w=0.3} {i}Sad?{/i}"

    MC surprised2 "Sad?"

    shiori "Yeah...{w=0.3} Even if it’s a scary Oni,{w=0.3} it must’ve been lonely, right?"

    MC sadcl2 "..."

    shiori "Didn’t it ever want someone to talk to?{w=0.2}"

    stop music fadeout 1.0

    MC annoyed2 "You're {glitch=7}weird,{/glitch} Shiori."

    show shi surprised
    with dissolve

    shiori "...Eh?"

    play music "Tense.ogg"
    show darken
    with dissolve

    MC mad2 "Every time we talk,{w=0.2} it’s about the Oni."

    MC hurt2 "You never asked if I was okay,{w=0.2} if I was scared,{w=0.2} or if I was injured..."

    MC mad2 "And I think you're hoping that it managed to survive somehow."

    show shi fear
    with dissolve

    shiori "{sc=5}No!{/sc} That’s not–{w=0.2}I mean–"

    show shi fear:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0

        linear 0.04 xoffset -14
        linear 0.04 xoffset 16
        linear 0.04 xoffset -13
        linear 0.04 xoffset 12
        linear 0.03 xoffset -10
        linear 0.03 xoffset 8
        linear 0.03 xoffset 0
        pause 0.05

    shiori "I care if you’re okay!"

    show shi sad
    with dissolve

    shiori "{w=0.2}...But I-um,{w=0.2} also just..."

    shiori "{w=0.2}...I keep thinking about it.{w=0.3} The Yamakui."

    shiori "It was probably awful and scary and hurt people,{w=0.3} {i}but...{/i}"

    shiori "I don’t think that means it didn’t {i}feel{/i} things."

    MC yan2 "You think it had feelings?"

    show shi surprised:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0

        linear 0.04 xoffset -14
        linear 0.04 xoffset 16
        linear 0.04 xoffset -13
        linear 0.04 xoffset 12
        linear 0.03 xoffset -10
        linear 0.03 xoffset 8
        linear 0.03 xoffset 0
        pause 0.05

    shiori "M-Maybe!"

    shiori "Don’t you?"

    MC sadcl2 "..."

    show shi sad
    with dissolve

    shiori "{color=#ff002e}At least it was hurt when you killed it, right?{/color}"

    MC yan2 "..."

    shiori "...I just think..."

    shiori "...Everyone should be loved.{w=0.2} Even {sc=1}monsters.{/sc}"

    shiori "{w=0.3}I hope someone hugs it before it dies, just once..."

    pause 0.4

    n2 "{b}LOVE?{/b}"

    n2 "{b}{i}HHHHRRAKkkKhh–HHHHK!{w=0.2} HhA!–KKAHhHAAHH!{/i}{/b}"

    play sound "sfx/jumpscare.mp3"

    with flashred

    n2 "{b}LOVE?{w=0.2} You wanna love the BEAST!?{/b}"

    n2 "{b}Stroke the BLEEDING claws,{w=0.2} kiss the CHEWING teeth?!{/b}"

    n2 "{b}Hold the GULLET while it feeds?!{/b}"

    n2 "{b}BAHAHA–{/b}"

    play sound "sfx/jumpscare.mp3"

    with flashred

    MC happy "Mmmph!"

    with vpunch

    n "The laugh {sc=5}explodes{/sc} out of your chest."

    n "Your hands {i}twitch{/i}.{w=0.2} Your spine {glitch=8}locks.{/glitch}"

    MC happy "That’s...{w=0.2} ngh–"

    show shi worried
    with dissolve

    shiori "...[persistent.player_name]-sama?"

    MC nervous2 "I’m fine."

    MC nervous2 "Kh.{w=0.2} I’m–fine."

    n2 "This girl.{w=0.2} So {b}warm{/b} when she talks."

    n2 "{i}Makes me wanna {b}peel{/b} the skin and see where the softness comes from~{/i}{nw}"

    show shi annoyed
    with dissolve

    shiori "A-Are you laughing!?"

    show shi angry:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0

        linear 0.10 yoffset 42 yzoom 0.95
        linear 0.08 yoffset -18 yzoom 1.08
        linear 0.07 yoffset 10 yzoom 0.98
        linear 0.08 yoffset 0 yzoom 1.0
        pause 0.07
    with vpunch

    shiori "You're so cruel!"

    MC hurt2 "No,{w=0.2} sorry,{w=0.2} I just–!"

    shiori "{sc=2}Hmph!{/sc}{w=0.2} I can't believe you laughed when I was trying to be nice!"

    shiori "YOU {sc=2}MEANIE!{/sc}"

    show shi angry:
        zoom 0.35
        xanchor 0.5
        xalign 0.4
        yalign -0.1
        yoffset 0
        yzoom 1.0
        xzoom 1.0




        linear 0.12 yoffset -22 xoffset 38
        linear 0.09 yoffset 46 xoffset 88
        linear 0.11 yoffset -16 xoffset 140
        linear 0.08 yoffset 62 xoffset 200
        linear 0.12 yoffset 0 xoffset 300

        linear 0.09 xzoom -1.0 matrixcolor BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A")  # in shadowwww
        linear 0.18 alpha 0.0

    pause 0.5
    hide shi

    n "{cps=14}She’s gone.{/cps}"

    n2 "See if she still says that when the hugging arms are {b}missing.{/b}"

    n "{sc=1}Shut up.{/sc}"

    n "{sc=1}Shut up shut up shut up–{/sc}"

    $ loop2_shiori_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear

    stop music
    scene black
    with fade
    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    return
