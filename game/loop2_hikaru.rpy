label loop2_hikaru:

    $ hsword = True

    play music "Battora.mp3"

    scene house night:
        zoom 0.5

    show hik rage:
        zoom 0.24
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1
        yzoom 1.0

        matrixcolor BrightnessMatrix(-0.8) * TintMatrix("#111111")

        ease 0.5 matrixcolor None zoom 0.3
    pause 0.1
    with sshake

    play music "Battora.mp3"

    n "You wake up to see Hikaru already barging in into your house."

    hikaru "I don’t care if it's forbidden{w=0.2} or if it kills me..."

    hikaru "You-{w=0.2} you took [persistent.player_name] from me."

    hikaru "{glitch=8}Yamakui...!{/glitch}"

    with sshake

    n "They’re sweating,{w=0.2} hands shaking,{w=0.3} smearing salt across the floor in thick,{w=0.2} frantic lines."

    show magic_circle at spin_forever behind hik:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    show hik rage:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1
        yzoom 1.0
    show darken

    n "It's... {w=0.1}a binding circle?"

    n "How does Hikaru know something like this?"

    n2 "This again."

    n2 "It's {i}useless.{/i}"

    show hik madcry:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.05 xoffset 92
        linear 0.04 xoffset 148
        linear 0.05 xoffset 100
        linear 0.04 xoffset 140
        linear 0.04 xoffset 120

        linear 0.03 xoffset 128
        linear 0.03 xoffset 112
        linear 0.03 xoffset 120

        pause 0.06

    hikaru "{sc=5}Y-you stole [persistent.player_name]'s face, you monster...{/sc}"

    show hik madcry:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.05 xoffset 92
        linear 0.04 xoffset 148
        linear 0.05 xoffset 100
        linear 0.04 xoffset 140
        linear 0.04 xoffset 120

        linear 0.03 xoffset 128
        linear 0.03 xoffset 112
        linear 0.03 xoffset 120

        pause 0.06

    hikaru "You dare use {i}that mouth{/i} to kiss me!"

    n "Wait–"

    n "{sc=1}Wait–{w=0.2} Hikaru–{/sc}"

    n "Please–{w=0.3} don’t do this–"

    n2 "HeheHAHAHAHEHhehe.{w=0.2} Let them {b}try.{/b}"

    n "Hikaru,{w=0.2} it’s me–{w=0.2} it's really {i}me{/i} in here–"

    n "I’m still here!{w=0.2} I’m–"

    n2 "{b}{i}D{w} E{w} A{w} D.{/i}{/b}"

    n "{color=#ff002e}DON’T!{/color}"

    play sound "sfx/quake.mp3"
    with sshake

    n "You feel the ground vibrate,{w=0.2} no,{w=0.3} wait,{w=0.2} it's your bones that are vibrating."

    hikaru "Why are you still smiling,{w=0.2} {sc=1}damn you!?{/sc}"

    MC yansm2 "You’re cute when you’re desperate."

    n "{i}No, stop this madness at once! Let me speak–{/i}"

    n "Hikaru,{w=0.2} I love you.{w=0.3} I’ve always–"

    n "{cps=15}...Run.{/cps}"

    MC "Why? As long as it's me,{w=0.2} you don't mind... Do you, Hikaru?"

    show hik rage:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.05 xoffset 92
        linear 0.04 xoffset 148
        linear 0.05 xoffset 100
        linear 0.04 xoffset 140
        linear 0.04 xoffset 120

        linear 0.03 xoffset 128
        linear 0.03 xoffset 112
        linear 0.03 xoffset 120

        pause 0.06

    hikaru "{sc=7}SHUT UP!{/sc}"

    show magic_circle at spin_forever behind hik:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        linear 5 zoom 2.0

    n "The circle glows.{w=0.3} You feel it {sc=5}cutting{/sc} into you."

    n2 "AhhhHH–{w=0.2} {i}YES–{/i}"

    hikaru "{cps=13}Give me back [persistent.player_name] !{/cps}"

    with vpunch

    MC "What do you mean?{w=0.2} I'm [persistent.player_name]."


    play sound "sfx/prang.mp3"
    hide magic_circle with in_shatter

    n "With one simple swoosh of your hand,{w=0.2} the whole binding circle {glitch=8}shatters{/glitch}."


    show hik panic:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.05 xoffset 92
        linear 0.04 xoffset 148
        linear 0.05 xoffset 100
        linear 0.04 xoffset 140
        linear 0.04 xoffset 120

        linear 0.03 xoffset 128
        linear 0.03 xoffset 112
        linear 0.03 xoffset 120

        pause 0.06

        linear 0.08 zoom 0.25 yoffset -44
        linear 0.11 yoffset 70


    hikaru "{i}No–{/i}"

    hikaru "{cps=14}No, please–{/cps}"

    hikaru "{sc=2}I did everything right...{/sc}"

    n2 "Is that all?"

    MC yansm2 "{cps=30}Time to say goodbye, Hikaru~{/cps}"

    n "{color=#ff002e}No–{/color}"

    hikaru "{sc=7}Damn it...!{/sc}"

    play sound "sfx/stumble.mp3"

    show hik panic:
        zoom 0.25
        xalign 0.4
        xoffset 120
        yoffset 20
        xzoom 1.0
        yzoom 1.0

        linear 0.09 xoffset 30 yoffset 14
        linear 0.07 xoffset 62 yoffset -18
        linear 0.11 xoffset 48 yoffset 10
        linear 0.09 xoffset 38 yoffset 70

        pause 0.07
    play sound "sfx/run.mp3"

    show hik panic:
        zoom 0.25
        xalign 0.4
        xoffset 38
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.01 xoffset -90 yoffset 50
        linear 0.02 xoffset -180 yoffset 60
        linear 0.05 xoffset -320 yoffset 78
        linear 0.08 alpha 0.0





    ## hikaru's sprites stumbles back and then runs

    ## shaking image of hikaru running frantically to the village

    scene black
    with sshake

    hikaru "{sc=8}SOMEONE–PLEASE–!!{/sc}"

    scene village night with in_212:
        zoom 0.5
    show man at midright:
        zoom 0.43
        ypos 0.1
    with dissolve
    show woman at right behind man:
        zoom 0.42
        xzoom-1
        yoffset 400
    with dissolve

    show hik panic at midleft :
        zoom 0.25
        yoffset 100
        xzoom -1
    with hpunch

    show darken

    "Man" "...Hikaru?"

    "Woman" "What’s all the noise?"

    show hik panic at midleft:
        zoom 0.25
        yoffset 100
        xzoom -1

        linear 0.08 xoffset -9
        linear 0.07 xoffset 8
        linear 0.08 xoffset -7
        linear 0.07 xoffset 6
        linear 0.08 xoffset -4
        linear 0.07 xoffset 4
        linear 0.09 xoffset 0
        pause 0.06

    hikaru "{sc=1}It’s Yamakui!!!{/sc}{w} IT’S STILL HERE–"

    show hik panic at midleft:
        zoom 0.25
        yoffset 100
        xzoom -1

        linear 0.08 xoffset -9
        linear 0.07 xoffset 8
        linear 0.08 xoffset -7
        linear 0.07 xoffset 6
        linear 0.08 xoffset -4
        linear 0.07 xoffset 4
        linear 0.09 xoffset 0
        pause 0.06

    hikaru "It’s wearing [persistent.player_name] ’s face–{w=0.2} {sc=2}YOU HAVE TO LISTEN!{/sc}"

    "Man" "...What?"

    show hik rage at midleft:
        zoom 0.25
        yoffset 100
        xzoom -1

        linear 0.08 xoffset -9
        linear 0.07 xoffset 8
        linear 0.08 xoffset -7
        linear 0.07 xoffset 6
        linear 0.08 xoffset -4
        linear 0.07 xoffset 4
        linear 0.09 xoffset 0
        pause 0.06

    hikaru "{sc=2}WE HAVE TO KILL THAT THING–THAT THING WEARING [persistent.player_name]!{/sc}"

    show hik panic at midleft:
        zoom 0.25
        yoffset 100
        xzoom -1
        linear 0.08 xoffset -9
        linear 0.07 xoffset 8
        linear 0.08 xoffset -7
        linear 0.07 xoffset 6
        linear 0.08 xoffset -4
        linear 0.07 xoffset 4
        linear 0.09 xoffset 0
        pause 0.06

    hikaru "Please...{w=0.3} please, believe me–"

    n2 "{b}Foolish.{w=0.2} Foolish.{w=0.2} FOOLISH.{/b}"

    "Man" "How dare you accuse [persistent.player_name] like that, Hikaru!"

    with vpunch

    "Woman" "They saved the village! They brought the armor back!"

    with vpunch

    "Man" "Unlike your father, who ran into the mist and never returned!"

    hikaru "{color=#ff002e}NO!{/color}"

    show hik rage at midleft:
        zoom 0.25
        yoffset 100
        xzoom -1

        linear 0.08 xoffset -9
        linear 0.07 xoffset 8
        linear 0.08 xoffset -7
        linear 0.07 xoffset 6
        linear 0.08 xoffset -4
        linear 0.07 xoffset 4
        linear 0.09 xoffset 0
        pause 0.06

    hikaru "My father wasn’t a coward–{w=0.2} HE WAS TRYING TO FIND A WAY OUT–{w=0.2} YOU KNOW THAT!"

    n2 "{cps=30}No one listens to the traitor’s child.{/cps}"

    n "Hikaru's voice starts to crack from screaming.{w=0.2} Their fists clench until the nails cut skin and bleeds..."

    hikaru "You're all going to {sc=1}DIE!{/sc}"

    hikaru "DON’T YOU UNDERSTAND?!{w=0.3} IT’S IN [persistent.player_name]! IT’S WEARING [persistent.player_name]'S SKIN!"

    hikaru "I’M TRYING TO {sc=1}SAVE YOU!{/sc}"

    play sound "sfx/stumble.mp3"

    show man at midright:
        zoom 0.43
        ypos 0.1
        linear 0.11 xpos 0.64
        pause 0.07
        linear 0.10 xpos 0.7

    show hik shocked at midleft:
        zoom 0.25
        yoffset 100
        xzoom -1
        linear 0.11 xoffset -80 yoffset 106
        linear 0.07 xoffset -140 yoffset 94
        linear 0.08 xoffset -112 yoffset 110
        linear 0.09 xoffset -100 yoffset 100
    $ renpy.pause(0.5)


    with sshake

    n "The man shoves Hikaru back like swatting a mad dog."

    "Man" "{size=+5}Enough!{/size}"


    "Man" "Look at yourself, Hikaru!{w=0.2} You’ve lost your mind!"

    "Woman" "You should be ashamed, screaming like this in front of the children!"

    n "{i}No...{/i}"

    MC sad2 "Sorry for the trouble...{w=0.2} Hikaru’s not well."

    n "{color=#ff002e}No!{/color}"

    MC sad2"Hikaru's been talking nonsense for days,{w=0.2} barely sleeping...{w=0.2} Seeing things in the woods, you know."

    n "{glitch=8}Hikaru's not wrong!{/glitch}"

    MC nervous2 "I tried to help."

    MC nervous2 "But...{w=0.2} I think Hikaru's gone mad. Just like Karasuma-san."

    show hik shocked at midleft:
        zoom 0.25
        yoffset 100
        xoffset -100
        xzoom -1

        # Jagged surprised jump
        linear 0.08 yoffset 62 xoffset -70    # Snap up/right suddenly (surprised)
        linear 0.07 yoffset 132 xoffset -140  # Drop down/left
        linear 0.07 yoffset 88 xoffset -110   # Bounce up/right again (less)
        linear 0.08 yoffset 100 xoffset -100  # Settle back to original

        pause 0.06

    hikaru "...!"

    n "I'm sorry...{w=0.3} Hikaru..."

    hikaru "...You..."

    hikaru "{sc=2}You LIAR–{/sc}"

    MC sadcl2 "Go home, Hikaru.{w=0.3} Before you hurt someone."

    "Man" "{sc=1}Let's go before you make a ruckus again!{/sc}"

    show man at midright:
        zoom 0.43
        ypos 0.1
        xpos 0.7
        linear 0.16 xpos 0.8
        linear 0.13 xpos 1.1 alpha 0.0
    show hik shocked at midleft:
        zoom 0.25
        yoffset 100
        xoffset -100
        xzoom -1
        linear 0.14 xoffset 60 yoffset 120
        linear 0.13 xoffset 220 yoffset 105
        linear 0.11 xoffset 360 yoffset 90 alpha 0.0
    show woman at right:
        zoom 0.42
        xzoom -1
        yoffset 400

        linear 0.3 xzoom 1 xoffset -100
    pause 0.1


    n "The man grabs Hikaru’s arm roughly{w=0.2} and pulls Hikaru away,{w=0.2} too stunned to struggle against him."

    scene black
    with out_212
    stop music fadeout 1.0

    hikaru "{cps=30}...No one’s listening...{/cps}"

    hikaru "{cps=30}{w=0.1}...You all deserve what’s coming...{/cps}"

    hikaru "You all–"

    hikaru "You all deserve to be {glitch=9}devoured...{/glitch}"
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

    n "It's here...{w=0.3}"

    play music "Blood Ritual.mp3"

    n "{glitch=7}And so are you–{/glitch}"

    scene village night at bg_run_shake:
        matrixcolor TintMatrix(Color(rgb=(0.60, 0.20, 0.20))) * BrightnessMatrix(-0.1)

    play muzak "sfx/run.mp3"

    hikaru "{sc=6}Hahh–hahh–hahhh–{/sc}"

    n2 "{b}I can hear it.{/b}"

    n2 "{b}Step.{w=0.2} Step.{w=0.2} Step.{w=0.3} FLEE.{/b}"

    n2 "Run, little thing."

    n2 "I’ll follow the footprints made from your blood."

    stop sound fadeout 1.0
    stop muzak

    play sound "sfx/shing.wav"

    scene forest night:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    show hik panic:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.47
        align (0.5, 0.005)

        linear 0.01 xalign 0.5 yalign 0.1
        linear 0.16 zoom 0.59 xalign 0.59 yalign -0.09 xoffset -122
        linear 0.12 zoom 0.25 xalign 0.4 yalign 0 xoffset 144 yoffset 0
        linear 0.07 yoffset 8
        linear 0.09 yoffset 85

    with vpunch

    n "...They're cornered now."

    hikaru "...You!"

    ## shing sai draw

    play sound "sfx/shing.wav"
    with hpunch

    n "Hikaru draws their sai now,{w=0.2} ready to fight to the death{w=0.3} and bring you down with them."

    n2 "{b}Like that will help.{/b}"

    show hik madcry
    with dissolve

    hikaru "I don’t care if I die."

    show hik madcry:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 85

        # Sudden lurch forward, then shaking as they shout
        linear 0.08 zoom 0.34 yoffset 28      # Jolt forward and down (mouth open, shout)
        linear 0.04 yoffset 35                # Small drop for impact
        linear 0.05 yoffset 28                # Snap up, shake
        linear 0.04 yoffset 33
        linear 0.04 yoffset 28
        linear 0.05 zoom 0.25 yoffset 85      # Return to start

        pause 0.07

    hikaru "{sc=2}I’ll drag you down screaming if it’s the last thing I do!{/sc}"

    MC smug2 "Why don't you try...?"


    hikaru "Kami-sama should’ve struck you down–"

    hikaru "But they didn’t.{w=0.2} Just like the rest of them–those cowards back in the village."

    hikaru "They turned their backs on me–"

    hikaru "Let you walk free–"

    hikaru "{color=#ff002e}They left me ALONE–!{/color}"

    show hik madcry:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 85

        # Jagged, trembling shake
        linear 0.06 xoffset 129 yoffset 74
        linear 0.05 xoffset 151 yoffset 99
        linear 0.04 xoffset 135 yoffset 81
        linear 0.05 xoffset 141 yoffset 93
        linear 0.04 xoffset 144 yoffset 85

        pause 0.06

    hikaru "{sc=3}A L O N E–!!{/sc}"

    show hik madcry:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 85

        # Jagged, trembling shake
        linear 0.06 xoffset 129 yoffset 74
        linear 0.05 xoffset 151 yoffset 99
        linear 0.04 xoffset 135 yoffset 81
        linear 0.05 xoffset 141 yoffset 93
        linear 0.04 xoffset 144 yoffset 85

        pause 0.06

    hikaru "{glitch=12}WHILE YOU ATE MY LOVER!!{/glitch}"

    n "Hikaru–{w=0.2} please–"

    n "RUN–"

    n "{sc=7}RUN BEFORE I CAN’T STOP THIS–{/sc}"

    n "I’m still here, inside this body–{w=0.1}I still love you–"

    n2 "{b}Shut up.{/b}"

    n2 "I’m hungry."

    MC evil2 "You were always the softest one."

    hikaru "You want me?"

    show hik rage:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        zoom 0.25
        xalign 0.4
        yalign 0
        xoffset 144
        yoffset 85

        # Jagged, trembling shake
        linear 0.06 xoffset 129 yoffset 74
        linear 0.05 xoffset 151 yoffset 99
        linear 0.04 xoffset 135 yoffset 81
        linear 0.05 xoffset 141 yoffset 93
        linear 0.04 xoffset 144 yoffset 85

        pause 0.06

    hikaru "{sc=3}Come and TRY!!!{/sc}"

    n2 "...Time to eat."

    n "STOP–{nw}"

    # Optional: Play sound effects in sync
    scene black
    play sound "swing.wav"
    show combo_slash_1
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "swing.wav"
    show combo_slash_2
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "swing.wav"
    show combo_slash_3
    $ renpy.pause(0.1, hard=True)

    with sshake
    pause 0.1

    n "Metal {sc=6}screams{/sc} against clawed hands."

    n "Their arm twists back{w=0.2} and you catch it easily,{w=0.2} snapping it."

    play sound "sfx/crack.mp3"
    pause 0.1
    with sshake
    pause 0.5

    play sound "sfx/pain.mp3"
    hikaru "{sc=7}Aahh–ghhk–{/sc}"

    show darken2
    with dissolve

    n "They stumble unto the ground,{w=0.2} their sai is gone.{w=0.3} One arm lies limp beside them..."

    n "But their other hand {sc=4}claws{/sc} the ground, still trying to reach you."

    n "{cps=13}You're towering over them now.{/cps}"

    play sound "sfx/heartbeat.mp3"

    hikaru "{cps=20}Ngh...{w=0.3} ha...{w=0.3} hah...{/cps}"

    hikaru "{i}You’re... still inside, right?{/i}"

    hikaru "{cps=14}I know you're watching.{/cps}"

    hikaru "[persistent.player_name]..."

    n "{color=#ff002e}Hikaru... No...{/color}"

    n2 "..."

    n2 "It's time to feast."

    ## erratic mouse
    pause 1.0

    call screen horror_forced_menu_jitter(items=[
    ("Save Hikaru", Jump("yesyeysysyqsad222"), False),
    ("Eat", Jump("yesyeysysyqsad222"), False)
])

label yesyeysysyqsad222:

    stop music fadeout 1.0

    n2 "{cps=10}Hold still.{/cps}"

    hikaru "{i}I’ll see them again soon...{/i}"

    pause 0.1

    hikaru "Under the tree..."

    pause 0.1


    hikaru "When...{w=0.5} the cherry blossoms...{w=0.5} bloom–"

    n2 "{cps=10}Open wide.{cps=10}"

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
    show darken2

    play music "sfx/monstermunch.mp3"
    $ renpy.pause(0.5)

    n2 "{cps=10}Sllk... ghhk... nrrrh...{/cps}"


    play sound "sfx/tearflesh.wav"
    n2 "Gkkk–chk–krRRSHK."

    play sound "sfx/swallow.mp3"
    n2 "Ghhhlk... glkk...{w=0.2} *gulp*."

    play sound "sfx/splurt.mp3"
    n2 "{cps=11}Nghh–skrrk–ssLLLK...{/cps}"

    play sound "sfx/slurrp.mp3"

    n2 "...It's done."

    stop music

    scene black
    with out_212

    n "..."

    n "They’re gone."

    n "{i}...no.{/i}"

    pause(1.0)

    n "...No."

    n "{sc=5}No no no no–{/sc}"

    n "{glitch=10}What did you–{/glitch}"

    n "{sc=7}WHAT DID YOU DO–{/sc}"

    n "{glitch=11}HIKARU WAS–{/glitch}"

    pause(1.0)

    n "{cps=15}Hikaru was my–{/cps}"

    n2 "Ah, you remember now that Hikaru's inside us?{w=0.2} About who you are?"

    n "{sc=8}I DIDN'T WANT THIS!{/sc}"

    n "{size=+6}{sc=8}YOU WEREN’T SUPPOSED TO KILL HIKARU!{/sc}{/size}"

    n "{w=0.3}.{w=0.3}.{w=0.3}You weren't supposed to...{w=0.3} I was trying to..."

    n "I thought if I just..."

    pause(0.5)

    n "...forgot about Hikaru, then you won't eat–{nw}"

    pause(1.0)

    n2 "Too late."

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}HIKARU IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}O N E M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    $ persistent.hikaru_dies = True

    $ persistent.loop2 = True

    $ MainMenu(confirm=False)()


    return
