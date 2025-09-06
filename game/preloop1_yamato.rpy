############# LOOP 1 WHERE EVERYONE IS ALIVE ###########################
label loop1_yamato_mandatory1:

    ## DOJO DAY
    yamato "Oi, oi. Look what the kami-sama dragged outta bed."

    MC "Morning to you too, Yamato-kun. You out here exorcising evil spirits or something?"

    yamato "Someone's gotta do it."

    MC "Why? I killed the Oni, didn't I? You can take a break once in a while, you know!"

    yamato "Tch... Standin’ there lookin’ so smug..."

    MC "All right, I think you're being unnecessarily hostile. What's gotten into you?"

    yamato "What's gotten into me is that yer bein' too dam clean for someone who fought the damn Yamakui!"

    yamato "I don't believe the brat I used to mop the floor with could easily kill 'em!"

    MC "Wait, you imply that I'm lying?"

    yamato "Keh..."

    yamato "Why don't we go one round to see which one of us is lyin', eh?"

    MC "So you want to kick my ass now?"

    yamato "What? The damned Oni Slayer won't back down from a challenge from lyin' ol' me, right?"

    MC "Fine! If you want proof, you damn well got one!!"

    n "He throws a wooden sword at you and you both start circling each other."

    play sound "sfx/clash.ogg"

    MC "Haaaaah!!"

    yamato "Tch! Swingin’ like a drunk ox, kusogaki!"

    n "You charge in, but he easily slips past you."

    n "His sword cuts the air, but you duck out just in time."

    MC "Are you holding back, Yamato-kun~? Or are you always this slow?"

    yamato "Oi, don’t get cocky. Ain’t doin’ shit like that!"

    n "Your sword sings again, he manage to parry once but you shifted your weight and swing one more time."

    n "It almost hits, but--"

    n "Yamato’s foot hits a soft patch, and he slips down, accidentally avoiding your swing."

    play sound "sfx/bodyfall.ogg"

    show yamato annoyed at midright

    yamato "Tch... Ahhh, fuckin’ hell..."

    MC "Yamato?!"

    n "You remember Yamato is never this careless, you wonder if he is doing this on purpose."

    n "You hand out your hand to help him stand, but he doesn't take it."

    yamato "Lost my footing, ’s all. Ain’t my lucky day."

    MC "...Yamato kun--"

    yamato "Oi. Don’t gimme that look."

    yamato "Yer the star now, yeah? Whole damn village sings yer name loud enough to wake the dead."

    yamato "Me? Just some mutt still barkin’ out orders to trees."

    MC "What are you talking about? Are you still mad that I get to kill the oni?"

    MC "Everyone knows that you're just as strong! No one will look down on you even though--"

    yamato "Tch. Don’t feed me that fluffy crap."

    MC "I’m not--"

    yamato "I used to be the strong one. Y'know that?"

    yamato "Back when ya still pissed yer hakama and swung like a fish outta water."

    n "That’s... That’s not how it happened. Is it?"

    yamato "I was the one who trained ya."

    MC "Yeah, but I was the one who killed the damn thing!"

    yamato "Hah. Ya really believe that? That thing tore warriors in half, scared the elders shitless and somehow... somehow {i}ya{/i} come back without a scratch?"

    MC "What, you think I’m making it up?!"

    yamato "Tch. I think... ya don’t even know yerself."

    n "Yamato hasn’t moved, but you feel cornered by his words. If you hadn't lied, you won't feel cornered."

    MC "Ha! Say whatever you want, I brought back the armor! Everyone saw it!"

    yamato "Yeah? Armor’s just scrap metal if ya ask me. Coulda been anyone’s. Coulda been planted. Coulda been--"

    n "He stops. His jaw locks tight. He almost said something else. Something worse."

    MC "What?"

    n "Yamato pauses, then looks down before staring you right at the eyes. He's hesitating...?"

    yamato "Tch, nevermind."

    yamato "Next red moon... {w}I’ll be watchin’ you."

    n "Weird... Yamato is usually not like this..."

    n "He was kind and always ready to help anyone in need of sparring partner, but now..."

    m "What's gotten into him?"

    MC "*scoff*"

    yamato "If ya really killed the Yamakui, ya wouldn’t be shakin’ right now."

    n "He walks out without looking back. You want to shout after him, but your throat closes up."

    n "You’re alone now."

    n "Alone."

    n "Except for the pounding in your ears."

    return

label loop1_yamato_mandatory2:

    $ loop1_yamato_mandatory2 = True

    ## DOJO NIGHT

    n "No one uses the dojo anymore after you return."

    n "But there he is, again. Swinging that katana of his like he has something to prove."

    yamato "Heh... Look who's here."

    yamato "Ya said we don't need t' train anymore because the goddamn Yamakui died, didn't ya?"

    MC "Shut up, I'm just checking on you."

    yamato "Heh, sure ya do."

    yamato "Red Moon’s near. Ya feel it?"

    MC "Stop talking like the Oni's gonna return!"

    MC "I mean, I brought it's armor back, right? What more proof do you want?!"

    yamato "Yeah? Ya sure 'bout that?"

    yamato "'cause Hikaru said it was too damn small to belong to the Oni."

    MC "Have either of you or Hikaru seen the oni? I was the only one who did and stayed alive!"

    yamato "All t' more reason to doubt ya."

    MC "...Damn, that was harsh."

    yamato "'Cause people's lives depend on it."

    yamato "Ya came home grinnin’ with blood on that armor, [persistent.player_name]. Told 'em they could sleep easy."

    yamato "So if they don’t wake up after the red moon's over..."

    yamato "That's on ya."

    n "The both of you go silent and stare at a red slash slowly forming across the sky, the first sign of the red moon coming."

    yamato "...Oi. [persistent.player_name]."

    MC "Huh?"

    yamato "What color was its blood?"

    n "The words stumble before you even think of an answer."

    menu:
        "Say it's red.":
            MC "It was... red."
            n "Why did you stutter? Of course it was red"
        "Say it's black.":
            MC "It was... black. Yeah. Black."
            yamato "...Black?"
            n "No, no, something's wrong."
            MC "I-I mean red?"

    yamato "Ya sure?"

    menu:
        "Yes. Definitely.":
            MC "Y-Yeah. Definitely!"
        "I think so...":
            MC "...I think so?"
            n "That didn't sound very convincing."

    yamato "Tch."

    n "He doesn't look convinced and leans closer, shrinking the gap between you. You can't breathe right."

    yamato "Say that again?"

    menu:
        "Red, I said.":
            MC "Red, I said!"
            n "Whoa, there's no need to yell!"
        "Stop asking me that!":
            MC "Why do you keep asking me that?!"
            yamato "Because you keep soundin’ like you’re lyin’."

    n "Your pulse pounds harder now. What is the point of this?"

    yamato "Last chance. What color was its blood?"

    menu:
        "Red.":
            MC "...Red."
        "Red again.":
            MC "I already told you. Red."

    MC "Red. Red. RedredredredredREDREDREDREDREDREDREDREDRED. RED!"

    yamato "..."

    ## creepy laugh scene

    yamato "...Heh..."

    yamato "...Heh... hehh... hhhhehhh--"

    yamato "Haaaahh... HHHahh--!!"

    yamato "AHAHAHAHA...!"

    MC "The hell was that for?"

    yamato "...Yeah, ya sounded like a liar."

    MC "You sounded like an asshole."

    yamato "Don't worry, [persistent.player_name], even if you're lyin'... I'd always be here, yeah?"

    yamato "I'd clean yer mess like always, and slay the blasted thing myself when the red moon comes."

    MC "...!!!"

    n "What did he mean by that?"

    n "You're sure the Oni's blood was red."

    n "It was red. You saw it--{w} didn’t you?"

    n "You stabbed it. {w}The liquid was dipping from your hands when you stab it. {w}Red. {w}Red. It HAD to be red."

    n "It was evry dark at the time, sure. But your sword was red, right? You remember that, right?"

    n "No--no, stop. Stop thinking about it. It was red. It was. {w}It was."

    n "Then why was he laughing like that?"
    return

label loop1_yamato_mandatory3:

    $ loop1_yamato_mandatory3 = True


    ## YOUR HOUSE NIGHT

    n "You are in your house when you hear footsteps outside."

    n "Why are you not asleep at this hour? Do you ever sleep? Does the fight haunt you so much that--"

    n "Ah, that doesn't matter."

    n "What matters now is that the footsteps are nearing."

    n "You stand away and walk towards it with bare feet, slowly, so they don't notice."

    n "You slide the panel softly, it almost doesn't make a sound."

    n "And there he is."

    n "Yamato."

    n "Crouched low by your shed, his shoulders are hunched, clearly stalking... or waiting."

    n "His hand rests near the latch, creeping slowly closer and closer."

    n "You drop out of sight fast, pulse crashing behind your ears."

    n "Today is not Yamato's patrol schedule."

    play sound "sfx/cloth_rustle.ogg"

    n "You immediately grab your sword, ready to fight."

    n "Why? It's just Yamato. Your childhood friend. Even though he is more irritable lately, surely he is not trying to harm you."

    n "You don’t make a sound until--"

    play sound "sfx/stone_kick.ogg"

    MC "...Tch."

    n "You almost growls as the blade presses to his back."

    MC "...Don’t."

    yamato "..."

    MC "Step away. {w}Slowly. {w}Or I’ll spill you across the floorboards."

    n "He freezes. You can feel his muscles shift under the blade, but he's still silent."

    MC "Give me a reason not to."

    yamato "Damn, who taught you to speak like that?"

    MC "Yamato."

    yamato "...I was just walkin' around."

    MC "You never walk around my house nowadays."

    yamato "The road goes where I say it does."

    n "His voice sounds like it had to fight its way out."

    MC "I think you are snooping around my house."

    yamato "Ya always think everyone’s watching you?"

    MC "Just tell me what you came here to do."

    yamato "..."

    MC "Are you trying to steal--"

    yamato "Why would I give a shit about your old junk?"

    MC "You know what's inside is not just junk."

    yamato "Heheheheh..."

    Yamato "Why so tense, [persistent.player_name]?"

    yamato "All stiff and hissin', makes me wonder what you’re hidin'."

    n "Your grip tightens, and your whole body wants to fight."

    n "But instead, you take a very deep breath... and walks closer to him."

    MC "Fine, if you want to look at it so bad, be my guest."

    yamato "Hah?"

    MC "The armor. That's what you’re here for, right?"

    yamato "Uh... I--"

    MC "I'll prove that it's authentic, that you and Hikaru are just looking for a reason to doubt me."

    n "Yamaot follows you inside. The armor sits where you left it, with dried blood still splattering across it."

    MC "Go ahead, see for yourself."

    yamato "...Tch. Looks even worse than I remember."

    MC "It was worse when I dragged it home."

    n "He crouches, then his hand hovers above the armor’s edge."

    yamato "Hmph."

    n "He pokes it, the armor clatters."

    yamato "...This really it?"

    MC "You’ve seen it before, when I brought it back."

    yamato "Doesn’t feel the same."

    MC "...You still think I lied?"

    yamato "...I think... {w}I dunno what to think."

    n "Yamato takes out a talisman from his sleeve and pushes it to the armor."

    n "You know it will react to the armor if it touches an evil spirit."

    n "You take a step back, circling him." ### HOHO EBCAUSE YOU ARE YAMAKUI GET IT GET IT

    MC "I mean, the thing is dead. So if you're looking for some sort of evil aura, there'd be none left."

    yamato "...If this is real, then you really--"

    MC "Yeah."

    yamato "...Huh."

    n "He circles the armor once, then again, looking for faults. Can't seem to find one."

    yamato "Ya could’ve at least cleaned it better."

    MC "I didn’t want to touch it again."

    n "He grunts and tries to lift the damn thing."

    yamato "...Kinda heavy for something so damn small."

    MC "Try dragging it downhill by yourself."

    n "He sits down, arms resting on his knees, and maybe, just maybe, recalculating."

    yamato "...A'ight, fine."

    n "Something in his gaze changes, and so is in the way he looks at you now."

    n "It's... a lot softer now."

    yamato "Guess I barked up the wrong tree. Hhh... {w}Tch. Damn embarrassing."

    MC "So you finally admit it?"

    yamato "Don’t push it, kid. I just... {w}got carried away. Thought I smelled somethin’ off, y’know? Guess I was sniffin’ shadows."

    n "He rubs the back of his neck, eyes avoiding yours."

    n "You feel as if the harsh features on his face falter under the shades of your oil lamp, almost slipping into something resembling regret."

    yamato "I’ll, uh... {w}head out. Don’t tell Shiori I was lurkin’ here like an idiot."

    MC "Yeah, yeah."

    n "He stands up then gives a half-hearted wave sheepishly as he vanishes into the dark."

    MC "..."

    MC "You idiot."

    return

label loop1_yamato_mandatory4:

    $ loop1_yamato_mandatory4 = True

    n "You were just walking from your house when you hear people arguing nearby."

    hikaru "...Are you saying I was wrong about the armor?"

    yamato "Tch. I dunno. Maybe... maybe size don’t matter after all."

    n "That’s strange. Yamato’s the one who always doubted you and alwaus swore that you couldn’t have done it..."

    n "So why is his voice shaking now?"

    hikaru "...What are you implying?"

    yamato "I went back to see the damn thing and put Shiori's talisman on it. Thought I’d catch somethin’ nasty clingin’ to it."

    yamato "Nothin’ happened. If Yamakui's alive, it shoulda have residue."

    hikaru "..."

    hikaru "Are you really sure?"

    yamato "I'm not fuckin' blind! It didn't shine one bit!"

    yamato "Felt like maybe... {w}maybe we’re barkin’ up the wrong damn tree."

    n "Hikaru goes still. Even from here you see the falter in their posture."

    hikaru "...You don’t mean--"

    yamato "I mean... maybe we’re wrong this time. Maybe [persistent.player_name] did kill the damn thing after all."

    n "The silence after is heavier than any word spoken."

    hikaru "This is absurd. You were the one who told me not to trust so easily. You said [persistent.player_name] was hiding something."

    yamato "...Yeah. I did."

    yamato "But... I dunno anymore."

    n "You stay hidden in the shadows, even after the both of them part ways."

    n "Watching."

    return

label loop1_yamato_mandatory5:

    $ loop1_yamato_mandatory5 = True

    n "Today's your patrolling schedule again."

    n "By the kami-sama.... there’s a voice out here."

    n "You're alone. You know you're alone. It's after midnight--"

    n "You're not supposed to hear anyone."

    n "Someone, or something, is muttering. Prayers in ancient language... And it's a voice that you're familiar with."

    n "You follow it. You shouldn’t... Not with the red moon so close...."

    n "...but your legs move anyway."

    n "You see Yamato, kneeling at the clearing. His hands on his sword, shaking. Head bowed so low he looks like a broken puppet."

    yamato "Master of the earth..."

    yamato "Give me flame..."

    Yamato "Give me..."

    n "--No--"

    n "There's a shadow behind him that has tendrils, or maybe limbs, all growing everywhere."

    n "An amalgamation of corpses and all dead things, perhaps."

    n "It has so many eyes in places that shouldn't have eyes."

    n "You can’t look at it directly, because you know it'll recognize you."

    MC "...Yamato."

    n "Why are you talking."

    n "Why is your voice calm. Why aren't you screaming...?"

    yamato "...grant me... flame...."

    MC "Yamato."

    Yamato "Hh..!!!"

    n "The thing folds out of existence as soon as Yamato's chanting stops."

    yamato "[persistent.player_name]...."

    n "He's frozen, eyes staring straight at you... {w}Or perhaps, to whatever is behind you "

    MC "...Did you just try to summon something?"

    n "You speak so-matter-of-factly it sounds rather unsettling."

    n "Wait, do you know what that thing was? Have you seen it before?"

    yamato "Y-you weren't supposed to see that, damnit."

    MC "What the hell was that?"

    yamato "I'm prayin' for the gods to protect us the next red moon."

    MC "That thing wasn't a god, you know that."

    yamato "Yeah, but that wasn't Yamakui either!"

    MC "You're gonna fight an oni with something worse!?"

    yamato "Ya don't understand a damn thing!"

    yamato "...I wanted t' believe ya, okay!?  But I don't know anymore if I'm strong enough to--"

    n "Yamato's voice breaks, his sword is clattering innthe ground now."

    yamato "...Ever since ya came back, people look at me like I’m some leftover."

    yamato "The village already got their hero, so what the hell do they need me for?"

    yamato "And... I ain’t stupid, a'ight? I know what they whisper."

    yamato "‘Course [persistent.player_name] came back stronger. [persistent.player_name] faced the Yamakui. [persistent.player_name] lived.'"

    yamato "Then they look at me like I’m--like I ain't worth shit if I ain’t swingin' at somethin'."

    MC "...So you prayed to whatever that thing was?"

    yamato "...I didn’t mean to summon..."

    yamato "...I just wanted somethin'. {w}Anything."

    yamato "I thought maybe if I got stronger--if I had just a bit more--maybe I'd matter again."

    MC "Haaaah...."

    MC "Oh, well."

    n "'Oh well'?"

    n "He tried to summon a creature that watched you from a body made of rotting arms and knowing eyes, and that's all you can say?"

    MC "Yamato..."

    n "You step closer. and gently puts your hand on his shoulder. Yamato jerks backwards, but doesn't swat your hand away."

    n "The contact should ease him. {w}Should."

    n "But somehow he is still trembling."

    MC "I'm still here, aren't I?"

    yamato "...Goddamn it, I'm so screwed..."

    MC "You're not screwed up."

    yamato "...Hh."

    n "Yamato finally eases, and you pull your hand away, gesturing for him to follow you."

    n "You walk back together in silence, the forest is now dead silent behind you, but it wasn't as eerie anymore."

    n "Nothing watches from the trees now. You are sure."

    n "You're {i}sure{/I}."

    ## so like the MC is yamakui, and the amalgamation is merely the corpses / ghosts of the things the yamakui has killed

    return
