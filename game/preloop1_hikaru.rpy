############# LOOP 1 WHERE EVERYONE IS ALIVE ###########################
label loop1_hikaru_mandatory1:

    scene shrine day with in_182:
        zoom 0.5


    n "Everyone is tense because of the red moon."

    n "You feel like more people will be at the shrine for prayers, so naturally you go there."

    n "The shrine is eerily quiet, though. It's as if something can just appear and you{nw}"

    scene black with in_32


    play sound "sfx/jumpscare.mp3"

    "???" "...Guess who."

    n "Suddenly, a pair of hands cover your eyes and you feel a breath right behind your ears."

    n "You freeze as you can’t tell if you’re breathing or just pretending to."

    play sound "sfx/chukle.mp3"

    "???" "Still jumpy, huh [persistent.player_name]?"

    n "You hear a soft chuckle behind you, a voice that you've heard it a lot of times."

    n "But that person doesn't usually giggle like that."

    n "Who--"

    play music "Hikaru.mp3"

    scene shrine day with out_32:
        zoom 0.5
    show hik happy:
        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.12 yoffset 30
        linear 0.10 yoffset 20
        linear 0.12 yoffset 30
        linear 0.10 yoffset 15
        linear 0.12 yoffset 40
        linear 0.12 yoffset 30
        linear 0.10 yoffset 20
        linear 0.12 yoffset 30
        linear 0.10 yoffset 15
        linear 0.12 yoffset 40
        linear 0.12 yoffset 35
        pause 0.15

    hikaru "Aw, did you forgot about me while you're fighting the Yamakui?"

    n "They finally let go of you, you turn around just to see hikaru."

    n "Didn't hikaru greet you with a cold demeanor when you return? Why is--"

    n "Hold on, let me remember..."

    MC nervous "...Hikaru?"

    hikaru "Surprise."

    show hik worried
    with dissolve

    hikaru "..."

    MC nervous "..."

    hikaru "Hey, are you all right, [persistent.player_name]?"

    n "This... {w=0.2}this part doesn’t feel familiar. But it sounds like it should be."

    show hik worried:
        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.4 zoom 0.55 yoffset 35
    pause 0.5
    scene shrine day:
        zoom 0.7
        xalign 0.5
        yalign 0.5

        ease 0.5 zoom 0.55
    show hik worried:
        zoom 0.5
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.4 zoom 0.4 yoffset 20

    $ _prev_music_volume = _preferences.volumes["music"]
    $ decrease_music_volume(0.3)
    $ renpy.block_rollback()

    n "Hikaru walks forward to touch you, but instinctively you step back, avoiding their outstretched hand."

    MC normal "Yeah, I'm fine. Can you step back?"

    show hik shocked
    with dissolve

    hikaru "Eh?"

    n "Wait. Why did you say that?"

    hikaru "Are you mad of me because I said the armor's too small?"

    MC surprised "What?"

    show hik sad
    with dissolve

    hikaru "You’ve been off ever since you've returned from slaying the Yamakui..."

    MC nervous "{k=-1}Um, ahahaha...{w=0.2} No, of course not. {w=0.2}I'm just... {w=0.3}{cps=10}tired, is all.{/cps}{/k}"

    hikaru "Ah, I... see."

    MC nervous "{k=-1}Sorry if I’ve been weird. I just...{/k}"

    MC nervous "{bt=1}I don’t know why this feels so strange right now.{/bt}"

    show hik angry
    with dissolve

    hikaru "But you remember what we are, {w=0.2}right?"

    n "Your stomach turns. What are you supposed to say to that?"

    MC nervous "{cps=40}Of course I do.{/cps}"

    n "You hear yourself answer without even thinking."

    hikaru "Really now?"

    show hik angry:
        zoom 0.4
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 20
        xoffset 0

        linear 0.4 zoom 0.48 yoffset 35

    n "They step closer and you feel like they're breaching your personal space. You want to leave."

    n "If you're together, then it should be okay to stay close like this {w}right?"

    MC confused "{size=*0.95}Hikaru, when did we...?{/size}"

    show hik normal
    with dissolve

    hikaru "...got together?"

    show hik happycl
    with dissolve

    hikaru "Our anniversary is next month, Dummy. Or did you forget that, too?"

    n "You don't remember any of that happening."

    n "But they sound so certain.... {w}Well, it’s easier to agree than to argue with something that might be true."

    n "You can find out later."

    MC nervous "{w=0.2}Right. I remember."

    show hik worried
    with dissolve

    hikaru "Do you? {w=0.2}Did the Yamakui knock your head so hard you had amnesia?"

    show shrine2 as wave_overlay behind hik:
        function WaveShader(amp = 0, melt="both", melt_params=(10,1.0,0.1))
        zoom 0.5
    with dissolve

    $ decrease_music_volume(0.3)
    $ renpy.block_rollback()

    n "Their fingers brush your arm to calm you down, to ground you, instead you feel something crawling upwards."

    MC nervous "{bt=1}Yeah! Yeah, I just need time to readjust.{/bt}"

    hikaru "Is that all it is?"

    MC nervous "{k=-1}Of course. What else would it be?{/k}"

    n "You regret the question the moment it leaves your mouth."

    n "Hikaru's expression sharpens for half a second before settling back into softness."

    show hik ex_blush
    with dissolve

    hikaru "I missed you so much, [persistent.player_name]..."

    hikaru "I'm really glad you got to return, even though you're...{w=0.1} weird now."

    MC sad "Yeah. I’m sorry."

    show hik sad
    with dissolve

    hikaru "Don't be. I think... {w}I think you just need to rest."

    n "Their hand lingers on your sleeve a moment too long before letting go."

    hide shrine2
    with dissolve

    $ restore_music_volume()
    $ restore_music_volume()

    hikaru "It’s okay. You’ll remember again."

    scene shrine day:
        zoom 0.55
        xalign 0.5
        yalign 0.5

        ease 0.5 zoom 0.5
    show hik sad:
        zoom 0.48
        xanchor 0.5
        xalign 0.4
        yalign 0
        yoffset 35
        xoffset 0

        linear 0.5 zoom 0.4 yoffset 30

    MC nervous "{sc=1}Y-Yeah....{/sc} Yeah! {cps=200}I'm gonna go rest now so see you, Hikaru!"

    scene black with out_212
    stop music fadeout 1.0

    n "You feel watched all the way down until Hikaru dissapears from view."

    n "You try to shake that feeling away, but you can't forget how Hikaru's eyes look like watching you leave."

    n "Hey..."

    n "What if Hikaru's the one being right and you just forgot?"

    n "Don't you think it's worth asking around for?"

    $ loop1_hikaru_mandatory1 = True

    #return

label loop1_hikaru_mandatory2:

    $ hsword = True

    scene dojo day with in_182:
        zoom 0.5
    show hik serious:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 25
        xoffset 0
    with dissolve

    hikaru "Hey."

    n "Hikaru is training today, their scarf is billowing eveyr time they move."

    n "You wonder why they are wearing a scarf. Isn't it unconvenient for battles?"

    MC annoyed "Why do you wear a scarf to battle?"

    show hik worried
    with dissolve

    hikaru "...Huh?"

    n "Hikaru's eyes alternate between you and the scarf, brows furrowing, as if you're asking a ridiculous question."

    play music "Tense.ogg"

    show darken
    with dissolve

    hikaru "It's because you gave it to me."

    MC surprised "...I did?"

    hikaru "Yes... You said so I don't get cold."

    MC annoyed "...I really don’t remember."

    show hik shocked
    with dissolve

    hikaru "...What?"

    show hik shocked:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 25
        xoffset 0

        ease 0.1 xoffset 16
        ease 0.1 xoffset -16
        ease 0.09 xoffset 12
        ease 0.09 xoffset -12
        ease 0.08 xoffset 8
        ease 0.08 xoffset -8
        ease 0.07 xoffset 4
        ease 0.07 xoffset -4
        ease 0.07 xoffset 0

    hikaru "Come on... Don't you remember? You tied it around my neck yourself."

    MC sad "...I really don't."

    n "Wrong thing to say."

    show hik rage:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.10 yoffset 10

        linear 0.07 yoffset 40

        # Bounce up slightly (recoil)
        linear 0.07 yoffset 18

        # Settle back down
        linear 0.10 yoffset 25
    with vpunch

    play sound "sfx/stomp.mp3"

    hikaru "{sc=5}What the hell are you talking about?{/sc}"

    n "Hikaru's usual calm demeanor drops immediately, their hands curl into fists at their sides."

    hikaru "{k=-1}You remember Shiori and Yamato.{/k}"

    hikaru "{k=-1}But not {w}{i}me?{/i}{/k}"

    show hik rage:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.10 yoffset 10

        linear 0.07 yoffset 40

        linear 0.07 yoffset 18

        linear 0.10 yoffset 25
    with vpunch

    play sound "sfx/stomp.mp3"

    with hpunch

    hikaru "{b}Not us?{/b}"

    show darken2
    hide darken
    with dissolve



    show hik rage behind darken2:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 25
        xoffset 0

        linear 0.10 zoom 0.36 yoffset 18 xoffset 0

        linear 0.14 zoom 0.55 yoffset -20 xoffset 18

        linear 0.06 zoom 0.52 yoffset -10 xoffset -10
        linear 0.06 zoom 0.55 yoffset -20 xoffset 10
        linear 0.04 xoffset 0

        pause 0.4
    with vpunch

    n "They grab the scarf with both hands and yank it off, thrusting it towards you."

    hikaru "{sc=3}You picked it! You said the red matched the color of the moon--{/sc}"

    hikaru "{sc=3}--and it gave you hope that we'll get through it!{/sc}"

    show hik panic
    with vpunch

    hikaru "You said I looked beautiful in it. {b}You said--{/b}"

    MC panic "{size=*0.95}{cps=30}Hikaru, I... {w}I don’t know what’s happening.{/cps}{/size}"

    hikaru "{k=-1}This isn’t right. This--{/k}"

    hikaru "{sc=5}What if something’s {b}wrong{/b} with you?{/sc}"

    MC annoyed "{w=0.2}Excuse me?"

    hikaru "{sc=2}Do you think this is funny?{/sc}"

    MC nervous "{size=*0.95}{cps=10}Hikaru--{/cps}{/size}"

    hikaru "{cps=150}When you were gone, I waited for you, You promised me you'd get back, but now you return and forgot everything about us--{/cps}"

    MC annoyed "{w=0.2}Hikaru, if we're really together as you said, why don't Yamato and Shiori said anything? Why didn't you hug me when I return?"

    hikaru "{sc=2}Because we're keeping it a {b}secret!{/b}{/sc}"

    MC surprised "{cps=40}Why?{/cps}"

    show hik rage
    with vpunch

    hikaru "*scoffs*"

    hikaru "{size=*0.95}...You're scaring me.{/size}"

    MC hurt "{w=0.2}You’re the one scaring me."

    show hik sad
    with dissolve

    hikaru "{k=-1}...This isn't you.{/k}"


    show hik panic behind darken2:
        zoom 0.55
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset -20
        xoffset 0

        linear 0.08 xoffset -18 yoffset -12
        linear 0.08 xoffset 16 yoffset -28
        linear 0.07 xoffset -14 yoffset -16
        linear 0.07 xoffset 12 yoffset -20
        linear 0.07 xoffset -8 yoffset -12
        linear 0.07 xoffset 7 yoffset -24
        linear 0.08 xoffset 0 yoffset -20

        linear 0.09 xoffset 6 yoffset -16
        linear 0.09 xoffset -6 yoffset -22
        linear 0.10 xoffset 0 yoffset -20

    pause 0.25

    hikaru "{sc=7}{b}Who ARE you!?{/b}{/sc}"

    n "Hikaru stares at you, breathing hard. Their face contorts into something... Is it grief? Suspicion? Anger?"

    show hik panic behind darken2:
        zoom 0.55
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset -20
        xoffset 0

        linear 0.18 zoom 0.34 yoffset 90 xoffset -40

        pause 0.22

        linear 0.4 xzoom -1.0 xoffset 24 yoffset 65 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
        #linear 0.09 xzoom -1.0 xoffset 0 yoffset 80

        linear 0.4 zoom 0.3 yoffset 120 xoffset -60 alpha 0.0

    pause 0.5

    hide hik

    n "Before you could make something out of it, they turn and storm off."

    n "And you’re left standing in the quiet."


    $ loop1_hikaru_mandatory2 = True

    #Return

label loop1_hikaru_mandatory3:

    scene village day with in_182:
        zoom 0.5
    with fade

    $ hsword = False

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

    play music "Idle.mp3"


    hikaru "[persistent.player_name]-san."

    n "Hikaru didn't call you with honorifics before..."

    MC annoyed "What do you want now?"

    show hik sad
    with dissolve

    hikaru "Sorry for yelling at you yesterday, I was... {w=0.2}frustrated."

    MC normal "..."

    show hik serious
    with dissolve

    hikaru "I asked for help and Shiori told me to give this to you."

    MC annoyed "What is it?"

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

    hikaru "A talisman. She said maybe... {w=0.2}maybe your memory problems were caused by trauma. Or worse."

    hikaru "It’s to help you remember."

    MC sad "{w=0.1}...Thanks."

    show red_flash_slow onlayer screens

    n "You take it and it feels quite warm in your hand. You turn it around, but can't find any heat source in it."

    n "Still, you smell something faintly burning, it's coming from the talisman."

    hide show red_flash_slow
    hide frame2
    hide charm
    with dissolve

    n "You pocket it and the odd smell dissapears immediately."

    show hik panic:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 25
        xoffset 0

        # Inhale (shoulders lift quickly)
        linear 0.10 yoffset 10

        # Sharp exhale/tremor
        linear 0.08 yoffset 32

        # Quick shudder (tiny up/down for breath catch)
        linear 0.06 yoffset 20
        linear 0.07 yoffset 29
        linear 0.05 yoffset 25

    # Settle
    pause 0.18

    hikaru "{cps=10}....{/cps}"

    n "You just heard hikaru's breath hitched, as if they had been holding their breath for a while."

    MC nervous "{w=0.2}...What?"

    hikaru "{k=-1}Do you feel anything? I mean--{w=0.1}does it hurt, or tingle, or maybe a flash of something? {w=0.1}Memory? {w=0.1}Emotion?{/k}"

    MC normal "Not really, no."

    hikaru "{w=0.2}Are you {i}sure?{/i}"

    MC normal "Yeah.... Why?"

    hikaru "{k=-1}It’s just--{/k}"

    $ decrease_music_volume(0.5)
    $ renpy.block_rollback()

    show hik worried
    with dissolve

    hikaru "{cps=50}I was hoping it would react.{/scps}"

    MC surprised "{w=0.2}React?"

    show hik panic
    with dissolve

    hikaru "{k=-1}I mean--help. {w}I meant {i}help.{/i}{/k}"

    MC annoyed "Where did Shiori get this, again?"

    show hik serious
    with dissolve

    hikaru "She said the old priest gave it to her."

    MC sad "...Ah."

    n "If it's from Shiori and the priest, then it should be okay right?"

    MC nervous "What is it for, again?"

    hikaru "Sleep."

    MC normal "Oh."

    $ decrease_music_volume(0.5)
    $ renpy.block_rollback()

    hikaru "...."

    MC normal "...."


    stop music

    $ restore_music_volume()
    $ restore_music_volume()

    pause 1.0

    n ".{w=0.3}.{w=0.3}.{w=0.3}"

    pause 1.0


    ## uncomfortable silence

    show hik sad2
    with dissolve

    hikaru "It doesn’t matter. I hope it'll get your memory back someday, maybe it... doesn't work immediately."

    hikaru "You should go back home. It’s late."

    MC sad "And you?"

    hikaru "I’ll be around. If you need me."

    hide hik
    with dissolve

    n "They walk away without another word."

    n "You pull the talisman out again once hikaru turns in a corner and out of sight."

    play sound "sfx/firecrackle.mp3"

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
    show red_flash_slow onlayer screens
    show darken2
    with vpunch

    n "This time the burning smell hits instantly. It stings your nostrils and makes your eyes water. There's a sharp, bitter smell that shouldn't be there."

    n "The paper feels hot and pulsing now."

    MC sad "..."

    n "You drop it, then you--"

    hide frame2
    hide charm

    play sound "sfx/stomp.mp3"
    with vpunch

    n "--stomp on it."

    play sound "sfx/stomp.mp3"
    with vpunch

    n "Again."

    play sound "sfx/stomp.mp3"
    with vpunch

    n "Again."

    hide red_flash_slow

    MC yan "..."

    n "Why? Clearly Hikaru was trying to be nice..."

    play sound "sfx/stomp.mp3"
    with vpunch
    pause 0.3
    play sound "sfx/stomp.mp3"
    with vpunch
    pause 0.3
    play sound "sfx/stomp.mp3"
    with hpunch

    n "You keep stomping until it's almost crumpled now, then kick a patch of dirt over it. As if that makes it disappear."

    n "..."

    scene black with out_212

    n "{blur}Let's just hope hikaru never finds out what you did.{/blur}"




    $ loop1_hikaru_mandatory3 = True

    #return

label loop1_hikaru_mandatory4:

    $ hmask = False

    scene house night:
        zoom 0.5

    n "You’ve just finished cleaning yourself when--"

    play sound "sfx/knock.wav"

    with vpunch
    pause 0.01
    with vpunch
    pause 0.01
    with vpunch
    pause 0.01

    hikaru "[persistent.player_name]-san? Are you home?"

    n "Hikaru."

    MC ysan "..."

    play sound "sfx/knock.wav"

    with vpunch
    pause 0.01
    with vpunch
    pause 0.01
    with vpunch
    pause 0.01

    hikaru "[persistent.player_name]-san?"

    play music "Dark.mp3"

    n "..."

    n "You don’t {i}have{/i} to answer. Of course not."

    n "But..."

    n "Maybe we should hear what they want to say?"

    n "Even though they are so persistent in saying that you two are more than friends, maybe Hikaru is not lying."

    n "You know they're not the type to lie."

    n "{glitch}Maybe just open it a crack...{/glitch}"

    ## so like, the mouse drags to yes, to open the door, but you can still pick no

    call screen horror_forced_menu(items=[
    ("Yes", Jump("hikaru_visit_continued"), False),
    ("No", Jump("hikaru_visit_rejected"), False)
])


label hikaru_visit_rejected:

    scene black
    with fade

    n "You pretend that you're not at home."

    n "That's fine... you must’ve had your reasons. But what are you so afraid of?"

    n "It's just Hikaru..."

    play sound "sfx/knock.wav"

    with vpunch
    pause 0.01
    with vpunch
    pause 0.01
    with vpunch
    pause 1.5

    n "After a series of repeated knocks with no avail, it stops."

    n "And you sit in the darkness alone again."

    scene black with fade
    $ renpy.pause(1.0)
    return

label hikaru_visit_continued:

    n "{glitch}Seems like no matter what your mind wants to do, your body keeps saying yes, huh?{/glitch}"

    play sound "sfx/sliding door.mp3"

    pause 0.3

    show hik serious:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    with dissolve

    pause 0.2

    stop sound

    hikaru "Good evening, [persistent.player_name]."

    MC normal "Hey, hikaru. Did you need something?"

    hikaru "I was just walking by... {w=0.1}and wondered if I should, uh, pay a visit."

    n "That's not true."

    n "They're lying. {glitch}It's really obvious.{/glitch} Hikaru is never good at lying."

    n "But don't you want to know why they’re really here?"

    n "You could say it's a bad time, that’d be fair."

    n "But let's be honest... {w}{i}You’re not really doing anything, and they’re already on your doorstep.{/i}"

    n "So it couldn't hurt to see what they're up to, right?"

    n "Go on. Just a few minutes...?"

    ## mouse creeps toward yes

    call screen horror_forced_menu(items=[
    ("Yes", Jump("hikaru_inside"), False),
    ("No", Jump("hikaru_doorclose"), False)
])


label hikaru_doorclose:

    MC sad "It's a bad time... Sorry."

    show hik sad
    with dissolve

    hikaru "Oh, I-I see. My apologies for intruding."

    play sound "sfx/doorslam.wav"

    scene black
    with fade

    n "Still shutting them out, huh?"

    n "That’s... {w=0.5}fine. I suppose."

    n "You closed the door in their face."

    n "Shame, now we won't know the real reason why they're here."

    scene black with fade
    $ renpy.pause(1.0)
    return

label hikaru_inside:

    n "It's {atl=-#,#,fade_in_text~0.6}F U T I L E{/atl} to resist."

    MC sad "Sorry it's messy."

    show hik happy
    with dissolve

    hikaru "It's a lot cleaner than usual, actually."

    hikaru "Or do you not remember that too?"

    n "Interesting, so they've been here before.  Maybe a couple of times."

    n "You don't remember ever inviting them, though. Odd."

    n "Well, that doesn't matter."

    show hik serious
    with dissolve

    hikaru "{w=0.2}...Is the armor still here?"

    MC normal "Yep."

    hikaru "Can I see it again?"

    n "{i}There it is.{/i}"

    n "I guess just taking a peek at the armor won't cause any harm, {w=0.3}{i}right?{/i}"

    call screen horror_forced_menu_two(items=[
    ("No", Jump("hikaru_armorrefuse"), False),
    ("Yes", Jump("hikaru_armor"), False)
])

label hikaru_armorrefuse:

    MC annoyed "Why?"

    hikaru "Because I am merely curious, that is all."

    MC annoyed "I don't think that's true."

    n "Still--"

    MC nervous "Look... {w=0.3}We don't know much about Yamakui, it could be cursed for all we know."

    MC normal "I'm trying to understand it before anyone else gets hurt."


    hikaru "{w=0.3}...Hmm."

    show hik normal
    with dissolve

    hikaru "I see. But if the Yamakui's dead, then it should be safe, right?"

    hikaru "And... {w=0.3}If it’s really that dangerous, why keep it at all?"

    MC smug "Because I slayed the damn thing. If anyone's protecting the village from it, it should be {b}me.{/b}"

    show hik worried
    with dissolve

    hikaru "..."

    hikaru "Makes sense, I guess."

    hikaru "All right. I won't push."

    n "They turn to leave, but hesitates just past your shoulder."

    show hik worried:
        linear 0.5 xzoom -1

    hikaru "...Still, be careful. Things like that tend to change people."

    hide hik
    with fade

    n "And then they're gone."


    n "If even hikaru suspects something... how long before others start asking, too?"

    scene black with fade
    $ renpy.pause(1.0)
    return


label hikaru_armor:

    n "{glitch}...Very good. Now you know you can't say {i}no.{/i}{/glitch}"

    MC normal "Fine, I guess just a peek wouldn't hurt."

    hide hik serious
    with dissolve

    scene house night:
        zoom 0.5
        xanchor 1
        yanchor 1

        ease 0.5 zoom 0.7 xoffset -420 yoffset -100


    hikaru "..."

    n "Hikaru walks around the armor, inspecting it with furrowed brows."

    n "You don't know what they are actually looking for. There's only dried blood and remnants of flesh."

    n "That's because you haven't washed it at all and left it bloodied like that."

    scene house night:
        zoom 0.7
        xanchor 1
        yanchor 1
        xoffset -420
        yoffset -100

        ease 0.5 zoom 0.5 xoffset 0 yoffset 0
    pause 0.4

    show hik normal:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    with dissolve

    hikaru "Thank you. That's all I need."

    n "That wasn’t so hard, was it?"

    MC normal "All right, since you're here... {w}Want some tea?"

    show hik happy
    with dissolve

    hikaru "Oh, speaking of tea... {w=0.1}I brought some for you."

    MC happycl "Oh, thank you."

    n "You brew the tea hikaru gave you. It looks like a perfectly normal green tea."

    show hik normal
    with dissolve

    hikaru "Shiori said to add the dried ume and dried kombu before you pour the tea over."

    MC nervous "I see... That's {w=0.1}interesting."

    n "You serve the tea for the both of you afterwards."

    n "Since you brew it yourself... {i}it will be fine if you drink it, right?{/i}"

    call screen horror_forced_menu_two(items=[
    ("No", Jump("hikaru_teareject"), False),
    ("Yes", Jump("hikaru_teadrink"), False)
])

label hikaru_teareject:

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show matcha:
        xanchor 0.5
        xalign 0.5
        yalign 0.33
    with dissolve

    n "As soon as the tea is ready, hikaru immediately sips it."

    n "You decide not to."

    show hik worried
    with dissolve

    hikaru "What's wrong?"

    MC "Nothing. I'm... {w=0.1}full."

    show hik normal
    with dissolve

    hikaru "Hmm."

    n "They say nothing more and finish their tea."

    n "What are you so afraid of? You're the one who brews it. hikaru clearly drank that tea and is fine."

    n "So what’s the hesitation?"

    n "Come on. Don’t be rude."

    n "Drink it."

    MC yan "..."

    MC yan "..."

    MC nervous "It’s late."

    hikaru "Mm."

    MC nervous "You should probably head back."

    show hik serious
    with dissolve

    hikaru "Yes. {w}Of course."

    n "Hikaru places the empty cup slowly on the table, eyes never leaving yours."

    show hik smilesad
    with dissolve

    hikaru "Thanks for... letting me see the armor."

    MC normal "Anytime."

    n "They smile, but there’s something distant in it now. As if they expected... something?"

    n "You should've drunk the tea."

    hikaru "Good night, [persistent.player_name]."

    scene black with fade
    $ renpy.pause(1.0)
    return




label hikaru_teadrink:

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show matcha:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.33
    with dissolve


    n "Hikaru drinks theirs and immediately finishes the cup."

    n "Nothing happens."

    n "Of course nothing happens."

    hide frame2
    hide matcha
    with dissolve

    $ haze_active = True
    show haze_effect at haze_transform
    with dissolve

    show hik normal
    with dissolve

    hikaru "Well?"

    n "The cup touches your lips, and you immediately drink it."

    play sound "sfx/gulp.wav"

    show red_flash_slow onlayer screens


    n "The taste of salt hits first, followed by sour... and ended up bitter at the tip of your tounge."

    stop music

    n "You can't breathe, you want to throw up blood, but you swallow it."

    play sound "sfx/gulp.wav"
    with flashred

    MC panic "{k=-1}Gh--!{/k}"

    n "The liquid drags down your throat like broken glass soaked in liquid."

    play sound "sfx/firecrackle.mp3"
    with flashred

    n "You feel it tearing."

    MC hurt "{cps=10}...Aah--{/cps}"

    show hik worried
    with dissolve

    hikaru "Is it too strong for you?"

    MC nervous "{size=*0.9}...No. It’s... {w=0.2}{cps=10}fine.{/cps}{/size}"

    play sound "sfx/firecrackle.mp3"
    with flashred

    play music "spooky.mp3"

    n "The warmth spreads immediately... then turns into burning."

    n "Down, down, down from your throat, into your chest, then ripping your gut apart."

    show hik panic
    with dissolve

    hikaru "Are you okay, [persistent.player_name]?"

    MC sad "{cps=10}...I'm... {w}fine...{/cps}"

    hikaru "Really? You look... mortified."

    show hik worried
    with dissolve

    hikaru "If you hated it that much, maybe--"

    $ haze_active = False
    hide haze_effect
    with dissolve

    play sound "sfx/gulp.wav"
    show hik shocked
    with flashred

    MC mad "{b}I'M FINE.{/b}"

    with vpunch

    n "You sip one more time to make a point."

    n "Big mistake."

    play sound "sfx/gulp.wav"
    with flashred

    n "The tea sloshes past your lips, and your stomach convulses as you force it down your throat again."

    n "The same burn, the same trail of salt, the same taste of your own blood..."

    n "...the same clawing ache in your stomach. Even worse now."

    n "Poison?"

    n "A curse?"

    n "But hikaru looks fine... and you're the one brewing it...."

    MC nervous "{cps=10}...Hhh--D-Did you say what this was? I didn't remember--{/cps}"

    show hik worried
    with dissolve

    hikaru "You drank it last year, and before that. On fact, the four of us did."

    hikaru "Remember the new year's celebration?"

    MC surprised "{w=0.2}W-Wh--"

    play sound "sfx/firecrackle.mp3"
    with flashred

    n "You can’t speak as the heat keeps rising, bile festering behind your throat."

    n "You want to spit it out, but you manage to muster a smile."

    MC nervous "{k=-1}Oh, really? Uh, what did--What did we drink again?{/k}"

    stop music
    show hik normal
    play sound "sfx/suzu.mp3"
    with vpunch

    hikaru "It’s only Obukucha, [persistent.player_name]-san."

    n "A pickled plum brings protection."

    n "Hikaru means well. Of course they mean well."

    MC sad "{size=*0.9}...Thanks. For the tea.{/size}"

    MC normal "{w=0.2}You should probably head out. It’s late."

    show hik smilesad
    with dissolve

    hikaru "Of course."

    hikaru "Feel better soon, okay?"

    MC normal "{size=*0.9}...Mm.{/size}"

    show hik smilesad behind darken2:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0

        linear 0.4 xzoom -1.0 xoffset 24 yoffset 65 matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))
        #linear 0.09 xzoom -1.0 xoffset 0 yoffset 80

        linear 0.4 zoom 0.3 yoffset 120 xoffset -60 alpha 0.0
    play sound "sfx/sliding door.mp3"

    $ hmask = True



    n "The door slides behind them."


    n ",,,"

    n "..."

    n "..."

    MC mad "..."

    scene house night:
        zoom 0.5
        xalign 0.5
        yalign 0.5

        linear 0.15 zoom 0.8 xoffset -100

    play sound "sfx/clatter.mp3"


    n "You lunge for the tray, rattling the cups."

    n "Your breath shakes."

    play music "heavy breathing.mp3"

    scene house night:
        zoom 0.8
        xoffset -100
        xalign 0.5
        yalign 0.5
        parallel:
            linear 1.0 zoom 0.82 xoffset -104 yoffset 2 blur 3
            linear 1.0 zoom 0.8 xoffset -100 yoffset -2 blur 1
            repeat
        parallel:
            linear 0.2 xoffset -101
            linear 0.2 xoffset -99
            linear 0.2 xoffset -100
            repeat

    MC "{sc=3}...Disgusting... {w}Disgusting... {w}Disgusting...{/sc}"

    n "You carry the tray outside and rip the door open and--"

    play sound "sfx/sliding door.mp3"


    scene black
    show darken2
    play sound "sfx/prang.mp3"
    with sshake

    n "--you throw the tray. Well, more like you slammed the tray into the ground that every glasswares breaks apart."

    MC mad "{cps=10}{sc=6}Haa... {w}Haa... {w}Haa...{/sc}{/cps}"

    MC mad "..."

    n "Why?"

    n "It’s just tea."

    n "Why are you shaking?"

    MC mad "{sc=8}{k=-1}Shut--{/k}{/sc}"

    MC mad "{cps=10}{sc=7}...Ngh.{/sc}{/cps}"

    play sound "sfx/doorslam.wav"

    scene house night:
        zoom 0.5

    with hpunch

    n "You step back inside, close the door and lean against the wood and breathe until your legs stop trembling."

    n "It's just tea, [persistent.player_name]..."


    $ loop1_hikaru_mandatory4 = True

    #return

label loop1_hikaru_mandatory5:

    $ ysword = False

    play music "Idle.mp3"

    scene shrine day with in_212:
        zoom 0.5

    n "You enter the shrine, looking for Shiori."

    n "You have something important to ask her today..."

    show shi normal at shiori_skipp:
        xalign 0.7
    with dissolve
    pause 0.6
    stop sound
    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 600

    with dissolve

    n "Coincidentally, Yamato's there too, for some reason."

    shiori "Ara~ Good morning [persistent.player_name]-sama!"

    show yam serious
    with dissolve

    yamato "Tch..."

    MC normal "Shiori-chan, I have something to ask you. Might as well ask Yamato as well."

    show shi smug
    with dissolve

    shiori "Oho~? Sounds serious."

    MC nervous "...Was I ever... {w}with hikaru?"

    show shi surprised
    show yam surprised
    with vpunch

    shiori "Eh?"

    yamato "{i}...Hah?{/i}"

    MC nervous "I mean... like {i}that.{/i}{w} Close.{w} Before the mountain. Were we...?"

    n "Both Yamato and Shiori stare at each other with disbelief."

    shiori "I don’t think so...? You two get along, but I’ve never heard hikaru say anything like that."

    shiori "Did something happen, [persistent.player_name]-sama?"

    show yam happy
    with dissolve

    yamato "Pffft... Keh."

    show yam happycl at left:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 600

        ease 0.05 yoffset -10
        parallel:
            ease 0.08 yoffset 10
            ease 0.08 yoffset -10
            ease 0.1 yoffset 0
            repeat 4

    yamato "{sc=8}AhahahaHHAHAHhahaha!{/sc}"


    yamato "{k=-1}[persistent.player_name]? With hikaru!?{/k}"

    MC annoyed "{size=*0.95}What's that supposed to mean?{/size}"

    yamato "{b}No fuckin' way!{/b}"
    with vpunch

    show yam evil
    with dissolve

    yamato "You’re loud and anoying. Hikaru won't talk unless ya kill 'er pet or somethin'!"

    yamato "{k=-1}Ya ain’t their type. Not by a long shot.{/k}"

    show shi normal:

        zoom 0.26
        xanchor 0.5
        xalign 0.5
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0
        xoffset 220

        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset -12
        linear 0.05 xoffset 12
        linear 0.05 xoffset -8
        linear 0.05 xoffset 8

        ease 0.2 xoffset 0
    show shi annoyed
    with vpunch

    shiori "{cps=12}Yamato-kun~ don’t be rude!{/cps}"

    show yam annoyed
    with dissolve

    yamato "Oi, I’m just sayin’ the truth."

    yamato "{k=-1}If you two were hidin’ somethin’, I’d have noticed. Shiori too.{/k}"

    show shi worried
    with dissolve

    shiori "{cps=12}Mm... I think so, right?{/cps}"

    show yam serious
    with dissolve

    yamato "{bt=1}Did the Yamakui hit yer head so hard ya start hallucinating a damn relationship?{/bt}"

    MC sad "..."

    MC sadcl "{size=*0.95}...I-I see.{/size}"

    shiori "{cps=22}You sure you're okay, [persistent.player_name]-sama?{/cps}"

    MC normal "I’m fine."

    yamato "Yeah, so that's the dumbest shit I've ever heard since ya came back from that damn mountain."

    shiori "If something’s bothering you, I can ask hikaru myself?"

    MC panic "{w=0.2}No. Don’t."

    n "Behind you, by the incense basin, an old woman mutters something... But your sharp ears catches it."

    $ decrease_music_volume(0.3)
    $ renpy.block_rollback()

    show oldwoman at center:
        zoom 0.48
        ypos 1.55
    hide yam
    hide shi
    show darken
    with dissolve

    "Woman" "Please... I pray [persistent.player_name]-sama doesn’t get too close to that one..."

    show yam angry:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0
        xoffset 400
    with easeinleft

    yamato "{k=-1}T’fuck did ya just say?{/k}"

    $ restore_music_volume()
    hide darken
    with dissolve

    "Granny" "I mean... Don’t you think hikaru has been... {w=0.2}off lately?"

    "Granny" "Just like Karasuma-san was. Before he--"

    yamato "Tch. This village ran one man off ‘cause it got spooked. An’ now ya wanna do it again to his kid!?"

    yamato "{b}Hikaru’s nothin’ like their father!{/b}"

    "Granny" "How would you know that?"

    show shi annoyed at right, bounci:
        zoom 0.26
        xanchor 0.5
        xalign 0.5
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0
        xoffset 450
    with vpunch
    play sound "sfx/stomp.mp3"

    shiori "Hikaru-san always helps me at the shrine, and will never hurt a soul!"

    "Granny" "You weren’t there that night..."

    yamato "{k=-1}Y’wanna blame someone, go stare at yerself in a mirror ‘til it cracks.{/k}"

    play sound "sfx/shing.wav"
    with vpunch

    $ ysword = True

    n "Yamato unsheathes his blade. Just a little."

    hide oldwoman
    with dissolve

    n "The old woman imemdiately back away, hands still clutching prayer beads."

    yamato "Tch. Damn cowards."

    scene black
    with dissolve

    n "You know... hikaru’s father vanished on the last Red Moon."

    n "Some say he chased the Yamakui, some say he tried to stop it."

    n "Some say he never even made it past the gates."

    n "You know how paranoia works. Plant one seed of doubt and suddenly it spreads like wildfire."

    n "Hikaru was only twelve back then, remember?"

    MC yan "No."

    n "You don't?{w} Huh."

    MC yan "..."

    n "Hm? How do I know that...?"

    MC yan "..."

    n "Mmm... {w}Odd. {cps=40}How {i}DO{/i} I know that when you don't even remember that?{/cps}"


    $ loop1_hikaru_mandatory5 = True

    return
