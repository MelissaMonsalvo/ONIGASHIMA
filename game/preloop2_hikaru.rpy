############# LOOP 2 WHERE ONE DIED ###########################



label loop2_hikaru_mandatory1:

    scene village day with in_182:
        zoom 0.5

    pause

    play sound "Sfx/walk grass.mp3"
    show hik normal:
        zoom 0.023
        xanchor 0.05
        xalign 0.63
        yalign 0
        yoffset 450
        xoffset 0
    with dissolve
    pause 0.3


    play music "Hikaru.mp3"

    hikaru "[persistent.player_name]."

    show hik normal:
        zoom 0.1
        xanchor 0.05
        xalign 0.63
        yalign 0
        yoffset 400
        xoffset 0
    with dissolve
    pause 0.3
    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0
    with dissolve
    stop sound

    n "Hikaru calls out to you casually. They usually call you by -san."

    n "But now it sounded... different. Their tone sounds different too."

    MC "Yeah?"

    hikaru "You looked pale this morning. {w}Are you alright?"

    n "Has Hikaru always talked to you like this?"

    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 60
        xoffset 0

        linear 0.4 zoom 0.4 yalign -40

    n "Hikaru's hand moves closer, almost brushing your arm. You feel uncoomfortable immediately."

    hikaru "You haven’t eaten properly in days. {w}Did something happen?"

    hikaru "Hey, if something happened up there... You can tell me."

    n "Their hand is entwined with yours now. You don't know what to make of it."

    n "{sc=1}Did you...?{/sc}"

    n "{sc=1}Did we--?{/sc}"

    n2 "Just go with it."

    MC "Kind of hard to concentrate if the villagers looks at you like you're lying."

    hikaru "Ah."

    hikaru "I... {w=0.1}can relate."

    MC "Yeah, sorry."

    hikaru "Don't be. {w}Hey, what if we go hunting instead?"

    hikaru "You know, like the old times? Your favorite pastime?"

    n "Even Hikaru looks at you with a little glint of disbelief..."

    n2 "Yes..."

    if not persistent.shiori_dies:
        MC "Sounds nice, is Yamato coming with us?"
    else:
        MC "Sounds nice, is Shiori coming too?"

    hikaru "It’ll just be us. No one else has to know."

    n2 "...They’re planning something."

    n "Or maybe it’s just a date."

    n2 "..."

    scene black
    with in_212

    play sound "Sfx/walk grass.mp3"

    n "You follow Hikaru into the woods, heart skipping for all the wrong reasons."

    scene forest night with fade:
        xpos 0
        blur 2
        linear 15 xpos -1920  # Move left by one screen width over 8 seconds (adjust speed)
        repeat
    show hik normal:
        zoom 0.5
        xalign 0.4
        yalign -0.15
        yoffset -400
        xzoom -1
        yzoom 1.0

        yoffset -400
        linear 0.5 yoffset -420
        linear 0.5 yoffset -400
        repeat

    n "You walk behind Hikaru. Their footsteps make almost no sound."

    n2 "Meat ahead."

    hikaru "There’s something ahead."

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show boar:
        xanchor 0.5
        xalign 0.5
        yalign 0.33
    with dissolve

    hikaru "See that boar? The right leg's limping."

    MC "Mmhmm."

    hikaru "On my signal, okay?"

    n2 "Signal? Fool. Just kill it."

    hikaru "{sc=1}Now!{/sc}"

    scene black

    # Optional: Play sound effects in sync
    stop sound
    scene black
    play sound "swing.wav"
    show combo_slash_1
    $ renpy.pause(0.1, hard=True)
    stop sound
    pause 0.1
    play sound "sfx/boar.mp3"

    n "Your blade strikes first and you take down the boar no problem."

    play music "heavy breathing.mp3"

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

    play sound "sfx/squelch.mp3"

    n "Except... {w}Hey..."

    n "Stop, you're drawing too much blood--"

    n2 "{i}Yessss... more...{/i} {w}let's pull it open."

    n2 "{i}Succulent ribs, juicy eyeballs.{/i}"

    n "No--{w}no, stop."

    play sound "sfx/hahh.mp3"

    n2 "{b}The smell...{/b} Hhahhh...."

    n2 "So {i}easy{/i} to chew--"

    n "Please--"

    n2 "{size=+8}DON’T INTERRUPT--{/size}"

    play sound "sfx/stumble.p3"

    hikaru "...[persistent.player_name]?"

    stop music
    stop sound

    scene forest day:
        zoom 0.5
    show hik normal:
        zoom 0.3
        xalign 0.5
        yoffset 150
        xzoom -1.0
        yzoom 1.0
    show darken
    with sshake

    MC "....!"

    play music "sfx/ forest night.wav"

    n "The boar lies beneath your hands, your hands are already digging into it, almost ripping into flesh."

    hikaru "{w=0.1}...Are you alright?"

    MC "I-I'm {w}just a little hungry."

    hikaru "Then let’s bring it back quickly. We’ll cook it together."

    n2 "Cook it?"

    n2 "No. {w=0.2}No fire. Fire kills the taste."

    n2 "{b}SHOULD'VE EATEN IT WHILE IT'S FRESH.{/b}"

    n "You wipe your blade on the grass. Your stomach lurches, but you help Hikaru clean the boar and carry it."

    play sound "Sfx/walk grass.mp3"

    scene forest night with fade:
        xpos 0
        blur 2
        linear 15 xpos -1920  # Move left by one screen width over 8 seconds (adjust speed)
        repeat
    show hik normal:
        zoom 0.5
        xalign 0.4
        yalign -0.15
        yoffset -400
        xzoom -1
        yzoom 1.0

        yoffset -400
        linear 0.5 yoffset -420
        linear 0.5 yoffset -400
        repeat

    n "The both of you are walking in total silence now."

    n "The boar swings gently between you, strung on a shared pole."

    hikaru "You... {w=0.5}You're sure you're {i}okay?{/i}"

    MC "...Sorry. Just thinking."

    hikaru "About what?"

    MC "Uh, {w=0.5}umm, {w=0.5}how the boar will taste."

    hikaru "Hungry already?"

    MC "...Yeah."

    hikaru "Don't worry, I'll make sure it'll taste good for everyone."

    scene black
    with out_212

    MC "..."

    $ loop2_hikaru_mandatory1 = True

    #return

label loop2_hikaru_mandatory2:

    scene shrine day:
        zoom 0.7
        xalign 0.5
        yalign 0.5


        ease 0.5 zoom 0.55
    show hik normal:
        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.4 zoom 0.4 yoffset 20


    n "When you arrive at the shrine, you see hikaru crouching down beside a curtain."

    hikaru "There’s... something here. Can you help me with--Ah!"
    with vpunch

    n "There's a hidden room, it reeks with mold, old rot, and... Ugh."

    n "A horrible smell envelops the room immediately."

    hikaru "{sc=1}...Kami-sama.{/sc}"

    play music "spooky.mp3"

    play sound "sfx/suzu.wav"

    show screen black_flicker
    with Pause(0.45)


    show gore:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    hide screen black_flicker
    show darken2


    n "Bones are scattered on the floor. Somene's remains, and some still has rotten meat on it."

    if persistent.shiori_eaten:
        n "There are ribbons tied with bells..."

        n "You’ve seen it in someone’s hair--"

        n "And ankle bracelets too..."

        n "No. Who?"

    elif persistent.yamato_eaten:
        n "You see a dark red sash, frayed at the end, alongside a bottle of sake."

        n "Someone wore that around their waist. You remember..."

        n "...the smell of sake in your mouth?"

    hide gore
    show hik normal:
        zoom 0.4
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 20
        xoffset 0

        linear 0.07 xoffset -18 yoffset 26
        linear 0.06 xoffset 12 yoffset 18
        linear 0.06 xoffset -8 yoffset 24
        linear 0.05 xoffset 0 yoffset 20
        # Subtle, soft return to original pose
        linear 0.10 yoffset 23
        linear 0.11 yoffset 20


    n "Hikaru's tears fall, hand shaking in disbelief."
    hikaru "{k=2}...!{/k}"

    hikaru "{sc=3}Wait, what?{/sc}"

    hikaru "{i}What's going on?{/i}"

    n "They’re crying."

    n2 "The soul knows what the mind forgets."

    hikaru "{k=2}Do I know this person?{/k}"

    hikaru "..."

    hikaru "{w=0.2}...Why can’t I remember?"

    hikaru "{k=2}[persistent.player_name]...{/k}"

    hikaru "Do you remember them?"

    MC "...I..."

    menu:
        "Say you don’t know":
            MC "...I’ve never seen these before."

            hikaru "..."

            hikaru "{sc=1}I... I see.{/sc}"

        "Say nothing":
            MC "..."

    hikaru "{w=0.2}Do you think they got eaten by Yamakui?"

    MC "If you can't remember them, then yes."

    hikaru "..."

    MC "But don't worry, I killed it! So there's no way anyone will get eaten again!"

    hikaru "{k=2}Y-Yes... That's right..{/k}"

    MC "Let's just go home, you look pale, Hikaru."

    hikaru "{i}Yeah...{/i}"

    scene black

    with fade

    n "You return to the shrine again to see Hikaru crouching at the same place as yesterday, shovel in hand."

    scene shrine day:
        zoom 0.7
        xalign 0.5
        yalign 0.5


        ease 0.5 zoom 0.55
    show hik normal:
        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.4 zoom 0.4 yoffset 20

    hikaru "{sc=2}It's {b}gone.{/b}{/sc}"

    show hik normal:
        zoom 0.4
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.4 xzoom -1

    hikaru "Weird... {w}{i}It was here yesterday...{/i}"

    hikaru "Do you know where the bones are? I'm about to bury them--"

    MC "No idea."

    if persistent.shiori_eaten:
        MC "Maybe the shrine maiden got rid of it?"

        hikaru "{sc=4}We have {b}NO{/b} shrine maiden!{/sc}"

        hikaru "{i}Or... {w=0.1}At least... {w=0.1}We had at some point?{/i}"

        hikaru "{w=0.2}Is this the shrine maiden?"

        n "You just shrug."

    elif persistent.yamato_eaten:
        MC "Did Shiori bury it?"

        hikaru "{k=2}No... I told Shiori that I'll bury it myself...{/k}"

    hikaru "{k=2}Did you--?{/k}"

    hikaru "...No. You wouldn’t."


    n "They turn toward you, slowly."

    show hik normal:
        zoom 0.4
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        xzoom -1

        linear 0.4 zoom 0.5 yoffset 40
        linear 0.1 yoffset 30


    hikaru "[persistent.player_name]...?"

    MC "Mm?"

    hikaru "I'm gonna go look for it. Maybe someone else buried it."

    MC "Okay, I'll stay here then."

    hikaru "Yeah, see you."

    show hik normal:

        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 30
        xoffset 0
        xzoom -1


        pause 0.22

        ease 0.4 xzoom 1 xoffset 10 yoffset 65 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
        #linear 0.09 xzoom -1.0 xoffset 0 yoffset 80

        linear 0.4 zoom 0.3 yoffset 120 xoffset 50 alpha 0.0

    n "They step away, but you remain a moment longer."

    n "Staring at the place where cloth used to lay folded over bone."

    n "You {b}should{/b} remember."

    n "Whoever owned the bones... {w=0.5}They used to laugh with you, {blur}didn't they...?{/blur}"

    scene black
    with out_182

    n2 "..."

    n2 "I only remember the {i}screaming.{/i}"

    $ loop2_hikaru_mandatory2 = True

    #return

label loop2_hikaru_mandatory3:

    play music "Night.mp3"

    scene moon3
    show hik normal:
        zoom 0.5
        xalign 0.5
        yalign 0.2
        xoffset 0
        yoffset 400


    n "You and Hikaru are sitting together on the roof."

    hikaru "You know what, I think you've changed since the mountains."

    hikaru "You're... a lot calmer now, and a lot less affectionate."

    hikaru "Are you mad at me?"

    n "Their hand moves slowly and stops over your chest, right above where your heartbeat should be."

    n2 "Hhhh..."

    hikaru "I feel like something’s missing."

    hikaru "Are you bored of me? Sorry that I got too paranoid about the bones, but--"

    hikaru "Don't you think that even the Yamakui is dead now, everything's still not how it's supposed to be?"

    n "You lean in..."

    hikaru "[persistent.player_name]...?"

    scene moon3:
        easein 0.33 zoom 1.4

    show hik normal:
        zoom 0.5
        xalign 0.5
        yalign 0.2
        xoffset 0
        yoffset 400

        # Smoothly zoom in and move head into frame
        easein 0.33 zoom 1.25 yalign 0.08 yoffset 170 xoffset 200

    n "...and shut them up with a kiss."

    ##3 squelching kiss

    n "Hikaru's mouth tries to follow, but--"

    show darken2

    stop music

    play sound "sfx/mmph.mp3"
    with sshake

    hikaru "Mmmph--"

    n2 "The tounge will know the path. {w}Slide it deep, and it'll find the center."

    n "{sc}The hell{/sc} are you talking about--"

    n2 "Still ripe."

    play sound "sfx/mmph2.mp3"
    with sshake

    n "Stop. Please. PLEASE--"

    n2 "Down. {w=0.2}Slide down. {w=0.2}Make room. {w=0.2}There's the soft windpipe{nw}"

    n2 "Warm, warm, warm all the way in.{nw}"

    n "Stopstopstopstopstopstopstop--"

    play sound "sfx/gag1.mp3"
    $ renpy.pause(0.4)

    hikaru "--ghhk--!"

    scene moon3:
        easeout 0.1 zoom 1

    show hik normal:
        zoom 1.25
        xalign 0.5
        yalign 0.08
        xoffset 200
        yoffset 170


        linear 0.09 zoom 0.67 yoffset 50 xoffset 60
        linear 0.11 zoom 0.52 yoffset 210 xoffset -120
        linear 0.08 zoom 0.5 yoffset 50 xoffset 0





    n "They shove you back, breathless."

    with hpunch

    hikaru "What... {w=0.1}the... [persistent.player_name]?"

    hikaru "That... {w=0.1}that {sc=1}wasn’t...{/sc}"

    n2 "Let’s go deeper this time."

    n "NO!"

    MC "..."

    MC "Why? You said I wasn't as affectionate."

    MC "This good enough for you?"

    hikaru "I-{w=0.1}I..."

    show hik normal:
        zoom 0.5
        xalign 0.5
        yalign 0.08
        xoffset 0
        yoffset 50

        # Rapid shake sequence
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 35 yoffset 65
        linear 0.04 xoffset -20 yoffset 42
        linear 0.04 xoffset 14 yoffset 55
        linear 0.04 xoffset -8 yoffset 49
        linear 0.04 xoffset 0 yoffset 50


    hikaru "You're being weird, [persistent.player_name]. What's... {w=0.1}{sc=1}what's gotten into you?{/sc}"

    MC "I don't understand."

    show hik normal:
        zoom 0.5
        xalign 0.5
        yalign 0.08
        xoffset 0
        yoffset 50

        # Rapid shake sequence
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 35 yoffset 65
        linear 0.04 xoffset -20 yoffset 42
        linear 0.04 xoffset 14 yoffset 55
        linear 0.04 xoffset -8 yoffset 49
        linear 0.04 xoffset 0 yoffset 50

    hikaru "I... {w=0.5}I just remembered--"

    show hik normal:
        zoom 0.5
        xalign 0.5
        yalign 0.08
        xoffset 0
        yoffset 50

        # Rapid shake sequence
        linear 0.05 xoffset -30 yoffset 30
        linear 0.05 xoffset 35 yoffset 65
        linear 0.04 xoffset -20 yoffset 42
        linear 0.04 xoffset 14 yoffset 55
        linear 0.04 xoffset -8 yoffset 49
        linear 0.04 xoffset 0 yoffset 50

    hikaru "The, uh--{w}fire. I left my irori still burning--"

    n "They gesture vaguely toward the trail, not even looking that direction."

    show hik normal:
        zoom 0.5
        xalign 0.5
        yalign 0.08
        xoffset 0
        yoffset 50

        # Sudden, sharp jerk back and down, with a bit of zoom out
        linear 0.11 zoom 0.38 yoffset 20 xoffset 60
        linear 0.09 zoom 0.34 yoffset 100 xoffset -40
        # Settle at the new, farther (lower) position
        linear 0.07 zoom 0.3 yoffset 170 xoffset 0


    hikaru "I should... {w=0.5}turn the fire off before my food burns to a crisp."
    play sound "sfx/whip.mp3"
    hide hik
    with hpunch

    n "Run, Hikaru, please... Just go away--"

    scene black
    with out_182

    MC "..."

    MC "..." ## change to eerie expression
    $ loop2_hikaru_mandatory3 = True

    #return

label loop2_hikaru_mandatory4:

    scene house night:
        zoom 0.5

    play sound "sfx/knock.wav"

    with vpunch
    pause 0.01
    with vpunch
    pause 0.01
    with vpunch
    pause 0.01

    n "You hear a soft knocking at your door, you open it to reveal Hikaru standing in front of your house."

    play sound "sfx/sliding door.mp3"

    pause 0.3

    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    with dissolve

    pause 0.2

    stop sound

    MC "Hey, Hikaru. Come in--"

    n "Hikaru doesn't budge."

    hikaru "{w}..."

    play music "Tense.ogg"

    hikaru "{i}I’ve been thinking.{/i}"

    hikaru "{k=2}Last night... {w}that wasn’t you, was it?{/k}"

    hikaru "{sc=3}The way you kissed me. That--{/sc}"

    hikaru "{i}That feels... {w}wrong.{/i}"

    MC "Huh?"

    show darken2

    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0

        # Quick, tight, uneven tremble
        linear 0.06 xoffset -7 yoffset 44
        linear 0.05 xoffset 4 yoffset 36
        linear 0.07 xoffset -3 yoffset 40
        linear 0.06 xoffset 5 yoffset 42
        linear 0.07 xoffset 0 yoffset 40
        repeat

    hikaru "{w=0.2}Your tongue is not that long, isn't it?"

    hikaru "{i}I've always known how your body feels like--{/i}"

    hikaru "{sc=3}[persistent.player_name] would never kiss like that.{/sc}"

    hikaru "{w}[persistent.player_name] never looked at me like I was something to-to... {i}unwrap and swallow.{/i}"

    hikaru "{sc=3}You're not [persistent.player_name].{/sc}"

    scene house night:
        zoom 0.5
        easein 0.4 zoom 0.7
    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
        easein 0.4 zoom 0.47 yoffset 20
    show darken2

    play sound "sfx/shing.mp3"

    n "You step forward, but Hikaru unsheates their sai."

    n "{i}No, just... {w}Run. Stay away from me, from us--{/i}"

    hikaru "{k=2}Who are you...?{/k}"

    hikaru "{sc=4}No, WHAT are you!?{/sc}"

    with hpunch

    scene black

    $ name_input_index = 0
    $ name_display = ""

    call screen fake_name_input

    $ name = name_display

    n "You feel your mouth move. Your jaw feels like it wants to unhinge--"

    n "Your name is--"

    n2 "{size=+6}{w=0.1}Y {w}a {w}m {w}a {w}k {w}u {w}i.{/size}"

    scene house night:
        zoom 0.7
    show hik normal:
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 20
        xoffset 0
        zoom 0.47
        yoffset 20
    show darken2

    hikaru "{k=2}...No.{/k}"

    play sound "sfx/heartbeat.mp3"
    with flashred
    $ renpy.pause(0.5)

    hikaru "{sc=3}No--no--{/sc}"

    n2 "{b}I told you.{/b}"

    n2 "{size=+6}{w=0.1}Y {w}a {w}m {w}a {w}k {w}u {w}i.{/size}"

    n2 "{i}That’s the real name under the skin.{/i}"

    play sound "sfx/stumble.mp3"

    show hik normal:
        zoom 0.47
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 20
        xoffset 0

        linear 0.11 zoom 0.36 yoffset 110 xoffset -30
        linear 0.10 zoom 0.3 yoffset 180 xoffset 0

        linear 0.05 xoffset -18 yoffset 194
        linear 0.04 xoffset 14 yoffset 172
        linear 0.06 xoffset 0 yoffset 180

    n "Hikaru stumbles back, hands trembling. Their mouth hanging open, wanting to scream but can’t."

    play sound "sfx/step_back.ogg"
    $ renpy.pause(0.3)

    hikaru "{k=2}You killed [persistent.player_name]...{/k}"

    MC "{w=0.1}Hikaru--"

    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 180
        xoffset 0

        # Huge, rapid shake for a shout
        linear 0.04 xoffset -44 yoffset 194
        linear 0.03 xoffset 38 yoffset 166
        linear 0.03 xoffset -29 yoffset 192
        linear 0.04 xoffset 23 yoffset 177
        linear 0.04 xoffset -14 yoffset 185
        linear 0.04 xoffset 0 yoffset 180


    hikaru "{sc=5}STAND BACK!{/sc}"

    hikaru "{sc=3}I’ll--I’ll kill you--{/sc}"

    hide hik
    with hpunch

    play sound "sfx/whip.mp3"

    n "Hikaru..."

    n2 "{i}Run, run little bird...{/i}"

    n2 "{size=+4}{w=0.08}B u t    {w}t h e    {w}r e d    {w}m o o n    {w}i s    {w}c o m i n g.{/size}"


    $ loop2_hikaru_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear

    return
