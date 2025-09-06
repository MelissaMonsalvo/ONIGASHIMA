### CONTAINS NON MANDATORY EVENTS FOR LOOP 1

label loop1_shiori_nonmandatory1:

    n "When you see shiori later that day, she is in the middle of tying something."

    n "You see strings attached across the trees, dozens and dozens of them."

    n "And dangling from each string are effigies. So many of them you can't count."

    mc "Whoa. You’ve been busy! Is there a festival coming...?"

    shiori "Oh, hi [player_name]-sama! I'm just making everyone's effigies for the upcoming red moon."

    mc "...Everyone?"

    shiori "Mm. You. Yamato. Hikaru. And of course the other villagers too!"

    mc "All right... But do we still need them?"

    shiori "Nothing's wrong with praying for protection right?"

    shiori "Or blessing. {w}Well, depending on who's watching~"

    n "The paper effigies sway gently, even though there's no wind."

    n "One has a red thread stitched around its throat. Another has a crude symbol carved across its belly."

    n "You finally find the one with your name, it's upside down."

    mc "Seriously, Shiori-chan?"

    mc "That’s how you hang mine? Did I do something to offend the spirits?"

    shiori "Oh? Maybe I tied it wrong~"

    mc "Oi, what’s next? You gonna paint on my door with blood?"

    mc "Haha. {w}Maybe I’m the sacrifice this year."

    n "Well, that was morbid."

    shiori "Um, I, sorry--"

    mc "That's fine, I’ll fix it myself."

    play sound "sfx/paper.ogg"

    n "You reach up turn your effigy upright."

    n "It spins slowly, {w}slowly, {w}sloooooowly, {w}then stops."

    n "It's facing you now, and right on cue, the strands of your hair rise."

    shiori "Oh. It's watching."

    mc "Huh?"

    shiori "Don’t you feel it?"

    shiori "Something is watching us now."

    n "You look around, there's no one else around but the two of you."

    ## audio dies now

    n "No one."

    n "Not even a sound."

    mc "...Alright. Creepy much? Can’t we wait 'til sundown to summon things?"

    shiori "..."

    n "You turn back to the effigies that somehow are still swaying, but not all of them."

    n "Even though... there's till no wind."

    n "You look again at yours, it's upside down again, rocking back and forth."

    n "Back and forth."

    n "Back and forth."

    n  "Back..."

    n "...and..."

    n "...forth."

    menu:
        "Fix it":
            n "You reach for it again."

            play sound "sfx/paper.ogg"

            n "The string creaks as you pull it and the other paper effigies shakes lightly."

            n "You watch as it twists and spins, then turns upside down again."

            jump stubborn_lilthang
        "Let it be":
            mc "Ah, whatever."
            return

label stubborn_lilthang:
    menu:
        "Fix it":
            play sound "sfx/string_creak.ogg"

            n "You fix it again, but it turns again."

            mc "Tche, what's wrong with you?"

            n "You hold it still this time, trying to pin it with brute strength."

            n "It turns in your hand. Again, by itself."

            n "Somehow, it' ends up upside down again."

            mc "Stubborn little thing..."

            shiori "Guess some things don’t want to face heaven, eh [player_name]-sama?"

            mc "The hell does that mean?"

            shiori "Maybe you should pin it with a clip?"

            mc "Yeah, guess that'll help."

            n "Shiori hands you one of her hair clips and you literally stabs it with the pin to keep it straight."

            mc "There. Fixed."

            jump stubborn_lilthang2


        "Let it be":
            mc "Ah, whatever."
            return

label stubborn_lilthang2:

    n "But it turns again, defying gravity and all of common sense."

    n "Upright, tilted, then... upside down again."

    mc "The hell is wrong with this thing!?"

    mc "Stay still—"

    play sound "sfx/paper.ogg"

    mc "I said stay—!"

    n "You snatch it with such forse that you don't realize you're crushing the paper spine without thinking."

    n "You twist the string tight, pull until it bites into your skin."

    mc "Stay. {w}Up. {w}Up! You little--"

    play sound "sfx/fabric_rip.ogg"

    n "You want to tear the damn thing into half, but then you realize something..."

    n "Shiori is watching you."

    shiori "Ara~"

    mc "...What?"

    shiori "It's just funny to see the hero that defeated the Yamakui is defeated by a piece of paper~"

    mc "Tch, whatever. I'm leaving."

    shiori "Stay safe~"

    n "You stomp away, not realizing that behind you, the broken effigy twitches once more, as if mocking you one final time."

    play sound "sfx/paper.ogg"

    $ loop1_shiori_nonmandatory1 = True

    return

############ FIRST NON MANDATORY EVENT STOPS HERE ###############


label loop1_shiori_nonmandatory2:

    n "You were just going to enter the shrine when you hear someone cursing inside "

    yamato "Tch... damn it--"

    play sound "sfx/flick.ogg"

    yamato "Ow--! The hell was that for?!"

    shiori "For swearing at the shrine and being so dumb you almost get yourself killed, of course!"

    yamato "Tch... ain’t my fault the damn rock gave out."

    play sound "sfx/flick.ogg"

    yamato "OW! Again?!"

    shiori "I warned you. No swearing when I’m treating you!"

    yamato "Ya didn’t warn me not to drop a tree trunk on my own leg too, didn'tcha?"

    shiori "Because~ I thought you have common sense!"

    n "Shiori gently dabs at Yamato’s arm."

    play sound "sfx/bandage.ogg"

    yamato "...Tch. I was just tryin’ to see if I could hold the damn thing up."

    shiori "With your bare arms?"

    yamato "That's how strength training works!"

    shiori "No, that's how you get broken bones!"

    yamato "Nothing's breakin'."

    shiori "No, but if you twitch again, I might help it along~"

    n "She smiles sweetly."

    yamato "Oi. You tryna kill me now?"

    shiori "Of course not~ But you’re very annoying when you’re hurt."

    shiori "And you use too many dirty words."

    yamato "Goddamn--{nw}"

    play sound "sfx/flick.ogg"

    yamato "Tch!"

    shiori "See? Again."

    n "He mutters something under his breath."

    play sound "sfx/flick.ogg"

    yamato "OW!! Okay, okay, fine! I’ll shut up!"

    shiori "Good boy, Yamato-kun~"

    n "She tapes the bandage down neatly and pats his shoulder."

    yamato "Hhff... {w}Thanks, I guess."

    shiori "Try not to break anything again before the red moon comes?"

    yamato "No promises."

    yamato "I’m still gonna try liftin’ it tomorrow."

    shiori "Ughhhh. This one's hopeless."

    shiori "Fine! Die! I'll write \"Here Lies Idiot\" if your tombstone!"

    n "Shiori steps back to the shrine, mumbling. You decide to see her next time since she seems to be in a bad mood."

    $ loop1_shiori_nonmandatory2 = True

    return

label loop1_shiori_nonmandatory3:

    show shiori smile at midright

    shiori "Good morning, [player_name]-sama."

    mc "Yo! Morning~ You're up early, huh?"

    shiori "Sorry for intruding~ I was looking for you."

    mc "Aw, really? What for?"

    shiori "Mmmmm~ I wanted to ask about the armor. You know the one~"

    mc "Armor? Oh, you mean Yamakui's?"

    shiori "Yeah... You know... Yamato said something strange."

    shiori "He said... the armor doesn’t match the old stories."

    mc "...What?"

    mc "The hell does {i}he{/i} know?"

    mc "What gives Yamato the right to say anything at all?"

    shiori "I just wanted to understand. You would’ve told me, right?"

    mc "You could’ve just asked me, instead of believing him."

    shiori "Yamato gets... like that sometimes. You know he's mad he didn't get to battle the Yamakui instead."

    shiori "So... He said... He said the armor doesn’t belong to the Yamakui at all."

    mc "Ha."

    ## mc laugh, sfx?

    mc "So what-so what, I made it up? I fished it out of some cave and rolled it in some animal blood?"

    shiori "That’s not what I said--"

    mc "But it’s what you’re {i}thinking.{/i}"

    shiori "..."

    mc "Yamato never even SAW the damn thing!"

    mc "I was the one who climbed, and fought, and stabbed--"

    mc "It screamed and bled and bit me, Shiori-"

    mc "It chewed through my arm and laughed in a voice that wasn’t its own-" ## MC is lying here

    mc "And I came back in {i}goddamn pieces.{/i}"

    mc "And you believe him, instead of me?"

    mc "Do you think I lied?"

    shiori "I never said that."

    mc "No, no, you didn’t, but you {i}think{/i} I brought back the wrong thing!"

    shiori "I think{nw}"

    mc "No! No, the hell with that."

    mc "He didn’t see what it looked like when it died."

    mc "He didn’t see it move even after I cracked its spine, after-afer it choke{w} im it's own BLOOD."

    ## programming note : the three lines below will kinda be fast forwarded so the players don't get to read it
    ## tbh if they scroll back they are a le to read it, just a lil tidbit

    mc "{cps=99}The sound that it made when I stabbed it all over and over and over{/cps}{nw}"

    shiori "{cps=99}Um-{/cps}{nw}"

    mc "{cps=99}The smell of it's corpse that makes me want to vomit but also feels like hunger itself.{/cps}{nw}"

    shiori "{cps=99}[player_name]-sama--{/cps}{nw}"

    mc "{cps=99}How the flesh clings on my skin and the putrid smell of blood splattered on my face.{/cps}{nw}"


    ## normal speed again

    mc "I heard that. I saw that. ME."

    shiori "..."

    ## her sprite shakes

    mc "Oh.{w} U-Um, sorry. I didn't mean-"

    mc "Oh, crap."

    mc "That was scary, huh? I really went off there, huh..."

    shiori "..."

    mc "Hahahaha..."

    mc "Sorry, Shiori-chan. I was just-"

    shiori "It's okay. I'll go tell Yamato that maybe... Maybe he's just imagining things."

    shiori "Silly me, accusing you like that while you risked yourself fighting the Yamakui..."

    shiori "Aha... ahahahaha...."

    shiori "Yamato's just jealous..."

    mc "Yeah, that prick is just jealous of me, Shiori-chan."

    scene black

    ## smaller text as shiori is whispering

    shiori "... But you didn't have any injuries on you, [player_name]"

    $ loop1_shiori_nonmandatory3 = True

    return

label loop1_shiori_nonmandatory4:

    ## night only (can be shrine or at the village square), only happens at the last day

    shiori "[player_name]-sama~"

    shiori "Do you know what today is?"

    mc "..."

    shiori "Mmm~ It’s almost here. Our days are numbered."

    shiori "{size=+10}{color=#FF2222}Three...{/color}{/size}"

    n "You feel cold air at the back of your neck."

    shiori "{size=+10}{color=#FF3333}Two...{/color}{/size}"

    n "Did something just move at the corner of your eye?"

    mc "What--"

    shiori "{size=+10}{color=#FF4444}One.{/color}{/size}"

    play sound "sfx/heartbeat.ogg"

    shiori "{fast}Red Moon.{/fast}"

    mc "..."

    n "But there’s only her smile."

    shiori "Are you ready~?"

    n "Shiori's hair sways softly in the wind, she looks so soft... So fragile."

    n "As if.. as if.. Everything could snap at any moment."

    n "{fast}Her nack{/fast}{nw}"

    shiori "Because I am~"

    n "It's an accusation. Indirectly, of course. But it slaps you in the face."

    n "Even though everyone praised you, the supposed hero, they seem to start hiding when the red moon is coming. A ritual, as always."

    shiori "l wonder who it’ll choose this time, if it's still alive, that is..."

    mc "Shiori."

    shiori "Mm?"

    mc "You don't trust me, do you."

    shiori "Ara~"

    shiori "If I don't, I won't be still hanging out with you like I do now, right?"

    shiori "Nee, nee. I care about you, you know that right?"

    shiori "I'll still believe in you, even though no one else don't, my [player_name]-sama."
    # bam sound? zoom in to her creepy face?
    shiori "Remember that~"

    $ loop1_shiori_nonmandatory4 = True

    return
