############# LOOP 1 WHERE EVERYONE IS ALIVE ###########################
label loop1_hikaru_mandatory1:

    n "Everyone is tense because of the red moon."

    n "You feel like more people will be at the shrine for prayers, so naturally you go there."

    n "The way to the shrine is eerily quiet, though. It's as if something can just appear and you{nw}"

    # JUMPSCARE here

    "???" "...Guess who."

    play sound "sfx/heartbeat.ogg"

    n "Suddenly, a pair of hands cover your eyes and you feel a breath right behind your ears."

    n "You freeze. Can’t tell if you’re breathing or just pretending to."

    "???" "Still jumpy, huh [persistent.player_name]?"

    n "You hear a soft chuckle behind you, a familiar voice that you've heard it a lot of times."

    n "Ah yes,,, Feels so familliar isn't it? You remember the soft giggle in their tone, how their voice raises an octave when they say your name."

    n "Who--"

    hikaru "Aw, did you forgot about me while you're fighting the Yamakui?"

    n "They finally let go of you, you turn around just to see Hikaru."

    n "Didn't Hikaru greet you with a cold demeanor when you return? Why is--"

    n "Hold on, let me remember..."

    MC "...Hikaru?"

    hikaru "Surprise."

    hikaru "..."

    MC "..."

    Hikaru "Hey, are you all right, [persistent.player_name]?"

    n "This... {w=0.2}this part doesn’t feel familiar. But it sounds like it should be."

    n "Hikaru walks forward to touch your, but instinctively you step back, avoiding their outstretched hand."

    MC "Yeah, I'm fine. Can you step back?"

    hikaru "Eh?"

    n "Wait. Why did you say that?"

    hikaru "Are you mad of me because I said the armor's too small?"

    MC "What?"

    hikaru "You’ve been off ever since you've returned from slaying the Yamakui "

    MC "Um, ahahaha... No, of course not. I'm just... tired, is all."

    hikaru "Ah, I... see."

    MC "Sorry if I’ve been weird. I just... {w=0.3}I don’t know why this feels so strange right now."

    hikaru "But you remember what we are, right?"

    n "Your stomach turns. What are you supposed to say to that?"

    MC "Of course I do."

    n "You hear yourself answer without even thinking."

    hikaru "Really now?"

    n "They step closer and you feel like they're breaching your proximity. This is odd..."

    n "If you're together, then it should be okay to stay close like this {w}right?"

    MC "Hikaru, when did we...?"

    hikaru "...Kissed?"

    hikaru "It's before you left, Dummy. Or did you forgrt that, too?"

    n "You don't remember kissing them."

    n "But they sound so certain.... {w}Well, it’s easier to agree than to argue with something that might be true."

    n "You can find out later."

    MC "Right. I remember."

    hikaru "Do you? Did the Yamakui knock your head so hard you had amnesia?"

    n "Their fingers brush your arm to calm you down, to ground you, instead you feel eerie."

    MC "Yeah! Yeah, I just need time to readjust."

    hikaru "Is that all it is?"

    MC "Of course. What else would it be?"

    n "You regret the question the moment it leaves your mouth."

    n "Hikaru's smile sharpens for half a second before settling back into softness."

    hikaru "I missed you so much [persistent.player_name]"

    hikaru "I'm really glad you got to return, even though you're weird now."

    MC "Yeah. I’m sorry."

    hikaru "Don't be. I think... I think you just need to rest."

    n "Their hand lingers on your sleeve a moment too long before letting go."

    hikaru "It’s okay. You’ll remember again."

    MC "Yeah.... Yeah! See you, Hikaru!"

    n "You feel watched all the way down until Hikaru dissapears from view."

    n "You try to shake that feeling away, but you can't forget how Hikaru's eyes look like when you turn away."

    n "Hey..."

    n "What if Hikaru's the one being right and you just forgot?"

    n "Don't you think it's worth asking around for?"

    return


    $ loop1_hikaru_mandatory1 = True

    return

label loop1_hikaru_mandatory2:

    hikaru "Hey."

    n "Hikaru is wearing a scarf today while they're training, it looks a little worn at the ends, but clearly they took care of it."

    n "You’ve seen it before. Haven’t you?"

    MC "Is that new?"

    hikaru "...Huh?"

    n "Hikaru's eyes alternate between you and the scarf, brows furrowing, as if you're asking a ridiculous question."

    hikaru "You mean the scarf?"

    MC "Yeah."

    hikaru "[persistent.player_name], you gave it to me."

    MC "...I did?"

    hikaru "Yes... You said so I don't get cold."

    MC "...I really don’t remember."

    hikaru "...What?"

    hikaru "Come on... Dpn't you remember? You tied it around my neck yourself."

    MC "...I really don't."

    n "Wrong thing to say."

    hikaru "What the hell are you talking about?"

    n "Hikaru's usual calm demeanor drops immediately, their hands curl into fists at their sides."

    hikaru "You remember Shiori and Yamato."

    hikaru "But not {/i}me?"

    hikaru "Not us?"

    n "They grab the scarf with both hands and yank it off. Thrust it toward you like proof in a courtroom."

    hikaru "You picked it! You said the red matched the color of the moon and it gave you hope that we'll get through it!"

    hikaru "You said I looked beautiful in it. You said--"

    n "Their mouth stops. Their shoulders are shaking now."

    MC "Hikaru, I... I don’t know what’s happening."

    hikaru "This isn’t right. This--"

    hikaru "What if something’s wrong with you?"

    MC "Excuse me?"

    hikaru "Do you think this is funny?"

    MC "Hikaru--"

    hikaru "When you were gone, I waited for you, You promised me you'd get back, but now you return and forgot everything about us--"

    MC "Hikaru, if we're really together as you said, why don't Yamato and Shiori said anything? Why didn't you hug me when I retirn?"

    hikaru "Because we're keeping it a secret!"

    MC "Why?"

    hikaru "*scoffs*"

    hikaru "...You're scaring me."

    MC "You’re the one scaring me."

    hikaru "...This isn't you."

    hikaru "Who ARE you!?"

    n "Hikaru stares at you, breathing hard. Their face contorts into something... Is it grief? Suspicion? Anger?"

    n "Before you could make something out of it, they turn and storm off."

    n "And you’re left standing in the quiet."

    return



    $ loop1_hikaru_mandatory2 = True

    return

label loop1_hikaru_mandatory3:


    hikaru "[persistent.player_name]-san."

    n "Was that honorifics? But Hikaru does call you that in public..."

    MC "What do you want now?"

    hikaru "Sorry for yelling at you yesterday, I was... frustrated."

    MC "..."

    hikaru "I asked for help and Shiori told me to give this to you."

    MC "What is it?"

    hikaru "A talisman. She said maybe... maybe your memory problems were caused by trauma. Or worse."

    hikaru "It’s to help you remember."

    MC "...Thanks."

    n "You take it and it feels quite warm in your hand. You turn it around, but can't find any heat source in it."

    n "Still, you smell something faintly burning, it's coming from the talisman."

    n "You pocket it and the odd smell dissapears immediately."

    hikaru "...."

    n "You just heard Hikaru's breath hitched, as if they had been holding their breath for a while."

    MC "...What?"

    hikaru "Do you feel anything? I mean--does it hurt, or tingle, or maybe a flash of something? Memory? Emotion?"

    MC "Not really, no."

    hikaru "Are you sure?"

    MC "Yeah.... Why?"

    hikaru "It’s just--"

    hikaru "I was hoping it would react."

    MC "React?"

    hikaru "I mean--help. I meant help."

    MC "Where did Shiori get this, again?"

    hikaru "She said the old priest gave it to her."

    MC "...Ah."

    n "If it's from Shiori and the priest, then it should be okay right?"

    MC "What is it for, again?"

    hikaru "Sleep."

    MC "Oh."

    hikaru "...."

    MC "...."

    ## uncomfortable silence

    hikaru "It doesn’t matter. I hope it'll get your memory back someday, maybe it... doesn't work immediately."

    hikaru "You should go back home. It’s late."

    MC "And you?"

    hikaru "I’ll be around. If you need me."

    n "They walk away without another word."

    n "You pull the talisman out again once Hikaru turns in a corner and out of sight."

    n "This time the burning smell hits instantly. It stings your nostrils and makes your eyes water. There's a sharp, bitter smell that shouldn't be there."

    n "The paper feels hot and pulsing now."

    MC "..."

    n "You drop it, then you--"

    ## thud

    n "--stomp on it."

    ## thud

    n "Again."

    ## THUD

    n "Again."

    MC "..."

    n "Why? Clearly Hikaru was trying to be nice..."

    n "You keep stomping until it's almost crumpled now, then kick a patch of dirt over it. As if that makes it disappear."

    n "..."

    n "Let's just hope Hikaru never finds out what you did."

    #return


    $ loop1_hikaru_mandatory3 = True

    return

label loop1_hikaru_mandatory4:

    n "You’ve just finished cleaning yourself when--"

    play sound "sfx/knock.ogg"

    hikaru "[persistent.player_name]-san? Are you home?"

    n "Hikaru."

    MC "..."

    hikaru "[persistent.player_name]-san?"

    n "..."

    n "You don’t {i}have{/i} to answer. Of course not."

    n "But..."

    n "Maybe we should hear what they want to say?"

    n "Even though they are so persistent in saying that you two are more than friends, maybe Hikaru is not lying."

    n "You know they're not the type to lie."

    n "Maybe just open it a crack..."

    ## so like, the mouse drags to yes, to open the door, but you can still pick no

    menu:
        "Open the door?"
        "Yes":
            jump hikaru_visit_continued
        "No":
            n "Oh. You're really not opening it, then?"
            n "Well. That's... your choice."
            jump hikaru_visit_rejected


label hikaru_visit_rejected:

    n "You pretend that you're not at home."

    n "That's fine... you must’ve had your reasons. But what are you so afraid of?"

    n "It's just Hikaru..."

    n "After a series of repeated knocks with no avail, it stops."

    n "And you sit in the darkness alone again."

    scene black with fade
    $ renpy.pause(1.0)
    return

label hikaru_visit_continued:

    hikaru "Good evening, [persistent.player_name]."

    MC "Hey, Hikaru. Did you need something?"

    hikaru "I was just walking by... and wondered if I should, uh, pay a visit."

    n "That's not true."

    n "They're lying. It's really obvious. Hikaru is never good at lying."

    n "But don't you want to know why they’re really here?"

    n "You could say it's a bad time, that’d be fair."

    n "But let's be honest... {w}You’re not really doing anything, and they’re already on your doorstep."

    n "So it couldn't hurt to see what they're up to, right?"

    n "Go on. Just a few minutes...?"

    ## mouse creeps toward yes

    menu:
        "Let Hikaru inside?"
        "Yes":
            MC "...Come in. It’s a bit messy, though."
            n "Great!{w} I mean{w} Good."
            jump hikaru_inside
        "No":

            jump hikaru_doorclose


label hikaru_doorclose:

    MC "It's a bad time... Sorry."

    Hikaru "Oh, I-I see. My apologies for intruding."

    n "Still shutting them out, huh?"

    n "That’s... fine. I suppose."

    n "You closed the door in their face."

    n "Shame, now we won't know the real reason why they're here."

    scene black with fade
    $ renpy.pause(1.0)
    return

label hikaru_inside:


    hikaru "Hm... When is it not always messy?"

    n "Interesting, so they've been here before.  Maybe a couple of times."

    n "You don't remember ever inviting them, though. Odd."

    n "Well, that doesn't matter."

    hikaru "...Is the armor still here?"

    MC "Yep."

    hikaru "Can I see it again?"

    n "There it is."

    n "I guess just taking a peek at the armor won't cause any harm, right?"

    menu:
        "Show the armor?"
        "Yes":
            jump hikaru_armor
        "No":
            jump hikaru_armorrefuse

label hikaru_armorrefuse:

    MC "Why?"

    hikaru "Because I am merely curious, that is all."

    MC "I don't think that's true."

    n "Still--"

    MC "Look... We don't know much about Yamakui, it could be cursed for all we know."

    MC "I'm trying to understand it before anyone else gets hurt."

    hikaru "...Hmm."

    hikaru "I see. But if the Yamakui's dead, then it should be safe, right?"

    hikaru "And... If it’s really that dangerous, why keep it at all?"

    MC "Because I slayed the damn thing. If anyone's protecting the village from it, it should be me."

    hikaru "..."

    hikaru "Makes sense, I guess."

    hikaru "All right. I won't push."

    n "They turn to leave, but hesitates just past your shoulder."

    hikaru "...Still, be careful. Things like that tend to change people."

    n "And then they're gone."

    n "If even Hikaru suspects something... how long before others start asking, too?"

    scene black with fade
    $ renpy.pause(1.0)
    return


label hikaru_armor:

    MC "Fine, I guess just a peek wouldn't hurt."

    n "You bring Hikaru inside to look at the armor, the cover folds away like skin as you pull it down."

    n "It looks smaller than you remember. That’s strange."

    hikaru "..."

    n "Hikaru circles around the armor, inspecting it with furrowed brows."

    n "You don't know what they are actually looking for. There's only dried blood and remnants of flesh."

    n "That's because you haven't washed it at all and left it bloodied like that."

    hikaru "Thank you. That's all I need."

    n "That wasn’t so hard, was it?"

    MC "All right, since you're here... Want some tea?"

    hikaru "Oh, speaking of tea... I brought some for you."

    MC "Oh, thank you."

    n "You brew the tea Hikaru gave you. It looks like a perfectly normal green tea."

    Hikaru "Shiori said to add the dried ume and dried kombu before you pour the tea over."

    MC "I see... That's interesting."

    n "You serve the tea for the both of you afterwards."

    n "Since you brew it yourself... it will be fine if you drink it, right?"

    menu:
        "Drink the tea?"
        "Yes":
            jump hikaru_teadrink
        "No":
            jump hikaru_teareject

label hikaru_teareject:

    n "As soon as the tea is ready, Hikaru immediately sips it."

    n "You decide not to."

    hikaru "What's wrong?"

    MC "Nothing. I'm... full."

    hikaru "Hmm."

    n "They say nothing more and finish their tea."

    n "What are you so afraid of? You're the one who brews it. Hikaru clearly drank that tea and is fine."

    n "So what’s the hesitation?"

    n "Come on. Don’t be rude."

    n "Drink it."

    MC "..."

    MC "..."

    MC "It’s late."

    hikaru "Mm."

    MC "You should probably head back."

    hikaru "Yes. {w}Of course."

    n "Hikaru places the empty cup slowly on the table, eyes never leaving yours."

    hikaru "Thanks for... letting me see the armor."

    MC "Anytime."

    n "They smile, but there’s something distant in it now. As if they expected... something?"

    n "You should've drunk the tea."

    hikaru "Good night, [persistent.player_name]."

    scene black with fade
    $ renpy.pause(1.0)
    return




label hikaru_teadrink:


    n "Hikaru drinks theirs and immediately finishes the cup."

    n "Nothing happens."

    n "Of course nothing happens."

    Hikaru "Well?"

    n "The cup touches your lips, and you immediately drink it."

    n "The taste of salt hits first, followed by sour... and ended up bitter at the tip of your tounge."

    n "You can't breathe, you want to throw up blood, but you swallow it."

    MC "Gh--!"

    n "The liquid drags down your throat like broken glass soaked in syrup."

    n "You feel it tearing."

    MC "...Aah--"

    hikaru "Is it too strong for you?"

    MC "...No. It’s... {W}fine."

    n "The warmth spreads immediately... then turns into burning."

    n "Down, down, down from your throat, into your chest, then ripping your gut apart."

    hikaru "Are you okay, [persistent.player_name]?"

    MC "...I'm... {w}fine..."

    hikaru "Really? You look... mortified."

    hikaru "If you hated it that much, maybe--"

    MC "I'M FINE."

    n "You sip one more time to make a point."

    n "Big mistake."

    play sound "sfx/gulp.ogg"

    n "The tea sloshes past your lips, and your stomach convulses as you force it down your throat again."

    n "The same burn, the same trail of salt, the same taste of your own blood..."

    n "...the same clawing ache in your stomach. Even worse now."

    n "Poison?"

    n "A curse?"

    n "But Hikaru looks fine... and you're the one brewing it...."

    MC "...Hhh--D-Did you say what this was? I didn't remember--"

    hikaru "You drank it last year, and before that. On fact, the four of us did."

    hikaru "Remember the new year's celebration?"

    MC "W-Wh--"

    n "You can’t speak as the heat keeps rising, bile festering behind your throat."

    n "You want to spit it out, but you manage to muster a smile."

    MC "Oh, really? Uh, what did--What did we drink again?"

    hikaru "It’s only Obukucha, [persistent.player_name]-san."

    scene black

    n "A pickled plum brings protection."

    n "Hikaru means well. Of course they mean well."

    MC "...Thanks. For the tea."

    MC "You should probably head out. It’s late."

    hikaru "Of course."

    hikaru "Feel better soon, okay?"

    MC "...Mm."

    n "The door slides behind them."

    n ",,,"

    n "..."

    n "..."

    MC "..."

    n "You lunge for the tray, rattling the cups."

    n "Your breath shakes."

    MC "...Disgusting... Disgusting... Disgusting..."

    n "You carry the tray outside and rip the door open and--"

    MC "Haa... Haa... Haa..."

    n "--you throw the tray. Well, more like you slammed the tray into the ground that every glasswares breaks apart."

    MC "..."

    n "Why?"

    n "It’s just tea."

    n "Why are you shaking?"

    MC "Shut--"

    MC "...Ngh."

    n "You step back inside, close the door and lean against the wood and breathe until your legs stop trembling."

    n "It's just tea, [persistent.player_name]..."

    #return

    $ loop1_hikaru_mandatory4 = True

    return

label loop1_hikaru_mandatory5:

    n "You walk up the shrine path, looking for Shiori."

    n "Coincidentally, Yamato's there too, for some reason."

    shiori "Ara~ Good morning [persistent.player_name]-sama!"

    yamato "Tch..."

    MC "Shiori-chan, I have something to ask you. Might as well ask Yamato as well."

    shiori "Oho~? Sounds serious."

    MC "...Was I ever... {w}with Hikaru?"

    shiori "Eh?"

    yamato "...Hah?"

    MC "I mean... like that.{w} Close.{w} Before the mountain. Were we...?"

    n "Both Yamato and Shiori stare at each other with disbelief."

    shiori "I don’t think so...? You two get along, but I’ve never heard Hikaru say anything like that."

    shiori "Did something happen, [persistent.player_name]-sama?"

    yamato "Pffft... Keh."

    play sound "sfx/snort.ogg"

    yamato "AhahahaHHAHAHhahaha!"

    yamato "[persistent.player_name]? With Hikaru!?"

    MC "What's that supposed to mean?"

    yamato "No fuckin' way!"

    yamato "You’re loud and anoying. And Hikaru? That one’s quiet as a grave!"

    yamato "Ya ain’t their type. Not by a long shot."

    shiori "Yamato-kun~ don’t be rude!"

    yamato "Oi, I’m just sayin’ the truth."

    yamato "If you two were hidin’ somethin’, I’d have noticed. Shiori too."

    shiori "Mm... I think so, right?"

    yamato "Did the Yamakui hit yer head so hard ya start hallucinating a damn relationship?"

    MC "..."

    MC "...I-I see."

    shiori "You sure you're okay, [persistent.player_name]-sama?"

    MC "I’m fine."

    yamato "Yeah, so that's the dumbest shit I've ever heard since ya came back from that damn mountain."

    shiori "If something’s bothering you, I can ask Hikaru myself?"

    MC "No. Don’t."

    n "Behind you, by the incense basin, an old woman mutters something... But your sharp ears catches it."

    "Woman" "Please... I pray [persistent.player_name]-sama doesn’t get too close to that one..."

    yamato "T’fuck did ya just say?"

    "Woman" "I mean... Don’t you think Hikaru has been… off lately?"

    "Woman" "Just like Karasuma-san was. Before he--"

    yamato "Tch. This village ran one man off ‘cause it got spooked. An’ now ya wanna do it again to his kid?"

    yamato "Hikaru’s nothin’ like their father!"

    "Man" "How would you know that?"

    shiori "Hikaru-san always helps me at the shrine, and will never hurt a soul!"

    "Woman" "You weren’t there that night..."

    yamato "Y’wanna blame someone, go stare at yerself in a mirror ‘til it cracks."

    n "Yamato unsheathes his blade. Just a little."

    n "The old couple imemdiately back away, hands still clutching prayer beads."

    yamato "Tch. Damn cowards."

    n "You know... Hikaru’s father vanished on the last Red Moon."

    n "Some say he chased the Yamakui. Sword in hand."

    n "Some say he chased the Yamakui. Some say he tried to stop it."

    n "Some say he never even made it past the gate."

    n "You know how paranoia works. Plant one seed of doubt and suddenly it spreads like wildfire."

    n "Hikaru was only twelve back then, remember?"

    MC "No."

    n "You don't?{w} Huh."

    MC "..."

    n "Hm? How do I know that...?"

    MC "..."

    n "Mmm... {w}Odd. How DO I know that when you don't even remember that?"


    $ loop1_hikaru_mandatory5 = True

    return
