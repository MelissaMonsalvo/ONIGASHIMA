label loop1_hikaru:

    $ hmask = False

    ## HIKARU'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS

    ## STILL IN DAY 5, HAPPENS AT THE END OF DAY 5

    scene forest day:
        zoom 0.5
    pause 0.2
    show hik normal behind darken:

        zoom 0.3
        xalign 0.5
        yoffset -600
        xzoom -1.0
        matrixcolor BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A")  # in shadowwww


        easein 0.2 yoffset 170

        matrixcolor None
        easeout 0.1 yoffset 165 xzoom -1.05 yzoom 0.95
        easein 0.1 yoffset 150 xzoom -1.0 yzoom 1.0
    with vpunch
    play sound "Sfx/landing.mp3"

    n "You find Hikaru, perched atop a tree. They jumps down as you come into view."

    hikaru "...[persistent.player_name]."

    play music "Doubt.mp3"

    MC nervous "Hikaru, I--"

    hikaru "Yes?"

    MC nervous "I asked Yamato and Shiori, and they said they don't know that there's something between us, so--"

    show hik sad
    with dissolve

    hikaru "That's because my father is branded traitor."

    hikaru "He tried to run away from the village, so he tried to find out a way out among the mist..."

    hikaru "But his body was never found."

    show hik worried
    with dissolve

    hikaru "So I suggested we start a relationship in secret."

    hikaru "Because I thought if they found out, they’d turn on you too."

    MC surprised "...Ah."

    n "Everything makes sense now."

    show hik sad:
        zoom 0.3
        xalign 0.5
        yoffset 150
        xzoom -1.0
        yzoom 1.0

        parallel:
            linear 0.07 xoffset -2 yoffset 152
            linear 0.06 xoffset 2 yoffset 149
            linear 0.08 xoffset -1 yoffset 151
            linear 0.06 xoffset 1 yoffset 150
            linear 0.07 xoffset 0 yoffset 150
            repeat

    hikaru "{sc=4}So when you forgot about me... {w=0.1]I thought you were possessed.{/sc}"

    hikaru "When you came back from the mountains, you looked like you and sounded like you..."

    hikaru "But you didn’t remember anything. The lake, the scarf, the promise...{w} Us."

    hikaru "{i}You smiled at me like I was just like the others.{/i}"

    hikaru "And I--I thought maybe... {cps=13}maybe something came back in your place.{/cps}"

    hikaru "Maybe it wore your face, and that’s why it didn’t know me."

    MC sad "..."

    n "They look up at you."

    show hik smilesad
    with dissolve

    hikaru "{glitch=7}But it’s still you, isn’t it?{/glitch}"

    hikaru "You’re not possessed, aren't you?"

    hikaru "{sc=1}Maybe you just hit your head... {w}Or...{/sc}"

    hikaru "{sc=1}...the fight was so traumatizing you wiped out some of your recent memories.{/sc}"

    show hik worried
    with dissolve

    hikaru "{i}I don't know...{/i}"

    hikaru "{cps=11}I was... making dozens and dozens of talisman so you'd come back.{/cps}"

    hikaru "{sc=5}But you came back different.{/sc}"

    n "Hikaru covers their face."

    show hik cry
    with dissolve

    hikaru "You’re here, the village's hero, breathing, laughing... {w=0.1}And I-I should be happy."

    hikaru "{sc=1}But it feels worse than if you’d died.{/sc}"

    hikaru "Maybe it's punishment from the gods... {w}For what my father did..."

    MC sadcl "...I'm sorry."

    MC sadcl "I don’t know what happened to me, or what I lost."

    MC sadcl "But... {w}I want to fix it."


    MC nervous "I want to remember {i}you{/i}, Hikaru."

    MC nervous "I want to start over... {w=0.1}If you’ll let me."

    show hik cry:
        zoom 0.3
        xalign 0.5
        yoffset 150
        xzoom -1.0
        yzoom 1.0

    hikaru "..."

    n "Hikaru looks up again. Their hands lower from their face, fingers smeared with tears."

    hikaru "You really mean that?"

    MC happy "Of course, Hikaru."

    show hik smilesad
    with dissolve

    hikaru "{sc=1}Tell me something, [persistent.player_name]...{/sc}"

    hikaru "{cps=13}Do you still {i}love me?{/i}{/cps}"

    n "{i}Their voice cracks again.{/i}"

    hikaru "How do you plan to remember everything we went though?"

    n "You don’t answer right away."

    MC normal "{k=-1}Well... If I loved you once, I can do it again.{/k}"

    MC happycl "And if you tell me again... {i}I’ll listen!{/i}"

    MC happycl "We’ll make new memories. {sc=1}A-And I’ll hold onto them this time!{/sc}"

    n "Hikaru hesitates for a moment, staring at your face, then wipes their own, nodding."

    show hik sad
    with dissolve

    hikaru "All right, fine..."

    hikaru "But tell me this... {w=0.2}What actually happened to you?"

    ## GASLIGHTING BEGIIIIINSSSSSS

    ## Your choices here will matter on whether hikaru believe you or not at the end

    $ hikaru_belief = 0

    menu:
        "I got bitten":
            $ hikaru_belief += 1
            MC "{sc=4}I got bitten by the Yamakui, passed out, then lose half of my memory.{/sc}"

            show hik worried
            with dissolve
            hikaru "{i}Then why'd you pretend nothing happened?{/i}"
            MC "I just don't want to concern you guys!"

        "My head hit something":
            $ hikaru_belief -= 1
            MC "{cps=12}I hit my head on something on the way back to the mountain...{/cps}"
            show hik worried
            with dissolve
            hikaru "{sc=3}But your head wasn't bleeding when you returned.{/sc}"
            MC "I don't know, maybe it's just bleeding internally?"
            hikaru "..."


    menu:
        "Smile":
            n "You muster the best smile you can conjure."
            n "It looks crooked."

        "Hug them":
            n "You step forward and hug Hikaru, their body stiffs in your arms, but they don't push you away."
            $ hikaru_belief += 1

    hikaru "...I..."

    n "Their voice breaks."

    hikaru "I want to."

    hikaru "I want to believe."

    MC sadcl "If you still need time, that's okay."

    MC sadcl "I'll be here... if you still love me. You can teach me again on how it was supposed to be."

    hikaru "{i}*Sigh*{/i}"

    show hik sadsmile
    with dissolve

    hikaru "...Okay."

    show hik sadsmile:
        zoom 0.4
        xalign 0.5
        yoffset 120
        xzoom -1.0
        yzoom 1.0


        linear 0.3 yoffset 145 zoom 0.35

        parallel:
            linear 0.3 alpha 0.8
            linear 0.2 alpha 0.5
            linear 0.4 alpha 0.0

    n "You don’t know if they believe you, but Hikaru never steps away."

    scene black
    with fade

    stop music

    n "And that's good enough for you. {w}For now."


    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}TWO DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

    with fade

    pause 0.5

    scene moon4
    with fade
    pause 0.2
    scene moon5
    with fade

    stop sound

    pause 0.5

    n "You start to seek Hikaru afterward, to show them that you stay true to your words."

    scene forest day:
        zoom 0.5
    show teru day:
        zoom 0.5

    n "Hikaru told you to meet up in the forest later in the day."

    play music "Hikaru.mp3"

    n "When you arrive, you see hundreds of paper effigies hung on the trees. They're perfectly aligned, all but one."
    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show terumc:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
        yzoom -1.0
    with dissolve

    n "The one with your name on it is crooked, its head is dangling where the feet should be."


    hide frame2
    hide terumc
    show hik normal:
        zoom 0.4
        xalign 0.5
        yoffset 120
        yzoom 1.0
    with dissolve

    hikaru "...[persistent.player_name]. You're here."

    MC normal "What's up with my effigy? Looks like I am cursed or something."

    hikaru "Ah, yes. Shiori-chan did say she tried fixing it, but this just won't budge."

    show hik worried
    with dissolve

    hikaru "So... {w=0.1}I was trying to fix it for her."

    hikaru "But it's so... stubborn."

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show terumc:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
        yzoom -1.0
        linear 1.0 rotate 15

        linear 1.0 rotate -10

        linear 0.5 rotate 0

        pause 1.0
        linear 0.2 yzoom -1.0
    pause 1.0

    n "Hikaru tries to shift it, but fails again."

    hide frame2
    hide terumc

    show hik sad
    with dissolve

    hikaru "Do you think... {w=0.2}It's a sign?"

    MC surprised "What, like an omen?"

    hikaru "Maybe."

    ## so like there is a counter for Hikaru's disbelief and it just shows how different Hikaru reacts at the ending

    menu:
        "Mock Hikaru":
            MC smugcl "I think you're being too {i}paranoid{/i}. I mean, Shiori could've just cut it unevenly or something."
            MC normal "{k=-1}It fell wrong, maybe, or the string slips. It happens.{/k}"
            hikaru "It's not like Shiori-chan to make mistakes like this. She had always been good at crafting."
            hikaru "{i}She even taught me how to make paper crafts....{/i}"

        "Act hurt":
            MC sad "{sc=5}You really think I'm cursed or something?{/sc} After all I did for the village?"
            MC sadcl "Or... Do you think I'm {glitch=8}lying{/glitch}?"

            $ hikaru_belief += 1
            n "You let your voice heave and falters for a bit while looking straight at Hikaru's eyes."
            show hik panic
            with dissolve
            hikaru "{cps=11}No, I--{/cps}"

    n "The paper still hangs upside down. You want to reach up and fix it, but your hand won’t move."

    n "Because you know it's pointless."

    show hik sad
    with dissolve

    hikaru "{sc=4}Hey...{/sc}"

    hikaru "{i}You're still you... Right?{/i}"

    MC annoyed "{sc=4}Again with the doubts?{/sc}"

    hikaru "...Sorry. Forget I asked."

    n "Hikaru stares for your face uncomfortably longer than it should, before looking away with a small nod."

    show hik serious:
        zoom 0.4
        xalign 0.5
        yoffset 120
        yzoom 1.0

        ease 0.5 xzoom -1

    hikaru "{cps=10}So I guess... Shiori's the one making a mistake, then.{/cps}"

    show hik serious:
        zoom 0.4
        xalign 0.5
        yoffset 120
        yzoom 1.0
        xzoom -1

        linear 0.3 yoffset 130 zoom 0.38 alpha 0.8
        linear 0.2 yoffset 140 zoom 0.36 alpha 0.5
        linear 0.4 yoffset 150 zoom 0.37 alpha 0.0
    hide hik

    n "They stare at the effigy once more before finally walking away."

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show terumc:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
        yzoom -1.0
        linear 0.12 rotate 8
        linear 0.09 rotate -6
        linear 0.10 rotate 10
        linear 0.09 rotate -8
        linear 0.09 rotate 7
        linear 0.09 rotate -5
        linear 0.10 rotate 12
        linear 0.12 rotate -9
        linear 0.10 rotate 0
        pause 0.3
        linear 0.2 yzoom -1.0

    pause 1.5

    n "You reach to it and forcibly try to flip it again, but it turns even though there's no wind."

    stop music

    play sound "sfx/riip.mp3"

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    hide terumc

    show terumc_right:
        zoom 0.5
        xalign 0.5
        xanchor 0.0
        yalign 0.33
        yzoom -1.0


    show terumc_left:
        zoom 0.5
        xalign 0.5
        xanchor 1.0
        yalign 0.33
        yzoom -1.0

        pause 0.2

        linear 0.5 yoffset 300 alpha 0.0  # Moves up off the screen, fades out




    with vpunch



    n "So you rip it in half instead."


    MC yan  "..."

    scene black with fade

    n "..."

    n "What you said about an omen suddenly comes true, moments later."

    n "You see the villages folk gather on the town square."

    show flesh2 at scary_flicker

    play music "sfx/Flies.mp3"

    n "They circle around a dog... or what remains of it."

    n "Its belly is torn wide, skin hangs in pieces, ribs pulled apart."

    n "The head is twisted at an unnatural angle, slack-jawed and one eye missing."

    n "Whatever attacked it was definitely has large claws."

    hikaru "{cps=13}...[persistent.player_name].{/cps}"

    hikaru "Something ate it..."

    hikaru "{sc=4}I think it’s the Oni. I think Yamakui--{/sc}"

    MC nervous "Hikaru, I killed it."

    hikaru "{i}What?{/i}"

    MC yan "The Yamakui,{w} I mean."

    hikaru "...Oh. {w=0.5}{i}Yes. Of course you did.{/i}"

    hikaru "But what did this...?"

    hikaru "...T-That can't be a bear, right? We have no bears in this mountain, so it could only be--"

    scene village night:
        zoom 0.5

    show hik panic at midleft :
        zoom 0.25
        yoffset 100
        xzoom -1
    with dissolve
    show man at midright:
        zoom 0.45
        ypos 0.1
    with dissolve
    show darken
    with dissolve

    "Man" "Hikaru, are you saying the Oni’s still walking around?"

    "Man" "Or are you saying [persistent.player_name] didn’t finish the job?"

    n "The accusation rings clear, none of them are talking about the corpse anymore."

    hikaru "..."

    "Man" "Why'd we trust {i}Karasuma's child{/i} than the person who brought the Oni's armor back?"

    hikaru "{glitch=7}I--{/glitch}"

    show hik panic at midleft :
        zoom 0.25
        yoffset 100
        xzoom -1

        parallel:
            linear 0.07 xoffset -2
            linear 0.06 xoffset 2
            linear 0.08 xoffset -1
            linear 0.06 xoffset 1
            linear 0.07 xoffset 0
            repeat

    hikaru "{sc=5}Sorry... Maybe I’m just being paranoid. Maybe... Maybe... it wasn’t what I thought.{/sc}"

    n "They’re breathing faster, eyes frantic, visibly twitching now."

    hikaru "{i}I just... made a mistake. I got confused.{/i}"

    hikaru "{cps=12}Yeah, that's what this is...{/cps}"

    hikaru "{sc=4}You killed Yamakui. I shouldn’t have said anything. I’m sorry.{/sc}"

    hikaru "{i}I’ll stop talking. I-I-{nw}{/i}"

    show hik panic at midleft :
        zoom 0.25
        yoffset 100
        xzoom -1

        linear 0.2 xzoom 1 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

    pause 0.2

    play sound "sfx/run.mp3"

    hide hik 
    with dissolve

    hide darken
    hide man
    with dissolve

    scene village night:
        zoom 0.5


    n "Hikaru runs away, clutching their head. You watch as they go."

    stop sound
    stop music

    n "Maybe you should run after them?"

    show yam serious at right:

        zoom 0.23
        yalign -0.04
        xzoom -1.0
        yzoom 1.0
        yoffset 0
    with dissolve

    yamato "..."

    scene black
    with dissolve

    $ ysword = True
    $ hmask = False
    $ hsword = True
    n "You can't find Hikaru anywhere, so you decide to go home instead."

    n "I think you should {nw}"

    play sound "swing.wav"

    show slash_arc
    pause 0.1
    scene house night:
        zoom 0.5
    with sshake
    MC hurt "...Gh--!"

    n "Your back slams the wall, red trickles down your shoulder. A figure steps forward fast, blade already swinging again."

    n "You snarl and surge up immediately, bracing for impact and preparing your counterattack."

    show yam angry:
        zoom 0.24
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1
        yzoom 1.0

        matrixcolor BrightnessMatrix(-0.8) * TintMatrix("#111111")

        ease 0.5 matrixcolor None zoom 0.3

    play music "Battora.mp3"

    yamato "Tch, knew it. Knew somethin’ was off the second I saw ya back!"

    MC mad "Yamato--"

    yamato "Nah. Nah. I ain’t listenin’ to that fake-ass voice comin’ outta your mouth."

    yamato "I saw ya, ya were standin’ there starin’ at the body all bloodied up. Same fuckin’ face, but not ya."

    n "Wait, I don't remember you--"

    menu:
        "Attack Yamato":
            n "You're going at his throat, and Yamato swings once more, aiming at your neck--"

        "Defend yourself":
            n "You step back and brace for Yamato's next attack--"
            $ hikaru_belief += 1

    scene black
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

    show yam rage:
        zoom 0.47
        align (0.5, 0.005)

        linear 0.01 xalign 0.5 yalign 0.1
        linear 0.16 zoom 0.29 xalign 0.41 yalign -0.09 xoffset 122
        linear 0.12 zoom 0.25 xalign 0.2 yalign 0 xoffset -144 yoffset 0
        linear 0.07 yoffset 8
        linear 0.09 yoffset 0

    show hik rage:
        zoom 0.47
        align (0.5, 0.005)

        linear 0.01 xalign 0.5 yalign 0.1
        linear 0.16 zoom 0.59 xalign 0.59 yalign -0.09 xoffset -122
        linear 0.12 zoom 0.25 xalign 0.8 yalign 0 xoffset 144 yoffset 0
        linear 0.07 yoffset 8
        linear 0.09 yoffset 85


    hide combo_slash_1
    hide combo_slash_2
    hide combo_slash_3

    n "You see steel sparks right in front of you as Yamato pulls back a step."

    hikaru "{sc=5}Stop it!{/sc}"

    with hpunch

    n "Hikaru stands between the two of you, sai raised."

    hikaru "{sc=4}Stand back, [persistent.player_name]-san!{/sc}"

    yamato "{size=+2}{sc=4}Ya serious right now? Ya blockin’ for 'em!?{/sc}{/size}"

    yamato "I saw [persistent.player_name] near the damned mutt before everyone found it! {size=+4}Pretty sure [persistent.player_name] killed it, damnmit!{/size}"

    hikaru "{i}Are you sure you're not just seeing things because you're jealous of [persistent.player_name]-san?{/i}"

    yamato "{sc=3}Ya think I’d come all the way here with my blades out if I wasn’t fuckin’ sure?{/sc}"

    yamato "{size=+6}Just fuckin' look at 'em!{/size}"

    n "There is a faint trace of red in your sleeve, it looks older than the blood from your own wound."

    n "No one would see it if you fold your arms, but they are now stretched out in combat stance."

    hikaru "...That wound could be from your attack!"

    with hpunch

    yamato "Or from before. {w=0.1}Ya gonna bet on {sc=0.1}that?{/sc}"

    n "Hikaru glances at you for a split second, hands trembling again, sai still pointed at Yamato."

    MC panic "Come on, you know me."

    MC panic "I didn’t do that. I wouldn't. Hikaru--"

    show hik angry2
    with dissolve

    hikaru "..."

    hikaru "{sc=6}Yamato-kun. {w=0.3}Go. {w=0.3}Leave. If you attack again... I won’t stop the next time.{/sc}"

    yamato "..."

    show yam evil
    with dissolve

    yamato "{size=+6}Hah!{/size}"

    yamato "You've fooled the entire village and even Hikaru, but ya ain't foolin' me."

    yamato "I hope you’re ready for what’s comin’, eh Hikaru? {w=0.1}'Cause when it shows its real face, it ain’t gonna stop at mutts."

    yamato "{size=+4}Ya better hope I’m wrong.{/size}"

    show yam evil:
        zoom 0.25

        xalign 0.2

        yalign 0

        xoffset -144

        yoffset 0

        linear 0.4 xzoom -1 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

    pause 0.4

    hide yam

    with dissolve

    stop music


    n "Yamato retreats and vanishes to the dark. Your knees weaken, but Hikaru’s hand catches your arm immediately."

    n "You're stil bleeding."

    play music "Love.mp3"

    show hik panic:
        zoom 0.25
        xalign 0.8
        yalign 0
        xoffset 144
        yoffset 40

        linear 0.15 zoom 0.35 xalign 0.6 yalign 0.15 xoffset 30 yoffset 300
        linear 0.13 zoom 0.4 xalign 0.5 yalign 0.28 xoffset 0 yoffset 400

    hikaru "Don’t move. Please. Let me--{w}just let me take care of it."

    n "Hikaru rips cloth fast. Their hands shake as they presses it to your shoulder "

    hikaru "{k=-2}It’s {color=#ff002e}red{/color}. It’s...{w}{sc=4}it’s {color=#ff002e}red{/color}.{/sc}{/k}"

    n "For a moment there, Hikaru is breathless and the cloth slips from their grip."

    MC nervous "Of course it is, what do you mean?"

    hikaru "{i}The Oni were always black-blooded. I’ve never seen one, but the folktale said that...{/i}"

    hikaru "They said the blood turned dark before it hit the ground. But...{w}Your blood looks normal."

    hikaru "{k=2}I just have to tell Yamato, {w=0.3}maybe he's not thinking straight, {w=0.3}maybe he's--{/k}"

    MC sadcl "...Hikaru."

    show hik madcry
    with dissolve

    hikaru "{i}Hey, [persistent.player_name]...{/i}"

    hikaru "{k=-1}If you’re still mine, then the {color=#ff002e}red{/color} moon will pass without a hitch...{/k}"

    hikaru "{k=1}And if you’re something else... then...{/k}"

    n "Silence again."

    n "You take both of Hikaru's hands, pulling it away from their face and moves closer."

    scene house night:
        zoom 0.5
        linear 0.4 zoom 0.55
    show hik madcry:
        zoom 0.4

        xalign 0.5

        yalign 0.28

        xoffset 0

        yoffset 400

        linear 0.3 zoom 0.5 yalign 0.2

    MC happycl "Hey, hey, I'm here. You don't have to worry anymore."

    MC nervous "I'm still the same [persistent.player_name] you love."

    show hik cry
    with dissolve

    hikaru "..."

    scene black
    with dissolve

    n "They sink into you, body trembling, shoulders tight. You feel their panic still coursing through under their jittery arms."

    hikaru "...Don’t go again."

    MC happycl "Never."

    show darken2
    with dissolve

    n "The blood spreads into their sleeves now, but Hikaru just close their eyes."

    n "You hold them as they slowly stop shaking, and you u listen to the rhythm of their breath..."

    stop music

    play sound "sfx/breathing.wav"

    n "Inhale..."

    pause 0.2

    n "Exhale..."

    play sound "sfx/breathing.wav"

    pause 0.4

    n "Inhale..."

    pause 0.2

    n "Exhale..."

    n "And the sound of their heartbeat ..."

    pause 0.3

    play sound "sfx/heartbeat.mp3"

    n "Thump."

    pause 0.2
    play sound "sfx/heartbeat.mp3"

    n "Thump."

    pause 0.2
    play sound "sfx/heartbeat.mp3"

    n "Thump."

    pause 0.2
    play sound "sfx/heartbeat.mp3"

    n "Thump."

    pause 0.2


    n "It's ringing in your ears now."

    n "You feel {cps=30}{i}alive.{/i}{/cps}"

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

    $ hsword = False

    scene house night:
        zoom 0.55
    show hik smilesad:
        zoom 0.5

        xalign 0.5

        yalign 0.2

        xoffset 0

        yoffset 400
    with in_212



    n "Hikaru never left your side, you wake to them still clinging to your shoulder."

    MC normal "Mh..."

    play music "Idle.mp3"

    show hik worried
    with dissolve

    hikaru "Oh no, your wounds are bleeding again."

    MC hurt "I'm okay--"

    hikaru "Wait--hold on. Let me change the bandage."

    play sound "sfx/riip.mp3"
    with hpunch

    n "Hikaru peels it back slowly, but your skin gets pulled in it. The wound bubbles and festers."

    n "Hikaru gently cleans the wounds with the salves and cloths found in your house and changes the bandage."

    n "Then they start humming instinctively, quietly, almost not audible."

    n "It’s a tune you don’t know how you know... but your mouth moves anyway."

    MC normal "...Hmm, hmmm, hmmm~"

    n "Odd, I remember that, too."

    n "You follow Hikaru's humming, half a breath behind. They raise their head at that."

    show hik shocked

    with hpunch

    hikaru "{k=2}...!{/k}"

    hikaru "{sc=3}[persistent.player_name]--{w=0.2}that--{/sc}"

    MC surprised "Mmm?"

    hikaru "{i}You remembered that? I thought--{w=0.2}I thought maybe you wouldn’t.{/i}"

    MC normal "Of course I remember."

    show hik blush
    with dissolve

    hikaru "{k=2}We used to--{/k}"

    hikaru "Ah, {w=0.1}well, my mom used to sing it when I couldn't sleep because of the oni, so.."

    hikaru "I taught you that, and you used to tease me that I should sing in public more often..."

    n "You tilt your head and let a small smile pull at the corners, enough to show endearment."

    MC happy "Well, at least I remember how it used to sound like."

    hikaru "Right... yeah. Of course. I just--{w=0.2}I didn’t want to assume. I didn’t know how much you lost, or if maybe it all got... {w=0.2}scrambled."

    show hik smileblush
    with dissolve
    
    hikaru "{i}I was afraid it was just me holding onto it. But this... {w}this feels better.{/i}"

    hikaru "We’re getting somewhere, aren’t we?"

    MC normal "Yeah, I think we're getting close."

    MC nervous "Actually... When the red moon is over, maybe we should come out on the open."

    show hik blush
    with dissolve

    hikaru "{w=0.2}You mean... {k=2}This? Us?{/k}"

    MC nervous "We’ll tell everyone that we're together. I mean since there's no more Oni, they won't care right?"

    MC happycl "Pretty sure Yamato and Shiori would understand."

    show hik panic
    with dissolve

    hikaru "{sc=5}No... don't!{/sc}"

    hikaru "{i}I know Yamato and Shiori would understand, but the others... They'll shame you!{/i}"

    MC annoyed "So what? Let ‘em talk. I don't care."

    n "You talk like it's so easy..."

    show hik sad
    with dissolve

    hikaru "{k=2}You’re serious about this?{/k}"

    MC smug "Of course, never been more sure!"



    menu:
        "'Are you ashamed of me?'":
            $ hikaru_belief += 1
            jump shame

        "'Forget I ever said that.'":
            jump forgettt


label shame:

    MC yan "Or... are you the one ashamed on me?"

    show hik panic:
        zoom 0.5
        xalign 0.5
        yalign 0.2
        xoffset 0
        yoffset 400

        parallel:
            linear 0.07 xoffset -24
            linear 0.07 xoffset 20
            linear 0.06 xoffset -16
            linear 0.06 xoffset 14
            linear 0.05 xoffset -10
            linear 0.05 xoffset 7
            linear 0.04 xoffset -3
            linear 0.04 xoffset 0

    hikaru "{sc=4}No, no, I would never--!{/sc}"

    hikaru "I just don't want them to look at you differently..."

    hikaru "{k=2}A-And they'll blame me for apparently seducing you.{/k}"

    n "You muster a serene smile as your voice turns velvety smooth, enveloping Hikaru with safety."

    MC annoyed "I won't let them, after all I'm the one who saved them from Yamakui. They'll listen to me."

    MC yan "Unless you don't want me to?"

    show hik blush
    with dissolve

    hikaru "...."

    hikaru "{k=1}I-I want that too. Of course I do.{/k}"

    hikaru "I’ve wanted that for a long time. I just... {w}I thought we agreed it was safer this way."

    hikaru "I didn’t know you still--"

    MC yan "Still what?"

    hikaru "...Still wanted me like that."

    MC happycl "Of course I do."

    n "You reach for their hand. Their fingers stay still, caught in yours."

    n "Slowly, their fingers finally curl around yours."

    show hik smileblush
    with dissolve

    hikaru "...Then after the Red Moon... {w=0.2}alright."

    n "Do you mean it, though?"

    n "Hikaru has wanted this so much and it pains them even to look at you like that in public."

    n "If you're lying, you'll {glitch}break{/glitch} them."

    n "Because whatever bait you're casting... {w}it's embedded far too deep now."

    jump loop1_redmoon_eve

label forgettt:
    MC yan "You know what? Forget I ever said that. You clearly don't want anyone to know "

    show hik sad
    with dissolve

    hikaru "{i}Please don't take it the wrong way, [persistent.player_name]... I just don't want to deal with the aftermath.{/i}"

    MC yan "Yeah, let's just pretend that we're nothing to each other until who knows when."

    hikaru "[persistent.player_name].... {w=0.1}I'm sorry..."

    hikaru "I still care about you a lot, even if I can only do this in secret "

    MC yan "Fine then, if that's what you want "

    jump loop1_redmoon_eve


label loop1_redmoon_eve:

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

    n "It's just hours before the red moon. The sky has turned light crimson."

    play music "Blood Ritual.mp3"

    scene village night:
        zoom 0.5
        xalign 0.5
        yalign 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    show hik worried:
        zoom 0.231
        yoffset 185
        xanchor 0.5
        xalign 0.5
        yalign 0
        xoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with in_212

    hikaru "It's soon..."

    MC normal "Yeah."

    show hik serious
    with dissolve

    hikaru "Right, so..."

    hikaru "Salt lines are down. I double-checked the wards, and Shiori-chan lit the incenses an hour ago."

    show hik worried
    with dissolve

    hikaru "I reinforced the barriers, but I... {w}I don't think it'll work... If-if..."

    hikaru "...If the Yamakui really comes back--"

    yamato "{sc=4}Oi.{/sc}"

    show yam annoyed at left, shakey:

        zoom 0.23
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

    show hik worried:
        zoom 0.231
        yoffset 185
        xanchor 0.5
        xalign 0.5
        yalign 0
        xoffset 0
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
        linear 0.2 xalign 0.7

    hikaru "Yamato-kun--"

    yamato "If shit starts happenin’ tonight or I find another dead body..."

    yamato "{b}{size=+6}That’s on YA.{/size}{/b}"

    MC mad "What the hell is that supposed to mean?"

    yamato "{sc=2}Don’t play dumb.{/sc}"

    yamato "Yer the one who said you killed it. Ya told us the Yamakui was gone."

    yamato "{i}So if it ain't...? Then you lied to all of us, to Hikaru.{/i}"

    MC hurt "Yamato--"

    yamato "{glitch=8}Don’t.{/glitch}"

    yamato "{sc=1}I ain’t scared of ya, or of whatever the hell is wearin’ ya.{/sc}"

    yamato "If anyone turns up gutted tomorrow, {w=0.1}I’ll drag yer ass through the streets and gut whatever’s inside. Even if Hikaru cares about ya."

    hikaru "..."

    hide yam
    with fade


    n "Yamato leaves immediately without waiting for a response and dissapears into the forest."

    show hik sad
    with dissolve

    hikaru "...What if he's right?"

    MC yan "Look at me."

    MC mad "I killed the Yamakui. Me. Whatever attacked that dog... It's gone now."

    MC mad "No one's getting killed lately right?"

    MC yan "I'm with you, if there's another oni out there, it’s not stronger than us."

    MC happycl "I defeated the Yamakui, remember?"

    n "You press your hand against theirs, then grips it so tight your nails leave marks to steady them."

    show hik smilesad
    with dissolve

    hikaru "...Okay."

    n "You’ve calmed them, again. Like you always used to."

    scene black
    show darken2
    with fade

    n "And I don’t know what you're trying to protect anymore."

    n "The village?"

    n "Hikaru?"

    n "Or yourself?"

    ### RED MOON TIIIMEEE

    n "..."

    n "..."

    n "..."

    stop music fadeout 1.0

    scene moon7
    with fade

    n "You're both staring at the red moon now, wind sofly blowing at your faces. It's oddly serene..."

    show hik serious:
        zoom 0.5
        xalign 0.5
        yalign 0.2
        xoffset 0
        yoffset 400


        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))



    hikaru "...It’s quiet."

    MC sadcl "Yeah."

    hikaru "If the Yamakui's here... {w}someone would've screamed, right?"

    MC sadcl "Definitely."

    hikaru "So... maybe you really DID kill it."

    MC happycl "See? I told you."

    show hik smilesad
    with dissolve

    hikaru "Sorry that I didn't believe you."

    hikaru "You must think that's rich, coming from me..."

    hikaru "But... Can we try again?"

    n "You let Hikaru lean against your shoulder now, and close your eyes."

    n "There's the sound of their heatbeat again..."

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.1}Thump.{/size}"
    with fade

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.2}Thump.{/size}"
    with fade

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.3}Thump.{/size}"
    with fade

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.4}Thump.{/size}"
    with fade

    n "Dawn is almost here."

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.5}Thump.{/size}"
    with fade

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.6}Thump.{/size}"
    with fade

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*1.8}Thump.{/size}"
    with fade

    play sound "sfx/heartbeat.mp3"
    pause 0.2
    n "{size=*2.0}Thump.{/size}"
    with fade

    if hikaru_belief <=3:
        jump hikaru_distrust
    else:
        jump hikaru_trust


label hikaru_trust:

    n "Hikaru's almost falling asleep, their neck is fully exposed to you now."

    n "Their pulse is visible under the red."

    n "You lean in, to wake them up, your foreheads are touching now."

    hikaru "[persistent.player_name]?"

    MC happycl "Hikaru..."

    MC yansm "...You'll meet [persistent.player_name]."

    MC yansm "In the afterlife, when I’m done with you."

    show hik panic

    hikaru "{sc=5}...!{/sc}"

    with sshake

    n "Wait, what are you doing? Why--"

    scene black
    with fade

    play muzak "sfx/hikaru_eaten.wav"

    n "Hikaru--"

    play sound "sfx/hikaru_Scream.mp3"

    hikaru "{k=-2}Aah--!{/k}"

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

    n "There's a sound of tearing flesh, a gurgle as an artery is nicked."

    n "{i}No, please, stop!{/i}"

    play sound "sfx/splurt.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n "{sc=4}What is wrong with you!?{/sc}"

    n "You told them you loved them, didn't you!?"

    n "You promised to come out to everyone that you're together, right!?"

    n "But now... Why...!?"

    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n "{sc=3}I can’t--{/sc}"

    n "{blur}I don’t want to see it...!{/blur}"

    n "{k=2}Please--!{/k}"

    n "{size=+3}{color=#ff0000}Please make it stop.{/color}{/size}"



    stop music


    play sound "sfx/slurrp.mp3"

    scene black
    with in_212

    stop sound

    n "The {color=#ff0000}red{/color} streaks and shadows are gone."

    n "And so is hikaru."

    n "Only the {color=#ff0000}red{/color} scarf that they used to wear remains."

    n "{i}I...{/i}"

    n "{sc=3}No, no...{/sc}"

    n "{i}My chest hurts... {w}My chest? Yours...?{/i}"

    n "Why does it hurt?"

    n "Why does it feel like I’m the one who got left behind?"

    n "..."

    n "{blur}...Who am I?{/blur}"

    n "..."

    n "{k=1}Who are you, really?{/k}"


    MC "..."

    MC "I DO remember where I saw the other red scarf, even if you don't."

    MC "We left it right next to your body."

    n "...!?"

    scene black

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}SHIORI IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}T W O M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    $ persistent.hikaru_dies = True

    $ persistent.loop1 = True


    return

label hikaru_distrust:

    show hik shocked
    with dissolve

    hikaru "{i}...Wait.{/i}"

    n "Their head lifts slowly."

    hikaru "{k=2}...You don’t...{/k}"

    hikaru "{sc=3}Where is your heartbeat?{/sc}"

    n "Huh?"

    n "They jolt upright."

    play sound "sfx/suzu.mp3"

    show hik rage:
        zoom 0.5
        xalign 0.5
        yalign 0.2
        xoffset 0
        yoffset 400


        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        linear 0.1 zoom 0.4 yoffset 250
    with sshake



    hikaru "{size=+4}{sc=5}Where is it!?{/sc}{/size}"

    MC "Hikaru--"

    hikaru "{sc=4}No! Stay back--!{/sc}"

    hikaru "{k=2}I trusted you. I let myself believe--{/k}"

    MC sadcl "*sigh* I was so close."

    hikaru "{sc=4}You’re not [persistent.player_name]. You’re not--{/sc}"

    n "Wait a minute."

    $ hsword = True

    play sound "sfx/shing.wav"

    n "Hikaru draws their sai and points it at you. At [persistent.player_name]. At..."

    n "...wait."

    show hik panic
    with vpunch

    hikaru "The {color=#ff0000}red moon{/color}... I'm..."

    hikaru "{i}...I'm next.{/i}"

    MC yan "..."

    hikaru "{sc=6}What did you do to [persistent.player_name]!?!?{/sc}"
    with sshake

    n "A sigil flares against your side, meant to burn and cleanse evil spirits. But you are more than that."

    n "In fact, defeating Hikaru is far too easy for you."

    scene black

    play sound "swing.wav"
    show combo_slash_2
    $ renpy.pause(0.1, hard=True)
    stop sound

    play sound "swing.wav"
    show combo_slash_3
    $ renpy.pause(0.1, hard=True)

    with sshake
    pause 0.1

    n "You overpower Hikaru easily as they fall to their knees."

    scene moon7
    with fade


    show hik panic:
        zoom 0.5
        xalign 0.5
        yalign 0.2
        xoffset 0
        yoffset 400


        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with sshake

    hikaru "{k=2}...ngh--{/k}"

    n "There is a dark gash on their shoulder... resembling the one on the dead dog ..."

    n "You did it? But how come I don't--"

    MC yansm "You done?"

    hikaru "{sc=5}N-no--!{/sc}"

    MC "Well, at least I can reunite the both of you now."

    scene black
    with fade

    play muzak "sfx/hikaru_eaten.wav"

    n "Hikaru--"

    hikaru "{k=-2}Ngh--!{/k}"

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

    n "It’s wet again. Louder this time. Closer."

    hikaru "{k=3}S-stay--...!{w} a-away...!{/k}"

    n "They’re crying now.... You..."

    n "No.... Hi-Hikaru...."

    play sound "sfx/splurt.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    stop sound

    n "There is a faint sound of bone crunching and ribs snapping and I..."


    stop music


    play sound "sfx/slurrp.mp3"

    scene black
    with in_212

    n "I can't hear Hikaru's voice anymore..."

    n "Why did you let me see it?"

    n "Why did you make me watch--"

    n "...Why do I still remember them?"

    n "Why does it still hurt?"

    n "...Why do I care?"

    n "{b}Why--{/b}"

    n "..."

    n "Who are you?"

    n "Who are you really?"

    $ persistent.hikaru_dies = True

    $ persistent.loop1 = True

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}HIKARU IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}T W O M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
