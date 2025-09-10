label loop2_yamato:


    play sound "sfx/wood_shift.ogg"

    n "You can feel the voices crawling up your spine... Someone praying at the shrine."

    n "Not to the kami-sama, but to something more anicent and sinister.. Blasphemous at it's core."

    n "And it draws you right to it, your blood feeling right at home."

    n "You're familliar with the voice. Of course it's Yamato."


    n "He’s... bent forward too far. Spine curled like a beast crawling toward a scent."

    play sound "sfx/whisper_low.ogg" loop

    n "He's clutching his stomach."

    n "His skin ripples, something is moving underneath. A worm-like creature, crawling under the surface."

    yamato "...rggna..."

    ## screen flicker

    n2 "GhhhhhH."

    yamato "{size=+4}{color=#552200}{w=0.2}Master{/w} {w=0.15}of{/w} {w=0.15}the{/w} {w=0.25}earth...{/color} {w=0.4}{color=#772200}Awake...{/color} {w=0.3}{color=#aa0000}AWAKE.{/color}{/size}"

    yamato "{color=#444400}{size=+2}daichi no nushi yo... {w=0.3}mezameyo, {w=0.3}{fast}mezameyo.{/fast}{/size}{/color}"

    pause(0.6)

    yamato "{size=+5}{color=#550000}Grant... me... strength...{/color} {w=0.3}{color=#aa4400}GRANT ME... FLAME.{/color}{/size}"

    yamato "{color=#773300}Ware ni... chikara o... {w=0.4}honou o... sazuke tamae...{/color}"

    pause(0.8)

    yamato "{size=+6}{color=#330000}RISE{/color} {w=0.2}from the... {color=#550000}depth...{/color} {w=0.4}{color=#772200}RISE{/color} {w=0.25}from the... {color=#993300}STONE.{/color}{/size}"

    yamato "{color=#220000}daichi no nushi yo... {w=0.4}Shin'en kara... {w=0.3}iwa kara... {w=0.3}ideyo...{/color}"

    n "Yamato lifts his head, you can see his eyes are rolled white."

    n "Blood starts to drip from his mouth that doesn’t stop moving, even when he’s no longer making sound."

    n2 "Don't have claws on your own, so you ask for another."

    n2 "HhhahhHhAHAAHHhh."

    n "You take a step back, eyes still glued to Yamato's twitchy figure."

    yamato "Heh."

    yamato "You came t’watch, huh?"

    yamato "Maybe now you’ll see what I become."

    yamato "When I pray t’something that can beat ya."

    n2 "Yamato."

    n2 "Yamato. Yamato. Yamato..."

    n2 "Little mutt crawling to the hole."

    n2 "Wants new teeth, ha?"

    n "The altar catches fire, then everything is enveloped in smoke..."

    if not persistent.hikaru_dies:

        hikaru "YAMATO!"

        n "Hikaru rushes in, Sai in hand."

        yamato "...!"

        hikaru "Yamato... What are you doing!?"

        yamato "Tch... Look at ya screamin’ like it matters now."

        yamato "Ya people always looked at [persistent.player_name] like they was gonna save us, but no, they returned a monster."

        hikaru "What!?"

        MC "He's gone insane because of his jealousy."

        hikaru "Yamato, this isn’t you at all--"

        yamato "I trained twice as hard. Bled for this place. And what do I get?"

        hikaru "So you--"

        hikaru "You thought summoning something worse was the answer?"

        yamato "{fast}I asked for power.{/fast}"

        yamato "And I fuckin’ got it."

        yamato "Th' damn Yamakui is still alive, so I'll have the power to kill it!"

        hikaru "Yamato, please--"

        n "The ground shudders. and Hikaru stumbles back, almost slipping on blood-slick stone."

        hikaru "What did you CALL!?"

        n "Yamato jerks suddenly--like something inside him pulls. His eyes roll back, lips peeling in a crooked smile."

        hikaru "Yamato--!!"

        n "He drops to one knee, laughing through blood."

    n "..and Yamato's gone."



    ### Hikaru or Shiori watches
    if not persistent.shiori_dies:

        n "You feel a presence behind you."

        shiori "...Yamato-kun?"

        n "Her voice cracks as she steps closer. She’s trying not to cry."

        shiori "[persistent.player_name]...? What was that just now?"

        shiori "W-What’s going on?"

        MC "...He’s gone, Shiori."

        shiori "That wasn’t a kami, was it?"

        shiori "The prayers... The chanting's all wrong..."

        MC "He’s beyond saving now."

        shiori "..."

        shiori "Stupid, stupid Yamato..."

        shiori "Always acting like he's the only one who suffers... {w}always pretending he's strong..."

        shiori "But he just needed someone to hug him. Someone to tell him it’s okay."

        n "Her lips tremble... {W}then curl up in a slow, bitter smile."

        shiori "Everything can be fixed."

        shiori "Right? I mean... if you just love someone enough..."

        shiori "Even the Yamakui... it just needs someone to see it as it really is."

        shiori "Maybe it’s angry because it’s lonely, and because we’re all so mean to it."

        shiori "But if we just... sat down... maybe lit some incense... and just talked..."

        shiori "It’d understand."

        shiori "It’d stop, right?"

        MC "..."

        shiori "If only I was given the chance to talk to it..."

        shiori "Because love always wins, doesn’t it?"

        n2 "Ha."

        n2 "She’s gone too."

        n2 "{fast}Split her open and see what 'love' looks like inside.{/fast}"

    else:

        n2 "He called it."

        n2 "Now let’s see if he can contain it."

    scene black with fade
    centered "DAY OF RED MOON."

    n "The sky is fully red now, it's just mere hours before the red moon is full."

    n "And of course, you saw the man practically crawling towards you."

    n "Limbs jerking, all bent up with one hand dragging behind, flopping."

    n2 "Look, look who is crawling back."

    yamato "...tonight."

    n "His voice folds in on itself, something else is speaking from behind him... {w}or from inside him."

    play sound "sfx/double_voice.ogg"

    yamato "T-tonight--t--tonight--"

    yamato "...Red moon..."

    yamato "Mine now."

    yamato "I will--"

    yamato "Tear you--"

    yamato "Tear--"

    yamato "YOU--"

    n2 "Growl all you want, mutt."

    yamato "No more GODS."

    yamato "YAMAKUI."

    yamato "KILL."

    yamato "TONIGHT--"

    yamato "{size=+10}{color=#ff2200}{b}TONIIIIIIIIIIIIIIIIIIIIIGHT--{/b}{/color}{/size}"

    n "He lunges--"

    n "But before you can even unsheate your claws--"

    MC "Hn?"

    n "You catch a glimpse of his back folding into the treeline, as if something pulled him out from beyond the dimension."

    n2 "Hunting meat."

    n2 "Interesting."

    scene black
    with fade

    n "...Yamato wants you dead."

    n "So of course you face his challenge head-on."

    n "He's no longer your friend, nor someone you look up to."

    n "So naturally you'd have to fight him, save him from himself, right...?"

    n2 "No."

    n2 "{i}Eat the meat before it rots beyond consumption.{/i}"

    n "..."

    n "The red moon is in it's full glory now."

    n "Yamato appears again while everyone is hiding in their houses."

    n "This time, he's less twitchy... {w}but a lot more mutated than before."

    n "His sword slides free."

    play sound "sfx/blade_draw_scream.ogg"

    n "It screams."

    n "I’ve never heard metal scream. I--I don’t know what that was."

    n "No. No, that sword is alive now--"

    yamato "Oni."

    yamato "Time to die!"

    n "That is no longer Yamato's voice anymore..."

    n "No. Yamato, stop. Please--just--stop this--"

    n "That’s not you talking!"

    n "You’re still in there! Please!"

    yamato "The master of the earth has blessed me!"

    n "Yamato raises his sword in an unexpected speed, and zig-zagged towards you."

    n "You draw your own weapon the moment he strikes."

    n "The impact is enough to crack the ground you're standing on."

    n2 "FASTER."

    n2 "TEAR HIM."

    n "No, please, this is wrong...!"

    n "Yamato used to spar with me under this same moonlight."

    n "We used to laugh. He used to swear when I tackle him down."

    n "Now he’s... he’s--"

    yamato "ThE ReD MoON wiLL be YoUR FuNeRAl--"

    n "You block, parry, twirl--"

    n "The blade in your hands splits Yamato’s in two, but it was only an afterimage."

    n2 "Still too slow--!"

    n "You kick him right at his stomach."

    yamato "...Nnn--!"

    play sound "sfx/vomit_eldritch.ogg"

    n "He recthes, out comes string of black, twitching, writhing things."

    yamato "Still--still ain’t done--!"

    yamato "I’ll break ya in pieces. One piece for the friend I can't remember, and another for [persistent.player_name]--"

    play sound "sfx/charge.ogg"

    scene black with slowdissolve
    play sound "sfx/slash_deep.ogg"
    $ renpy.pause(1.0)
    play sound "sfx/thud_body.ogg"

    n "Everything stops."

    n "Yamato hits the stone floor as you hover above them."

    n "He’s kneeling now, fists clenched so tight, muttering, mumbling, that same chant again."

    n "Asking for power, for blessing..."

    yamato "Daichi no nushi yo..."

    yamato "Mezameyo..."

    yamato "MeZaMEyo..."

    n "He keeps chanting it, again and again and again--"

    n2 "Ahhh, little mutt prays so sweetly."

    n2 "Didn’t know he was feeding me."

    n "You take one step forward."

    MC "...yo...meza...me...shunu chiida..."

    play sound "sfx/glitch_click.ogg"

    MC "...eeyotaz...eh...o...kara...ta...ware..."

    yamato "...!"

    MC "...o...meza...meza...yo...nush...chiida...nush...chiida..."

    play sound "sfx/heartbeat_deep.ogg"
    $ renpy.pause(0.6)

    yamato "...What... {w}what the fuck are you saying..."

    MC "Your prayers, don't they go something like this?"

    yamato "You’re... saying it backwards--"

    MC "Yamato-kun..."

    MC "Who do you think the master of the earth is?"

    yamato "No--!"

    yamato "No--!"

    yamato "NO--!"

    yamato "YOU’RE--"

    MC "{size=+4}{color=#aa0000}Mountains. Earth. Same thing{/color}{/size}"

    MC "The mountains belongs to me, Yamato."

    play sound "sfx/bone_creak.ogg"
    $ renpy.pause(0.5)

    n "Yamato scrambles back immediately as realization slaps him in the face."

    yamato "GHhhAAAGhghh--"

    MC "I gave you teeth, claws, power, eeeeverything you wanted."

    MC "But it'll never be as strong as mine."

    n "His fingers snap sideways as they claw at his own chest."

    play sound "sfx/scream_warp.ogg"

    yamato "I WASN'T TRYING TO--"

    MC "But you prayed to me."

    MC "ME."

    me "Yamakui."

    ## yamato sfx scream

    n "You step over the ruin of what used to be Yamato."

    n2 "Charred is better than rotting."

    n "Your foot lands beside his cheek."

    n "The one that used to sneer at you, call you dumbass, and taught you how to--"

    n2 "No. He taught YOU."

    n2 "He's nothing to me."

    play sound "sfx/flesh_squelch_soft.ogg"

    n2 "O N L Y M E A T."

    n "I--"

    play sound "sfx/squelch1.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/gush.ogg"
    $ renpy.pause(0.3)

    n2 "JjJJuIiiiiiICe--"

    play sound "sfx/bite_rip.ogg"

    n "The texture hits first, then the feeling of tendons snapping. It feels chewy in your mouth."

    play sound "sfx/wet_tear1.ogg"
    $ renpy.pause(0.3)

    n2 "Mmmmgh--hhhnnnHH."

    n "Please stop."

    n "Stop. He's my friend. My friend. My best friend--"

    n2 "A friend? Really?"

    n2 "He was so ready to tear this face apart."

    play sound "sfx/gulp.ogg"

    n "I am going to puke, urk--"

    play sound "sfx/squelch2.ogg"
    $ renpy.pause(0.2)
    play sound "sfx/lick_wet.ogg"

    n2 "GLLLRHkkk... HHhhhehhehh..."

    n "I can’t--I can’t watch this--"

    n2 "LOOK. LOOK. {w=0.2}SEE."

    n2 "There is no god to pray to."

    n2 "Your kami-sama has turned his back on you."

    play sound "sfx/bite_soft.ogg"

    n "I don’t want to exist anymore."

    n2 "...One more to go."

    $ persistent.yamato_dies = True

    $ persistent.loop2 = True

    ## at the end of the route yamato dies

    yamato "I ded."

    return
