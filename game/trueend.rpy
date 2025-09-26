label truend:

    scene bg shrine_night with fade

    # Show all three characters in their exact positions
    show hik normal:
        zoom 0.231
        xanchor 0.5
        yalign -0.09
        xzoom 1.0
        yzoom 1.0
        yoffset 460

    show yam normal:
        zoom 0.23
        xanchor 0.5
        yalign -0.04
        xzoom 1.0
        yzoom 1.0
        yoffset 0

    show shi normal:
        zoom 0.26
        xanchor 0.5
        xalign 0.5
        yalign -0.60
        yoffset 0
        xzoom 1.0
        yzoom 1.0

    with dissolve

    n "They called this meeting without you."

    n "but you let them, anyway."

    show hik serious
    with dissolve
    hikaru "Yamato. Shiori. I... need you to listen."

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

    n "Yamato crosses his arms, scowling. Shiori’s eyes wander to the dark corners."

    show yam serious
    with dissolve
    yamato "So ya thinkin' what I'm thinkin'. [persistent.player_name]'s hella odd lately."

    show hik sad
    with dissolve
    hikaru "Yes. More than off, even... I think it's not really [persistent.player_name] that came back from the mountains."

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
    with dissolve
    yamato "WHAAAAAAAAAAAAAAAAAAT!? The hell did ya just say?!"
    yamato "Ya mean t’tell me, all this time... you and that idiot were--?"

    show hik sad
    with dissolve
    hikaru "Yes. [persistent.player_name] was my partner. My... {w}lover."

    n "Shiori tilts her head, her mouth curling into a mischievous smile. Yamato’s voice cracks, rough with something like betrayal."

    show shi smug
    with dissolve
    shiori "Ehehe... I had my suspicions~"
    shiori "You two were always soooo awkward around each other, all blushy and stuff. I thought maybe..."

    show yam annoyed
    with dissolve
    yamato "Tch... t’hell... Why the secrets, then?"


    hikaru "Because of my father, the man who was branded a traitor. No one would accept me with [persistent.player_name]."

    show hik sad with dissolve
    hikaru "So we kept it hidden, even from you guys."
    hikaru "I'm... sorry about that."

    show hik worried with dissolve
    hikaru "So... That's why I know it's not [persistent.player_name], because [persistent.player_name] didn't even know we're together."
    hikaru "Because only the two of us are supposed to know."
    hikaru "This... thing wears their face, but it is {i}not{/i} [persistent.player_name]."

    show yam shocked with dissolve
    # Shiori stays normal for transition
    shiori "...Then what will you do, Hikaru?"

    show hik serious with dissolve
    hikaru "I think... we cannot ignore it anymore."
    hikaru "Or we'll all die."
    hikaru "My theory... That [persistent.player_name] may be possessed by Yamakui. Or worse, [persistent.player_name]'s body has been stolen."

    show yam angry with dissolve
    yamato "Tch... fuck... Don’t say it like that, Hikaru."
    yamato "But... yeah. I been thinkin’ the same damn thing. Somethin’s off. Ain’t just me bein’ jealous."

    show shi sad with dissolve
    shiori "...I thought so to."
    shiori "But... I don't want to stop it."

    show yam shocked with dissolve
    n "What? Did she just--?!"

    show yam angry with dissolve
    yamato "...Oi. The hell did ya just say, Shiori-chan?"

    show hik surprised with dissolve
    hikaru "Shiori-chan...?"

    show shi worried with dissolve
    shiori "Because I think it's not that bad!"
    shiori "Do you remember that night where I was missing and you guys were looking for me?"

    show shi sad with dissolve
    shiori "I was left in the forest that night... tied up, wrists bleeding, gagged. I was about to be sacrificed."
    shiori "I think... it was the old priest? Or maybe someone else. I forgot their face."
    shiori "But the Yamakui came and spared me, ate the priest instead! Even though I was the easier meal!"

    show yam shocked with dissolve
    n "Bound in the forest? As a child...?"

    show shi happyblush with dissolve
    shiori "That’s when I knew. Yamakui only eats bad people."
    shiori "I believe that it spares the ones it loves."

    show yam rage with dissolve
    yamato "Ya’ve lost it. Ya’ve completely lost it, Shiori!"

    show hik panic with dissolve
    hikaru "Shiori-chan, why didn't you tell us!?"

    return


    shiori "Well, you know whoever that was eaten got forgotten, right? You'd just say I was crazy!"

    hikaru "Still, that's insane..."
    yamato "Tch... I don’t get you, Shiori. How the hell can ya defend somethin’ that’s been eatin’ us alive for generations?"

    hikaru "You knew it ate the villagers one by one! You cannot keep pretending it is anything but a monster."

    shiori "Ehehe... pretend? I’m not pretending, Hikaru-san~"
    shiori "When no one else saved me, Yamakui did. That’s all that matters to Shiori~"

    yamato "Ya think sparin’ ya one time makes it good?!"
    yamato "It’s eaten people, Shiori! Real people. Families, neighbors, friends. What part o’ that don’t ya get?!"

    hikaru "Even if it spared you, that doesn’t erase the rest...!"
    hikaru "If we do nothing, it will come for all of us!"

    shiori "Mouu~ You two don’t understand anything"
    shiori "You have never been save by Yamakui-sama!"

    yamato "Yer insane."

    hikaru "...Shiori-chan. Please."

    shiori "No. I won’t help you kill it. {w}I won’t."

    n "That playful lilt drops, just for an instant."

    shiori "If you want to fight it, do it without me."

    n "And with that, she turns away, dragging her feet as if daring them to call her back."
    n "The shrine doors creak as Shiori disappears into the dark. The silence left behind is unbearable."

    yamato "God damn it..."
    hikaru "..."
    hikaru "No, let's try again tomorrow, Yamato."
    hikaru "We can still save her, she's not too far gone."

    yamato "What are we gonna do, then?"
    hikaru "...I think I have a plan."

    with fade

    n "Hikaru and Yamato returns again to the Shrine as Shiori is absentmidedly sweeping dirt."

    hikaru "Shiori-chan--"
    shiori "What now?"

    hikaru "We were all friends, weren't we? The four of us."
    hikaru "Don't you forget all about [persistent.player_name]?"

    n "Hikaru hands her a letter written by... [persistent.player_name]. You.{w} Me?"

    hikaru "Remember these letters and whishes we used to write down when we were kids?"
    hikaru "And this scarf--"

    n "The red scarf...."
    n "I remember that..."
    n "I was wearing that, when I--"
    n "Wait."

    hikaru "We were best friends, weren't we!? The Yamakui ate our friend!"
    hikaru "How could you say that Yamakui only ate the bad people!?"

    yamato "Oi, Shiori! Open yer damn eyes already!"
    yamato "Ya think this monster’s some savior? Some lover? Tch... bullshit!"

    n "Yamato slams his fist into the shrine pillar, making Shiorijolt."

    yamato "Who the hell protected ya from bullies, huh? Who stood between ya an’ the bigger kids? It was [persistent.player_name]!"
    hikaru "Our friend who never hurt anyone, Shiori-chan. Please, just try to remember."
    yamato "Yeah. That bastard didn’t deserve to die!"

    shiori "..."

    n "Shiori’s lips tremble. Her eyes dart between them. For once... she is speechless."

    shiori "I--"

    hikaru "Please. Shiori-chan. Don’t let your feelings blind you."
    hikaru "Deep down, you already know the truth."

    shiori "I know that [persistent.player_name]'s not a bad person..."

    hikaru "..."
    hikaru "No matter what you choose in the end, we're still going to kill it."
    hikaru "I won’t watch this... {w}this monster wear [persistent.player_name]'s face and kill everyone."

    yamato "Tch... damn right. I ain’t sittin’ back either."
    hikaru "If you still consider [persistent.player_name] your friend... Then you'll come with us."

    shiori "...."

    shiori "..Fine, I'll help."

    shiori "But only because I think we can save both Yamakui and our friend."

    scene black
    with fade

    n "Later, Shiori brings them to the innermost part of the shrine, where old documents reside."

    shiori "I think we can start from these if we want to find clues about the Yamakui."
    shiori "I was looking into the Yamakui but someone... maybe the old priest tried to stop me from it."
    yamato "Tch. Half of it’s rotted. What’s it say?"

    shiori "Something about... {w}famine, and long winters when nothing grew.'"
    shiori "It says... outsiders were 'invited' to the village. But... no one was ever recorded leaving."
    hikaru "Did they stay in the village?"
    shiori "I don't think so... It says 'offerings made at the altar, so our children would not starve.'"
    yamato "Damned sacrifices."

    shiori "There’s more. Look here. The priests wrote... {w}'Kami-sama grew silent after.'"
    shiori "'We are forever condemned from their light'"
    hikaru "The kami-sama turned their face away."
    shiori "'And a new god rose from the mountains'"

    hikaru "...Yamakui."

    shiori "That was all I managed to find, I'll look into it more..."

    yamato "Tch... So all this is just a punishment for what our damned ancestors did?"

    shiori "..."

    hikaru "I think we'll stop here for now. Shiori, keep trying to look into it."
    hikaru "Yamato, we'll try to find a way out of the village."
    yamato "Huh? But there ain't a way out, the elders said--"
    hikaru "My father went out to look for it. And even though no one knew what happened to him..."
    hikaru "Since everyone still remembers him, it's possible he didn't get eaten by the Yamakui."

    yamato "..."

    yamato "Fine."
    yamato "We'll go first thing in the morning."

    with fade

    n "The mountain path should’ve led out. But the farther they walk, the whiter the air becomes."
    n "A thick mist is swallowing everything. Rocks vanish, trees blur, even sound feels muffled and strange."

    yamato "Oi... this ain’t right. I walked this trail before. Where the hell’s the gate?"

    hikaru "It should be here. The road leads straight--"

    n "Their words cut off as the mist parts, just for a second. A drop rumbles beneath Hikaru’s feet."

    with vpunch

    hikaru "Ah--!"

    n "They stumble, tries to flap their wings but it seems like the air is dragging Hikaru down."

    yamato "OI!!"

    n "Yamato lunges, arm hooking around Hikaru’s waist. He manage to save Hikaru, barely."

    yamato "Tch--hold on, dammit!! Don’t ya dare--"
    hikaru "My wings... What's going on!?"

    yamato "Climb now, think later, damnit!"

    n "Hikaru claws back onto solid ground, as yamato pulls Hikaru back above."

    hikaru "Haa... Haa..."

    hikaru "...If you hadn’t..."

    yamato "Shuddup, I don't wanna hear it."

    hikaru "The elders... they always warned us not to leave."

    yamato "...Said the gods’d be angry. Or some shit."

    hikaru "It's a dead end, then..."

    yamato "Sorry, Hikaru. But I think yer dad's down there."

    hikaru "..."

    hikaru "Let's just... go back to the village."

    n "They return to the shrine to find Shiori already laying out older scrolls on the floor."

    shiori "I didn't find much, but I think this part explains more."

    shiori "So this part talks about 'The bargain for food that never failed and wombs that never emptied.'"
    hikaru "That is how the fields flourished... how the children were always strong. Even thought the Yamakui is picking off the villagers one by one."

    shiori "That's because it's the price."
    shiori "Every red moon, Yamakui comes to eat someone."

    hikaru "So the mist is the barrier to keep people from running away."
    yamato "No wonder the elders told us never to leave. They knew. They fuckin’ knew."
    shiori "It is considered an act so blasphemous, to pray to a god other than Kami-sama."

    yamato "Tch. That all ya found, Shiori?"

    shiori "No, look at this part here..."
    shiori "The texts mention the Oni Slayer’s blade. The one [persistent.player_name] carried up the mountain."
    yamato "Okay, but if [persistent.player_name] had it, why still lose?"
    shiori "Because [persistent.player_name] didn't have this..."

    n "Shiori shows several talismans, hidden under a decorated box, wrapped around aceremonial dagger."
    hikaru "Wait, but why didn't they?"
    shiori "Remmeber when the elder looked surprised [persistent.player_name] managed to kill the Yamakui?"
    hikaru "...Oh."
    yamato "Shit."

    shiori "...."

    shiori "[persistent.player_name] was never supposed to win."

    hikaru "No way--!"

    yamato "Damn it all t' hell! I'm gonna get that damned old man--"

    hikaru "Yamato, stop. All we need to do now is to find the blade."
    hikaru "Since the Yamakui's here, their lair is unguarded. We'll look for the blade there."
    hikaru "Shiori...stay here. Keep Yamakui in the village."

    shiori "..."
    shiori "I'm scared now..."
    shiori "So the Yamakui is not as kind as I thought."
    shiori "Am I gonna be okay?"

    hikaru "The red moon's still in a few days, as long as you stay in public, you'd be fine."
    hikaru "All you need to do is use the villagers to distract them."

    shiori "...Okay."


    hikaru "Then it is settled. Yamato-kun and I go to the mountain. Shiori-chan holds the village."
    shiori "Don’t die on me before we get the chance, you two."
    yamato "Tch. Don’t screw this up, Shiori."
    hikaru "This is for [persistent.player_name]. For the friend we lost."

    scene black
    n "and on they went."
    n "The mountain air is suffocating, the mist here is blood red, a different color than at the village borders."


    yamato "Tch... what the hell’s that smell...?"
    hikaru "Smells like... rotting corpses."
    yamato "Or shit."

    n "They step into the cave and their breath stops immediately. The cave is made of meat. Heaps of it. Skin, fat, bone, shredded and piled like refuse."

    play sound "sfx/flesh_squelch.ogg"
    $ renpy.pause(1.0)

    n "The stench of sweet rot fills their lungs until both gag."

    yamato "Ghh--fuck--!"

    hikaru "Cover your nose--!"

    n "But it doesn’t help, as the air itself tastes spoiled."

    n "They walk deeper and deeperm into heaps of flesh shifting as if alive."

    yamato "The blade’s here. Has t’be. Somewhere in this godforsaken filth."
    hikaru "Can you still--?"
    yamato "Yeah, yeah, ya worry about yerself."

    n "They crouch, hands trembling as they dig through meat and viscera, shoving aside organs and whatever was left of Yamakui's meals."

    yamato "Urk, how come that thing lives in a place like this--"

    hikaru "Hold on--"
    hikaru "There--!"

    n "Something glints under piles and piles of flesh, but then blood sloughs down in wet waves, swallowing it."

    yamato "Goddammit--keep diggin’!"

    hikaru "...!"
    hikaru "That's--"
    hikaru "NO...!"

    yamato "...!?"

    hikaru "[persistent.player_name]..."

    n "Ah."
    n "They finally found me."

    hikaru "You said you'd come back. You promised me--"

    yamato "Th'.. Th' fucker really took away [persistent.player_name]'s skin by some batshit crazy magic..."

    hikaru "You didn’t deserve this...! You were... You were... the only one who trusted me..."
    hikaru "Even though the whole village condemned me, I could go on because of you..."

    hikaru "How do I live in this world without you...!?"

    yamato "..."

    yamato "Hikaru..."

    hikaru "...I'll kill it."

    hikaru "I'll kill it. I’ll kill that Oni in your name."
    hikaru "Swear on it or I'll die trying."

    yamato "...I'm sorry."

    n "..."

    n "Hikaru..."

    scene black

    with dissolve

    n "Live your life... and be happy..."
    n "Without me..."

    n2 "..."

    n "...Are you ready?"
    n "To finally die?"

    n2 "...HhAh."
    n2 "BrInG It On."

    scene black
    with dissolve

    n "When you step out of your house, just the night before the red moon..."

    n "You see them. Shiori. Yamato. Hikaru."

    shiori "You should recognize this, [persistent.player_name]."
    MC "..."

    yamato "This is the real [persistent.player_name]."
    yamato "Yer just wearin' their skin, ya damn Oni!"

    MC "hHa..."
    MC "HahHAHAhahahAHHahHAHaaaaaaa!"

    hikaru "What's so funny1?"

    MC "I wAS tRaPpED iN a LoOp."
    MC "KiLl. EaT. RetUrn. WaIt FOr tHE NeXt ReD MoON."
    MC "So BooOOOOooOoOrEd."
    MC "ThEN I mEt YoUR fRIenD."
    MC "MaKEs ThiNGs FuN."
    MC "BuT nOW..."
    MC "NoT FuN AnyMOrE... HuH?"
    MC "iT's OvEr."

    n "Shiori begins chanting as her body glows."

    shiori "山の鬼よ、立ち去れ、立ち去れ！"
    shiori "Yama no oni yo, tachisare, tachisare!"

    shiori "深淵に、闇に帰れ！"
    shiori "Shin'en ni, yami ni kaere!"

    MC "UrK--"

    hikaru "[persistent.player_name]... I'm sorry."

    n "Hikaru raises the talismans wrapped around a ceremonial dagger, a binding circle apeparing on the ground, under your feet."

    yamato "Get lost, Oni!"

    yamato "Haaaaaaaaaaaaaaaaa--!"

    n "Yamato drives the broken Oni Slayer blade straight through your chest. You don't even try to dodge."

    mc "HaHa... HAhA... hah..."
    mc "YoU GoT mE."
    mc "FiNaLlY."

    n2 "I cOuLd'vE mOvEd. cOuLd’vE tEaR yOu ApArT."
    n2 "bUt--"
    n2 "I dOn'T wAnNa."

    mc "I'M tIrEd."
    mc "sO... {w}tIrEd."

    n2 "It’S oVEr."
    n2 "nO mOrE rEd MoOnS."
    n2 "nO mOrE lOoPs."
    n2 "nO mOrE yOu."
    n2 "nO mOrE Me."

    mc "bUt--"
    mc "HeY."

    mc "It WaS fUn."
    mc "ThAnK yOu, [persistent.player_name]..."
    mc "FoR mAkInG mE WanT To DIe."

    shiori "山の鬼よ、立ち去れ、立ち去れ！"
    shiori "Yama no oni yo, tachisare, tachisare!"

    shiori "深淵に、闇に帰れ！"
    shiori "Shin'en ni, yami ni kaere!"

    n "The seal ignites. The circle glows more, and more, until everything turns to..."

    n "...white."

    n "And I..."
    n "...I feel warm again."
    n "For the first time in so long."

    n "Thank you. All of you."

    n "Let me finally..."

    n "...rest."

    with fade

    hikaru "Hi, [persistent.player_name]."

    hikaru "I hope you are well, whereever you are now."

    hikaru "I'd like to think you're in heaven now."

    hikaru "The mist isn’t coming back, and no more red moons."

    hikaru "No more Yamakui."

    hikaru "We let the villagers know about what the elders did."

    hikaru "The elders were banished for it."

    hikaru "My father... they finally cleared his name."

    hikaru "Too little, too late."

    hikaru "It won’t erase what they did to him."

    hikaru "...Or to you."

    pause 1.0

    hikaru "I'm leaving."

    pause 0.5

    yamato "...Figured."

    shiori "Where will you go?"

    hikaru "I don’t know. Somewhere past the fields. Somewhere far from this mountain."

    shiori "You won’t come back, will you?"

    hikaru "No."
    hikaru "This village... buried my father in silence, called me a traitor..."
    hikaru "And it buried [persistent.player_name], too."
    hikaru "It let a monster wear their face while everyone looked the other way."

    yamato "You don’t have to explain."

    hikaru "I’m not trying to justify it."
    hikaru "I just... I can’t breathe here anymore."

    shiori "Hikaru-san..."
    shiori "Will you be back?"

    hikaru "Don't think so, but I’ll write."

    shiori "You better. Or I’ll send a curse with your name on it~"

    yamato "Don’t write too much. I ain’t gonna read a damn novel."

    hikaru "Then I’ll write it just for me... or [persistent.player_name]."

    hikaru "How about you two?"

    yamato "Tche, someone needs to protect the damn village."
    shiori "And I'd have to be here so Yamato doesn't stab himself~"
    yamato "Oi."
    shiori "Oh, and..."

    shiori "Someone needs to tend to [persistent.player_name]'s grave too."
    shiori "The very first grave... with a name."

    hikaru "..."

    hikaru "Yeah."


    scene black with fade
    $ renpy.pause(2.5)

    centered "{size=+10}[我らは汝の名を忘れない]{/size}"
    centered "warera wa nanji no na o wasurenai"
    centered "We will remember your name."

    pause 2.5

    show text "[persistent.player_name]" with dissolve
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
