label preloop1_scene1:

    ## shrine day

    n "The shrine's door’s half-open when you pass by. You didn’t mean to eavesdrop..."

    n "You just stopped walking, that’s all."

    n "That’s {i}all.{/i}"

    shiori "...Hold still, Yamato."

    yamato "Tch. I am."

    shiori "Nooo, you’re twitching. Again~"

    yamato "'Cause it’s damn cold. Yer puttin’ that on with ice fingers or somethin’?"

    shiori "Ehehe~ Maybe you shouldn’t’ve sprained your whole arm trying to chop wood like it's the Yamakui~"

    yamato "I was trainin’. S’important."

    shiori "Overdoing it isn’t training. It’s dumb."

    yamato "I said I’m fine."

    yamato "Gah—!"

    shiori "See? Your arm says otherwise~"

    yamato "...Didn’t hurt that much."

    shiori "Yeah? So what does that 'Gah!' for?"

    yamato "Did not."

    shiori "Did too~"

    yamato "Oi—"

    shiori "Ah ah ah~! Don’t move! One more twitch and I’ll tie this whole bandage into a bow, and then you'll be suuuper embarrassed!"

    yamato "Ya wouldn’t dare."

    shiori "Wouldn’t I~?"

    n "..."

    shiori "Okay, there. Don't break the other arm, too."

    yamato "...Thanks."

    shiori "...Hm?"

    yamato "For... {w=0.1}y'know. Bein' annoying, but still patchin’ me up."

    shiori "Ara~ Was that your idea of a compliment?"

    yamato "Don't make me take it back."

    shiori "Bonk~"

    with vpunch

    n "You hear a soft thud. Probably her knuckles to his forehead."

    yamato "Ow. What the hell."

    shiori "[persistent.player_name] is not here to bonk you, so I'm doing this instead."

    n "Yamato grumbles something too low to catch. You can hear Shiori's laughter."

    n "You step away before they see you."

    $ preloop1_extra = True

    return

label preloop1_scene2:

    ## dojo day

    n "The clack of wooden swords draws you in."

    n "Seems like they haven’t noticed you. Or maybe they have. Hikaru probably has."

    n "You peek through the slats and see Yamato pacing around Hikaru, fixing their stance."

    yamato "Ya call that balance? Ya’d fall flat if someone sneezed on you."

    hikaru "...Understood."

    yamato "Raise yer guard. {w}Higher. {w}No—{w}there. Kami-sama, you’ll get gutted if you keep slackin’ like that."

    hikaru "I am {i}trying.{/i}"

    yamato "Tch. Try harder. {w=0.1}Step again."

    n "Hikaru moves again as Yamato strikes back."

    yamato "Footwork. {w=0.1}Again."

    hikaru "Yes."

    n "The sparring slows. Hikaru lowers their weapon, sweat sticking their fringe to their face."

    yamato "Ya don’t have to push like this. Ain’t like yer plannin’ to be an Oni-slayer or somethin’."

    hikaru "{w=0.1}...I am training to protect someone."

    yamato "...Ha?"

    n "Hikaru doesn't answer, but their grip’s gone loose."

    yamato "Shiori?"

    hikaru "..."

    yamato "[persistent.player_name]?"

    hikaru ".{w=0.1}.{w=0.1}."

    n "Did Hikaru's eyes just flick to where you're standing near?"

    yamato "Fine, be all mysterious. Just don’t train yerself into the damn dirt."

    hikaru "I can still improve."

    yamato "Yeah, yeah. We all got ghosts chasin’ us."

    yamato "{w=0.1}...Again. From the top."

    yamato "Protectin’ someone ain’t just swingin’ harder. Got it?"

    hikaru "...I understand."

    n "You press your back to the outer wall."

    n "And keep walking."

    $ preloop2_extra = True

    return

label preloop1_scene3:

    ## forest day

    n "When you step to the forest, you see Hikaru flying all around the trees while Shiori shouts from below."

    shiori "Higher~ {w=0.1}Higher~ {w=0.1}Left a bit~"

    hikaru "You said right."

    shiori "Ara, did I~?"

    hikaru "...You are doing this on purpose."

    shiori "Maybe~ {w=0.1}But you look cute when you’re concentrating~"

    hikaru "{w=0.1}...Please be serious."

    shiori "I am~ Very serious. This is sacred work, after all."

    n "Hikaru moves higher, tying another paper effigy to a thin branch above her reach."

    shiori "That one’s for the lady who ran the bathhouse, remember?"

    hikaru "The one who made bitter tea?"

    shiori "Mmhm~ She always scolded me for stealing sweets."

    hikaru "{w=0.1}...You stole from her?"

    shiori "I borrowed them~! With intent to never return~"

    hikaru "{w=0.1}...That is not better."

    n "They both pause to look at the dolls already swaying in the breeze."

    shiori "Ne~ Hikaru~"

    hikaru "...Yes?"

    shiori "What kind of person do you like~?"

    hikaru "...That is irrelevant."

    shiori "Ehhh~? Come on~ No one’s around~ Except the spirits~ {w=0.1}And [persistent.player_name] hiding behind a tree somewhere, probably~"

    hikaru "I— {w=0.1}[persistent.player_name]'s not—"

    shiori "Hehe~ You’re flustered~"

    hikaru "{w=0.1}...I am not."

    shiori "Is it [persistent.player_name]-sama~, ehhh~?"

    hikaru "...I just...{w=0.1} admire their resolve."

    shiori "Ara~ Resolve, is it? Not [persistent.player_name]-sama's smile~? Not the way [persistent.player_name]-sama pats your head sometimes~?"

    hikaru "...That was once."

    shiori "And you floated away like a startled bird~ So cute~"

    hikaru "Shiori—"

    shiori "And~! You didn’t even deny it~"

    hikaru "Please focus on the ritual."

    shiori "Aww~ Don’t pout~ I’ll tell you mine too."

    hikaru "...You will?"

    shiori "I like strong people~"

    hikaru "Yamato, then?"

    shiori "Ehh~ Yamato's strong, but~"

    shiori "I mean really strong~ {w=0.1}Someone who makes you feel small just by being there?"

    hikaru "...That sounds oddly specific."

    shiori "Mmm~ Maybe that’s the point~"

    hikaru "...Let’s finish the rest."

    shiori "Aww~ You're no fun~ But your ears are all red~"

    hikaru "They are not."

    shiori "{cps=10}Liar~{/cps}"

    n "You step back before your name comes up again."

    n "But Shiori’s laughter is still ringing in your ears."

    $ preloop3_extra = True

    return

label preloop1_scene4:

    # forest night

    if loop1_yamato_mandatory3 == True:
        jump scene4var1
    else:
        jump scene4var2

label scene4ver2:

    n "Tonight is not your patrol day. It's Yamato and Hikaru's."

    n "You hear their voices from afar, but you decide not to approach them."

    yamato "...How many charms didja count tonight?"

    hikaru "Seven. Two were cracked."

    yamato "Tch. Figures."

    hikaru "The cracks were fresh."

    yamato "If the Yamakui's dead... The charms should hold."

    hikaru "I agree."

    yamato "...Ya think it's really gone?"

    hikaru "What do you mean?"

    yamato "The Yamakui."

    hikaru "..."

    yamato "Everyone says [persistent.player_name] killed it. But I ain’t seen a corpse. Ain’t seen {i}anything.{/i}"

    hikaru "Neither have I."

    yamato "Does that sound right to ya?"

    hikaru "...No."

    yamato "Thought so."

    n "They stop walking. Maybe Yamato checking the trees. Maybe not."

    yamato "...[persistent.player_name] came back different."

    hikaru "..."

    yamato "Ya noticed, yeah?"

    hikaru "Yes."

    yamato "The way [persistent.player_name] talks now. Methinks half their sentences sound like guesses."

    hikaru "They forget things, yes. Like ou—"

    yamato "Ha?"

    hikaru "{w=0.1}Nevermind."

    yamato "C'mon, Hikaru. What else did [persistent.player_name] forget?"

    hikaru "..."

    yamato "{w=0.1}...Well?"

    hikaru "That’s... {w=0.1}complicated."

    yamato "Huh."

    hikaru "..."

    yamato "Whatever. {w=0.1}Ain’t my business."

    yamato "Still weird. Like...{w=0.1} We got our friend back, but somethin’s off."

    hikaru "I know."

    yamato "Guess we just keep walkin'."

    hikaru "Just... {w=0.1}Keep your guard up, Yamato."

    yamato "Yeah, always."

    $ preloop4_extra = True

    return

label scene4ver3:

    n "Tonight is not your patrol day. It's Yamato and Hikaru's."

    n "They walk side by side, but not talking."

    n "You decide to leave because the tension is sharper than a blade."

    $ preloop4_extra = True

    return


label preloop1_scene4:

    # shrine night

    n "You see Hikaru kneeling alone near the altar."

    n "But when you're about to walk in, another voice cuts the silence."

    shiori "Ne, Hikaru~"

    hikaru "...Yes?"

    shiori "Who are you praying for~?"

    hikaru "...My father."

    shiori "Oh~"

    shiori "It’s been a long time, hasn’t it?"

    hikaru "Yes."

    shiori "But everyone still remembers him."

    hikaru "..."

    shiori "So... {w=0.1}It wasn’t Yamakui."

    hikaru "I don’t think so."

    shiori "Do you believe he’s still alive?"

    hikaru "{w=0.1}...I don’t know."

    shiori "He didn't say anything to you when he left?"

    hikaru "He said he was looking for a way out."

    hikaru "But if he’s alive... Why didn’t he come back for me?"

    shiori "..."

    hikaru "...I ask that every time I come here."

    n "Shiori doesn’t speak for a while, but then she steps beside Hikaru."

    shiori "{w=0.1}...I’ll pray too."

    hikaru "You don’t have to."

    shiori "But I {i}want{/i} to."

    n "She clasps her hands."

    shiori "Dear Kami-sama, please watch over Hikaru’s father. Wherever he is~"

    shiori "And maybe nudge him a little, so he remembers the way home."

    n "The candle flutters. Did Kami-sama hear her prayer, or an entirely different god?"

    $ preloop5_extra = True

    return

label preloop1_scene6:

    $ preloop6_extra = True

    n "The village streets at night are unusually quiet. You see Shiori and Yamato walking ahead."

    n "You follow from a distance but don't catch up to them."

    n "...Weird."

    shiori "Yamato-kun, why are you following me?"

    yamato "Ha. I’m only here because I had to pass this way."

    shiori "Sure you did~"

    yamato "I ain’t worried. {w}It’s just dumb for a girl to walk around at night after what happened."

    shiori "After what didn’t happen, you mean~?"

    yamato "Don’t start. I still don’t buy it."

    shiori "That the Yamakui’s gone~?"

    yamato "...Monsters like that don’t die THAT easy."

    shiori "But [persistent.player_name] said they killed it~"

    yamato "...Not a chance."

    shiori "Hmm~ You ARE jealous~"

    yamato "What?"

    shiori "Of [persistent.player_name]~"

    yamato "Hell no."

    shiori "You sure~? Because they came back a hero..."

    yamato "Tch."

    shiori "And everyone listens to them~ Even you~"

    yamato "I ain’t jealous."

    yamato "It's... {w}just..."

    shiori "...Just?"

    yamato "...I started sword trainin’ first. Took more hits, tried harder."

    yamato "But [persistent.player_name]’s the one everyone calls 'guardian' now."

    shiori "..."

    yamato "...Don’t tell [persistent.player_name] I said that."

    shiori "{cps=10}Hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm~{/cps}"

    yamato "I-I mean it!"

    shiori "Yeah, yeah. I didn’t hear anything~!"

    yamato "Shiori—Ah, shit."

    n "She runs off laughing while Yamato groans under his breath."

    n "He just watches her vanish around the bend, then turns back the way he came."

    n "You instinctively duck behind one of the houses."

    n "...Why?"

    $ preloop6_extra = True

    return

    # village night

label preloop1_scene7:

    $ preloop7_extra = True

    ## vilage day

    n "You are walking down the village path when you see an old woman wobbling away, one hand grips a wooden bucket. The other waves Yamato away."

    "Old Woman" "I said I’m fine, you foul-mouthed brute!"

    yamato "Tch—Lady, I’m just tryna help—"

    "Old Woman" "Don’t {i}'lady'{/i} me with that tone! Watch your mouth!"

    yamato "Watch yer—?! I didn’t even say nothin’!"

    "Old Woman" "You were about to!"

    yamato "How th' fuck—"

    "Old Woman" "There! You see?! Swearing again! Bad child!"

    yamato "Oi! 'S just punctuation!"

    hikaru "...She is correct."

    yamato "Whose side are you on!?"

    hikaru "The village elder’s, obviously."

    yamato "Damn traitor—"

    n "The old woman snatches the bucket back with surprising strength and waddles off, grumbling about ‘youths these days’ and ‘potty-mouthed deer.’"

    yamato "If I were [persistent.player_name], th' damn granny won't—"

    hikaru "Perhaps you can try leading with silence next time."

    yamato "Perhaps ya shut the hell up next time."

    shiori "Ehehe~ Yamato got scolded~"

    yamato "I’ll scold YER face in a minute!"

    shiori "Such language~ In broad daylight~"

    hikaru "Children are present."

    yamato "You’re both DEAD!"

    n "He turns sharply, nearly slips on a puddle, and swears loud enough to earn a second round of glares from the shopkeepers."

    n "Both Hikaru and Shiori laugh..."

    n "...but you don't."

    return

label preloop1_scene8:

    n "The dojo is mostly shadow after dark. Hikaru and Yamato are sitting down after a spar, they don’t know you’re here."

    yamato "Ya ever gonna tell us?"

    hikaru "Hm?"

    yamato "Which ya are."

    hikaru "..."

    yamato "C’mon. Ya hide it better than most, but I ain’t blind."

    hikaru "I didn't hide it because I'm ashamed, if you think that way. It is simply irrelevant."

    yamato "Tch. That’s a shinobi thing?"

    hikaru "It is."

    hikaru "A shinobi is meant to be no one. Gender... {w=0.1}face... {w=0.1}name. All of it is weight."

    yamato "Sounds damn lonely."

    hikaru "...It is."

    yamato "Then why wear the scarf?"

    hikaru "..."

    hikaru "Because it makes me feel like {i}someone.{/i}"

    hikaru "Even if the village thinks {w=0.1}I'm not... But someone does."

    yamato "..."

    shiori "Oh~ There you guys are! The two most antisocial creatures in the village~"

    yamato "Tch."

    hikaru "You were looking for us?"

    shiori "Mmhm~ I made bentos, but [persistent.player_name]’s gone~ I looked everywhere."

    yamato "...Gone?"

    hikaru "...[persistent.player_name] weren’t at the shrine?"

    shiori "Nope!"

    yamato "..."

    hikaru "..."

    shiori "But it’s fine~ I’ll find [persistent.player_name]-sama later. For now, sit down!"

    n "She places the boxes between them. They immediately sit up straighter and eat."

    n "As if this is a habit for them."

    n "Funny, you don't feel familiar at all, like you don't belong."

    n "You slink back to the darkness so they don't see you watching."

    n "...Yet."

    $ preloop8_extra = True

    return
