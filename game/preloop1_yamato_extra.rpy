### CONTAINS NON MANDATORY EVENTS FOR LOOP 1

label loop1_yamato_nonmandatory1:

    n "You have volunteered to go on a night patrol."

    n "Of course, since the Yamakui is not around anymore, it really isn't needed."

    n "But some of the paranoid townspeople–including Yamato–decide that night patrols are still mandatory, at least until the next red moon proves that it's gone."

    play sound "sfx/steps_dirt.ogg"
    $ renpy.pause(0.4)

    n "You're about to doze off when you hear leaves rustling behind you."

    n "Maybe it's the wind? But you feel like it has weight, though."

    MC "...Who's there?"

    n "You stop and tries to listen again."

    MC "Hey–?"

    n "That was clearly a footstep."

    n "It stops when you stop, and continues when you walk. You are being followed."

    n "You immediately spin around at that, blades drawn."

    ## jumpscare sfx

    MC "AHHH!"

    yamat "Pft–"

    yamato "Ffffuckin’ hell, did ya just squeal like a damn sissy!?"

    MC "WHAT THE HELL, YAMATO?!"

    yamato "BWAH! Ya shoulda seen yer face just now!"

    MC "You–! Kami-sama, why are you even out here?!"

    yamato "Patrollin'. Same as ya "

    MC "I thought you were the damned Oni!"

    ## slipped there MC hohoho

    yamato "Yeah? Funny, 'cause ya said you've killed it."

    MC "I mean-you-you think that’s funny?! I almost cut you down!"

    yamato "Tch. Ya ain’t got the stones."

    MC "I thought something–"

    yamato "What? The Yamakui crawled back outta its pit?"

    MC "T-That’s not what I said."

    yamato "Didn’t have to. Ya looked ready to shit nails."

    n "He steps closer, but you decide not to back down."

    yamato "Oi, [persistent.player_name]. Ya always this jumpy when the moon ain’t out?"

    MC "...Bite me."

    yamato "Feisty."

    n "He walks past you, swords still not drawn. Seems like he's not trying to challenge you to a duel this time."

    n "But still, your hand can't help gripping the hilt of your own sword."

    MC "You really weren’t tryin’ to mess with me?"

    yamato "Nah."

    yamato "I walk where I want. Ain’t my fault if ya piss yourself when the twigs start talkin’."

    n "Your stomach twist, but that's not important right now."

    n "Something else is bugging you."

    MC "..."

    MC "...Where’d you come from?"

    yamato "West path."

    MC "No you didn’t."

    yamato "Huh?"

    MC "I walked that path just now, I didn't see you there."

    n "His smile falters."

    yamato "It's dark."

    MC "..."

    n "That sounds like a lot of crap, doesn't it?"

    n "You remember those footsteps. The ones that stopped when yours did, it was matching your pace."

    n "You already felt them long before he showed his face."

    MC "...How long were you behind me?"

    yamato "Haa?"

    MC "How long, Yamato?"

    yamato "You accusin’ me of tailin’ ya, [persistent.player_name]?"

    MC "..."

    yamato "Would ya believe me if I said I was lookin' out for ya?"

    MC "Yeah, right. What kind of bullcrap is that?"

    n "He doesn't answer your question and walks away again."

    n "You wait for his steps to fade, then longer. Until you can't even smell him in the air."

    ## weird phrasing is intentional 'cuz yamakui can smell scent

    n "And your hand still won’t leave the hilt."

    $ loop1_yamato_nonmandatory1 = True

    return

label loop1_yamato_nonmandatory2:

    n "You enter the shrine expecting Shiori, but you are welcomed by the sight of another familiar face instead."

    n "Yamato is kneeling in full posture in front of the altar with sword across both palms."

    n "Weird. He usually mutters death threats, not prayers."

    MC "Yamato is praying?"

    shiori "I know, right? The stars have aligned, finally~"

    yamato "Tch. Ya two keep talkin' shit and I’ll offer ya next."

    MC "The last time you go to the shrine to pray was- was- I don't even remember, Shiori. Has he gone to the shrine in his life at all?"

    shiori "Not if he's not bleeding. He's only here to be patched up, usually."

    yamato "Oi. Shut the hell up. I'm concentratin’ here."

    n "Yamato closes his eyes again and his lips are muttering incantations that you can't hear clearly."

    n "The little shrine flame wavers.... Then..."

    ### FWOOOOOOOOOOOOOMMMMMMMMMMMM

    n "It flares red, then black, then red again. As if the gods are angry for some reason."

    shiori "KYAAA–"

    MC "GAH! Whoa!! That’s not normal, right?! That’s definitely not normal!"

    yamato "The fuck?! It wasn’t doin’ that a second ago!"

    MC "Are you cursed!?"

    show yamato frown at center

    yamato "I didn’t even touch anything! Don’t pin this on me!"

    shiori "Yamato-kun, you never prayed and once you do the gods are mad at you."

    shiori "Did you thought of something dirty mid-prayer~?"

    yamato "OI! I said nothing weird! It just–went off!"

    shiori "Or... the gods saw all your sins and your thoughts then decide you are blasphemous, Yamato-kun..."

    n "She says it with a syrupy sugary voice, but there’s a weird glint in her eye."

    yamato "Cut that cryptic shit out already, Shiori!"

    MC "Shiori-chan, don’t freak him out, he’s gonna run straight into a temple pillar next."

    yamato "I {b}do not{/b} run from shit!"

    shiori "Fufufu~ Then why’d your hand twitch, hmm~?"

    yamato "Tch. Y’all’re insufferable."

    yamato "...Whatever. This dump’s cursed."

    n "He storms off muttering, boots thumping loud down the old stairs."

    n "You and Shiori exchange a look."

    shiori "Ne~ [persistent.player_name]-kun, would you like a blessing too~?"

    MC "Hahah, me?! Nah, no way! I don’t wanna cause the shrine to explode!"

    shiori "Hmm~ But you’d look very divine all lit up, I think."

    MC "Ha... Haha... That's not creepy at all, Shiori-chan."

    n "Shiori giggles, then spins away down the steps, leaving you alone with the flame."

    n "It still burns with that unnatural red color... closer to black flame."

    n "Did Yamato's prayers cause this or... something else?"

    n "You squat down, closer to the flame now."

    n "Your hand hovers near the flame, enough to feel the sting, wondering if it would turn another color."

    MC "...Hmm."## creepy MC smile sprite

    $ loop1_yamato_nonmandatory2 = True

    return

label loop1_yamato_nonmandatory3:

    n "You're swinging your sword absentmindedly, when you hear an unmistakable sound of footsteps behind you, coming closer."

    play sound "sfx/step_dirt_slow.ogg"

    MC "Hoo, look who's early in the morning~"

    yamato "Tch. Can’t a guy visit without bein’ grilled?"

    MC "Just saying. You usually doze off 'till noon."

    yamato "Shaddup."

    n "He sets something down next to you."

    MC "...What’s that?"

    yamato "Onigiri."

    MC "Huh?"

    yamato "Dumbass, it's food. Just eat it."

    MC "...You made these?"

    yamato "What, ya think I can’t cook?"

    MC "No, I just–"

    yamato "Don’t get weird about it."

    n "You pick the still-warm onigiri. He looks away when you take a bite."

    MC "Oh! It's actually good~!"

    yamato "Damn right it is."

    n "You eat in silence for a while."

    n "Yamato sits down beside you with arms over his knees and stares at your face. It feels rather uncomfortable now."

    MC "Thanks."

    yamato "Tch. Whatever."

    yamato "..."

    yamato "Ya still trainin’ every morning?"

    MC "Sometimes."

    yamato "Then lemme help."

    MC "...Help?"

    yamato "I’m bored."

    MC "You... {w}sure?"

    yamato "Just grab the damn sword already."

    n "He tosses a wooden sword at you right after you finish the onigiri."

    MC "...Hah."

    MC "Alright, fine. But I’m not going easy on you."

    yamato "That's more like it."

    n "And for the first time in days..."

    n "...he no longer tries to accuse or test you."

    $ loop1_yamato_nonmandatory3 = True

    return
