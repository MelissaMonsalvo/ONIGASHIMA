############# LOOP 2 WHERE ONE DIED ###########################



label loop2_hikaru_mandatory1:

    hikaru "[persistent.player_name]."

    n "Hikaru calls out to you casually. They usually call you by -san."

    n "But now it sounded... different. Their tone sounds different too."

    MC "Yeah?"

    hikaru "You looked pale this morning. {w}Are you alright?"

    n "Has Hikaru always talked to you like this?"

    n "Hikaru's hand moves closer, almost brushing your arm. You feel uncoomfortable immediately."

    hikaru "You haven’t eaten properly in days. {w}Did something happen?"

    hikaru "Hey, if something happened up there... You can tell me."

    n "Their hand is entwined with yours now. You don't know what to make of it."

    n "Did you...?"

    n "Did we--?"

    n2 "Just go with it."

    MC "Kind of hard to concentrate if the villagers looks at you like you're lying."

    hikaru "Ah."

    hikaru "I... can relate."

    MC "Yeah, sorry."

    hikaru "Don't be. {w}Hey, what if we go hunting instead?"

    hikaru "You know, like the old times? Your favorite pastime?"

    n "Even Hikaru looks at you with a little glint of disbelief..."

    n2 "Yes..."

    if not persistent.shiori_dies:
        MC "Sounds nice, is Yamato coming with us?"
    else:
        MC "Sounds nice, is Shiori coming too?"

    hikaru "It’ll just be us. No one else has to know."

    n2 "...They’re planning something."

    n "Or maybe it’s just a date."

    n2 "..."

    n "You follow Hikaru into the woods, heart skipping for all the wrong reasons."

    n "You walk behind Hikaru. Their footsteps make almost no sound."

    n2 "Meat ahead."

    hikaru "There’s something ahead."

    hikaru "See that boar? The right leg's limping."

    MC "Mmhmm."

    hikaru "On my signal, okay?"

    n2 "{fast}Signal?{/fast} Fool. Just kill it."

    hikaru "Now!"

    n "Your blade strikes first and you take down the boar no problem."

    n "Except... [w}Hey..."

    n "Stop, you're drawing too much blood--"

    n2 "Yessss... more... {w}let's pull it open."

    n2 "Succulent ribs, juicy eyeballs."

    n "No--{w}no, stop."

    n2 "*Smell* it... Hhahhh...."

    n2 "So easy to chew--"

    n "Please--"

    n2 "{fast}DON’T INTERRUPT--{/fast}"

    play sound "sfx/grassstep.ogg"

    hikaru "...[persistent.player_name]?"

    MC "....!"

    n "The boar lies beneath your hands, your hands are already digging into it, almost ripping into flesh."

    hikaru "...Are you alright?"

    MC "I-I'm just a little hungry."

    hikaru "Then let’s bring it back quickly. We’ll cook it together."

    n2 "Cook it?"

    n2 "No. {w=0.2}No fire. Fire kills the taste."

    n2 "SHOULD'VE EATEN IT WHILE IT'S FRESH."

    n "You wipe your blade on the grass. Your stomach lurches, but you help Hikaru clean the boar and carry it."

    n "The both of you are walking in total silence now."

    n "The boar swings gently between you, strung on a shared pole."

    hikaru "You... You're sure you're okay?"

    MC "...Sorry. Just thinking."

    hikaru "About what?"

    MC "Uh, umm, how the boar will taste."

    hikaru "Hungry already?"

    MC "Yeah."

    hikaru "Don't worry, I'll make sure it'll taste good for everyone."

    MC "..."

    $ loop2_hikaru_mandatory1 = True

    return

label loop2_hikaru_mandatory2:

    n "When you arrive at the shrine, you see hikaru crouching down beside a curtain."

    hikaru "There’s... something here. Can you help me with--Ah!"

    n "There's a hidden room, it reeks with mold, old rot, and... Ugh."

    n "A horrible smell envelops the room immediately."

    hikaru "...Kami-sama."

    n "Bones are scattered on the floor. Somene's remains, and some still has rotten meat on it."

    if persistent.shiori_eaten:
        n "There are ribbons tied with bells..."

        n "You’ve seen it in someone’s hair--"

        n "And ankle bracelets too..."

        n "No. Who?"

    elif persistent.yamato_eaten:
        n "You see a dark red sash, frayed at the end, alongside a bottle of sake."

        n "Someone wore that around their waist. You remember..."

        n "...the smell of sake in your mouth?"


    n "Hikaru's tears fall, hand shaking in disbelief."

    hikaru "...!"

    hikaru "Wait, what?"

    hikaru "What's going on?"

    n "They’re crying."

    n2 "The soul knows what the mind forgets."

    hikaru "Do I know this person?"

    hikaru "..."

    hikaru "...Why can’t I remember?"

    n "They turn around."

    show hikaru pale at midright with dissolve

    hikaru "[persistent.player_name]..."

    hikaru "Do you remember them?"

    MC "...I..."

    menu:
        "Say you don’t know":
            MC "...I’ve never seen these before."

            hikaru "..."

            hikaru "I... I see."

        "Say nothing":
            MC "..."

    hikaru "Do you think they got eaten by Yamakui?"

    MC "If you can't remember them, then yes."

    hikaru "..."

    MC "But don't worry, I killed it! So there's no way anyone will get eaten again!"

    hikaru "Y-Yes... That's right.."

    MC "Let's just go home, you look pale, Hikaru."

    hikaru "Yeah..."

    scene black

    with fade

    n "You return to the shrine again to see Hikaru crouching at the same place as yesterday, shovel in hand."

    hikaru "It's gone."

    hikaru "Weird... It was here yesterday..."

    hikaru "Do you know where the bones are? I'm about to bury them--"

    MC "No idea."

    if persistent.shiori_eaten:
        MC "Maybe the shrine maiden got rid of it?"

        hikaru "We have NO shrine maiden!"

        hikaru "Or... At least... We had at some point?"

        hikaru "Is this the shrine maiden?"

        n "You just shrug."

    elif persistent.yamato_eaten:
        MC "Did Shiori bury it?"

        hikaru "No... I told Shiori that I'll bury it myself..."

    hikaru "Did you--?"

    hikaru "...No. You wouldn’t."

    play sound "sfx/breath_hold.ogg"
    $ renpy.pause(0.8)

    n "They turn toward you, slowly."

    show hikaru pale at midright

    hikaru "[persistent.player_name]...?"

    MC "Mm?"

    hikaru "I'm gonna go look for it. Maybe someone else buried it."

    MC "Okay, I'll stay here then."

    hikaru "Yeah, see you."

    n "They step away, but you remain a moment longer."

    n "Staring at the place where cloth used to lay folded over bone."

    n "You *should* remember."

    n "Whoever owned the bones... They used to augh with you, didn't they...?"

    n2 "..."

    n2 "I only remember the screaming."

    $ loop2_hikaru_mandatory2 = True

    return

label loop2_hikaru_mandatory3:

    n "You and Hikaru are sitting together under the shrine awning."

    hikaru "You know what, I think you've changed since the mountains."

    hikaru "You're... a lot quieter now, and a lot less affectionate."

    hikaru "Are you mad at me?"

    n "Their hand moves slowly and stops over your chest, right above where your heartbeat should be."

    n2 "{fast}Hhhh...{/fast}"

    hikaru "I feel like something’s missing."

    hikaru "Are you bored of me? Sorry that I got too paranoid about the bones, but--"

    hikaru "Don't you think that even the Yamakui is dead now, everything's still not how it's supposed to be?"

    n "You lean in..."

    hikaru "[persistent.player_name]...?"

    n "...and shut them up with a kiss."

    ##3 squelching kiss

    n "Hikaru's mouth tries to follow, but--"

    hikaru "Mmmph--"

    n2 "The tounge will know the path. {w}Slide it deep, and it'll find the center."

    n "What are you talking about--"

    n2 "Still ripe."

    play sound "sfx/kiss_press_deep.ogg"
    $ renpy.pause(1.5)

    n "Stop. Please. PLEASE--"

    n2 "Down. {w=0.2}Slide down. {w=0.2}Make room. {w=0.2}There's the soft windpipe{nw}"

    n2 "Warm, warm, warm all the way in."

    n "Stopstopstopstopstopstopstop--"

    play sound "sfx/gag.ogg"
    $ renpy.pause(0.4)

    hikaru "--ghhk--!"

    play sound "sfx/pull_away.ogg"

    n "They shove you back, breathless."

    show hikaru pale at midright with dissolve

    hikaru "What... the... [persistent.player_name]?"

    hikaru "That... that wasn’t..."

    n2 "Let’s go deeper this time."

    n "NO!"

    MC "..."

    MC "Why? You said I wasn't as affectionate."

    MC "This good enough for you?"

    hikaru "I-I..."

    hikaru "You're being weird, [persistent.player_name]. What's... what's gotten into you?"

    MC "I don't understand."

    hikaru "I... I just remembered--"

    hikaru "The, uh--fire. I left my irori still burning--"

    n "They gesture vaguely toward the trail, not even looking that direction."

    hikaru "I should... turn the fire off before my food bruns to a crisp."

    n "Run, Hikaru, please... Just go away--"

    MC "..."

    MC "..." ## change to eerie expression
    $ loop2_hikaru_mandatory3 = True

    return

label loop2_hikaru_mandatory4:

    n "You hear a soft knocking at your door, you open it to reveal Hikaru standing in front of your house."

    MC "Hey, Hikaru. Come in--"

    n "Hikaru doesn't budge."

    hikaru "..."

    hikaru "I’ve been thinking."

    hikaru "Last night... that wasn’t you, was it?"

    hikaru "The way you kissed me. That--"

    hikaru "That feels... wrong."

    MC "Huh?"

    hikaru "Your tongue is not that long, isn't it?"

    hikaru "I've always known how your body feels like--"

    hikaru "[persistent.player_name] would never kiss like that."

    hikaru "[persistent.player_name] never looked at me like I was something to-to... {i}unwrap and swallow.{/i}"

    hikaru "You're not [persistent.player_name]."

    n "You step forward, but Hikaru unsheates their sai."

    n "No, just... {w}Run. Stay away from me, from us--"

    hikaru "Who are you,,,?"

    hikaru "No, WHAT are you!?"

    $ name_input_index = 0
    $ name_display = ""

    call screen fake_name_input

    $ name = name_display

    n "You feel your mouth move. Your jaw feels like it wants to unhinge--"

    n "Your name is--"

    n2 "{fast}Y a m a k u i.{/fast}"

    hikaru "...No."

    play sound "sfx/heartbeat.ogg"
    $ renpy.pause(0.5)

    hikaru "No--no--"

    n2 "I told you."

    n2 "Y a m a k u i."

    n2 "That’s the real name under the skin."

    play sound "sfx/fabric_rustle.ogg"

    n "Hikaru stumbles back, hands trembling. Their mouth hanging open, wanting to scream but can’t."

    play sound "sfx/step_back.ogg"
    $ renpy.pause(0.3)

    hikaru "You killed [persistent.player_name]..."

    MC "Hikaru--"

    hikaru "STAND BACK!"

    hikaru "I’ll--I’ll kill you--"

    play sound "sfx/running_steps.ogg"
    stop ambient fadeout 1.0

    n "Hikaru..."

    n2 "Run, run little bird..."

    n2 "B u t t h e r e d m o o n i s c o m i n g."

    $ loop2_hikaru_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear

    return
