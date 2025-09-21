############# LOOP 1 WHERE EVERYONE IS ALIVE ###########################
label loop1_yamato_mandatory1:

    scene dojo day with in_182:
        zoom 0.5

    pause 1.0

    show yam normal:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        xzoom -1
        yzoom 1.0
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        pause 0.8

        ease 0.5 xzoom 1 matrixcolor None xoffset 120

    ## DOJO DAY

    play music "Yamato.mp3"
    pause 0.5
    yamato "Oi, oi. Look what the kami-sama dragged outta bed."

    MC normal "Morning to you too, Yamato-kun. You out here exorcising evil spirits or something?"

    yamato "Someone's gotta do it."

    MC "Why? I killed the Oni, didn't I? You can take a break once in a while, you know!"

    yamato "Tch... Standin’ there lookin’ so smug..."

    MC "All right, I think you're being unnecessarily hostile. What's gotten into you?"

    yamato "What's gotten into me is that yer bein' too damn clean for someone who fought the fuckin' Yamakui!"

    with vpunch

    yamato "I don't believe the brat I used to mop the floor with could easily kill 'em!"

    MC "Wait, you're saying... that I'm lying?"

    yamato "Keh..."

    yamato "Why don't we go one round to see which one of us is lyin', eh?"

    MC "So you want to kick my ass now?"

    yamato "What? The damned \"Oni Slayer\" won't back down from a challenge from lyin' ol' me, right?"

    MC "Fine! If you want proof, you damn well got one!!"

    play sound "sfx/clash.ogg"

    MC "Haaaaah!!"

    play sound "swing.wav"

    scene black

    show slash_arc
    scene dojo day:
        zoom 0.5
    show yam normal:
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
    with vpunch

    yamato "{sc=1}Tch! Swingin’ like a drunk ox, kusogaki!{/sc}"

    n "You charge in, but he easily slips past you."

    scene black

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

    scene dojo day:
        zoom 0.5

    show yam normal:
        zoom 0.47
        align (0.5, 0.005)


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.29 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.25 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0


    hide combo_slash_1
    hide combo_slash_2
    hide combo_slash_3

    n "His sword cuts the air, but you duck out just in time."

    MC "Are you holding back, Yamato-kun~? Or are you always this slow?"

    show yam normal:
        zoom 0.25
        xalign 0.4
        xoffset 144
        yoffset 0

        # Rapid, small side-to-side shakes (as if shouting)
        linear 0.06 xoffset 154
        linear 0.06 xoffset 134
        linear 0.06 xoffset 149
        linear 0.05 xoffset 139
        linear 0.07 xoffset 144

    yamato "{sc=1}Oi, don’t get cocky. Ain’t doin’ shit like that!{/sc}"

    n "Your sword sings again, he manage to parry once but you shifted your weight and swing one more time."

    show yam normal behind slash_fx:
        zoom 0.26
        align (0.4, 0.2)
        linear 0.1 align (0.5, 0.3) zoom 0.4
        pause 0.05
        linear 0.2 align (0.4, 0.005) zoom 0.26
    with vpunch


    play sound "swing.wav"
    show slash_vertical
    $ renpy.pause(0.1, hard=True)
    with vpunch

    n "It almost hits, but--"

    play sound "sfx/fall.mp3"
    show yam normal:
        zoom 0.26
        align (0.4, 0.005)
        yoffset 0

        linear 0.10 yoffset -20

        linear 0.25 yoffset 1100

        pause 0.4


    with vpunch


    n "Yamato’s foot trips on something, and he slips down, accidentally avoiding your swing."

    n "..."

    stop music fadeout 1.0

    yamato "Tch... {w=0.1}Ahhh, fuckin’ hell..."

    MC "Yamato?!"

    n "You remember Yamato is never this careless, you wonder if he is doing this on purpose."

    n "You hand out your hand to help him stand, but he doesn't take it."

    show yam normal with easeinbottom:
        zoom 0.26
        align (0.4, 0.005)
        yoffset 0

    yamato "Lost my footing, ’s all. Ain’t my lucky day."

    MC "...Yamato kun--"

    yamato "Oi. Don’t gimme that look."

    yamato "Yer the star now, yeah? Whole damn village sings yer name loud enough to wake the dead."

    yamato "Me? Just some mutt still barkin’ out orders to trees."

    MC "What are you talking about? Are you still mad that I get to kill the oni?"

    MC "Everyone knows that you're just as strong! No one will look down on you even though--"

    yamato "Tch. Don’t feed me that fluffy crap."

    play music "Tense.ogg"

    MC "I’m not--"

    yamato "I used to be the strong one. Y'know that?"

    yamato "Back when ya still pissed yer hakama and swung like a fish outta water."

    n "That’s... That’s not how it happened. Is it?"

    yamato "{size=+2}{sc=3}I was the one who trained ya.{/sc}{/size}"

    MC "{sc=2}Yeah, but I was the one who killed the damn thing!{/sc}"

    yamato "Hah. {w=0.1}Ya really believe that? That thing tore people in half, scared the elders shitless and somehow... somehow {i}ya{/i} come back without a scratch?"

    MC "{cps=91}What, {w=0.1}you think I’m making it up?!{/cps}"

    yamato "{sc=1}Tch.{/sc} I think... ya don’t even know yerself."

    n "Yamato hasn’t moved, but you feel cornered by his words. If you hadn't lied, you won't feel cornered."

    MC "{cps=10}Ha!{/cps} Say whatever you want, I brought back the armor! Everyone saw it!"

    yamato "Yeah? Armor’s just scrap metal if ya ask me. Coulda been anyone’s, or {i}planted--{/i}"

    n "He stops. His jaw locks tight. He almost said something worse."

    MC "{cps=9}What?{/cps}"

    n "Yamato pauses, then looks down before staring you right at the eyes. He's hesitating...?"

    yamato "{sc=5}Tch, nevermind.{/sc}"

    show darken
    with dissolve

    yamato "{size=+4}{color=#ff003c}Next red moon...{w}I’ll be watchin’ ya.{/color}{/size}"

    n "Weird... Yamato is usually not like this..."

    n "He was kind and always ready to help anyone in need of sparring partner, but now..."

    n "What's gotten into him?"

    MC "{sc=2}*scoff*{/sc}"

    yamato "{glitch}If ya really killed the Yamakui, ya wouldn’t be shakin’ right now.{/glitch}"

    show yam normal:
        linear 0.4 xzoom -1 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
    pause 0.1

    hide yam
    hide darken
    with dissolve

    stop music fadeout 1.0

    n "He walks out without looking back. You want to shout after him, but your throat closes up."

    n "You’re alone now."

    n "Alone."

    n "Except for the pounding in your ears."

    scene black

    pause 0.3

    #return

label loop1_yamato_mandatory2:

    $ loop1_yamato_mandatory2 = True

    scene dojo day with in_182:
        zoom 0.5

    pause 1.0

    n "No one uses the dojo anymore after you return."

    play music "Night.mp3"

    show yam normal with dissolve:
        zoom 0.26
        align (0.5, 0.005)
        yoffset 0

    n "But there he is, again. Swinging that katana of his like he has something to prove."

    yamato "Heh... Look who's here."

    yamato "Ya said we don't need t' train anymore because the goddamn Yamakui died, didn't ya?"

    MC "Shut up, I'm just checking on you."

    yamato "{sc=3}Heh, sure ya do.{/sc}"

    yamato "Red Moon’s near. Ya feel it?"

    MC "{sc=1}Stop talking like the Oni's gonna return!{/sc}"

    MC "{size=+2}I mean, I brought its armor back, right? What more proof do you want?!{/size}"

    yamato "{w=0.1}Yeah? Ya {i}sure{/i} 'bout that?"

    yamato "'cause Hikaru said it was too damn small to belong to the Oni."

    MC "{sc=0.5}Have either of you or Hikaru seen the oni?{/sc}"

    MC "{sc=0.5}I was the only one who did and stayed alive!{/sc}"

    with vpunch

    yamato "All t' more reason to doubt ya."

    MC "...Damn, that was harsh."

    yamato "'Cause people's lives depend on it."

    $ _prev_music_volume = _preferences.volumes["music"]

    $ decrease_music_volume(0.5)
    $ renpy.block_rollback()

    show yam normal:
        zoom 0.26
        align (0.5, 0.005)
        yoffset 0

        parallel:
            linear 2.2 zoom 0.3 align (0.55, 0.002) yoffset 40 xoffset 20
        parallel:

            linear 0.6 align (0.52, 0.04)
            linear 0.5 align (0.48, 0.02)
            linear 0.6 align (0.52, 0.04)
            linear 0.5 align (0.55, 0.02)


    yamato "Ya came home grinnin’ with blood on that armor, [persistent.player_name]. Told 'em they could sleep easy."

    show yam normal:
        zoom 0.3
        align (0.55, 0.02)
        yoffset 40

        parallel:
            linear 2.2 zoom 0.35 align (0.6, 0.002) yoffset 70 xoffset 20
        parallel:

            linear 0.6 align (0.52, 0.04)
            linear 0.5 align (0.48, 0.02)
            linear 0.6 align (0.52, 0.04)
            linear 0.5 align (0.55, 0.02)

    yamato "{size=+2}So if they don’t wake up after the {glitch}red moon's{/glitch} over...{/size}"

    yamato "{fi=13-1.5-20}That's on ya.{/fi}"

    MC "..."

    yamato "{w=0.1}...Oi. [persistent.player_name]."

    MC "Huh?"

    yamato "What color was its blood?"

    n "The words stumble before you even think of an answer."

    menu:
        "Say it's {color=#ff082d}red.{/color}":
            show darken2
            with dissolve
            MC "It was... {color=#ff082d}red.{/color}"
            n "Why did you stutter? Of course it was {color=#ff082d}red.{/color}"
        "Say it's black.":
            MC "It was... black. Yeah. Black."
            yamato "...Black?"
            n "No, no, something's wrong."
            show darken2
            with dissolve
            MC "I-I mean {color=#ff082d}red{/color}?"

    yamato "Ya sure?"

    menu:
        "Yes. Definitely.":
            MC "Y-Yeah. Definitely!"
        "I think so...":
            MC "...I think so?"
            n "That didn't sound very convincing."

    yamato "Tch."

    show yam normal:
        zoom 0.35
        align (0.55, 0.02)
        yoffset 70
        xoffset 20

        parallel:
            linear 2.2 zoom 0.42 align (0.65, 0.002) yoffset 95 xoffset 20
        parallel:
            linear 0.6 align (0.52, 0.04)
            linear 0.5 align (0.48, 0.02)
            linear 0.6 align (0.52, 0.04)
            linear 0.5 align (0.65, 0.02)


    n "He doesn't look convinced and leans closer, shrinking the gap between you. You can't breathe right."

    yamato "Say that again?"

    menu:
        "{color=#ff082d}Red{/color}, I said.":
            MC "{color=#ff082d}Red{/color}, I said!"
            with sshake
            n "Whoa, there's no need to yell!"
        "Stop asking me that!":
            MC "Why do you keep asking me that?!"
            with hpunch
            yamato "Because you keep soundin’ like you’re lyin’."

    n "Your pulse pounds harder now. What is the point of this?"

    yamato "Last chance. {cps=15}What color was its blood?{/cps}"

    menu:
        "{color=#ff082d}Red.{/color}":
            MC "{color=#ff082d}...Red.{/color}"
        "{color=#ff082d}Red.{/color} Again.":
            MC "I already told you. {color=#ff082d}Red.{/color}"

    stop music
    $ restore_music_volume()

    MC "{color=#ff082d}Red. Red. RedredredredredREDREDREDREDREDREDREDREDRED. RED!{/color}"

    yamato "..."

    ## creepy laugh scene

    show yam normal:
        zoom 0.42
        align (0.65, 0.002)
        yoffset 95
        xoffset 20


        parallel:
            linear 0.07 yoffset 120
            linear 0.05 yoffset 88
            linear 0.06 yoffset 110
            linear 0.04 yoffset 92
            linear 0.06 yoffset 105
            linear 0.05 yoffset 95
            repeat
    play music "Narukami.mp3"
    yamato "{sc=2}...Heh...{/sc}"

    yamato "{sc=3}{k=2}...Heh... hehh... hhhhehhh--{/k}{/sc}"

    yamato "{sc=4}{size=+2}{k=1}Haaaahh... HHHahh--!!{/k}{/size}{/sc}"

    with vpunch


    yamato "{size=+8}{sc=7}AHAHAHAHA...!{/sc}{/size}"

    with sshake

    MC "The hell was that for?"

    show yam normal:
        zoom 0.42
        align (0.65, 0.002)
        yoffset 95
        xoffset 20
    with dissolve

    yamato "...Yeah, ya sounded like a liar."

    MC "You sounded like an asshole."

    yamato "Don't worry, [persistent.player_name], even if you're lyin'... I'd always be here, yeah?"

    yamato "I'd clean yer mess like always, and slay the blasted thing myself when the red moon comes."

    show yam normal:
        zoom 0.42
        align (0.65, 0.002)
        yoffset 95
        xoffset 20
        alpha 1.0


        parallel:
            linear 1 zoom 0.3
        parallel:
            ease 0.5 xoffset 35 yoffset 105
            ease 0.5 xoffset 5 yoffset 95
            repeat 1


        linear 0.8 alpha 0.0

    MC "...!!!"

    pause 2

    n "He left..."

    n "What did he mean by that?"

    n "You're sure the Oni's blood was {color=#ff082d}red{/color}."

    n "It was {color=#ff082d}red{/color}. You saw it--{w} didn’t you?"

    n "You stabbed it. {w}The liquid was dipping from your hands when you stabbed it. {w}{color=#ff082d}Red{/color}. {w}{color=#ff082d}Red{/color}. It HAD to be {color=#ff082d}red{/color}."

    n "It was very dark at the time, sure. But your sword was {color=#ff082d}red{/color}, right? You remember that, right?"

    n "No. {w}No, stop. Stop thinking about it. It was {color=#ff082d}red{/color}. It was. {w}It {i}was.{/i}"

    n "Then why was he laughing like that?"

    scene black

    pause 0.3

    stop sound



    #return

label loop1_yamato_mandatory3:

    $ loop1_yamato_mandatory3 = True


    ## YOUR HOUSE NIGHT

    scene house night:
        zoom 0.5

    play music "sfx/walk grass.mp3"

    n "You are in your house when you hear footsteps outside."

    n "Why are you not asleep at this hour? Do you ever sleep? Does the fight haunt you so much that--"

    n "Ah, that doesn't matter."

    n "What matters now is that the footsteps are nearing."

    n "You see a shadow outside your door."
    scene white_bg
    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 900
        xzoom -1
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
    show darken
    with fade

    stop music
    n "Yamato."

    n "Crouched low, hunched shoulders, clearly stalking... {w=0.2}or waiting."

    n "Today is not Yamato's patrol schedule."

    n "You immediately grab your sword, ready to fight--"

    n "Why? It's just Yamato. Your childhood friend. Even though he is more irritable lately, surely he is not trying to harm you."

    n "You don’t make a sound until--"

    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 900
        xzoom -1
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        ease 0.4 zoom 0.29

        linear 0.05 xoffset 920
        linear 0.05 xoffset 900
        linear 0.05 xoffset 925
        linear 0.05 xoffset 895
        linear 0.05 xoffset 900

    MC "{sc=2}...Tch.{/sc}"

    n "You almost growls as the blade presses to his back."

    play music "sfx/forest night.wav"

    MC "{size=+3}{b}...Don’t.{/b}{/size}"

    yamato "..."

    MC "{b}Step away.{/b} {w}{size=+2}Slowly.{/size} {w}{sc=3}Or I’ll spill you across the floorboards.{/sc}"

    n "He freezes. You can feel his muscles shift under the blade, but he's still silent."

    MC "{size=+2}C'mon, Yamato. Give me a reason not to.{/size}"

    yamato "Damn, who taught you to speak like that?"

    MC "{b}Yamato.{/b}"

    yamato "...I was just walkin' around."

    MC "{sc=2}You never walk around my house nowadays.{/sc}"

    yamato "The road goes where I say it does."

    n "His voice sounds like it had to fight its way out."

    MC "{k=2}I think you are snooping around my house.{/k}"

    yamato "Ya always think everyone’s watching you?"

    MC "Just tell me what you came here to do."

    yamato "..."

    MC "Are you trying to steal--"

    yamato "Why would I give a shit about your old junk?"

    MC "You know what's inside is not just junk."

    yamato "{sc=4}Heheheheh...{/sc}"

    yamato "{size=+2}{k=2}Why so tense, [persistent.player_name]?{/k}{/size}"

    yamato "{sc=3}All stiff and hissin', makes me wonder what you’re hidin'.{/sc}"

    scene black
    with sshake

    n "Your grip tightens, and your whole body wants to fight."

    n "But instead, you take a very deep breath... and walks closer to him."

    scene house night:
        zoom 0.5
    with fade



    MC "Fine, if you want to look at it so bad, be my guest."

    show yam normal:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        xzoom -1
        yzoom 1.0
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        pause 0.8

        ease 0.2 xzoom 1 matrixcolor None xoffset 120
    with dissolve

    yamato "Hah?"

    MC "The armor. That's what you’re here for, right?"

    yamato "Uh... I--"

    MC "I'll prove that it's authentic, that you and Hikaru are just looking for a reason to doubt me."

    hide yam
    with dissolve

    scene house night:
        zoom 0.5
        xanchor 1
        yanchor 1

        ease 0.5 zoom 0.7 xoffset -420 yoffset -100
    show darken
    with dissolve

    MC "Go ahead, see for yourself."

    yamato "...Tch. {w}Looks even worse than I remember."

    MC "It was worse when I dragged it home."

    n "He crouches, then his hand hovers above the armor’s edge."

    yamato "{sc=2}Hmph.{/sc}"

    play sound "sfx/kickmetal.mp3"

    with sshake

    n "He kicks it, the armor clatters."

    MC "Easy."

    yamato "...This really it?"

    MC "You’ve seen it before, when I brought it back."

    yamato "Doesn’t feel the same."

    MC "{w=0.2}...You still think I lied?"

    yamato "...I think... {w}{i}I dunno what to think.{/i}"

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show charm:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
    with dissolve

    n "Yamato takes out a talisman from his sleeve and pushes it to the armor."

    n "You know it will react to the armor if it touches an evil spirit."

    n "You take a step back, circling him."

    MC "I mean, the thing is dead. So if you're looking for some sort of evil aura, there'd be none left."

    yamato "{w=0.2}...If this is real, then you really--"

    MC "Yeah."

    yamato "...{w=0.2}Huh."

    n "He circles the armor once, then again, looking for faults. Can't seem to find one."

    yamato "...Ya could’ve at least cleaned it better."

    MC "I didn’t want to touch it again."

    n "He grunts and tries to lift the damn thing."

    yamato "{w=0.2}...Kinda {w=0.4}heavy for something so damn small."

    MC "Try dragging it downhill by yourself."

    scene house night:
        zoom 0.7
        xanchor 1
        yanchor 1
        xoffset -420
        yoffset -100

        ease 0.5 zoom 0.5 xoffset 0 yoffset 0
    pause 0.4

    show yam normal:
        zoom 0.3
        xalign 0.4
        yalign -0.15
        yoffset 0
        xzoom -1
        yzoom 1.0
    with dissolve

    n "He sits down, arms resting on his knees, and maybe, just maybe, recalculating."

    yamato "{fi=1}...A'ight, fine.{/fi}"

    n "Something in his gaze changes, and so is in the way he looks at you now."

    n "It's... a lot softer now."

    yamato "Guess I barked up the wrong tree. Hhh... {w}Tch. Damn embarrassing."

    MC "So you finally admit it?"

    yamato "Don’t push it, kid. I just... {w}{i}got carried away. Thought I smelled somethin’ off, y’know? Guess I was sniffin’ shadows.{/i}"

    n "He rubs the back of his neck, eyes avoiding yours."

    n "You feel as if the harsh features on his face falter under the shades of your oil lamp, almost slipping into something resembling regret."

    yamato "I’ll, uh... {w}head out. Don’t tell Shiori I was lurkin’ here like an idiot."

    MC "Yeah, yeah."

    show yam normal:
        zoom 0.3
        xalign 0.4
        yalign -0.15
        yoffset 0
        xzoom -1
        yzoom 1.0

        ease 0.5 yoffset -140
    with dissolve

    pause 0.3

    hide yam
    with dissolve

    n "He stands up then gives a half-hearted wave sheepishly as he vanishes into the dark."

    MC "..."

    MC "You idiot."

    stop music

    scene black

    pause 0.3

    #return

label loop1_yamato_mandatory4:

    $ loop1_yamato_mandatory4 = True

    scene village day:
        zoom 0.5

    n "You were just walking from your house when you hear people arguing nearby."

    play music "Tense.ogg"

    show hik normal:
        zoom 0.231
        xanchor 0.5
        yalign -0.09
        xzoom 1.0
        yzoom 1.0
        yoffset 100
        xoffset 1400

    with dissolve
    pause 0.3
    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 600

    with dissolve

    hikaru "{w=0.1}{k=-1}...Are you saying I was wrong about the armor?{/k}"

    yamato "Tch. I dunno. Maybe... {w=0.3}{sc=1}maybe th' armor don’t matter after all.{sc}"

    n "That’s strange. {w=0.1}Yamato’s the one who always doubted you and always swore that you couldn’t have done it..."

    n "So why is his voice shaking now?"

    hikaru "...What are you {i}implying?{/i}"

    yamato "I went back to see the damn thing and put Shiori's talisman on it. Thought I’d catch somethin’ nasty clingin’ to it."

    yamato "Nothin’ happened. If Yamakui's alive, it shoulda have residue."

    hikaru "..."

    hikaru "{atl=-#,#,fade_in_text~0.6}Are you really sure?{/atl}"

    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 600

        linear 0.09 yoffset 65

        linear 0.08 yoffset 30

        linear 0.12 yoffset 0



    yamato "{sc=3}I'm not fuckin' blind! It didn't shine one bit!{/sc}"

    yamato "Felt like maybe... {w}{i}maybe we’re barkin’ up the wrong damn tree.{/i}"

    n "Hikaru goes still. Even from here you see the falter in their posture."

    hikaru "{b}...You don’t mean--{/b}"

    yamato "I mean... maybe we’re wrong this time. {w=0.3}Maybe [persistent.player_name] {b}did{/i} kill th' damn thing after all."

    pause 0.5

    n "The silence after is heavier than any word spoken."

    show hik normal:
        zoom 0.231
        xanchor 0.5
        yalign -0.09
        xzoom 1.0
        yzoom 1.0
        yoffset 100
        xoffset 1400

        linear 0.5 xzoom -1 xoffset 1430

    hikaru "{sc=2}This is absurd.{/sc} {i}You{/i} were the one who told me not to trust so easily. You said [persistent.player_name] was hiding something."

    yamato "...Yeah. I did."

    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 600

        linear 0.5 xzoom -1 xoffset 500

    yamato "{k=-1}But... I dunno anymore.{/k}"

    scene black
    with fade

    n "You stay hidden in the shadows, even after the both of them part ways."

    n "Watching."

    stop music

    #return

label loop1_yamato_mandatory5:

    $ loop1_yamato_mandatory5 = True

    play music "sfx/forest night.wav"

    scene black
    with fade

    n "You decide to patrol tonight even though Yamato don't ask you to."

    n "It's closer to the red moon, of course, but--"

    n "You hear mutterings, prayers in ancient language... And it's a voice that you're too familiar with."

    n "You follow it."

    n "Maybe with the red moon so close you shouldn't do something like that..."

    n "...but your legs move anyway."

    scene forest night with fade:
        zoom 0.5
        yanchor 1

        pause 0.1
        linear 2 zoom 0.7
    pause 0.5
    show yam normal:
        zoom 0.35
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.5 zoom 0.3


    play music "noinomai.mp3"
    n "You see Yamato, kneeling at the clearing. His hands on his sword, shaking. Head bowed so low he looks like a broken puppet."

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

    n "--No...."

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



    n "There's a shadow behind him with many eyes in places that shouldn't have eyes."

    n "You can’t look at it directly, because you know it'll recognize you."

    MC "...Yamato."

    n "Why is your voice so calm? {w}Why aren't you screaming...?"

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

    MC "{sc=0.3}Yamato!{/sc}"

    stop music

    play sound "sfx/distort.mp3"



    scene forest night:
        zoom 0.5
    show yam normal:
        zoom 0.3
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000

        linear 0.5 zoom 0.3

    with in_212
    hide screen eyessss

    yamato "{color=#ff1111}{b}Wha--!!!{/b}{/color}"

    n "The thing folds out of existence as soon as Yamato's chanting stops."

    yamato "[persistent.player_name]...."

    play music "Tense.ogg"

    n "He's frozen, eyes staring straight at you... {w}Or perhaps, to whatever is behind you. {w=0.3}"

    MC "...Did you just try to summon something?"

    n "{w=0.2}You speak so matter-of-factly it sounds rather unsettling.{w=0.2}"

    n "{i}Wait, do you know what that thing was?{w=0.2} Have you seen it before?{/i}"

    yamato "Y-ya weren't supposed to see that, damnit."

    MC "What the hell was that?"

    yamato "I'm prayin' for the gods to protect us the next red moon."

    MC "That thing doesn't look like a god."

    show yam normal:

        zoom 0.3
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000

        parallel:
            easein 0.1 yoffset 60
            easeout 0.1 yoffset 0
            easein 0.08 yoffset 20
            easeout 0.08 yoffset 80
            easeout 0.1 yoffset 0

        parallel:
            easein 0.1 yzoom 0.95 xzoom 1.05
            easeout 0.1 yzoom 1.0 xzoom 1.0
            easein 0.08 yzoom 0.97 xzoom 1.03
            easeout 0.08 yzoom 1.0 xzoom 1.0

    yamato "Yeah, but that wasn't Yamakui either!"

    MC "You're gonna fight an oni with something worse?"

    yamato "{sc=0.2}Shit, you don't know anything, do ya?{/sc}"

    n "Yamato's voice breaks, his sword is clattering in the ground now. {w=0.2}"

    yamato "{k=-1}...Ever since ya came back, people look at me like I’m some leftover.{/k}"

    yamato "The village already got their hero, so what the hell do they need me for?"

    yamato "And... I ain’t stupid, a'ight? I know what they're sayin'."

    yamato "‘Course [persistent.player_name] came back stronger, faced the Yamakui and lived.'"

    yamato "Then they look at me like I’m--like I'm just a jealous bloke. {w=0.2}"

    yamato "{w=0.1}Tch, maybe I {i}am.{/i} But I'm not just some loser howlin' at the moon."

    MC "...So you prayed to whatever that thing was?"

    show yam normal:
        zoom 0.3
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000

        linear 0.05 xoffset 990
        linear 0.05 xoffset 1010
        linear 0.05 xoffset 985
        linear 0.05 xoffset 1015
        linear 0.05 xoffset 995
        linear 0.05 xoffset 1005

        ease 0.3 xoffset 1000


    yamato "...I didn’t mean to summon--{nw}"

    yamato "{glitch=1.1}I thought maybe if I got stronger--if I had just a bit {i}more{/i}--maybe I'd be--{/glitch}"

    MC "Haaaah...."

    MC "Oh, well."

    n "{i}'Oh well?' {/i}{w=0.2}"

    n "He tried to summon a creature that watched you from a body made of {color=#ff1111}{i}rotting arms{/i}{/color} and knowing eyes, and that's all you can say?"

    MC "Yamato..."

    scene forest night:
        zoom 0.5
        yanchor 1

        pause 0.1
        linear 1 zoom 0.6
    show yam normal:
        zoom 0.30
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 1000

        parallel:

            linear 1 zoom 0.38
        pause 0.1
        linear 0.05 xoffset 990
        linear 0.05 xoffset 1010
        linear 0.05 xoffset 1000

    n "You step closer and gently put your hand on his shoulder. {w=0.2}Yamato jerks backwards, but doesn't swat your hand away."

    n "{i}The contact should ease him. {w=0.2}Should.{/i}"

    n "But somehow he is still trembling. {w=0.3}"

    MC "You're more than just a jealous guy, Yamato. You're the one who always sparred with me and taught me the basics of swordsmanship."

    yamato "...Hh."

    MC "'Cmon, let's go back before whatever that thing was decide to return."

    scene black
    with dissolve

    play sound "sfx/walk grass.mp3"

    n "Yamato finally eases, and you pull your hand away, gesturing for him to follow you."

    n "You walk back together in silence. {w=0.3} The forest is now dead silent behind you, but it wasn't as eerie anymore."

    n "Nothing watches from the trees now. {w=0.2} You are sure."

    n "You're {i}sure{/i}."

    ## so like the MC is yamakui, and the amalgamation is merely the corpses / ghosts of the things the yamakui has killed

    #return
    jump prologue_loop1
