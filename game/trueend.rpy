label truend:

    $ ysword = False
    $ hmask = False
    $ hsword = False

    scene shrine night:
        zoom 0.5

    # Show all three characters
    show hik normal at hikaru_zoom, right

    show yam normal at left:
        xalign 0.25
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    with dissolve

    n "They called this meeting without you."

    n "But you let them, anyway."

    play music "Somber.mp3"

    show hik serious
    with dissolve
    hikaru "Yamato. Shiori. I... {i}need{/i} you to listen."

    show yam annoyed
    with dissolve
    yamato "Oi, what’s this ‘bout draggin’ us here in the middle o’ the damn night?"
    yamato "Ya better make it good, Hikaru."

    show shi surprised
    with dissolve
    shiori "Yaaawn~ I only came because you said this is important, Hikaru-san~"

    show hik worried
    with dissolve
    hikaru "...It is about [persistent.player_name]."


    show yam serious
    with dissolve
    yamato "So ya thinkin' what I'm thinkin'. [persistent.player_name]'s hella odd lately."

    show hik sad
    with dissolve
    hikaru "Yes. More than off, even... I think it's {i}not really{/i} [persistent.player_name] that came back from the mountains."

    shiori "Huh? What do you mean, Hikaru-san?"

    show hik sad
    with dissolve
    hikaru "Listen... I... have a confession."

    pause 1.0
    hikaru "I'm with [persistent.player_name]. For a long time, more than a year."

    show yam surprised
    with dissolve
    yamato "With...?"

    show shi happyblush
    with dissolve
    shiori "As in {i}in love{/i}, Yamato~"

    show yam shocked
    with dissolve
    yamato "Wha--"

    show yam rage
    with vpunch
    yamato "{sc=7}WHAAAAAAAAAAAAAAAAAAT!?{/sc} The hell did ya just say?!"
    yamato "Ya mean t’tell me, all this time... you and that idiot were--?"

    show hik sad
    with dissolve
    hikaru "Yes. [persistent.player_name] was my partner. My... {i}lover.{/i}"

    show shi smug
    with dissolve
    shiori "Ehehe... I had my suspicions~"
    shiori "You two were always soooo awkward around each other, all blushy and stuff. I thought maybe..."

    show yam annoyed
    with dissolve
    yamato "Tch... t’hell... Why the {b}secrets{/b}, then?"

    hikaru "Because of my father, the man who was branded a traitor. No one would accept me with [persistent.player_name]."

    show hik sad with dissolve
    hikaru "So we kept it hidden, even from you guys."
    hikaru "I'm... sorry about that."

    show hik worried with dissolve
    hikaru "So... That's why I know it's {i}not{/i} [persistent.player_name], because [persistent.player_name] didn't even know we're together."
    hikaru "Because only the two of us are supposed to know."
    hikaru "This... thing wears their face, but it is {color=#b10000}{i}not{/i}{/color} [persistent.player_name]."

    show yam serious with dissolve
    # Shiori stays normal for transition
    shiori "...Then what will you do, Hikaru?"

    show hik serious with dissolve
    hikaru "I think... we cannot ignore it anymore."
    hikaru "Or we'll all die."
    hikaru "My theory... That [persistent.player_name] may be {i}possessed{/i} by Yamakui. Or worse, [persistent.player_name]'s body has been stolen."

    show yam annoyed with dissolve
    yamato "Tch... fuck... Don’t say it like that, Hikaru."
    yamato "But... yeah. I been thinkin’ the same damn thing. Somethin’s off. Ain’t just me bein’ jealous."

    show shi sad with dissolve
    shiori "...I thought so to."
    shiori "But... I don't want to stop it."

    show yam surprised with dissolve
    n "{cps=14}What? Did she just--?!{/cps}"

    show yam angry with dissolve
    yamato "...Oi. The hell did ya just say, Shiori-chan?"

    show hik surprised with dissolve
    hikaru "{i}Shiori-chan...?{/i}"

    show shi worried with dissolve
    shiori "Because I think it's not that bad!"
    shiori "Do you remember that night where I was missing and you guys were looking for me?"

    stop music fadeout 1.0

    show shi sad
    show darken
    with dissolve
    shiori "{i}I was left in the forest that night... tied up, wrists bleeding, gagged. I was about to be sacrificed.{/i}"
    shiori "I think... it was the old priest? Or maybe someone else. I forgot their face."
    shiori "{glitch=7}But the Yamakui came and spared me, ate the priest instead!{/glitch} Even though I was the easier meal!"

    show yam shocked with dissolve
    n "Bound in the forest? As a child...?"

    show shi happyblush with dissolve
    shiori "That’s when I knew. Yamakui only eats {i}bad{/i} people."
    shiori "I believe that it spares the ones it loves."

    hide darken
    with dissolve

    play music "Tense.ogg"

    play sound "sfx/stumble.mp3"

    show yam rage with vpunch
    yamato "{b}Ya’ve lost it.{/b} Ya’ve completely lost it, Shiori!"

    show hik panic with dissolve
    hikaru "{i}Shiori-chan, why didn't you tell us!?{/i}"


    show shi yansmbl with dissolve
    shiori "{glitch=8}Well, you know whoever that was eaten got forgotten, right?{/glitch} You'd just say I was crazy!"

    show hik shocked with dissolve
    hikaru "Still, that's insane..."

    show yam angry with dissolve
    yamato "Tch... I don’t get you, Shiori. How the hell can ya defend somethin’ that’s been eatin’ us alive for generations?"

    show hik serious with dissolve
    hikaru "{b}You knew it ate the villagers one by one!{/b} You cannot keep pretending it is anything but a monster."

    show shi smug with dissolve
    shiori "Ehehe... pretend? I’m not pretending, Hikaru-san~"

    show shi happyblush with dissolve
    shiori "{i}When no one else saved me, Yamakui did.{/i} That’s all that matters to Shiori~"

    show yam rage with vpunch
    yamato "Ya think sparin’ ya one time makes it good?!"

    yamato "{color=#b10000}It’s eaten people, Shiori!{/color} Real people. Families, neighbors, friends. What part o’ that don’t ya get?!"

    show hik shocked with dissolve
    hikaru "Even if it spared you, that doesn’t erase the rest...!"

    show hik worried with dissolve
    hikaru "If we do nothing, it will come for all of us!"

    play sound "thud.mp3"

    show shi annoyed with vpunch
    shiori "Mouu~ You two don’t understand anything!"

    play sound "thud.mp3"

    show shi angry with vpunch
    shiori "You have never been saved by Yamakui-sama!"

    show yam angry with dissolve
    yamato "{sc=1}Yer insane.{/sc}"

    show hik sad with dissolve
    hikaru "...Shiori-chan. Please."

    show shi annoyed with dissolve
    shiori "No. I won’t help you kill it. {w}I won’t."

    n "That playful lilt drops, just for an instant."

    show shi annoyed with dissolve
    shiori "{cps=13}If you want to fight it, do it without me.{/cps}"
    stop music fadeout 1.0

    show shi angry:
        zoom 0.26
        xanchor 0.5
        xalign 0.5
        yalign -0.60
        xzoom 1.0
        yzoom 1.0
        alpha 1.0

        linear 0.4 xzoom -1 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        linear 0.2 zoom 0.13 alpha 0.0

    n "And with that, she turns away, dragging her feet as if daring them to call her back."
    n "{i}The shrine doors creak as Shiori disappears into the dark.{/i} The silence left behind is unbearable."

    show yam ngh with dissolve

    yamato "God damn it..."
    hikaru "..."

    show hik serious
    with dissolve
    hikaru "No, let's try again tomorrow, Yamato."
    hikaru "We can still save her, she's not too far gone."

    yamato "What are we gonna do, then?"
    hikaru "...I think I have a plan."


    scene black

    with fade

    n "Hikaru and Yamato returns again to the Shrine as Shiori is absentmindedly sweeping dirt."

    play music "Hope2.mp3"

    scene shrine day:
        zoom 0.5

    show hik normal at hikaru_zoom, right
    with dissolve

    show yam normal at left:
        xalign 0.25
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    show hik worried with dissolve
    hikaru "Shiori-chan--"

    show shi annoyed with dissolve
    shiori "What now?"

    show hik sad with dissolve
    hikaru "We were all friends, weren't we? The four of us."
    hikaru "{i}Don't you forget all about{/i} [persistent.player_name]?"

    n "Hikaru hands her a letter written by... [persistent.player_name]. You.{w} Me?"

    show hik sad with dissolve
    hikaru "Remember these letters and {i}whishes{/i} we used to write down when we were kids?"
    hikaru "And this scarf--"

    show darken
    $ decrease_music_volume(0.2)
    $ renpy.block_rollback()

    n "The red scarf...."
    n "{cps=13}I remember that...{/cps}"
    n "I was wearing that, when I--"

    pause 1
    n "{cps=10}Wait.{/cps}"

    hide darken

    $ restore_music_volume()

    show hik panic with dissolve
    hikaru "{sc=1}We were best friends, weren't we!?{/sc} The Yamakui ate our friend!"
    hikaru "How could you say that Yamakui only ate the bad people!?"

    show yam angry with dissolve
    yamato "Oi, Shiori! Open yer damn eyes already!"
    yamato "Ya think this monster’s some savior? Some lover? Tch... {b}bullshit!{/b}"

    play sound "thud.mp3"
    with sshake

    n "Yamato slams his fist into the shrine pillar, making Shiori {glitch=7}jolt.{/glitch}"

    show yam rage with dissolve
    yamato "Who the hell protected ya from bullies, huh? Who stood between ya an’ the bigger kids? It was [persistent.player_name]!"

    show hik worried with dissolve
    hikaru "{i}Our friend who never hurt anyone, Shiori-chan. Please, just try to remember.{/i}"

    show yam serious with dissolve
    yamato "Yeah. That bastard didn’t deserve to die!"

    show shi sad with dissolve
    shiori "..."

    n "{i}Shiori’s lips tremble. Her eyes dart between them. For once... she is speechless.{/i}"

    show shi surprised with dissolve
    shiori "I--"

    show hik serious with dissolve
    hikaru "Please. Shiori-chan. Don’t let your feelings blind you."
    hikaru "Deep down, you already know the {i}truth{/i}."

    show shi sad with dissolve
    shiori "I know that [persistent.player_name]'s not a bad person..."

    show hik sad with dissolve
    hikaru "..."
    hikaru "No matter what you choose in the end, we're still going to kill it."
    hikaru "I won’t watch this... {w}this monster wear [persistent.player_name]'s face and kill everyone."

    show yam angry with dissolve
    yamato "Tch... damn right. I ain’t sittin’ back either."

    show hik serious with dissolve
    hikaru "If you still consider [persistent.player_name] your friend... Then you'll come with us."

    show shi sad with dissolve
    shiori "...."

    show shi worried with dissolve
    shiori "..Fine, I'll help."
    shiori "But only because I think we can save both Yamakui and our friend."

    scene shrine night:
        zoom 0.5
    show darken2
    with fade

    show hik normal at hikaru_zoom, right
    with dissolve

    show yam normal at left:
        xalign 0.25
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    n "Later, Shiori brings them to where old documents reside."

    show shi worried with dissolve
    shiori "I think we can start from these if we want to find clues about the Yamakui."
    shiori "I was looking into the Yamakui but someone... {w=0.1}tried to stop me from it."

    show yam annoyed with dissolve
    yamato "Tch. Half of it’s rotted. What’s it say?"

    show shi sad with dissolve
    shiori "Something about... {w}famine, and long winters when nothing grew.'"
    shiori "{i}It says... outsiders were 'invited' to the village.{/i} But... no one was ever recorded leaving."

    show hik serious with dissolve
    hikaru "Did they stay in the village?"

    show shi worried with dissolve
    shiori "I don't think so... It says 'offerings made at the altar, so our children would not starve.'"

    show yam angry with dissolve
    yamato "Damned sacrifices."

    show shi surprised with dissolve
    shiori "There’s more. Look here. The priests wrote... {w}'Kami-sama grew silent after.'"
    shiori "'We are forever condemned from their light'"

    show hik sad with dissolve
    hikaru "{i}The kami-sama turned their face away.{/i}"

    show shi normal with dissolve
    shiori "'And a new god rose from the mountains'"

    show hik shocked with dissolve
    hikaru "{b}...Yamakui.{/b}"

    show shi sad with dissolve
    shiori "That was all I managed to find, I'll look into it more..."

    show yam annoyed with dissolve
    yamato "Tch... So all this is just a punishment for what our damned ancestors did?"

    show shi sad with dissolve
    shiori "..."

    show hik normal with dissolve
    hikaru "I think we'll stop here for now. Shiori, keep trying to look into it."
    hikaru "Yamato, we'll try to find a way out of the village."

    show yam surprised with dissolve
    yamato "Huh? But there ain't a way out, the elders said--"

    show hik serious with dissolve
    hikaru "My father went out to look for it. And even though no one knew what happened to him..."

    show hik sad with dissolve
    hikaru "Since everyone still remembers him, it's possible he didn't get eaten by the Yamakui."

    show yam sad with dissolve
    yamato "..."

    show yam serious with dissolve
    yamato "{i}Fine.{/i}"
    yamato "We'll go first thing in the morning."


    with fade

label mist_fall:

    scene cliff
    show particleFog with dissolve:
        ypos 0.4
    with fade

    show hik normal behind particleFog:
        zoom 0.31
        xalign 0.75
        yalign -0.09
        xanchor 0.5
        yoffset 50
        xzoom 1.0
        yzoom 1.0

    show yam normal behind particleFog:
        zoom 0.29
        xalign 0.25
        yalign -0.04
        xanchor 0.5
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    n "The mountain path should’ve led out. But the farther they walk, the whiter the air becomes."
    n "A thick mist is swallowing everything. Rocks vanish, trees blur, even sound feels muffled and strange."

    show yam surprised with dissolve
    yamato "{sc=1}Oi...{/sc} this ain’t right. I walked this trail before. Where the hell’s the gate?"

    show hik worried  with dissolve
    hikaru "It should be here. The road leads straight--{w=0.1}"

    n "Their words cut off as the mist parts, just for a second. A drop rumbles beneath Hikaru’s feet."

    with vpunch

    play sound "sfx/stumble.mp3"

    show hik panic:
        zoom 0.31
        xalign 0.75
        yalign -0.09
        xanchor 0.5
        yoffset 50
        xzoom 1.0
        yzoom 1.0
        linear 0.2 yoffset 400
    hikaru "{sc=1}Ah--!{/sc}{w=0.1}"
    with vpunch

    n "They stumble, tries to flap their wings but it seems like the air is dragging Hikaru down."

    show yam shocked with sshake:
        zoom 0.29
        xalign 0.25
        yalign -0.04
        xanchor 0.5
        yoffset 0
        xzoom 1.0
        yzoom 1.0

        linear 0.2 xoffset 300
    yamato "{b}OI!!{/b}{w=0.1}"

    n "Yamato lunges, arm hooking around Hikaru’s waist. He manage to save Hikaru, barely."

    show yam rage with dissolve
    yamato "Tch--hold on, {sc=1}dammit!!{/sc} Don’t ya dare--"

    hikaru "{i}My wings... What's going on!?{/i}{w=0.1}"

    show yam serious  with dissolve
    yamato "Climb now, think later, damnit!"
    show yam shocked:
        zoom 0.29
        xalign 0.25
        yalign -0.04
        xanchor 0.5
        yoffset 0
        xoffset 300
        xzoom 1.0
        yzoom 1.0

        linear 0.5 xoffset 0
    show hik sad:
        zoom 0.31
        xalign 0.75
        yalign -0.09
        xanchor 0.5
        yoffset 400
        xzoom 1.0
        yzoom 1.0
        linear 0.5 yoffset 50
    n "Hikaru claws back onto solid ground, as yamato pulls Hikaru back above."

    show hik sad  with dissolve
    hikaru "Haa... {w=0.1}Haa..."

    hikaru "{w=0.1}...If you hadn’t..."

    show yam annoyed  with dissolve
    yamato "Shuddup, I don't wanna hear it."

    show hik worried  with dissolve
    hikaru "The elders... {w=0.1}they always warned us not to leave."

    show yam sad  with dissolve
    yamato "...Said the gods’d be angry. Or some shit."

    show hik sad  with dissolve
    hikaru "It's a dead end, then..."

    show yam sad  with dissolve
    yamato "Sorry, Hikaru. {w=0.1}But I think yer dad's down there."

    show hik sad  with dissolve
    hikaru "..."

    hikaru "{i}Let's just... {w=0.1}go back to the village.{/i}"

    scene shrine day with in_212:
        zoom 0.5

    show shi worried:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0
    with dissolve


    n "They return to the shrine to find Shiori already laying out older scrolls on the floor."

    show hik serious at hikaru_zoom, right

    show yam serious at left:
        xalign 0.25
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0




    shiori "I didn't find much, but I think this part explains more."
    shiori "So this part talks about 'The bargain for food that never failed and wombs that never emptied.'"

    hikaru "That is how the fields flourished... how the children were always strong. Even thought the Yamakui is picking off the villagers one by one."

    show shi sad with dissolve
    shiori "That's because it's the price."
    shiori "Every red moon, Yamakui comes to eat someone."

    show hik worried with dissolve
    hikaru "So the mist is the barrier to keep people from running away."

    show yam angry with dissolve
    yamato "No wonder the elders told us never to leave. They knew. They fuckin’ knew."

    show shi annoyed with dissolve
    shiori "It is considered an act so blasphemous, to pray to a god other than Kami-sama."

    show yam annoyed with dissolve
    yamato "Tch. That all ya found, Shiori?"

    show shi surprised with dissolve
    shiori "No, look at this part here..."
    shiori "The texts mention the Oni Slayer’s blade. The one [persistent.player_name] carried up the mountain."

    show yam surprised with dissolve
    yamato "Okay, but if [persistent.player_name] had it, why still lose?"

    show shi worried with dissolve
    shiori "Because [persistent.player_name] didn't have this..."

    n "Shiori shows several talismans, hidden under a decorated box, wrapped around a ceremonial dagger."

    show hik surprised with dissolve
    hikaru "Wait, but why didn't they?"

    show shi sad with dissolve
    shiori "Remember when the elder looked surprised [persistent.player_name] managed to kill the Yamakui?"

    show hik shocked with dissolve
    hikaru "...{w=0.1}Oh."

    show yam shocked with dissolve
    yamato "{w=0.1}Shit."

    show shi sad with dissolve
    shiori "....{w=0.1}"

    show shi sad with dissolve
    shiori "{i}[persistent.player_name] was never supposed to win.{/i}"

    show hik shocked with dissolve
    hikaru "{b}No way--!{/b}"

    show yam rage with dissolve
    yamato "{sc=1}Damn it all t' hell!{/sc} I'm gonna get that damned old man--"

    show hik serious with dissolve
    hikaru "Yamato, stop. All we need to do now is to find the blade."
    hikaru "Since the Yamakui's here, their lair is unguarded. We'll look for the blade there."
    hikaru "Shiori...stay here. Keep Yamakui in the village."

    show shi sad with dissolve
    shiori "...{w=0.1}"

    show shi fear with dissolve
    shiori "{glitch=7}I'm scared now...{/glitch}"

    show shi sad with dissolve
    shiori "So the Yamakui is not as kind as I thought."
    shiori "Am I gonna be okay?"

    show hik normal with dissolve
    hikaru "The red moon's still in a few days, as long as you stay in public, you'd be fine."
    hikaru "All you need to do is use the villagers to distract them."

    show shi worried with dissolve
    shiori "...{w=0.1}Okay."

    show hik serious with dissolve
    hikaru "Then it is settled. Yamato-kun and I go to the mountain. Shiori-chan holds the village."

    show shi sad with dissolve
    shiori "{i}Don’t die on me before we get the chance, you two.{/i}"

    show yam annoyed with dissolve
    yamato "Tch. Don’t screw this up, Shiori."

    show hik angry2 with dissolve
    hikaru "This is for [persistent.player_name]. {w=0.1}For the precious friend we lost."



    scene black
    n "And on they went.{w=0.3}"
    n "The mountain air is suffocating, the mist here is {color=#ff002e}blood red{/color}, a different color than at the village borders."

label body_discovery:

    show flesh
    show darken2
    play music "spooky.mp3"

    show hik panic behind darken2:
        zoom 0.31
        xalign 0.75
        yalign -0.09
        xanchor 0.5
        yoffset 50
        xzoom 1.0
        yzoom 1.0

    show yam annoyed behind darken2:
        zoom 0.29
        xalign 0.25
        yalign -0.04
        xanchor 0.5
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    yamato "Tch... what the hell’s that smell...?"
    hikaru "{i}Smells like... rotting corpses.{/i}"
    yamato "{sc=4}Or shit.{/sc}"

    n "They step into the cave and their breath stops immediately. {w=0.2}The cave is made of meat. Heaps of it. Skin, fat, bone, shredded and piled like refuse."

    play sound "sfx/splurt.mp3"
    $ renpy.pause(1.0)

    n "The stench of {color=#ff002e}sweet rot{/color} fills their lungs until both gag.{w=0.3}"

    show yam panic at shakey
    yamato "{sc=7}Ghh--fuck--!{/sc}"

    show hik worried with dissolve
    hikaru "Cover your nose--!"

    n "But it doesn’t help, as the air itself {i}tastes{/i} spoiled."
    n "They walk deeper and deeper into heaps of flesh {glitch=12}shifting as if alive{/glitch}."

    show yam serious with dissolve
    yamato "The blade’s here. Has t’be. Somewhere in this godforsaken filth."
    show hik worried with dissolve
    hikaru "Can you still--?"
    show yam annoyed with dissolve
    yamato "Yeah, yeah, ya worry about yerself."

    n "They crouch, hands trembling as they dig through meat and viscera, shoving aside organs and whatever was left of Yamakui's meals.{w=0.2}"

    yamato "Urk, how come that thing lives in a place like this--"

    show hik surprised with dissolve
    hikaru "{cps=18}Hold on--{/cps}"
    show hik surprised with vpunch
    hikaru "There--!"

    n "Something glints under piles and piles of flesh, but then blood sloughs down in {sc=4}wet waves{/sc}, swallowing it."

    show yam panic with dissolve
    yamato "{b}Goddammit--keep diggin’!{/b}"

    show hik shocked with dissolve
    hikaru "...!"
    hikaru "{glitch=16}That's--{/glitch}"
    hikaru "{color=#ff002e}NO...!{/color}"


    show yam shocked with dissolve
    yamato "...!?"

    show hik cry with dissolve
    hikaru "{cps=13}[persistent.player_name]...{/cps}"

    stop music fadeout 1.0

    show gore:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    with flashred

    n "Ah."
    n "They finally {i}found{/i} me."

    hide gore
    with dissolve

    hikaru "You said you'd come back. You promised me--"

    show yam sad with dissolve
    yamato "Th'.. {w=0.1}Th' fucker really took away [persistent.player_name]'s skin by some batshit crazy magic..."

    show hik madcry with dissolve
    hikaru "You didn’t deserve this...! You were... {w=0.1}You were... {w=0.1}the only one who trusted me..."
    hikaru "Even though the whole village condemned me, I could go on because of you..."


    hikaru "{sc=2}How do I live in this world without you...!?{/sc}"

    show yam sad with dissolve
    yamato "..."

    yamato "Hikaru..."

    play music "Final Battle.mp3"

    hikaru "...I'll kill it."

    hikaru "{b}I'll kill it. {w=0.1}I’ll kill that Oni in your name.{/b}"
    hikaru "Swear on it or I'll die trying."

    yamato "{w=0.1}...I'm sorry."

    n "{cps=14}...{/cps}"

    n "Hikaru..."

    scene black

    with dissolve

    n "{i}Live your life... {w=0.1}and be happy...{/i}"
    n "Without me..."

    n2 "..."

    n "...Are you ready?"
    n "{cps=12}To finally die?{/cps}"

    n2 "...{glitch=20}HhAh.{/glitch}"
    n2 "{sc=10}BrInG It On.{/sc}"


    scene black
    with dissolve

label confrontation:



    $ ysword = True
    $ hmask = True
    $ hsword = True

    scene village night:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

    show hik serious at hikaru_zoom, right:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with dissolve
    show yam serious at yamato_zoom, left:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with dissolve

    show shi angry:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with dissolve

    n "When you step out of your house, just the night before the red moon...{w=0.3}"

    n "You see them. Shiori. Yamato. Hikaru."

    show shi angry with dissolve
    shiori "You should recognize this, [persistent.player_name]."

    show hik serious with dissolve
    MC "..."

    show yam rage with dissolve
    yamato "{sc=4}This is the real [persistent.player_name].{/sc}"
    yamato "Yer just wearin' their skin, ya damn Oni!"

    MC yansm3 "{cps=18}hHa...{/cps}"
    MC "{glitch=13}HahHAHAhahahAHHahHAHaaaaaaa!{/glitch}"

    hikaru "What's so funny!?"

    MC "{sc=6}I wAS tRaPpED iN a LoOp.{/sc}"
    MC "KiLl. EaT. RetUrn. WaIt FOr tHE NeXt ReD MoON."
    MC "{b}So BooOOOOooOoOrEd.{/b}"
    MC "ThEN I mEt YoUR fRIenD."
    MC "MaKEs ThiNGs FuN."
    MC "BuT nOW..."
    MC sad3 "{sc=4}NoT FuN AnyMOrE... HuH?{/sc}"
    MC "{cps=13}iT's OvEr.{/cps}"

    n "Shiori begins chanting as her body glows."

    scene cg_trueending:
        zoom 0.5
        xalign 0.5
        yalign 0.5

        parallel:
            easein 2.0 zoom 0.62
            easeout 2.0 zoom 0.58
            repeat


        parallel:
            ease 0.5 xoffset 12
            ease 0.5 xoffset -12
            repeat
    show expression Text("山の鬼よ", style="jojo_text") at jojo_scatter1
    show expression Text("立ち去れ、立ち去れ！", style="jojo_text") at jojo_scatter2
    show expression Text("深淵に、闇に帰れ", style="jojo_text") at jojo_scatter3
    pause 2.0

    shiori "{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}Oni of the mountains,{/sc}{/outlinecolor}{/color}{/size}{w=0.2}{fast}{size=+1}{color=#ff0000}{sc=6}begone,{/sc}{/color}{/size}{w=0.5}{fast}{size=+1}{color=#ff0000}{sc=6}begone!{/sc}{/color}{/size}"

    pause 2

    hide expression Text
    hide expression Text
    hide expression Text

    show expression Text("山の鬼よ", style="jojo_text") at jojo_attack4
    show expression Text("立ち去れ、立ち去れ！", style="jojo_text") at jojo_attack5
    show expression Text("深淵に、闇に帰れ", style="jojo_text") at jojo_attack6

    shiori "{cps=14}{alpha=0.8}{sc=6}Back to the depths.{/sc}{/alpha}{/cps}{w=0.3}{size=+10}{color=#aa0000}{sc=6}Back to the dark!{/sc}{/color}{/size}"



    pause 2

    with sshake

    hide expression Text
    hide expression Text
    hide expression Text


    hikaru "[persistent.player_name]... I'm sorry."

    n "Hikaru raises the talismans wrapped around a ceremonial dagger, a binding circle appearing on the ground, under your feet."

    yamato "Get lost, Oni!"

    yamato "{sc=3}Haaaaaaaaaaaaaaaaa--!{/sc}"

    n "Yamato drives the broken Oni Slayer blade straight through your chest. You don't even try to dodge."

    n2 "{cps=16}HaHa... HAhA... hah...{/cps}"
    n2 "YoU GoT mE."
    n2 "{b}FiNaLlY.{/b}"

    n2 "I cOuLd'vE mOvEd. cOuLd’vE tEaR yOu ApArT.{w=0.2}"
    n2 "bUt--{w=0.2}"
    n2 "{i}I dOn'T wAnNa.{/i}{w=0.2}"

    n2 "I'M tIrEd."
    n2 "{cps=14}sO... {w}tIrEd.{/cps}"

    n2 "{i}It’S oVEr.{/i}"
    n2 "nO mOrE rEd MoOnS."
    n2 "nO mOrE lOoPs."
    n2 "nO mOrE yOu."
    n2 "nO mOrE Me."

    n2 "bUt--"
    n2 "HeY."

    n2 "It WaS fUn."
    n2 "{cps=12}ThAnK yOu, [persistent.player_name]...{/cps}"
    n2 "FoR mAkInG mE WanT To DIe."

    show expression Text("山の鬼よ", style="jojo_text") at jojo_scatter1
    show expression Text("立ち去れ、立ち去れ！", style="jojo_text") at jojo_scatter2
    show expression Text("深淵に、闇に帰れ", style="jojo_text") at jojo_scatter3
    pause 2.0


    shiori "{size=*1.1}{color=#ffffff}{outlinecolor=#000000}{sc=6}Oni of the mountains,{/sc}{/outlinecolor}{/color}{/size}{w=0.2}{fast}{size=+1}{color=#ff0000}{sc=6}begone,{/sc}{/color}{/size}{w=0.5}{fast}{size=+1}{color=#ff0000}{sc=6}begone!{/sc}{/color}{/size}"


    pause 2.0


    hide expression Text
    hide expression Text
    hide expression Text

    pause 0.5

    show expression Text("山の鬼よ", style="jojo_text") at jojo_attack4 as o1
    show expression Text("立ち去れ、立ち去れ！", style="jojo_text") at jojo_attack5 as o2
    show expression Text("深淵に、闇に帰れ", style="jojo_text") at jojo_attack6 as o3

    shiori "{cps=14}{alpha=0.8}{sc=6}Back to the depths.{/sc}{/alpha}{/cps}{w=0.3}{size=+10}{color=#aa0000}{sc=6}Back to the dark!{/sc}{/color}{/size}"

    pause 2.0

    hide expression Text
    hide expression Text
    hide expression Text

    n "The seal ignites. The circle glows more, and more, until everything turns to..."

    scene white_bg
    with out_182

    show petals_dense2
    show petals_scatter2

    n "...{sc=5}white.{/sc}"

    stop music fadeout 1.0

    n "And I..."
    n "...I feel warm again."
    n "For the first time in so long."

    n "Thank you. All of you."

    n "Let me finally..."

    n "...rest."

    play music "Ending.mp3"




    hikaru "{cps=17}Hi, [persistent.player_name].{/cps}"

    hikaru "{i}I hope you are well, whereever you are now.{/i}"

    hikaru "I'd like to think you're in heaven now."

    hikaru "The mist isn’t coming back, and there's no more red moons."

    hikaru "No more Yamakui."

    hikaru "We let the villagers know about what the elders did."

    hikaru "The elders were banished for it."

    hikaru "My father... they finally cleared his name."

    hikaru "{i}Too little, too late.{/i}"

    hikaru "It won’t erase what they did to him."

    hikaru "...Or to you."

    $ hmask = False

    scene village day:
        zoom 0.5

    with fade

    show hik normal at hikaru_zoom, right

    show yam normal at left:
        xalign 0.25
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.44
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    with dissolve


    show hik serious with dissolve
    hikaru "I'm leaving."

    pause 0.5

    show yam sad with dissolve
    yamato "...Figured."

    show shi worried with dissolve
    shiori "Where will you go?"

    show hik sad with dissolve
    hikaru "I don’t know. Somewhere past the fields. Somewhere far from this mountain."

    show shi sad with dissolve
    shiori "You won’t come back, will you?"

    show hik sad with dissolve
    hikaru "{b}No.{/b}"
    hikaru "This village... {w=0.1}buried my father in silence, called me a traitor..."
    hikaru "And it buried [persistent.player_name], too."
    hikaru "It let a monster wear their face while everyone looked the other way."

    show yam serious with dissolve
    yamato "You don’t have to explain."

    show hik normal with dissolve
    hikaru "I’m not trying to justify it."
    hikaru "I just... I can’t {i}breathe{/i} here anymore."

    show shi sad with dissolve
    shiori "Hikaru-san..."
    shiori "Will you be back?"

    show hik sad with dissolve
    hikaru "Don't think so, but I’ll write."

    show shi smug with dissolve
    shiori "You better. Or I’ll send a {sc}curse{/sc} with your name on it~"

    show yam annoyed with dissolve
    yamato "Don’t write too much. I ain’t gonna read a damn novel."

    show hik smilesad with dissolve
    hikaru "Then I’ll write it just for me... or {i}[persistent.player_name].{/i}"

    show hik normal with dissolve
    hikaru "How about you two?"

    show yam serious with dissolve
    yamato "Tche, someone needs to protect the damn village."

    show shi happyblush with dissolve
    shiori "And I'd have to be here so Yamato doesn't stab himself~"

    show yam annoyedbl with dissolve
    yamato "Oi."

    show shi happy with dissolve
    shiori "Oh, and..."

    show shi sad with dissolve
    shiori "Someone needs to tend to [persistent.player_name]'s urn too."
    show yam sad with dissolve
    shiori "The very first urn... {w=0.1}with a name."

    show hik sad with dissolve
    hikaru "{cps=10}...{/cps}"

    show hik serious with dissolve
    hikaru "{b}Yeah.{/b}"


    scene black with fade
    $ renpy.pause(2.5)

    $ phrase = "我らは汝の名を忘れない"
    $ n_chars = len(phrase)
    $ center_x = 0.5
    $ spacing = 0.045    # <<<<<< REDUCE SPACING FOR CENTERED LOOK
    $ start_x = center_x - (spacing * (n_chars-1) / 2)
    $ y_center = 0.5

    show expression Text("我", style="jojo_bigtext") at wriggle_zoomout(0.00, start_x+spacing*0, y_center, 2.1) as wrb1
    show expression Text("ら", style="jojo_bigtext") at wriggle_zoomout(0.10, start_x+spacing*1, y_center, 2.1) as wrb2
    show expression Text("は", style="jojo_bigtext") at wriggle_zoomout(0.20, start_x+spacing*2, y_center, 2.1) as wrb3
    show expression Text("汝", style="jojo_bigtext") at wriggle_zoomout(0.30, start_x+spacing*3, y_center, 2.1) as wrb4
    show expression Text("の", style="jojo_bigtext") at wriggle_zoomout(0.40, start_x+spacing*4, y_center, 2.1) as wrb5
    show expression Text("名", style="jojo_bigtext") at wriggle_zoomout(0.50, start_x+spacing*5, y_center, 2.1) as wrb6
    show expression Text("を", style="jojo_bigtext") at wriggle_zoomout(0.60, start_x+spacing*6, y_center, 2.1) as wrb7
    show expression Text("忘", style="jojo_bigtext") at wriggle_zoomout(0.70, start_x+spacing*7, y_center, 2.1) as wrb8
    show expression Text("れ", style="jojo_bigtext") at wriggle_zoomout(0.80, start_x+spacing*8, y_center, 2.1) as wrb9
    show expression Text("な", style="jojo_bigtext") at wriggle_zoomout(0.90, start_x+spacing*9, y_center, 2.1) as wrb10
    show expression Text("い", style="jojo_bigtext") at wriggle_zoomout(1.00, start_x+spacing*10, y_center, 2.1) as wrb11

    pause 2.0


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

    pause 2.0

    show expression Text("We will remember your name", style="jojo_bigtext") at Position(xalign=0.5, yalign=0.5)



    pause 2.5

    hide expression Text

    show expression Text("[persistent.player_name]", style="jojo_bigtext") at Position(xalign=0.5, yalign=0.5)


    with dissolve
    $ renpy.pause(3.5)

    return

    $ persistent.shiori_dies = False
    $ persistent.yamato_dies = False
    $ persistent.hikaru_dies = False

    $ persistent.loop1 = False
    $ persistent.loop2 = False
    $ persistent.loop3 = False

    $ persistent.loop2_shiori_ghost1 = False
    $ persistent.loop2_shiori_ghost2 = False
    $ persistent.loop2_shiori_ghost3 = False
    $ persistent.loop2_shiori_ghost4 = False
    $ persistent.loop2_shiori_ghost5 = False

    $ persistent.loop2_yamato_ghost1 = False
    $ persistent.loop2_yamato_ghost2 = False
    $ persistent.loop2_yamato_ghost3 = False
    $ persistent.loop2_yamato_ghost4 = False
    $ persistent.loop2_yamato_ghost5 = False

    $ persistent.loop2_hikaru_ghost1 = False
    $ persistent.loop2_hikaru_ghost2 = False
    $ persistent.loop2_hikaru_ghost3 = False
    $ persistent.loop2_hikaru_ghost4 = False
    $ persistent.loop2_hikaru_ghost5 = False

    $ persistent.seen_true_end = True

    return
