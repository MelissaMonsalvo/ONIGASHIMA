label prologue_loop1:

    ### this has the prologue after one person has been devoured

    $ loop2_shiori_mandatory1 = True
    $ loop2_shiori_mandatory2 = True
    $ loop2_shiori_mandatory3 = True
    $ loop2_shiori_mandatory4 = True

    $ loop2_yamato_mandatory1 = True
    $ loop2_yamato_mandatory2 = True
    $ loop2_yamato_mandatory3 = True
    $ loop2_yamato_mandatory4 = True

    $ loop2_hikaru_mandatory1 = True
    $ loop2_hikaru_mandatory2 = True
    $ loop2_hikaru_mandatory3 = True
    $ loop2_hikaru_mandatory4 = True


    scene black with fade

    MC panic2 "Haa... {w=0.4}Haa..."

    scene black with fade
    show flesh2 at scary_flicker

    play music "heavy breathing.mp3"

    n "{cps=18}It is dark.{/cps}"

    n "We're here again...?"

    MC panic2 "Gh... khhh..."

    n "Are you choking?"

    n "You shouldn’t be. You’re alive. You won, remember?"

    n "Wait a second, you've been through this before... This feels familiar..."

    play muzak "sfx/squelch.mp3"

    n "Again."

    n "You stab again. {w=0.1}Again. Again.{w=0.2} {color=#ff0000}Wait.{/color} {w=0.2}{color=#ff0000}Stop.{/color}"

    n "Haven't you stabbed this thing to oblivion before?"

    n2 "Again."

    n "..."

    n "W-h-"

    n "Who was that? Was that you?"

    n "You grip the hilt harder, your sword is sticky now, covered with blood."

    n "You’ll need to clean it. Later. Burn it maybe."

    n "What... {w=0.1}did you kill?"

    n2 "...You."

    n "...What?"

    n "Isn't this supposed to be Yamakui? But wait..."

    n "It has red blood? And doesn't it supposed to have claws? A-and this is Yamakui's lair. And you're alive."

    n "This makes no sense."

    n "No, no, that can’t be right. The sound that it made when you cut through it was {i}NOT{/i} human at all."

    n "You heard it screamed, right? {w=0.2}Or did it cry out?"

    n "Did it say your name with its dying breath?"

    n "You lift the blade again, about to stab the creature {w=0.2}{size=+4}{color=#990000}{atl=-#,#,fade_in_text~0.6}{glitch=1.1}again{/glitch}{/atl}{/color}{/size}."

    n "{size=+4}{color=#990000}Stop.{/color}{/size}"

    stop muzak

    MC yan2 "...."


    n "{size=+2}{color=#880000}Please. Stop.{/color}{/size}"

    n "You saved the village. This was... {w=0.2}noble."

    n "Stabbing a thing that is no longer alive, {w=0.5}again, {w=0.4}again, {w=0.3}again, {w=0.2}again, and {w=0.1}again is {i}not{/i} noble. {w=0.3}That's not what heroes do."

    n "You're sure it's {atl=-#,#,fade_in_text~0.6}{glitch=1.1}dead{/glitch}{/atl} now. You can go, return to the village, and..."

    n2 "{size=*0.95}{k=-1}Snap, {w=0.1}chew, {w=0.1}swallow, {w}d e v o u r.{/k}{/size}"

    n "That voice again... Is that you, [persistent.player_name]?"

    n "......"

    n "...."

    n "..."

    n "{size=*0.9}{k=-1}You must be hallucinating things.{/k}{/size}"



    scene black with fade



    n "{cps=18}It’s time to return to the village.{/cps}"

    play muzak "sfx/forest night.wav"



    n "You start down the mountain, but these legs {i}don't feel like yours{/i}."

    play sound "sfx/metal drag.wav"
    $ renpy.pause(0.8)

    n "{w=0.2}The sound of armor dragging follows behind you. It grinds the stone path as you drag it along with one hand."

    play sound "sfx/metal drag.wav"
    $ renpy.pause(0.8)

    n "The elders said the Yamakui wore stone armor. That its body was too large for skin alone."

    n "This... this is your proof. You dragged it with you, so they'd believe you."

    n "Because there was {i}nothing else{/i} left. {w=0.2}Because you--"

    n2 "{size=+2}{color=#880000}{glitch=1.1}--stole it.{/glitch}{/color}{/size}"

    n "..."

    play sound "sfx/metal drag.wav"
    $ renpy.pause(0.8)

    n "They won’t doubt you. {w=0.2}Not when they see this."

    n "You did it. You killed it. You’re {i}sure{/i}."

    n "{size=+2}{color=#880000}You’re sure.{/color}{/size}"

    MC annoyed2 "Hhh..."

    n "{w=0.2}It’s cold and quiet and eerie and absolutely NOT what you expected."

    n "You just fought the thing they feared for generations. Where’s the fanfare?"

    n "Shouldn’t the forest open up for you? Shouldn’t the world feel..."

    n "{size=*0.95}{k=-1}...safe?{/k}{/size}"

    n "You imagine the clouds parting, or gold light spilling down, or flowers blooming or... something."

    n2 "Pfft... hkkk-HRAHAHAH."

    n "--!"

    n2 "Gold light. Pretty lie. {w}Ha."

    n "What--"

    n2 "Keep telling that lie to yourself, won't you?"

    n "..."

    play sound "sfx/metal drag.wav"
    $ renpy.pause(0.8)

    n "You keep walking, tracing the familiar pathway to the village that the Yamakui used to trail when they go..."

    n "...to the village..."

    n "...before... the red moon..."

    n "{cps=10}...{/cps}"

    n2 "{size=+2}Done talking?{/size}"

    n "No. That's {i}not{/i} true."

    n "You killed the Oni. That's what is supposed to happen. {w=0.3}So now you're going home."

    n "{w=0.2}You’ll be a hero."

    n "{b}{cps=8}{glitch=1.1}A hero.{/glitch}{/cps}{/b}"


    scene village day with in_182:
        zoom 0.5


    n "..."

    n "Finally."

    n "Once you step on the village borders, everything changes."

    n "The sky looks like it splits into two once the treeline dissapears... The heavenly shine that you've imagined."

    MC happy2 "Hey, guys. I'm back."

    show woman:
        xzoom -1
        zoom 0.35
        xalign 0.65
        ypos 0.2

        linear 0.1 ypos 0.3 zoom 0.2
    with vpunch
    play sound "sfx/bucketdrop.wav"
    $ renpy.pause(0.8)

    n "Someone sees you, drops their bucket  Everyone stops what they are doing to look at you."

    n2 "{blur}{color=#ff2b54}So many necks to snap.{/color}{/blur}"

    play music "Tense.ogg"
    stop muzak

    "Woman" "{size=*0.95}{k=-1}No way...{/k}{/size}"

    hide woman
    with dissolve

    scene village day:
        zoom 0.5
        yanchor 1
        pause 0.1
        linear 2 zoom 0.7 xalign 0.6

    play sound "sfx/walk grass.mp3"


    stop sound

    n "You walk toward a familliar-looking elder and hands the armor out. He steps forward and examines the armor, brows furrowing."

    show elder:
        xzoom -1
        zoom 1
        xalign 0.65
        ypos 0.25
    with dissolve

    MC "So?"

    "Elder" "Im-Impossible..."

    "Elder" "This couldn't be..."

    "Elder" "The Oni is... dead?"

    n "Insteade of cheering, people just stare..."

    hide elder
    with dissolve

    play music "Doubt.mp3"

    show woman at left:
        zoom 0.5
        ypos 0.2
    with dissolve
    show man at center:
        zoom 0.5
        ypos 1.67
    with dissolve
    show oldman at right:
        zoom 0.5
        xoffset -50
        ypos 1.67
    with dissolve

    n "Hands reach for you, but they seem to be unsteady. Everyone looks...conflicted and unsure."

    n "That's odd, shouldn't they be celebrating? Shouldn't they be joyous?"

    n "Shouldn't they call your name?"

    n "Wait, what is your name again?"

    n2 "{blur}{color=#ff2b54}Y A M A K U I{/color}{/blur}" ## use horror text

    n "NO."

    n2 "{cps=201}Yamakui. Yamakui. Yamakui--"

    n "No, that’s-{w}That’s NOT-!"

    "Man" "Did you really kill the yamakui, [persistent.player_name]?"

    MC smug2 "Yeah! I took down that Oni in one blow! Well... maybe two! Or ten! Who’s counting?!"

    "Elder" "[persistent.player_name], you have done us a great service."

    n2 "Hungry."

    n "Shut up."

    n2 "{cps=201}Hungry hungry hungry."

    n "{cps=201}Shut up {size=+3}shut up{/size} {size=+6}shut up{/size} {size=+9}shut up{/size} {size=+12}shut up{/size}--"

    "Woman" "Great job, [persistent.player_name]-san..."

    "Old Man" "...Are we really safe now?"

    n "{cps=57}No one looks at the armor.{/cps}"

    n "They looked worried still, because someone was recently devoured. Someone by the name of--"

    n "--huh?"

    n "Why can't I remember their name? That's odd, let me think again. Were they your friend?"

    n2 "{sc=1}{color=#ff2b54}Don't think too much.{/color}{/sc}"

    if not persistent.shiori_dies:
        jump speechhh2shiori
    else:
        jump speechhh2noshiori

label speechhh2shiori:

    scene village day:
        # Start at normal crop
        anchor (0.5, 0.5)
        xpos 0.5 ypos 0.5
        xanchor 0.5 yanchor 0.5
        zoom 0.6
        linear 0.15 zoom 0.61
        linear 0.08 xpos 0.51 ypos 0.49
        linear 0.08 xpos 0.5 ypos 0.5
        # Second stumble, more pronounced
        linear 0.12 zoom 0.63
        linear 0.10 xpos 0.48 ypos 0.52
        linear 0.10 xpos 0.5 ypos 0.5
        # Hold at max zoom
        linear 0.15 zoom 0.62
        pause 0.3

    n "Later, you are pulled to stand in front of everyone, almost stumbling on your feet."

    n "You wonder why the Elder's hand is shaking when he tugs your arm."

    n "Or maybe that's your own hand that's trembling."

    show elder:
        xzoom -1
        zoom 0.8
        xalign 0.65
        ypos 0.1
    with dissolve

    "Elder" "Come. Let them see it clearly."

    n "You raise the armor."

    n "Sunlight catches the edges. Something {i}wet{/i} glistens, red trails slide off the plating."

    n "It's {color=#ff0000}red.{/color} Yamakui's blood is black."

    n "{atl=-#,#,fade_in_text~0.6}You lied.{/atl}"

    "Elder" "{b}Look well, all of you.{/b}{w=0.3}"

    "Elder" "{b}For years, we have lived in shadow.{/b}{w=0.2}"

    "Elder" "We boarded our windows, {i}whispered our prayers{/i}, and cremated ashes without names.{w=0.2}"

    "Elder" "{b}The Yamakui haunted us longer than memory itself.{/b}{w=0.4}"

    "Elder" "{b}And yet...{/b}{w=0.4}"

    "Elder" "{b}[persistent.player_name] climbed that mountain and came back.{/b} {i}Where no one else could.{/i}{w=0.3}"

    play sound "sfx/clap.mp3"

    n "The crowd claps, but they don't seem to be excited. Odd."

    stop sound

    "Elder" "{b}Never again will we light our fires with fear.{/b}{w=0.3}"

    "Elder" "{b}Never again will we sleep listening for footsteps.{/b}{w=0.3}"

    "Elder" "{b}Never again will our loved ones vanish under the Red Moon.{/b}{w=0.3}"

    "Elder" "{b}And never again will we... forget.{/b}{w=0.6}{nw}"

    hide elder
    with fade

    "Girl" "Speech, [persistent.player_name]!"

    n "A voice rises from the crowd. Shiori’s, maybe."

    MC normal2 "Thank you, everyone. I didn’t do it alone."

    MC normal2 "I had your hopes, your prayers, {w}your bento."

    MC smugcl2 "Aaaand that weird old charm from our beloved shrine maiden..."

    MC smugcl2 "Still stuck in my pocket, by the way, thanks Shiori!"

    n2 "It stings. Throw it away."

    n "Don’t."

    n2 "Let's rip apart the shrine maiden next."

    n "Stop. {i}Please.{/i}"

    MC nervous2 "...{w=0.3}I..."

    MC nervous2 "...{w=0.3}I climbed that mountain."

    MC nervous2 "...{w=0.3}Faced it head-on...."

    MC nervous2 "...{w=0.3}And I, {w=0.3}I won."

    MC smug2 "{w=0.3}So let’s celebrate! No more fear!"


    n "They seem to believe you now."

    n "{cps=7}They believe you.{/cps}"

    n "The armor is still in your hand, the only proof that you killed Yamakui."

    n "As you step down from the shrine, the crowd parts."

    n2 "{glitch}Hungry, hungry, hungry.{/glitch}"

    $ _prev_music_volume = _preferences.volumes["music"]

    $ decrease_music_volume(0.2)
    $ renpy.block_rollback()
    pause 0.2

    hide elder
    show woman at midleft :
        zoom 0.5
        ypos 0.2
    with dissolve
    show man at midright:
        zoom 0.5
        ypos 0.1
    with dissolve
    show darken
    with dissolve

    n "You can still hear the scared whispers of the villagers ringing in your ears."

    "Man" "The next Red Moon’s coming soon, isn’t it?"

    "Woman" "Think we’ll be safe this time?"

    "Man" "I don't know, but..."

    "Man" "...there’s nothing left to hide from. Right?"

    n "...Right?"

    n2 "AhaHAHAhahaHa."

    $ restore_music_volume()

    scene village day:
        zoom 0.5
    with dissolve

    n "You hear your name again."

    n "The armor still hangs limply from your hand."

    n "It feels...{w} heavier now."

    n "And that red ooze is still dripping."

    jump LI_intro_noshiori

label speechhh2noshiori:

    scene village day:
        # Start at normal crop
        anchor (0.5, 0.5)
        xpos 0.5 ypos 0.5
        xanchor 0.5 yanchor 0.5
        zoom 0.6
        linear 0.15 zoom 0.61
        linear 0.08 xpos 0.51 ypos 0.49
        linear 0.08 xpos 0.5 ypos 0.5
        # Second stumble, more pronounced
        linear 0.12 zoom 0.63
        linear 0.10 xpos 0.48 ypos 0.52
        linear 0.10 xpos 0.5 ypos 0.5
        # Hold at max zoom
        linear 0.15 zoom 0.62
        pause 0.3

    n "Later, they drag you toward the shrine steps."

    n "The Elder holds your arm, but you can’t tell whose hand is trembling. Yours, maybe."

    show elder:
        xzoom -1
        zoom 0.8
        xalign 0.65
        ypos 0.1
    with dissolve

    "Elder" "Come. Let them see it clearly."

    n "You raise the armor."

    n "Sunlight catches the edges. Something {i}wet{/i} glistens, red trails slide off the plating."

    n "It's {color=#ff0000}red.{/color} Yamakui's blood is black."

    n "{atl=-#,#,fade_in_text~0.6}You lied.{/atl}"

    "Elder" "{b}Look well, all of you.{/b}{w=0.3}"

    "Elder" "{b}For years, we have lived in shadow.{/b}{w=0.2}"

    "Elder" "We boarded our windows, {i}whispered our prayers{/i}, and cremated ashes without names.{w=0.2}"

    "Elder" "{b}The Yamakui haunted us longer than memory itself.{/b}{w=0.4}"

    "Elder" "{b}And yet...{/b}{w=0.4}"

    "Elder" "{b}[persistent.player_name] climbed that mountain and came back.{/b} {i}Where no one else could.{/i}{w=0.3}"

    play sound "sfx/clap.mp3"

    n "The crowd claps, but they don't seem to be excited. Odd."

    stop sound

    "Elder" "{b}Never again will we light our fires with fear.{/b}{w=0.3}"

    "Elder" "{b}Never again will we sleep listening for footsteps.{/b}{w=0.3}"

    "Elder" "{b}Never again will our loved ones vanish under the Red Moon.{/b}{w=0.3}"

    "Elder" "{b}And never again will we... forget.{/b}{w=0.6}{nw}"

    pause 0.5

    n "....."

    with dissolve

    pause 0.3

    n "......"

    with dissolve

    pause 0.3

    n "Silence."

    with dissolve

    pause 0.3

    MC annoyed2 "....?"

    n "Wait, {w=0.2}shouldn't someone say something by now?"

    n "Someone always says something here. {blur}A girl’s voice{/blur} I think her name was--"

    n "No, I can't remember her..."

    n "She should be laughing with her sweet voice by now, but you don't hear it."

    n "{blur}Someone{/blur} should ask you to say a speech now, right?"

    n2 "The stringy one."

    n "..."

    n2 "Sounded shrill when devoured."

    n "I... {w=0.2}don’t remember that."

    n "...."

    n "Since no one asked you for a speech, it ends right there "

    with fade

    n "As you step down from the shrine, the crowd parts."

    n2 "{glitch}Hungry, hungry, hungry.{/glitch}"

    $ _prev_music_volume = _preferences.volumes["music"]

    $ decrease_music_volume(0.2)
    $ renpy.block_rollback()
    pause 0.2

    hide elder
    show woman at midleft :
        zoom 0.5
        ypos 0.2
    with dissolve
    show man at midright:
        zoom 0.5
        ypos 0.1
    with dissolve
    show darken
    with dissolve

    n "You can still hear the scared whispers of the villagers ringing in your ears."

    "Man" "The next Red Moon’s coming soon, isn’t it?"

    "Woman" "Think we’ll be safe this time?"

    "Man" "I don't know, but..."

    "Man" "...there’s nothing left to hide from. Right?"

    n "...Right?"

    n2 "AHahaHAHA."

    $ restore_music_volume()


    scene village day:
        zoom 0.5
    with dissolve

    n "You hear your name again."

    n "The armor still hangs limply from your hand."

    n "It feels...{w} heavier now. Somehow."

    n "And that red ooze is still dripping."

    #jump check_who_ded
    jump LI_intro_noshiori

label check_who_ded:

    if persistent.shiori_dies == True:
        jump LI_intro_noshiori
    elif persistent.hikaru_dies == True:
        jump LI_intro_nohikaru
    else:
        jump LI_intro_noyamato

label LI_intro_noshiori:

    n "But of course, you don't get far."

    show yam normal at yamato_zoom, left
    with dissolve
    pause 0.3
    show hik normal at hikaru_zoom, right
    with dissolve

    n "Because Yamato and Hikaru find you, they are your childhood friends--"

    n "Wait a second."

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xoffset -40
        yzoom 1.0
        xzoom 1.0
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.04 alpha 0.1 xoffset 12
        linear 0.04 alpha 1.0 xoffset 0
        linear 0.05 alpha 0.25 xoffset -14
        linear 0.04 alpha 1.0 xoffset 0
        repeat 3

        parallel:
            linear 0.07 alpha 0.1
            linear 0.12 alpha 0.0
        parallel:
            linear 0.09 xoffset 25
            linear 0.10 xoffset -22
            linear 0.05 xoffset 0
    pause 0.5
    hide shi

    n "Wasn’t there {glitch}someone else?{/glitch}"

    n "You remember the rice paddies, the muddy sandals, the laughters and the paper effigies--"

    n "Someone used to hang those paper effigies."

    n "There were four of you. Weren’t there {glitch}four?{/glitch}"

    play sound "sfx/walk grass.mp3"

    show yam annoyed
    with dissolve

    yamato "Tch. Look who finally shows up."

    show hik happy
    with dissolve

    hikaru "Welcome home, [persistent.player_name]-san."

    MC smug2 "Oi. That how you greet a hero?"

    yamato "Hero my ass. Ya ran off alone, idiot."

    MC smugcl2 "C’mon, tradition’s tradition. Oni slayer always goes solo."

    yamato "Fuckin' tradition..."

    n "Wait... {w}There should be another voice now, someone who usually tease Yamato..."

    n "No, wait... {w}Not Hikaru... {w}Hikaru's a quiet person."

    n "..."

    show hik worried
    with dissolve

    hikaru "...Don’t you forget something, [persistent.player_name]?"

    MC surprised2 "Huh? What, like a souvenir? I brought the armor, didn’t I?"

    hikaru "...I see."

    n "Hikaru’s voice lowers, eyes drifting slowly to the armor."

    show hik angry
    with dissolve

    hikaru "...It's rather small for something like the Yamakui, isn’t it?"

    MC nervous2 "...What?"

    show yam serious
    with dissolve

    yamato "Oi. What’s that supposed t' mean?"

    hikaru "...Forget it."

    n "The silence stretches again."

    n "Someone should occupy this space right now."

    n "Someone should've said something to fill the quiet."

    n "But no one else is there but the three of you."

    n2 "...She is {w}D E A D."

    show hik angry behind darken:

        zoom 0.231
        yoffset 460

        linear 0.4 xzoom -1 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
    pause 0.2
    hide hik with dissolve

    play sound "sfx/walk grass.mp3"
    pause 0.4
    stop sound fadeout 1.0

    n "Hikaru shrugs, turns and walks away."

    MC sad2 "...Hikaru?"

    show yam annoyed
    with dissolve

    yamato "Tch, whatever."


    hide yam with dissolve

    play sound "sfx/walk grass.mp3"
    pause 0.4
    stop sound fadeout 1.0


    n "Yamato follows. The empty space between you seems larger now."

    scene black
    show darken2
    with fade

    n "You look down at the armor, it feels heavier. Your fingers ache from holding it."

    n "You thought you cleaned it better."

    n2 "But we both know this is not mine."

    #jump beforesecondloop


label LI_intro_nohikaru:

    scene village day:
        zoom 0.5
    with dissolve

    n "But of course, you don’t get far."

    show shi normal at shiori_skipp:
        xalign 0.44
    with dissolve
    pause 0.6
    stop sound
    show yam normal at yamato_zoom, left
    with dissolve
    pause 0.3

    n "Because Shiori and Yamato find you."

    n "Your childhood friends. {w}Two of them?"

    show hik normal at hikaru_zoom, right:

        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.04 alpha 0.1 xoffset 12
        linear 0.04 alpha 1.0 xoffset 0
        linear 0.05 alpha 0.25 xoffset -14
        linear 0.04 alpha 1.0 xoffset 0
        repeat 3

        parallel:
            linear 0.07 alpha 0.1
            linear 0.12 alpha 0.0
        parallel:
            linear 0.09 xoffset 25
            linear 0.10 xoffset -22
            linear 0.05 xoffset 0
    pause 0.3
    hide hik

    n "{w=0.3}...Weren’t there more? {glitch}You cared for them more than the others...{/glitch} {w}didn't you?"

    n "Yes, you remember the rice paddies, muddy ankles, chasing cats and sparring...."

    n "Didn't one of you never talk much?"

    n "Who was it?"

    n2 "{blur}The mushy one.{/blur}"

    n "..."

    show shi happyblush
    with dissolve

    shiori "Ehehe~ [persistent.player_name]-samaaa~!"

    shiori "You came back~! I was so sure you'd get squished into pancake mochi~!"

    MC annoyed2 "Oi, rude. I’m not that easy to mash."

    show yam annoyed
    with dissolve

    yamato "Hnh. Coulda fooled me, dumbass. Leavin’ us without a word, ya promised ya'd bring me along!"

    MC smugcl2 "C’mon, you know how it is. Oni slayer tradition."

    yamato "Tradition’s for corpses."

    show shi annoyed at shakey:
        xalign 0.44

    shiori "Mou~ Yamato-kun's just mad he didn’t get to do anything cool~"

    yamato "Tch. I stayed behind t’guard the goddamn village."

    show shi smug
    with dissolve

    shiori "Did you now? Aren't you just sulky [persistent.player_name] didn't bring you along?"

    n "There should be someone cutting the conversation right now, someone who observe, someone who is--"

    n2 "--Tender "

    n "...What?"

    n2 "{cps=25}Soft around the ribs.{/cps}"

    n "..."

    show shi happy
    with dissolve

    shiori "Ne ne~ [persistent.player_name]-sama! You have to tell us what Yamakui looked like! Did it have fangs? Big claws? Did it talk?"

    MC nervous2 "Uh... Big. Yeah. Bloody. And...."

    hide shi happy
    show shi yansm:
        zoom 0.26
        yalign -0.60
        yoffset 0
        xalign 0.44
        parallel:
            easein 0.4 zoom 0.34 yalign -0.1
            easeout 0.4 zoom 0.26 yalign -0.60

    shiori "{sc=1}Beau~tiful?{/sc}"

    n2 "Hah."

    MC surprised2 "...What?"

    show yam angry
    with dissolve

    yamato "Oi, cut it out."

    show shi happy
    with dissolve

    shiori "What~? I’m just sayin’! Maybe Yamakui-sama's got a pretty face!"

    yamato "Damn Oni's got teeth, that's what."

    n "They bicker again, but something is missing. {i}Someone{/i} is missing."

    n "There was four of you. {i}You’re sure of it.{/i}"

    n "{w=0.3}...Right?"

    MC normal2 "Yeah, whatever they looked like now, it doesn't matter now."

    show yam annoyed
    with dissolve

    yamato "Tch. Ain’t like I’m complainin’. Ya came back in one piece."

    show shi surprised
    with dissolve

    shiori "Especially not clean like that~ {w}Not even a scratch on you!"

    show yam smug
    with dissolve

    yamato "Almost like ya ain’t fought anything at all, eh?"

    MC happycl2 "Ehh, just got Lucky's all!"

    yamato "What, damned oni bonked their head on a stone and dropped dead?"

    MC nervous2 "{k=-1}Something like that, yeah...!{/k}"


    n "Yamato and Shiori says nothing else, but their smile fades as yours does."
    scene black
    show darken2
    with fade

    n "You look down at the armor."

    n "You thought you cleaned it better."

    #jump beforesecondloop

label LI_intro_noyamato:

    scene village day:
        zoom 0.5
    with dissolve

    n "But of course, you don’t get far."

    show shi happy at shiori_skipp:
        xalign 0.44
    with dissolve
    pause 0.6
    stop sound
    pause 0.3
    show hik normal at hikaru_zoom, right
    with dissolve

    n "Because Shiori and Hikaru, your childhood friends find you."

    n "You grew up together, train together, sit under the same tree together, and chase each other on the paddy fields."

    n "There were always four sets of muddy shoes by the door."

    n "Wait, four?"

    show yam normal at yamato_zoom, left:
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.04 alpha 0.1 xoffset 12
        linear 0.04 alpha 1.0 xoffset 0
        linear 0.05 alpha 0.25 xoffset -14
        linear 0.04 alpha 1.0 xoffset 0
        repeat 3

        parallel:
            linear 0.07 alpha 0.1
            linear 0.12 alpha 0.0
        parallel:
            linear 0.09 xoffset 25
            linear 0.10 xoffset -22
            linear 0.05 xoffset 0
    pause 0.3
    hide yam
    with dissolve

    n "...Wasn’t there one more?"

    n2 "The loud one."

    n "..."

    n2 "All muscle, gamey."

    show shi happyblush
    with dissolve

    shiori "Ehehe~ [persistent.player_name]-samaaa~!"

    shiori "You came back~! You didn’t explode or get squashed or turned into dough!"

    MC annoyed2 "Oi, rude. I’m tougher than I look."

    show hik happy
    with dissolve

    hikaru "Welcome home, [persistent.player_name]-san."

    n "There should be someone grumbling now, that you left them to fight the Yamakui all by yourself..."

    n2 "That one stopped moving halfway down the throat."

    n "..."

    shiori "Ne ne~ Did Yamakui look like the legends? Big and scary? Lots of fangs? Or was it kinda cute~?"

    MC smug2 "I think it looked like it needed stabbing."

    show shi annoyed at shakey:
        xalign 0.44

    shiori "Muuuu, why are you so stingy, [persistent.player_name]???"

    show hik sad
    with dissolve

    hikaru "..."

    n "Silence falls when Shiori stops talking."

    n "Someone should have said something by now..."

    show shi happyblush at bounci:
        xalign 0.44

    shiori "You must be starving, [persistent.player_name]-sama. Shiori's gonna make alllll~ the food you want!"

    MC smugcl2 "{cps=35}How 'bout {/cps}{cps=5}venison?{/cps}"

    show shi surprised
    with dissolve

    shiori "Eh...? I don't think I have... {w}that...."

    show hik angry
    with dissolve

    hikaru "..."

    pause 0.5

    MC surprised2 "What is it?"

    hikaru "{w=0.5}...Do you feel like something’s missing?"

    MC nervous2 "Huh?"

    show hik angry
    with dissolve

    hikaru "I don’t know. I keep thinking there should be..."

    hikaru "{w=0.5}...four of us "

    MC sad2 "..."

    n "You-{w=0.1}I... {w}don’t know what to say."

    hikaru "...Forget it."

    show shi worried at shakey:
        xalign 0.44

    shiori "Ah, mou... Let's go eat before Hikaru's making odd theories again!"

    MC normal2 "Yeah, agreed."

    scene black
    show darken2
    with fade

    n "The fourth voice still doesn’t come."

    n "The armor clinks in your hand as you carry around with you behind Shiori and Hikaru."

    n "..."

    n "{cps=10}You wonder what venison tastes like, again.{/cps}"

    jump beforesecondloop

label beforesecondloop:

    scene white_bg
    with out_182

    show petals_dense
    show petals_scatter

    play music "noinomai.mp3"

    n "Time passes slowly when you're waiting."

    n2 "Hungry, hungry, hungry."

    n "You wake. You laugh. You sleep. You talk.{w=0.3} Repeat."

    n "You do all the things that safe people do."

    n "{i}So you must be safe.{/i}"

    n "But from what?"

    n "The village tries to be more bright and cheery, but there's always this heavy feeling in the air."

    n "They greet you kindly, politely. A bit... rehearsed, so to speak."

    n "And slightly afraid."

    n "No one speaks about the mountain anymore."

    n "Instead, they light incense more often, close their doors faster..."

    n "...and never once stare at you in the eye."

    n "You never ask why."

    n2 "No need."

    n "..."

    n "Meanwhile, the moon is starting to shift again."

    n "They say it only turns red a few times a year."

    n "{i}{blur}That’s when the Yamakui comes down.{/blur}{/i}"

    n "All the villagers can do now is waiting, wondering... If you've truly killed the Yamakui."

    n2 "{w=0.2}You know the answer.{w=0.2}"

    n "{k=-1}T-The Yamakui is dead.{/k}"

    n "There was a scream, a pool of blood, and... and... the weight of flesh, giving under your hand."

    n "You... You remember stabbing...."

    n "{blur}Me-You-We-It...?{/blur}"

    n "{w=0.15}Again. Again. Again.{w=0.2}"

    n2 "Again."

    n "You made sure a thousand times..."

    n "So the Red Moon shouldn’t mean anything this time."

    n "It should rise, and pass, and no one should vanish or be forgotten--"

    n "No one should{nw}"

    n2 "No one should remember."

    jump map

    return
