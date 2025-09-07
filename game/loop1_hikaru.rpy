label loop1_hikaru:

    ## HIKARU'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS

    ## STILL IN DAY 5, HAPPENS AT THE END OF DAY 5

    n "You find Hikaru, perched atop a tree. They jumps down as you come into view."

    hikaru "...[persistent.player_name]."

    MC "Hikaru, I--"

    hikaru "Yes?"

    MC "I asked Yamato and Shiori, and they said they don't know that there's something between us, so--"

    hikaru "That's because my father is branded traitor."

    hikaru "He tried to run away from the village, so he tried to find out a way out among the mist..."

    hikaru "But his body was never found."

    hikaru "So I suggested we start a relationship in secret."

    hikaru "Because I thought if they found out, they’d turn on you too."

    MC "...Ah."

    n "Everything makes sense now."

    hikaru "So when you forgot about me... I thought you were possessed."

    hikaru "When you came back from the mountains, you looked like you and sounded like you..."

    hikaru "But you didn’t remember anything. The lake, the scarf, the promise...{w} Us."

    hikaru "You smiled at me like I was just like the others."

    hikaru "And I--I thought maybe... maybe something came back in your place."

    hikaru "Maybe it wore your face, and that’s why it didn’t know me."

    MC "..."

    n "They look up at you."

    hikaru "But it’s still you, isn’t it?"

    hikaru "You’re not possessed, aren't you?"

    hikaru "Maybe you just hit your head... or... the fight was so traumatizing you wiped out some of your recent memories."

    hikaru "I don't know..."

    n "Their arms tremble. Their knees start to buckle, but they don’t sit. They stand there, shaking like a leaf that refuses to fall."

    hikaru "I was.. making dozens and dozens of talisman so you'd come back."

    hikaru "But you came back empty."

    n "Hikaru covers their face."

    hikaru "You’re here, the village's hero, breathing, laughing... And I-I should be happy."

    hikaru "But it feels worse than if you’d died."

    hikaru "Maybe it's punishment from the gods... {w}For what my father did..."

    MC "...I'm sorry."

    MC "I don’t know what happened to me, or what I lost."

    MC "But... {w}I want to fix it."

    MC "I want to remember you, Hikaru."

    MC "I want to start over... If you’ll let me."

    hikaru "..."

    n "Hikaru looks up again. Their hands lower from their face, fingers smeared with tears."

    hikaru "You really mean that?"

    MC "Of course, Hikaru."

    hikaru "Tell me something, [persistent.player_name]..."

    hikaru "Do you still love me?"

    n "Their voice cracks again."

    hikaru "How do you plan to remember everything we went though?"

    n "You don’t answer right away."

    MC "Well... If I loved you once, I can do it again."

    MC "And if you tell me again... I’ll listen!"

    MC "We’ll make new memories. A-And I’ll hold onto them this time! Promise!"

    n "Hikaru hesitates for a moment, staring at your face, then wipes their own, nodding."

    hikaru "All right, fine..."

    hikaru "but tell me this... What actually happened to you?"

    ## GASLIGHTING BEGIIIIINSSSSSS

    ## Your choices here will matter on whether hikaru believe you or not at the end

    $ hikaru_belief = 0

    menu:
        "I got bitten":
            $ hikaru_belief += 1
            MC "I got bitten by the Yamakui, passed out, then lose half of my memory."
            hikaru "Then why'd you pretend nothing happened?"
            MC "I just don't want to concern you guys!"
        "My head hit something":
            $ hikaru_belief -= 1
            MC "I hit my head on something on the way back to the mountain..."
            hikaru "But your head wasn't bleeding when you returned."
            MC "I don't know, maybe it's just bleeding internally?"
            hikaru "..."

    hikaru "Then what happened to the scarf?"

    MC "T-The scarf..."

    n "Yes, you remembered saying a scarf that's the exact same with Hikaru's somewhere, it might be at--"

    menu:
        "I left it":
            $ scarf_left = False
            $ hikaru_belief += 1
            MC "I left it at the mountains, the Yamakui ripped it off me."
            hikaru "I-I see..."
        "I forgot where it is":
            $ scarf_left = True
            MC "I can't find it anywhere, haha... Maybe it'll turn up somewhere?"
            hikaru "..."

    hikaru "[persistent.player_name]..."

    hikaru "Where is the talisman I gave you?"

    MC "Wha--?"

    hikaru "The one I said can ward off evil. Where is it?"

    MC "Um, well... It must've fell somewhere! Hahaha..."

    hikaru "..."

    menu:
        "Reach for their hand":
            n "You take Hikaru's hand, gently, trying to soothe them."
            MC "Hikaru."
            MC "Even though I don't remember everything, I remember this."
            n "What is this, exactly?"

        "Say you love them again":
            $ hikaru_belief += 1
            MC "I don't remember everything exactly, but I remember my feelings for you."
            MC "I remember... caring about you, always have, always will."
            MC "You’re the reason I stayed alive."
            hikaru "Really?"

    MC "You see... I was just... scared because I've lost my memories. I didn’t want to lose you too."

    MC "But I’m here now, and I want to get to know you again."

    hikaru "...That’s..."

    hikaru "I..."

    hikaru "..."

    hikaru "..."

    MC "...You believe me, right?"

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

    MC "If you still need time, that's okay."

    m "I'll be here... if you still love me. You can teach me again on how it was supposed to be."

    hikaru "*Sigh*"

    hikaru "...Okay."

    n "You don’t know if they believe you, but Hikaru never steps away."

    n "And that's good enough for you. {w}For now."

    scene black

    ## TWO DAYS BEFORE THE RED MOON

    centered "TWO DAYS BEFORE THE RED MOON."

    n "You start to seek Hikaru afterward, to show them that you stay true to your words."

    n "Hikaru told you to meet up in the forest later in the day."

    n "When you arrive, you see hundreds of paper effigies hung on the trees. They're perfectly aligned, all but one."

    n "The one with your name on it is crooked, its head is dangling where the feet should be."

    hikaru "...[persistent.player_name]. You're here."

    MC "What's up with my effigy? Looks like I am cursed or something."

    hikaru "Ah, yes. Shiori-chan did say she tried fixing it, but this just won't budge."

    hikaru "So... I was trying to fix it for her."

    hikaru "But it's so... stubborn."

    n "Hikaru tries to shift it, but fails again."

    hikaru "Do you think... It's a sign?"

    MC "What, like an omen?"

    hikaru "Maybe."

    ## so like there is a counter for Hikaru's disbelief and it just shows how different Hikaru reacts at the ending

    menu:
        "Mock Hikaru for being paranoid":
            MC "I think you're being too paranoid. I mean, Shiori could've just cut it unevenly or something."
            MC "It fell wrong, maybe, or the string slips. It happens."
            hikaru "It's not like Shiori-chan to make mistakes like this. She had always been good at crafting."
            hikaru "She even taught me how to make paper crafts...."

        "Act hurt":
            MC "You really think I'm cursed or something? After all I did for the village?"
            MC "Or... Do you think I'm lying?"
            $ hikaru_belief += 1
            n "You let your voice heave and falters for a bit while looking straight at Hikaru's eyes."
            hikaru "No, I--"


    n "The paper still hangs upside down. You want to reach up and fix it, but your hand won’t move."

    n "Because you know it's pointless."

    hikaru "Hey..."

    hikaru "You're still you... Right?"

    MC "Again with the doubts?"

    hikaru "...Sorry. Forget I asked."

    n "Hikaru stares for your face uncomfortably longer than it should, before looking away with a small nod."

    hikaru "So I guess... Shiori's the one making a mistake, then."

    n "They stare at the effigy once more before finally walking away."

    n "You reach to it and forcibly try to flip it again, but it turns even though there's no wind."

    n "So you rip it in half instead."

    MC "..."

    scene black with fade

    n "..."

    n "What you said about an omen suddenly comes true, moments later."

    n "You see the villages folk gather on the town square."

    play sound "sfx/flybuzz.ogg"

    n "They circle around a dog... or what remains of it."

    n "Its belly is torn wide, skin hangs in pieces, ribs pulled apart."

    n "The head is twisted at an unnatural angle, slack-jawed and one eye missing."

    n "Whatever attacked it was definitely has large claws."

    hikaru "...[persistent.player_name]."

    hikaru "Something ate it..."

    hikaru "I think it’s the Oni. I think Yamakui--"

    MC "Hikaru, I killed it."

    hikaru "What?"

    MC "The Yamakui."

    hikaru "...Oh. {w=0.5}Yes. Of course you did."

    hikaru "But what did this...?"

    hikaru "...T-That can't be a bear, right? We have no bears in this mountain, so it could only be--"

    "Man" "Hikaru, are you saying the Oni’s still walking around?"

    "Man" "Or are you saying [persistent.player_name] didn’t finish the job?"

    play sound "sfx/murmur.ogg"

    n "The accusation rings clear, none of them are talking about the corpse anymore."

    hikaru"..."

    "Old Man" "Why'd we trust Karasuma's child than the person who brought the Oni's armor back?"

    hikaru "I--"

    hikaru "Sorry... Maybe I’m just being paranoid. Maybe... Maybe... it wasn’t what I thought."

    n "They’re breathing faster, eyes frantic, visibly twitching now."

    hikaru "I just... made a mistake. I got confused."

    hikaru "Yeah, that's what this is..."

    hikaru "You killed Yamakui. I shouldn’t have said anything. I’m sorry."

    hikaru "I’ll stop talking. I-I-{nw}"

    n "Hikaru runs away, clutching their head. You watch as they go."

    n "Maybe you should run after them?"

    ## show Yamato at a distance

    Yamato "..."

    scene black
    with fissolve

    n "You can't find Hikaru anywhere, so you decide to go home instead."

    n "I think you should {nw}"

    play sound "sfx/knife_draw.ogg"

    MC "...Gh--!"

    n "Your back slams the wall, red trickles down your shoulder. A figure steps forward fast, blade already swinging again."

    n "You snarl and surge up immediately, bracing for impact and preparing your counterattack."

    yamato "Tch, knew it. Knew somethin’ was off the second I saw ya back!"

    MC "Yamato--"

    yamato "Nah. Nah. I ain’t listenin’ to that fake-ass voice comin’ outta your mouth."

    yamato "I saw ya, ya were standin’ there starin’ at the body all bloodied up. Same fuckin’ face, but not ya."

    n "Wait, I don't remember you--"

    menu:
        "Attack Yamato":
            n "You're going at his throat, and Yamato swings once more, aiming at your neck--"

        "Defend yourself":
            n "You step back and brace for Yamato's next attack--"
            $ hikaru_belief += 1


    n "You see steel sparks right in front of you as Yamato pulls back a step."

    hikaru "Stop it!"

    n "Hikaru stands between the two of you, sai raised."

    hikaru "Stand back, [persistent.player_name]-san!"

    yamato "Ya serious right now? Ya blockin’ for 'em?"

    yamato "I saw [persistent.player_name] near the damned mutt before everyone found it! Pretty sure [persistent.player_name] killed it, damnmit!"

    hikaru "Are you sure you're not just seeing things because you're jealous of [persistent.player_name]-san?"

    yamato "Ya think I’d come all the way here with my blades out if I wasn’t fuckin’ sure?"

    yamato "Just fuckin' look at 'em!"

    n "There is a faint trace of red in your sleeve, it looks older than the blood from your own wound."

    n "No one would see it if you fold your arms, but they are now stretched out in combat stance."

    hikaru "...That wound could be from your attack!"

    yamato "Or from before. Ya gonna bet on that?"

    n "Hikaru glances at you for a split second, hands trembling again, sai still pointed at Yamato."

    MC "Come on, you know me."

    MC "I didn’t do that. I wouldn't. Hikaru--"

    hikaru "..."

    hikaru "Yamato-kun. {w=0.3)Go. {w=0.3}Leave. If you attack again... I won’t stop the next time."

    yamato "..."

    yamato "Hah!"

    yamato "You've fooled the entire village and even Hikaru, but ya ain't foolin' me."

    yamato "I hope you’re ready for what’s comin’, eh Hikaru? 'Cause when it shows its real face, it ain’t gonna stop at mutts."

    yamato "Ya better hope I’m wrong."

    n "Yamato retreats and vanishes to the dark. Your knees weaken, but Hikaru’s hand catches your arm immediately."

    n "You're stil bleeding."

    hikaru "Don’t move. Please. Let me--just let me take care of it."

    n "Hikaru rips cloth fast. Their hands shake as they presses it to your shoulder "

    hikaru "It’s red. It’s... {w}it’s red."

    n "For a moment there, Hikaru is breathless and the cloth slips from their grip, then pulls tight again."

    MC "Of course it is, what do you mean?"

    hikaru "The Oni were always black-blooded. I’ve never seen one, but the folktale said that..."

    hikaru "They said the blood turned cold before it hit the ground. But... {w}Your blood looks normal."

    hikaru "I just have to tell Yamato, maybe he's not thinking straight, maybe he's--"

    MC "...Hikaru."

    hikaru "Hey, [persistent.player_name]..."

    hikaru "If you’re still mine, then the red moon will pass without a hitch..."

    hikaru "And if you’re something else... then..."

    n "Silence again."

    n "You take both of Hikaru's hands, pulling it away from their face and moves closer."

    MC "Hey, hey, I'm here. You don't have to worry anymore."

    MC "I'm still the same [persistent.player_name] you love."

    hikaru "..."

    n "They sink into you, body trembling, shoulders tight. You feel their panic still coursing through under their jittery arms."

    hikaru "...Don’t go again."

    MC "Never."

    n "The blood spreads into their sleeves now, but Hikaru just close their eyes."

    n "You hold them as they slowly stop shaking, and you u listen to the rhythm of their breath..."

    n "Inhale..."

    n "Exhale..."

    n "Inhale..."

    n "Exhale..."

    n "And the sound of their heartbeat ..."

    n "Thump, thump, thump, thump..."

    n "It's ringing in your ears now."

    n "You feel alive."

    ## ONE DAY BEFORE THE RED MOON

    centered "ONE DAY BEFORE THE RED MOON."

    n "Hikaru never left your side, you wake to them still clinging to your shoulder."

    MC "Mh..."

    hikaru "Oh no, your wounds are bleeding again."

    MC "I'm okay--"

    hikaru "Wait--hold on. Let me change the bandage."

    play sound "sfx/cloth_rip.ogg"

    n "Hikaru peels it back slowly, but your skin gets pulled in it. The wound bubbles and festers."

    n "Hikaru gemtly cleans the wounds with the salves and cloths found in your house and changes the bandage."

    n "Then they start humming instinctively, quietly, almost not audible."

    n "It’s a tune you don’t know how you know... but your mouth moves anyway."

    MC "...Hmm, hmmm, hmmm~"

    n "Odd, I remember that, too."

    n "You follow Hikaru's humming, half a breath behind. They raise their head at that."

    hikaru "...!"

    hikaru "[persistent.player_name]--that--"

    MC "Mmm?"

    hikaru "You remembered that? I thought--I thought maybe you wouldn’t."

    MC "Of course I remember."

    hikaru "We used to--"

    hikaru "Ah, well, my mom used to sing it when I couldn't sleep because of the oni, so..."

    hikaru "I taught you that, and you used to tease me that I should sing in public more often..."

    n "You tilt your head and let a small smile pull at the corners, enough to show endearment."

    MC "Well, at least I remember how it used to sound like."

    hikaru "Right... yeah. Of course. I just--I didn’t want to assume. I didn’t know how much you lost, or if maybe it all got... scrambled."

    hikaru "I was afraid it was just me holding onto it. But this... this feels better."

    hikaru "We’re getting somewhere, aren’t we?"

    MC "Yeah, I think we're getting close."

    MC "Actually... When the red moon is over, maybe we should come out on the open."

    hikaru "You mean... This? Us?"

    MC "We’ll tell everyone that we're together. I mean since there's no more Oni, they won't care right?"

    MC "Pretty sure Yamato and Shiori would understand."

    hikaru "No... don't!"

    hikaru "I know Yamato and Shiori would understand, but the others... They'll shame you!"

    MC "So what? Let ‘em talk. I don't care."

    n "You talk like it's so easy..."

    hikaru "You’re serious about this?"

    MC "Of course, never been more sure!"

    menu:
        "'Are you ashamed of me?'":
            $ hikaru_belief += 1
            jump shame

        "'Forget I ever said that.'":
            jump forgettt


label shame:

    MC "Or... are you the one ashamed on me?"

    hikaru "No, no, I would never--!"

    hikaru "I just don't want them to look at you differently..."

    hikaru "A-And they'll blame me for apparently seducing you."

    n "You muster a serene smile as your voice turns velvety smooth, enveloping Hikaru with safety."

    MC "I won't let them, after all I'm the one who saved them from Yamakui. They'll listen to me."

    MC "Unless you don't want me to?"

    hikaru"...."

    hikaru "I-I want that too. Of course I do."

    hikaru "I’ve wanted that for a long time. I just... {w}I thought we agreed it was safer this way."

    hikaru "I didn’t know you still--"

    MC "Still what?"

    hikaru "...Still wanted me like that."

    MC "Of course I do."

    n "You reach for their hand. Their fingers stay still, caught in yours."

    n "Slowly, their fingers finally curl around yours."

    hikaru "...Then after the Red Moon... {w=0.2}alright."

    n "Do you mean it, though?"

    n "Hikaru has wanted this so much and it pains them even to look at you like that in public."

    n "If you're lying, you'll break them."

    n "Because whatever bait you're casting... {w}it's embedded far too deep now."

    jump loop1_redmoon_eve

label forget:
    MC "You know what? Forget I ever said that. You clearly don't want anyone to know "

    hikaru "Please don't take it the wrong way, [persistent.player_name]... I just don't want to deal with the aftermath."

    MC "Yeah, let's just pretend that we're nothing to each other until who knows when."

    hikaru "[persistent.player_name].... I'm sorry..."

    hikaru "I still care about you a lot, even if I can only do this in secret "

    MC "Fine then, if that's what you want "

    jump loop1_redmoon_eve


label loop1_redmoon_eve:

    centered "DAY OF THE RED MOON."

    n "It's just hours before the red moon."

    n "The moon’s still half pale, but the sky has turned light crimson."

    hikaru "It's soon..."

    MC "Yeah."

    hikaru "Right, so..."

    hikaru "Salt lines are down. I double-checked the wards, and Shiori-chan lit the incenses an hour ago."

    hikaru "I reinforced the barriers, but I... {w}I don't think it'll work... If-if..."

    hikaru "...If the Yamakui really comes back--"

    yamato "Oi."

    hikaru "Yamato-kun--"

    yamato "If shit starts happenin’ tonight or I find another dead body..."

    yamato "That’s on YA."

    MC "What the hell is that supposed to mean?"

    yamato "Don’t play dumb."

    yamato "Yer the one who said you killed it. Ya told us the Yamakui was gone."

    yamato "So if it ain't...? Then you lied to all of us, to Hikaru."

    MC "Yamato--"

    yamato "Don’t."

    yamato "I ain’t scared of ya, or of whatever the hell is wearin’ ya."

    yamato "If anyone turns up gutted tomorrow, I’ll drag yer ass through the streets and gut whatever’s inside. Even if Hikaru cares about ya."

    hikaru "..."

    n "Yamato leaves immediately without waiting for a response and dissapears into the forest."

    hikaru "...What if he's right?"

    MC "Look at me."

    MC "I killed the Yamakui. Me. Whatever attacked that dog... It's gone now."

    MC "No one's getting killed lately right?"

    MC "I'm with you, if there's another oni out there, it’s not stronger than us."

    MC "I defeated the Yamakui, remember?"

    n "You press your hand against theirs, then grips it so tight your nails leave marks to steady them."

    hikaru "...Okay."

    n "You’ve calmed them, again. Like you always used to."

    n "And I don’t know what you're trying to protect anymore."

    n "The village?"

    n "Hikaru?"

    n "Or yourself?"

    ### RED MOON TIIIMEEE

    n "..."

    n "..."

    n "..."

    ### suuuuper uncomfrotable silence

    n "You're both staring at the red moon now, wind sofly blowing at your faces. It's oddly serene..."

    n "For the first time since you've seen them, Hikaru looks... in peace."

    hikaru "...It’s quiet."

    MC "Yeah."

    hikaru "If the Yamakui's here... {w}someone would've screamed, right?"

    MC "Definitely."

    hikaru "So... maybe you really DID kill it."

    MC "See? I told you."

    hikaru "Sorry that I didn't believe you."

    hikaru "You must think that's rich, coming from me..."

    hikaru "But... Can we try again?"

    n "You let Hikaru lean against your shoulder now, and close your eyes."

    m "There's the sound of their heatbeat again..."

    n "Thump."

    n "Thump."

    n "Thump."

    n "Thump."

    n "Dawn is almost here."

    n "Thump."

    n "Thump."

    n "Thump."

    n "Thump."

    if hikaru_belief <=3:
        jump hikaru_distrust
    else:
        jump hikaru_trust


label hikaru_trust:

    n "Hikaru's almost falling asleep, their neck is fully exposed to you now."

    n "Their pulse is visible under the red."

    n "You lean in, closer..."

    MC "...You can try again, with [persistent.player_name]."

    MC "In the afterlife, when I’m done with you."

    hikaru "...!"

    n "Wait, what are you doing? Why--"

    window hide
    $ renpy.pause(0.8)
    play sound "sfx/squelch1.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/squelch2.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/chew_wet.ogg"

    n "Hikaru--"

    hikaru "Aaaah--!"

    n "Hikaru makes a noise, louder, louder, they're practically screaming now."

    n "There's a sound of tearing flesh, a gurgle as an artery is nicked."

    n "No, please, stop!"

    n "What is wrong with you!?"

    n "You told them you loved them, didn't you!?"

    n "You promised to come out to everyone that you're together, right!?"

    n "But now... Why...!?"

    n "I can’t--"

    n "I don’t want to see it...!"

    n "Please--!"

    n "{size=+3}{color=#ff0000}Please make it stop.{/color}{/size}"

    ## veeeeeeeeeerrrryyyy long eating sound but like nothing on screen

    n "The red streaks and shadows are gone."

    n "And so is hikaru."

    n "Only the red scarf that they used to wear remains."

    n "I..."

    n "No, no..."

    n "My chest hurts... Is it yours...? Or mine...?"

    n "Why does it hurt?"

    n "Why does it feel like I’m the one who got left behind?"

    n "..."

    n "...Who am I?"

    n "..."

    n "Who are you, really?"

    MC "..."

    MC "I DO remember where I saw the other red scarf, even if you don't."

    MC "We left it right next to that body you tore up."

    n "...!?"

    scene black

    centered "HIKARU IS DEVOURED."

    $ persistent.hikaru_dies = True

    $ persistent.loop1 = True

    $ persistent.trueending.unlocked = False


    return

label hikaru_distrust:

    hikaru "...Wait."

    n "Their head lifts slowly."

    hikaru "...You don’t..."

    hikaru "Where is your heartbeat?"

    n "Huh?"

    n "They jolt upright."

    hikaru "Where is it!?"

    MC "Hikaru--"

    hikaru "No! Stay back--!"

    play sound "sfx/step_back.ogg"

    n "They stumble backward, nearly tripping over the roots."

    hikaru "I trusted you. I let myself believe--"

    MC "*sigh* I was so close."

    hikaru "You’re not [persistent.player_name]. You’re not--"

    n "Wait a minute."

    play sound "sfx/dagger_draw.ogg"

    n "Hikaru draws their sai and points it at you. At [persistent.player_name]. At..."

    n "...wait."

    hikaru "The red moon... I'm..."

    hikaru "...I'm next."

    MC "..."

    hikaru "What did you do to [persistent.player_name]!?!?"
    play sound "sfx/spell.ogg"

    n "A sigil flares against your side, meant to burn and cleanse evil spirits. But you are more than that."

    n "In fact, defeating Hikaru is far too easy for you."

    play sound "sfx/clash.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/squelch1.ogg"
    $ renpy.pause(0.3)

    n "You overpower Hikaru easily as they fall to their knees."

    hikaru "...ngh--"

    n "There is a dark gash on their shoulder... resembling the one on the dead dog ..."

    n "You did it? But how come I don't--"

    MC "You done?"

    hikaru "N-no--!"

    MC "Well, at least I can reunite the both of you now."

    window hide
    $ renpy.pause(0.8)
    play sound "sfx/squelch2.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/chew_wet.ogg"
    $ renpy.pause(0.3)
    window show

    n "It’s wet again. Louder this time. Closer."

    hikaru "S-stay--...!{w} a-away...!"

    n "They’re crying now.... You..."

    n "No.... Hi-Hikaru...."

    play sound "sfx/chew_deep.ogg"

    n "There is a faint sound of bone crunching and ribs snapping and I..."

    n "I can't hear Hikaru's voice anymore..."

    n "Why did you let me see it?"

    n "Why did you make me watch--"

    n "...Why do I still remember them?"

    n "Why does it still hurt?"

    n "...Why do I care?"

    n "Why--"

    n "..."

    n "Who are you?"

    n "Who are you really?"

    $ persistent.hikaru_dies = True

    $ persistent.loop1 = True

    $ persistent.trueending.unlocked = False

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
