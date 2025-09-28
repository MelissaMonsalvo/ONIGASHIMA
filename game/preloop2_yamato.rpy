############# LOOP 2 WHERE ONE DIED ###########################
label loop2_yamato_mandatory1:

    $ ysword = False

    play music "sfx/forest night.wav"

    scene dojo day:
        zoom 0.5

    $ loop2_yamato_mandatory1 = True

    stop sound

    show yam annoyed:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        xzoom -1
        yzoom 1.0


    yamato "{sc=3}Oi.{/sc}"

    yamato "I been lookin' for ya."

    MC normal2 "...Yamato."

    yamato "{i}Tch.{/i} Don't gimme that voice."

    yamato "Ain’t here for pleasantries."

    MC annoyed2 "Okay...?"

    yamato "I got questions."

    MC "About...?"

    show yam angry:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        xzoom -1
        yzoom 1.0

        ease 0.1 zoom 0.45 yoffset 50 xoffset -100
    with vpunch

    yamato "{sc=2}Don't fuckin’ play innocent.{/sc}"

    yamato "You went up that mountain and came back without a single scratch."

    yamato "{w=0.1}There ain't no way that's happenin'."

    MC yan2 "..."

    n2 "{cps=13}Hah.{/cps}"

    yamato "So I’m askin’, {i}what the hell happened up there?{/i}"

    n "Say something. {w}Anything."

    MC yan2 "I got bit."

    show yam surprised
    with dissolve

    yamato "{i}Bit?{/i}"

    MC yan2 "Yeah, the damn Yamakui bit me. That’s why I–"

    show yam annoyed
    with dissolve

    yamato "Bullshit. Where?"

    MC annoyed2 "Here."

    play sound "sfx/rustle.mp3"

    n "You pull your collar down and shows a mark just below the neck."

    n "It looks like a bite, all right."

    n "{glitch=6}But it's starting to rot at the edges...{/glitch}"

    stop music

    play sound "sfx/stretch.mp3"
    show gore:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    with flashred
    show darken2
    with vpunch

    n "{cps=14}Oh wait, it’s actually melting–{/cps}"


    hide gore

    play music "spooky.mp3"



    show yam rage:
        zoom 0.45
        xalign 0.4
        yalign 0
        yoffset 50
        xzoom -1
        yzoom 1.0
        xoffset -100

        easeout 0.20 xalign 0.5 yoffset -120 zoom 0.35
        easein 0.15 yoffset 20 zoom 0.37
        easeout 0.10 zoom 0.2 yoffset 150


    yamato "{sc=5}The FUCK.{/sc}"

    yamato "{w}What the hell is that?!"

    yamato "That ain’t a wound. That’s... That’s–"

    $ ysword = True

    play sound "sfx/shing.wav"


    with hpunch


    yamato "{i}Shit, what ARE you?!{/i}"



    n "Yamato unsheates his blades now."

    show yam shocked
    with dissolve

    yamato "{sc=5}That ain’t–That's a corpse...!{/sc}"

    MC evil2 "I thought you wanted proof?"

    show yam rage
    with dissolve

    yamato "Yeah?! Well, ya gave me a damn horror show!"

    n2 "{i}Let him scream. I wanna see what his ribs sound like.{/i}"

    n "Stop. Please stop. Don’t talk like that. Don’t even ASK.."

    MC yansm2 "{i}It’s only a wound, Yamato.{/i}"

    MC smug2 "I mean it's a Yamakui, it's bound to leave a curse or something."

    show yam ngh
    with dissolve

    yamato "Nah. That ain’t no wound I ever seen."

    yamato "That thing’s... That thing's {glitch=5}crawling under your fuckin’ skin.{/glitch}"

    n2 "{cps=11}It fits goooood.{/cps}"

    n2 "{cps=11}Tight.{/cps}"

    show yam angry
    with dissolve

    yamato "...You’re lyin'."

    show yam rage

    with vpunch

    yamato "{i}If the fuckin' Yamakui's dead then the curse would fuck off!{/i}"

    MC annoyed2 "No–"


    show yam panic:
        zoom 0.2
        xalign 0.5
        yalign 0
        yoffset 150
        xzoom -1
        yzoom 1.0
        xoffset -100.

        easeout 0.12 zoom 0.70 yoffset -120

        linear 0.05 xoffset -430
        linear 0.05 xoffset -435
        linear 0.05 xoffset -420
        linear 0.05 xoffset -480
        linear 0.04 xoffset -400

    play sound "Sfx/whip.mp3"


    yamato "{sc=4}Don’t you lie t’me!{/sc}"

    with sshake

    yamato "{sc=2}I trusted ya!{/sc}"

    n2 "{i}So loud,{w} this mutt.{/i}"

    n2 "Let's shut him up."

    n "DO NOT. Don’t touch him. Don’t even think about it–"


    yamato "Tch..."

    n "His hand is trembling. You have never seen Yamato this horrified before."

    show yam ngh:
        zoom 0.70
        xalign 0.5
        yalign 0
        yoffset -120
        xoffset -400
        xzoom -1
        yzoom 1.0

        easeout 0.14 zoom 0.60 yoffset -40 xoffset -350

        easein 0.14 zoom 0.50 yoffset 40

        easeout 0.16 zoom 0.45 yoffset 50 xoffset -325

        linear 0.10 yoffset 30
        linear 0.10 yoffset 50 xoffset -300

    play sound "Sfx/stumble.mp3"

    pause 1

    stop sound


    yamato "{k=2}Shit. I need t’think.{/k}"

    yamato "{sc=3}Don’t even fuckin’ BREATHE near me right now, you get it!?{/sc}"

    play sound "Sfx/whip.mp3"

    hide yam
    with hpunch

    n "He’s gone."

    n2 "He’ll come back."

    n2 "They always do. {w}Meat doesn’t wander far."

    n "You look down at your shoulder."

    stop music

    play sound "sfx/stretch.mp3"
    show red_flash_slow onlayer screens

    n "The skin wriggles, then closes itself again."

    scene black
    hide red_flash_slow

    MC yansm2 "..."

    return

label loop2_yamato_mandatory2:

    scene dojo day with in_182:
        zoom 0.5

    pause 1.0

    show yam rage:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        xzoom -1
        yzoom 1.0

        pause 0.8

    with hpunch

    play music "Doubt.mp3"


    yamato "{sc=3}Ah hell, what are you doing here!?{/sc}"

    MC annoyed2 "Don't mind me, I just want to spar."

    show yam rage:
        zoom 0.2
        xalign 0.5
        yalign 0
        yoffset 150
        xoffset -100
        xzoom -1
        yzoom 1.0


        linear 0.07 yoffset 120

        linear 0.10 yoffset 200 yzoom 0.92 xzoom -1.06

        linear 0.03 xoffset -120
        linear 0.03 xoffset -80

        easeout 0.12 yoffset 100 yzoom 1.0 xzoom -1.0 xoffset -100

        easein 0.14 yoffset 150


    play sound "sfx/stomp.mp3"
    with vpunch

    yamato "{b}Fuck off!{/b}"

    MC smug2 "What, the great Yamato is afraid of a little curse?"

    show yam ngh
    with dissolve

    yamato "{k=1}Wh–{/k}"

    MC smug2 "Can't believe the guy who used to shout he'd kill the Yamakui now {i}runs away with his tails between his legs.{/i}"

    MC yansm2 "What are you, {sc=1}coward?{/sc}"

    show yam rage:
        zoom 0.2
        xalign 0.5
        yalign 0
        yoffset 150
        xoffset -100
        xzoom -1
        yzoom 1.0

        linear 0.04 xoffset -120 yoffset 145
        linear 0.04 xoffset -80 yoffset 155
        linear 0.04 xoffset -110 yoffset 152
        linear 0.04 xoffset -90 yoffset 148
        linear 0.04 xoffset -100 yoffset 150
        repeat
    yamato "{sc=2}Damn you–{/sc}"

    show yam rage:
        zoom 0.2
        xalign 0.5
        yalign 0
        yoffset 150
        xoffset -100
        xzoom -1
        yzoom 1.0

        linear 0.05 zoom 0.6 yoffset -100
    scene black

    play music "Battora.mp3"



    play sound "swing.wav"
    show slash_giant_arc at center
    $ renpy.pause(0.1, hard=True)
    with vpunch

    n "Yamato grabs his sword then rushes towards you."

    n "He always had that fast and clean form, even sharper than you or Hikaru."

    play sound "swing.wav"
    show slash_x1
    $ renpy.pause(0.1, hard=True)
    with vpunch

    n "You usually couldn't dodge because he's too{nw}"

    n2 "{glitch=6}S l o w.{/glitch}"

    n "You move without thinking."

    play sound "swing.wav"
    show combo_slash_2
    $ renpy.pause(0.1, hard=True)
    stop sound

    n "Parry, then twist."

    n "Your blade dances gracefully and you reappear behind him."

    n "Yamato swings backwards in desperation, instinctually."

    play sound "swing.wav"
    show slash_x1
    $ renpy.pause(0.1, hard=True)
    with vpunch

    n "But you're faster and trip his legs."

    scene dojo day:
        zoom 0.5
    show yam panic:
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

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0
    with sshake

    yamato "{k=2}Wha–!{/k}"

    show darken2
    with flashred

    play sound "sfx/crack.mp3"
    pause 0.1

    hide darken2

    n "You heard his knees popping."

    n2 "{cps=13}Again.{/cps}"

    n2 "{sc=4}Break it.{/sc}"

    n "You slam the sword forward–"

    scene dojo day:
        zoom 1
        xalign 0.5
        yalign 0.5
        linear 0.5 rotate 180 zoom 1.5
    pause 0.3
    scene black

    with vpunch
    stop music
    play sound "sfx/thud.mp3"

    n "He hits the ground. Hard."

    scene dojo day:
        zoom 0.7
        yoffset -100
    show yam angry:
        zoom 0.4
        xalign 0.4
        xoffset 180
        yoffset 150
        xzoom 1
        yzoom 1.0


        linear 0.9 yzoom 0.97 yoffset 158
        linear 1.1 yzoom 1.01 yoffset 144
        repeat
    with hpunch

    yamato "{i}Ghk–! Fuck!{/i}"

    n "He’s kneeling, wheezing and clutching his side."

    yamato "{k=2}Y-you–{/k}"

    yamato "{w}You’re not even breakin’ a sweat. Since when...?"

    yamato "{sc=3}No... What the fuck {b}are{/b} you?{/sc}"


    call screen horror_forced_menu_jitter(items=[
    ("K I L L K I L L K I L L", Jump("ya_kill"), False),
    ("E A T E A T E A T E A T", Jump("ya_ate"), False)
])

label ya_kill:
    n "Are you insane!? Stop!"

    jump yyyesss

label ya_ate:
    n "No! Please, stop!"

    jump yyyesss

label yyyesss:

    n2 "Look at him. Little animal is cornered."

    n "Stop. Stop thinking like that. That’s not–"

    MC yan2 "Yamato–"



    show yam panic
    with sshake

    yamato "{k=2}S-Stay back!{/k}"

    yamato "{sc=4}You ain’t foolin’ anyone anymore!{/sc}"

    yamato "{i}Whatever curse ya brought down that mountain–{/i}"

    yamato "{sc=3}Tch, damn it!{/sc}"

    show yam panic:
        # Start from end of breathing
        zoom 0.4
        xalign 0.4
        xoffset 180
        yoffset 150
        xzoom 1
        yzoom 1.0

        linear 0.18 yoffset 130 xzoom -1

        pause 0.12

        easeout 0.42 xalign -0.2 xoffset -320 zoom 0.32 yoffset 160

        linear 0.16 alpha 0

    play sound "sfx/run.mp3"

    with sshake

    n "Yamato scrambles away frantically, but still heavily wounded."

    n "What are you doing...? He's going to tell the others and–"

    n2 "Let him, let them aaallllll come."

    n2 "I want to see what they taste like... one by one."

    stop sound


    $ loop2_yamato_mandatory2 = True

    return

label loop2_yamato_mandatory3:

    play music "Sfx/forest night.wav"

    scene shrine night with in_212:
        zoom 0.5
    show yam sad:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        yzoom 1.0

    show darken

    n "You see Yamato kneeling before the urns without names."

    n "He lights the incense, then presses both fists together... They're still shaking."

    yamato "{sc=2}Tch...{/sc}"

    yamato "{i}Didn’t think I’d be back here so soon.{/i}"

    yamato "I still dunno what t’say."

    n2 "Hn? Something’s here."

    n2 "I can smell it."


    ### SHIORI GHOST PATH
    if persistent.shiori_dies:

        show screen black_flicker
        with Pause(0.45)  # 0.05*8 + buffer for full duration (optional)
        hide screen black_flicker

        n "You see her before you hear anything."

        n "She’s standing between the urns, her mouth stretches open, then splits slowly."

        n "Who...?"

        play sound "sfx/riip.mp3"

        n "Her face peeling open like a purse made of meat, from lip, to cheek, then her ears..."

        n2 "Ah. The stringy one."

        n "But Yamato can't seem to see her."

        yamato "{w=0.1}Whoever you were, I remembered having ya as a friend..."

        yamato "Sometimes I dreamed of a girly voice in my sleep... {i}Maybe it's ya.{/i}"

        yamato "{sc=3}...I shoulda gone up there with ya.{/sc}"

        yamato "Tch. {w}Dunno if you hear me."

        yamato "{k=2}But this is all I can give.{/k}"

        n "The incense smoke trails toward her, as if she's inhaling it."

        show screen black_flicker
        with Pause(0.45)  # 0.05*8 + buffer for full duration (optional)
        hide screen black_flicker

        n2 "HraHaHHAhHAhahhh"

        n2 "She followed us down the throat."

        n2 "Let her stay there forever."

    ### HIKARU GHOST PATH
    else:
        show screen black_flicker
        with Pause(0.45)  # 0.05*8 + buffer for full duration (optional)
        hide screen black_flicker

        n "There’s something standing by the incense..."

        n "Their mask has melted into the bone. You can see the skull beneath it."

        n "Ah... Who..."

        n "Why do I feel...?"

        n2 "That's your favorite."

        n "The eye sockets are dark. But you know they see you."

        n "You can feel it on your skin."

        yamato "{sc=2}Tch... I can't even remember how ya look like...{/sc}"

        yamato "But I remembered I got another sparring partner other than [persistent.player_name]."

        yamato "{w=0.1}I shoulda said goodbye properly."

        yamato "{i}Now I gotta light this stupid stick and hope it gets to ya somehow.{/i}"

        show screen black_flicker
        with Pause(0.45)  # 0.05*8 + buffer for full duration (optional)
        hide screen black_flicker

        n2 "HUhhUhhhuHUHuHuuhh."

        n2 "You'll join them soon."

    ### COMMON ENDING

    scene black
    with dissolve

    n "Yamato bows one more time before leaving."

    n "Whatever that was... He didn't see it."

    n2 "But we {i}do.{/i}"

    n2 "{cps=10}Because the meat is always with us.{/cps}"

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


    $ loop2_yamato_mandatory3 = True

    return

label loop2_yamato_mandatory4:

    scene black

    $ ysword = False


    n "Why... Why are you in the forest this late?"

    n2 "Sshh... Listen. {w=0.2}Look."

    scene forest night with fade:
        zoom 0.5
        yanchor 1

        pause 0.1
        linear 2 zoom 0.7
    pause 0.5
    show yam eldritch:
        zoom 0.35
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000

        linear 0.05 xoffset 982 yoffset 18 xzoom 1.04 yzoom 0.93
        pause 0.06
        linear 0.03 xoffset 1024 yoffset -19 xzoom 0.93 yzoom 1.07
        pause 0.10
        linear 0.02 xoffset 1012 yoffset 6 xzoom 0.97 yzoom 1.06
        pause 0.13
        linear 0.01 xoffset 1000 yoffset 0 xzoom 1.0 yzoom 1.0
        pause 0.03
        linear 0.04 xoffset 991 yoffset 2 xzoom 1.01 yzoom 0.97
        linear 0.03 xoffset 1005 yoffset 5 xzoom 0.98 yzoom 1.03
        pause 0.07
        pause 0.18
        repeat


    play music "noinomai.mp3"

    n "Yamato is on his knees, with his hands clawed into the dirt."

    yamato "{sc=3}HrghKKKK!{/sc}"

    n "Black water floods from his mouth. It's thick, writhing... alive?"

    yamato "{i}Haaah... Hhhhaaaaahh...{/i}"

    n "His face is contorting... No one should look like {b}THAT.{/b}"

    n "What is happening?!"

    n "You hear a popping, crunching sound. It's as if... as if... something inside him is rearranging."

    n "The black water pools at his knees. It moves without touching him, having a mind of its own"

    yamato "{w}Tch..."

    yamato "{sc=2}Knew you were watchin’...{/sc}"

    MC surprised2 "{k=2}...Yamato?{/k}"

    yamato "{w}Wanna laugh again, huh? Go on. Do it."

    yamato "{k=2}I ain't scared anymore.{/k}"

    yamato "{sc=5}NO NO NO. Not scared not scared not scared.{/sc}"

    yamato "{i}Red moon's comin’... and I’m gonna peel the meat off your damn bones.{/i}"

    show yam eldritch:
        zoom 0.35
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000
    with hpunch
    play sound "sfx/crack.mp3"

    show darken2
    with dissolve

    yamato "When it rises... {w=0.2}you {i}fall{/i}."

    ## menu text will be distorted via UI, not text tag here

    call screen horror_forced_menu_shaking(items=[
    ("T H E {color=#ff0015}R E D M O O N{/color}", Jump("yesyeysysyqsad"), False),
    ("I S C O M I N G", Jump("yesyeysysyqsad"), False)
])

label yesyeysysyqsad:
    n "No, no, no, stop–"
    n2 "AhhhhHHHhh... He SPEAKS now."

    n2 "Little boy thinks he's brave."

    n2 "HRAHaHAHaHaaa... oh, bite back, bite down, BITE OUT HIS TONGUE!"

    yamato "{sc=3}I’m stronger now. {w=0.2}Don’t need skin to hold me back anymore.{/sc}"

    yamato "You come near me, [persistent.player_name], I’ll drag you through yer own blood.."

    MC evil2 "Try. {w=0.1}{w=0.1}TRY. {cps=150}TRY. TRY TRY TRY TRY {w=0.1}TRY–{/cps}{nw}"

    yamato "{sc=3}Tch. WATCH me.{/sc}"

    scene black
    with out_212

    n2 "I am."

    n2 "I A M {w=0.1}W A T C H I N G {w=0.1}Y O U."

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
