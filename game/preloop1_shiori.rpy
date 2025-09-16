############# LOOP 1 WHERE EVERYONE IS ALIVE ###########################
label loop1_shiori_mandatory1:

    $ loop1_shiori_mandatory1 = True

    ## always the first scene with shiori

    play music "Shiori.mp3"

    scene shrine day:
        zoom 0.5
    with fade

    n "The shrine looks the same as always."

    n "Stone steps, with red paint that flakes if you look close enough. Fresh, but actually... {w}old and tattered."

    n "Just like your whole village."

    play sound "sfx/bell_small.ogg"

    show shi normal at shiori_skipp2
    with dissolve

    shiori "{bt=1}[persistent.player_name]-sama~!{/bt}"

    shiori "Hehe, I just finished sweeping. You came at the perfect time!"

    MC normal "Yo! Shiori! Always so busy at the shrine, huh?"

    shiori "It’s your shrine too, you know. You could've helped."

    n "{i}Is it?{/i}"

    MC "Heh... {w}yeah. Guess I should come by more. Bet the gods missed me."

    shiori "They’d have to remember you first~"

    MC "Eh?"

    shiori "I’m joking~"

    shiori "It’s been so quiet, you know."

    shiori "Yamato comes once in a while just to curse at the gods. Hikaru just comes to pray, but won't stay to eat my bento!"

    shiori "They don’t really talk much anymore."

    MC "...That’s kinda weird. They used to, didn’t they? I mean, we all used to hang out together, right?"

    shiori "We did. Back then."

    shiori "The four of us."

    n "You nod before you even think."

    MC "Right, yeah. We always used to hang out by that, uh... {w=0.2}that rock thing. The... {w}{i}Dosojin{/i}?"

    shiori "Mhm~"

    MC "And we had those snacks... {w=0.2}What were they? Rice cakes?"

    shiori "They were pickled plums, actually."

    MC "Whoops, okay. {w=0.2}Right. {w=0.2}Salty stuff. I remember."

    n "{i}Do you?{/i}"

    shiori "It’s strange how different things feel now."

    shiori "When you're gone, Yamato-kun was yelling about how you’d get yourself killed. Hikaru-san wouldn’t stop writing charms for your safety."

    shiori "But now? They're being weird with you."

    MC "Heh... maybe they're just jealous I did it. Yamakui’s gone, after all."

    shiori "Sure. Maybe that’s it."

    n "She twirls the broom in her hand as she looks up to the ceiling, clearly trying to remember something."

    MC "I mean, it’s not like I wanted all the attention, y’know? I just-{w=0.2}I did what I had to."

    shiori "And you came back. That’s all that matters."

    MC "Of course I do. I promised you, didn’t I?"

    n "{i}Did you?{/i}"

    n "{size=*0.95}What exactly did you promise her?{/size}"

    n "To return? {w=0.3}To keep visiting? {w=0.3}Or..."

    show shi normal:
        zoom 0.5
        xalign 0.4
        yalign 0
        yoffset 0   
        xzoom 1.0
        yzoom 1.0

        ease 0.5 xzoom -1.0
        ease 0.5 xalign 0.35

    n "Shiori just nods and turns away, stepping toward the shrine door."

    shiori "Will you stay a while? Shiori's really lonely..."

    shiori "I’ll make tea, then we can pray together! Just like before~"

    MC "Yeah. {w=0.2}Sure. {w=0.2}I’ve got time. Feels like forever since we did that."

    n "{alpha=0.8}The incense grows thick once you've stepped in behind Shiori. The smell hits the back of your nose immediately, overwhelming...{/alpha}"

    n "{i}You didn’t remember it being this sharp...{/i} {w=0.2}Or maybe that’s just how memory works?"

    n "{size=*0.95}...Or maybe {atl=-#,#,fade_in_text~0.5}not all the memories are yours.{/atl}{/size}"

    n "Maybe it's fine, as long as Shiori remembers the same thing."

    n "{size=*0.95}{i}...That should be enough.{/i}{/size}"

    #return

label loop1_shiori_mandatory2:

    scene black
    with fade

    ## this happens if you visit the shrine at night

    scene shrine night with in_182:
        zoom 0.5
    

    play music "Night.mp3"

    n "The shrine is still open. Even this late, the doors remain unbarred, and the smoke from the incense still swirls."

    MC normal "They never put it out, huh..."

    n "People say the gods watch this place most closely when the moon turns red."

    n "They say it’s the last place the Yamakui dares enter."

    show shi normal at shiori_skipp2
    with dissolve

    shiori "...[persistent.player_name]-sama?"

    shiori "Why are you here at this hour?"

    MC "I can't sleep, so thought I’d check on you. Still awake, huh?"

    shiori "Yes... I'm still in the middle of lighting all the lanterns."

    MC "Why?"

    shiori "..."

    shiori "In case someone needs to find their way."

    MC "Who?"

    shiori "Well, it can be anyone~"

    MC "And the flowers? You’ve been leaving more of them lately... {w=0.2}Who are they for?"

    shiori "The dead. Everyone who got eaten."

    n "You stare at the gravestones, there are no names written on them."

    MC "Whose graves are those?"

    shiori "I-I don't remember their names."

    $ renpy.music.set_volume(0.7)
    pause 0.2
    $ renpy.music.set_volume(0.6)
    pause 0.2
    $ renpy.music.set_volume(0.5)
    pause 0.2
    $ renpy.music.set_volume(0.4)
    pause 0.2
    $ renpy.music.set_volume(0.3)
    pause 0.2
    $ renpy.music.set_volume(0.2)
    pause 0.2
    $ renpy.music.set_volume(0.1)
    pause 0.2

    show darken
    with dissolve
    play sound "sfx/suzu.mp3"

    MC "Wait, really?"

    n "Funny, because you {i}don't remember{/i} any names either."

    n "Surely someone was taken by the Yamakui. {w=0.2}That's why you were sent to kill it, right? {w=0.2}That's why everyone is afraid."

    n "There weren't remains, but bloodstains... {w=0.3}{alpha=0.7}evidence of something being mauled.{/alpha}"

    n "But you {size=*0.95}can't place a name.{/size}"

    n "Who was taken last? {w=0.2}A child? {w=0.2}A friend? {w=0.5}{i}{sc=5}Your parents?{/sc}{/i}"

    n "Because you came back home and there's no parents at home. {w=0.2}{cps=12}Did they get eaten, too?{/cps}"

    MC "...Can you remember anyone?"

    shiori "The elder said that everyone who got eaten by Yamakui {alpha=0.7}{cps=10}got wiped off from everyone's memory...{/cps}{/alpha}"

    MC "Or maybe they were {glitch=15}{i}never there to begin with?{/i}{/glitch}"

    play sound "sfx/stomp.wav"

    hide shi normal
    hide darken
    show shi normal:
        zoom 0.5 
        xalign 0.4 
        yalign 0 
        yoffset 0 
        xzoom 1.0 
        yzoom 1.0

        parallel:
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
            easein 0.08 yoffset -10
            easeout 0.08 yoffset 0

        parallel:
            easein 0.1 yzoom 0.95 xzoom 1.05
            easeout 0.1 yzoom 1.0 xzoom 1.0
            easein 0.08 yzoom 0.97 xzoom 1.03
            easeout 0.08 yzoom 1.0 xzoom 1.0
    with vpunch

    shiori "[persistent.player_name]-sama, that is a cruel thing to say...!"

    MC "Oi, oi. I didn't mean it like that, Shiori-chan.."

    n "You actually did."

    MC "But, anyway, if they didn't exist... Then who are you offering for?"

    shiori "..."

    MC "Shiori?"

    n "Suddenly, the smell of insence makes you want to gag."

    shiori "They’re for the... {w}ones who are gone, like I said."

    n "She says nothing else, and you decide it's not worth pressing."

    n "{k=-1}But the questions linger.{/k}"

    n "{cps=39}Graves without names.{/cps}"

    n "{cps=30}The shrine staying open even when no one prays.{/cps}"

    n "And... {w=0.2}{glitch=1.1}offerings{/glitch} without a god to receive it."


    #return

    $ loop1_shiori_mandatory2 = True
    #return

label loop1_shiori_mandatory3:

    $ loop1_shiori_mandatory3 = True
    ## day scene shrine (scene only appears at day 4/5)

    n "This morning, you come into the smell of rot lingering on the shrine."

    n "It reminds you to the smell of the mountains when you left Yamakui's lair."

    show shiori normal at midright

    shiori "Ah, [persistent.player_name]-sama~"

    shiori "You’re just in time! I was preparing the offering."

    MC "Heh. Lucky me, huh? Need help?"

    shiori "Always~"

    n "Shiori's sleeves are damp. You see a dark smear near her elbow."

    shiori "Can you hand me the insides of that bowl?"

    MC "This one?"

    n "You reach out, your fingers press into something {cps=10}{alpha=0.8}cold{/alpha}{/cps} and soft."

    n "It {sc=4}gives{/sc} slightly when you squeeze further."

    ## SQUELCH, SQUELCH

    n "The texture is the same as an {size=*0.9}{i}overripe fruit{/i}{/size}."

    ## SQUELCH, SQUELCH

    n "Then a {color=#aa0000}{cps=12}sticky red liquid{/cps}{/color} wells up around your thumb as you scoop it to your hand."

    n "It's {cps=8}{alpha=0.7}warm...{/alpha}{/cps} as warm as Shiori's hand when you brush against it as you hand the thing to her."


    MC "Fresh?"

    shiori "Mm. It should be."

    MC "You butcher this yourself?"

    shiori "Ara~ You think little ol' me have the strength to do it?"

    n "There's no right answer to that."

    n "She lays out four flat plates.  The red liquid seeps out and follows the grain."

    n "But every cut is perfect."

    show shiori neutral at midright

    shiori "Okay! So all we have to do is eat the offering and the gods will listen to our prayers."

    shiori "...Supposedly."

    MC "What are the two other plates for?"

    shiori "It's for Yamato and Hikaru! But, ummm.. They said they can't come so might as well be just the two of us."

    play sound "sfx/slurp.ogg"

    n "She lifts a strip and {sc=6}bites{/sc} straight through it."

    # plop sfx

    n "There’s a {size=*0.95}{i}popping{/i}{/size} sound as something hollow inside ruptures."

    n "A {cps=14}{color=#ff0000}{outlinecolor=#660000}wet squelch{/outlinecolor}{/color}{/cps} follows, her lips sliding shut over the offering."

    n "She {k=2}chews{/k} once, then swallows {alpha=0.8}{i}effortlessly{/i}{/alpha}."

    ## she smiles at you afterwards

    MC "Alright then."

    n "You pick up a piece. The surface seems {alpha=0.7}slick{/alpha}. A thick mucous sheen coats it, and it {sc=4}slides{/sc} through your fingers once before you get a grip."

    MC "...Itadakimasu."

    play sound "sfx/squelch2.ogg"

    n "You put it in your mouth."

label chew_loop:
    menu:
        "Eat":
            n "It’s already on your tongue. You chew before you think."
            jump chew_loop
        "Chew":
            n "It resists your teeth, but eventually gives. You feel something inside it burst like a blister."
            jump chew_loop1

label chew_loop1:

    menu:
        "Chew":
            n "You crush it again. There’s a snap, then a gush of thick, gluey fluid over your tongue."
            jump chew_loop1
        "Swallow":
            n "You gulp it down. It catches halfway, then slides easily. You feel it the whole way down."
            jump gulgulp

label chew_loop2:

    menu:
        "Chew":
            n "You keep chewing. It stretches and shreds coil between your teeth."
            n "There’s something rubbery stuck behind your molars. You keep working it, gagging slightly."
            jump chew_loop2
        "Swallow":
            n "It’s gone."
            jump gulgulp

label gulgulp:
    MC "...Not bad. Kind of chewy, though."

    shiori "..."

    MC "What?"

    shiori "I thought you were going to puke."

    MC "Hah. I’ve had worse during night guard duty."

    shiro "Ah-I see."

    play sound "sfx/drip.ogg"

    n "Another strip slides off the tray, leaving a smear behind."

    MC "So, what is it? Boar? Deer?"

    shiori "{cps=14}{alpha=0.7}{sc=4}Wouldn't you like to know, [persistent.player_name]-sama.{/sc}{/alpha}{/cps}"

    MC "Eh, just curious is all."

    play sound "sfx/squelch1.ogg"

    n "You lift another even though Shiori doesn't ask you to. It slurps, plaps, you don’t even attempt to chew on this one."

    play sound "sfx/slurp.ogg"

    n "It slides down with a thick gulp."

    n "Shiori watches you eating, staring. Her mouth still open, with a strand of red hanging from her lip."

    n "She wipes it with blood under her fingernails."

    n "There's almost nothing left on the bowl."

    n "But you’re not even full."

    return

label loop1_shiori_mandatory4:

    # night at the shrine

    n "....."

    n "There's no one around when you walk in."

    n "Where's Shiori?{nw}"

    ## dongggg sfx false jumpscaree

    MC "--!?"

    shiori "Ehehe~"

    shiori "Did I startle you, [persistent.player_name]-sama?"

    MC "Y-yeah, kinda! You didn’t give me any warning--"

    shiori "Hikaru said ceremonial bells drive evil spirits away."

    shiori "Sooo I'm just checking."

    MC "...Checking?"

    shiori "If there’s anything evil around, of course! Since the red moon is coming, and all!"

    shiori "If I find one, I’ll banish it~"

    n "She raises the bell again."

    MC "Wait, maybe we don’t have to--"

    shiori "Shhh."

    shiori "Let’s begin~"

    n "She closes her eyes."

    n "The wind stills. Even the bugs stop chirping."

    play sound "sfx/bell_ceremony.ogg"

    n "She rings the bell again. It feels closer this time, even though she's standing the same distance away."

    window hide
    $ renpy.pause(0.5)
    window show

    show expression Text("山の鬼よ", style="jojo_text") at jojo_scatter1
    show expression Text("立ち去れ、立ち去れ！", style="jojo_text") at jojo_scatter2
    show expression Text("深淵に、闇に帰れ", style="jojo_text") at jojo_scatter3
    pause 2.0

    n "She chants clearly, loudly. The bell in her hand sways slightly with her rhythm."

    ## multiple chanting, the words are shaking at the screen as she chants

    show expression Text("山の鬼よ", style="jojo_text") at jojo_attack4
    show expression Text("立ち去れ、立ち去れ！", style="jojo_text") at jojo_attack5
    show expression Text("深淵に、闇に帰れ", style="jojo_text") at jojo_attack6


    MC "{cps=8}{sc=6}{color=#ff0000}Ghh--{/color}{/sc}{/cps}"

    n "The sky overhead is very still, not even a breeze through the trees."

    n "No monsters, nothing comes out from the bushes."

    shiori "{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{bt=6}Oni of the mountains,{/bt}{/outlinecolor}{/color}{/size} {w=0.2}{fast}{size=+8}{shader=jitter}{color=#ff0000}begone!{/color}{/shader}{/size}"

    shiori "{cps=14}{alpha=0.8}{vert}Back to the depths.{/vert}{/alpha}{/cps}{w=0.3}{size=+10}{sc=5}{color=#aa0000}Back to the dark!{/color}{/sc}{/size}"

    n "Shiori chants even louder. {w=0.3}The insects have gone quiet."

    MC "{cps=7}{alpha=0.7}{i}Shiori--!{/i}{/alpha}{/cps}"  # grimacing faaaaaceeee
    shiori "Eh?"

    MC "I think that's enough, no evil spirits are here tonight."

    MC "See? Nothing "

    shiori "You're right, I don’t sense anything~"

    MC "Yeah, so you can stop now."

    shiori "You sure? You look like you saw something just now, [persistent.player_name]-sama."

    MC "I'm--fine."

    shiori "Mm~ I’m glad."

    shiori "Because if there *was* something evil nearby..."

    shiori "I’d have to do a lot more than ring a bell, y'know?"

    n "The bell swings gently in her hand, but she doesn't ring it this time. instead, she waits."

    ## uncomfortable silence until the next line, maybe add a loong pause....

    n "But nothing comes out "

    return


label loop1_shiori_mandatory5:

    n "Location : Forest Day"
    $ loop1_shiori_mandatory5 = True
    ## forest bg

    n "She’s already sitting there when you arrive."

    n "The sakura tree hasn’t bloomed in years."

    n "You used to say it would, one day."

    n "You said a lot of things, didn't you?"

    shiori "Do you remember the day before they sent you off to the mountain and we said our goodbyes here?"

    MC "Heh... yeah! Right here under this old tree. I remember...."

    menu:
        "We all cried.":
            MC "We all cried because you all think I wouldn't make it."
            shiori "Mhm~ We did."
        "We all said a prayer.":
            MC "We all said a prayer for my success. I think you were the one who suggested it."
            shiori "Ehehe~ Yeah. That sounds right."

    n "She nods, still looking at the sky."

    shiori "And Yamato said something dumb again back then, right?"

    menu:
        "He said he wanted to come with me.":
            MC "He wanted to come too, didn't he? But I told him not to, 'cause no one's gonna protect the village when I was gone."
            shiori "Yeah~"
        "He was crying.":
            MC "The stupid oath actually cried because he was so sure I was gonna die, right?"
            MC "He made a pretty ridiculous face, too. Didn't know Yamato could cry like that."
            shiori "Hehe~ I remember something like that..."

    n "You’re smiling, and your chest feels warm."

    n "Isn’t this what it’s supposed to feel like?"

    shiori "...And you."

    shiori "You said you’d protect us."

    menu:
        "I said I'd protect everyone. Always.":
            MC "Yeah... I stood right there and said it, didn’t I? That I’d protect everyone."
            MC "And I did, right? When I slayed the Yamakui!"
            shiori "Did you~?"
        "I promised you I'll be back.":
            MC "I promised you that no matter what happens, I'll come back to you, Shiori."
            MC "That's what's keeping me here. Right beside you."
            shiori "..."


    shiori "Yeah, that was a very pleasant day, [persistent.player_name]"

    shiori "{cps=62}{alpha=0.8}Except...{/alpha}{/cps}"

    shiori "{alpha=0.7}{sc=3}It didn’t happen like that.{/sc}{/alpha}"

    MC "{cps=9}{alpha=0.7}Huh?{/alpha}{/cps}"

    shiori "{cps=14}{vert}You left without saying goodbye to us, [persistent.player_name].{/vert}"

    shiori "{cps=12}{alpha=0.7}We only knew because the village elder told us you left. Said you did it on purpose so no one would come after you.{/alpha}"

    n "Did you mixed your memories up? What's happening?"

    MC "{sc=4}{alpha=0.7}N-no! That’s not-- I  said goodbye to you, at least... Right, Shiori?{/alpha}{/sc}"

    shiori "{cps=52}{glitch=10}[persistent.player_name], you’re lying. I remember more than anyone else.{/glitch}"

    shiori "{alpha=0.8}Don't try to make things up.{/alpha}"

    MC "{cps=59}{sc=3}{alpha=0.7}I-- I just--{/alpha}{/sc}"

    n "Guess you can't get yourself out of this situation."

    shiori "{fi=2.0}But that's okay! If you lie again tomorrow.... or if something happens during the red moon... I'll still be here for you.{/fi}"

    shiori "{cps=52}{alpha=0.7}Even if Yamato and Hikaru told me otherwise.{/alpha}"

    n "You extend your hand, about to grab Shiori's wrist as she moves away."

    n "What are you doing? Stop it. Stop."

    shiori "{cps=53}{alpha=0.6}I should go. It’s getting late~{/alpha}"

    shiori "{fi=1.8}Tomorrow’s the Red Moon, [persistent.player_name]-sama.{/fi}"

    shiori "{sc=3}{alpha=0.8}Let’s be honest then, okay?{/alpha}{/sc}"

    n "She walks away, as your body freezes in place."

    MC "…"

    MC "Shit." ## wrong expression here

    ## If you see this breakdown scene, you are entering Shiori's route.

    scene bg room_night with fade
    play music "bgm/mind_break.ogg" fadein 1.5

    n "You run."

    play sound "sfx/steps_wood.ogg"

    n "You slam the door on your house and scrambles towards the armor you brought back."

    n "It’s still here, right where you left it."

    n "It's still wrapped up like a corpse."

    play sound "sfx/cloth_rustle.ogg"

    n "You rip the cloth away with trembling hands."

    n "Indeed, it is too small for a being such as the Yamakui-{nw}"

    mc "{b}I killed it.{/b}"

    mc "{color=#ff3333}I killed that kuso-yarou up there.{/color}"

    mc "{size=+4}{sc=5}It screamed. It fucking screamed, gods damn it, it *died.*{/sc}{/size}"

    play sound "sfx/metal_hit.ogg"

    n "You kick the chestplate. The noise it makes is wet."

    mc "I remember how it sounded like, how it talked like, how it looked like-"

    mc "{fast}{sc=4}{color=#bb1111}You.{/color}{/sc}"

    n "Me."

    mc "{b}...You said I was the hero.{/b}"

    mc "You said it. Now say it again."

    mc "{b}...Why the hell won’t you say it?{/b}"

    n "..."

    mc "{sc=3}You’ve been here this whole time.{/sc}"

    mc "Narrating every step, whispering like a kami stuck in my spine."

    mc "{size=+2}But now? Now you shut up?{/size}"

    mc "{sc=3}...You liked watching me squirm, didn’t you?{/sc}"

    mc "So what is it now? Scared? Huh?"

    play sound "sfx/heartbeat_deep.ogg"

    n "..."

    mc "{size=+2}You should be.{/size}"

    mc "I did what you asked. I followed your damn story."
    play sound "sfx/flesh_pull.ogg"

    n "Your hand slides down the chestplate-{nw}"

    mc "{sc=5}There you are.{/sc}"

    mc "...You never said what to do once the screaming stopped."

    n "..."

    mc "All right, if that's how you wanna play."

    n "..."

    mc "{b}Let's play for a little bit more.{/b}"

    n "...."

    ## uncomfortable silence

    mc "...Oi."

    mc "{sc=3}You still there?{/sc}"

    mc "{sc=4}Hey?{/sc}"

    mc "Don’t you wanna finish your pretty little story?"

    n "..."

    mc "{b}Heh.{/b}"

    mc "{b}You'd better, or I'll finish it for you.{/b}"

    n "Wait, what are you-"

    mc "{size=+6}{color=#993333}{shader=jitter}Don’t look away now.{/shader}{/color}{/size}"

    window hide
    $ renpy.pause(2.0)
    window show

    centered "{size=+10}{color=#FF2222}THE RED MOON IS COMING{/color}{/size}"

    stop music fadeout 3.0

    return
