label prologue2:

    scene black with fade

    mc "Haa... {w=0.4}Haa..."

    play sound "sfx/huff.ogg" loop
    show screen huffing_effect

    n "It’s dark."

    n "We're here again...?"

    mc "Gh... khhh..."

    n "Are you choking?"

    n "You shouldn’t be. You’re alive. You won, remember?"
    
    n "Wait a second, you've been through this before... This feels familiar..."

    play sound "sfx/squelch1.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/squelch2.ogg"
    $ renpy.pause(0.3)

    n "Again."

    n "You stab again. Again. Again. Wait. Stop."
    
    n "Haven't you stabbed this thing to oblivion before?"

    play sound "sfx/squelch3.ogg"
    $ renpy.pause(0.2)

    n2 "Again."

    n "…"

    n "Wh—"

    n "Who was that? Was that you?"

    n "You grip the hilt harder, your sword is sticky now, covered with blood."

    n "You’ll need to clean it. Later. Burn it maybe."

    n "What... did you kill?"

    window hide
    $ renpy.pause(1.0)
    window show

    n2 "...You."

    play sound "sfx/heartbeat_deep.ogg"
    $ renpy.pause(0.4)

    n "...What?"

    n "Isn't this supposed to be Yamakui? But wait..."

    n "It had hands, not claws. Doesn't it supposed to have claws? A-and this is Yamakui's lair. And you're alive."
    
    n "This makes no sense."

    n "No, no, that can't be right. The sound that it made when you cut through it was NOT human at all."

    play sound "sfx/whimper.ogg"

    n "You heard it screamed, right? Or did it cry out?"

    n "Did it say your name with it's dying breath?"

    n "You lift the blade again, about to stab the creature {w}again."

    play sound "sfx/squelch1.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/squelch2.ogg"
    $ renpy.pause(0.3)

    n "Stop."

    mc "...."

    play sound "sfx/squelch1.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/squelch2.ogg"
    $ renpy.pause(0.3)
    play sound "sfx/drip2.ogg"
    $ renpy.pause(0.4)

    n "Please. Stop."

    n "You saved the village.  This was... {w}noble."

    n "Stabbing a thing that is no longer alive, again, again, again, again, and again is not noble. That's not what heroes do."
    
    n "You're sure it's dead now. You can go, return to the village, and..."
    
    n2 "Snap, chew, swallow, devour."
    
    n "That voice again... Is that you, [player_name]?"
    
    n "......"
    
    n "...."
    
    n "..."
    
    n "You must be hallucinating things."

    scene black with fade

    # ambient sound — wind, insects, unease
    play sound "sfx/crickets_night.ogg" loop

    n "It’s time to return to the village."

    play sound "sfx/armor_drag1.ogg"
    $ renpy.pause(0.8)

    n "You start down the mountain, but these legs don't feel like yours."

    n "The sound of armor clinking follows behind you. It grinds the stone path as you drag it along with one hand."

    play sound "sfx/armor_clink1.ogg"
    $ renpy.pause(0.5)

    n "The elders said the Yamakui wore stone armor. That its body was too large for skin alone."

    n "This... this is your proof. You dragged it with you, so they'd believe you."

    n "Because there was nothing else left. {w}Because you--"

    n2 "--tore it."

    n "..."

    play sound "sfx/armor_drag2.ogg"
    $ renpy.pause(1.2)

    n "They won’t doubt you. Not when they see this."

    n "You did it. You killed it. You’re {i}sure{/i}."

    n "You’re sure."

    mc "Hhh..."

    play sound "sfx/breath_exhale.ogg"

    n "It’s cold and quiet and eerie and absolutely what you have imagined."

    n "You just fought the thing they feared for generations. Where’s the fanfare?"

    n "Shouldn’t the forest open up for you? Shouldn’t the world feel..."

    n "...safe?"

    n "You imagine the clouds parting, or gold light spilling down, or flowers blooming or... something."

    play sound "sfx/laugh_glitch1.ogg"
    $ renpy.pause(0.2)

    n2 "Pfft... hkkk—HRAHAHAH."

    n "--!"

    n2 "Gold light. Pretty lie. Ha."

    n "What--"

    n2 "Keep telling that lie to yourself, won't you?"
    
    n "..."

    play sound "sfx/steps_dirt.ogg"
    $ renpy.pause(0.4)

    n "You keep walking, tracing the familiar pathway to the village that the Yamakui used to trail when they go..."
    
    n "...to the village..."
    
    n "...before... the red moon..."
    
    n "..."
    
    n2 "Done talking?"
    
    n "No. That's not true "

    n "You killed the Oni. That's what is supposed to happen. So now you're going home."

    n "You’ll be a hero."

    n "A hero."

    n "..."
label tehvillageee:

    n "Finally."

    n "Once you step on the village borders, everything changes."

    n "The sky looks like it splits into two once the treeline dissapears... The heavenly shine that you've imagined."

    
    mc "Hey, guys. I'm back."

    n "Someone sees you, drops their bucket  Everyone stops what they are doing to look at you."
    
    n2 "So many necks to snap."
    
    man "No way..."
    
    woman "[player_name] is back?"
    
    man "That's impossible... Alive?"

    n "You walk toward a familliar-looking elder and hands the armor out. He steps forward and examines the armor, brows furrowing."
    
    mc "So?"

    elder "Yes... {w}I believe this is truly the Yamakui's armor."
    
    pause 0.5

    elder "The Oni is... dead?"

    n "Insteade of cheering, people just stare..."

    n "Hands reach for you, but they seem to be unsteady. Everyone looks...conflicted and unsure."

    n "That's odd, shouldn't they be celebrating? Shouldn't they be joyous?"
    
    n "Shouldn't they call your. name?"
    
    n "Wait, what is your name again?"
    
    n2 "Y A M A K U I" ## use horror text

    n "NO."

    n2 "{fast}Yamakui. Yamakui. Yamakui.{/fast}"

    n "No, that’s—{w}That’s NOT—!"

    play sound "sfx/heartbeat.ogg"
    $ renpy.pause(1.0)

    man "Did you really kill the yamakui, [player_name]?"

    mc "Yeah! I took down that Oni in one blow! Well... maybe two! Or ten! Who’s counting?!"

    elder "[player_name], you have done us a great service."

    n2 "Hungry hungry hungry."

    n "Shut up."

    n "Shut up shut up shut up shut up—"

    woman "Great job, [player_name]-san..."

    kid "[player_name]-sama, are we really safe now?"

    n "{cps=7}No one looks at the armor.{/cps}"

    n "They looked worried still, because someone was recently devoured. Someone by the name kf--"
    
    n "--huh?"
    
    n "Why can't I remember their name? That's odd, let me think again. Were they your friend?"

    n2 "Don't think too much."
    
label speechhh2shiori:

    show bg shrine_day with fade
    show villagers_happy at center
    play music "bgm/festival_soft.ogg" fadein 1.5

    n "Later, they drag you toward the shrine steps."

    n "The Elder holds your arm, but you can’t tell whose hand is trembling. Yours, maybe."

    elder "Come. Let them see it clearly."

    show mc proud at midleft with dissolve

    n "You raise the armor."

    n "Sunlight catches the edges. Something {i}wet{/i} glistens. Red trails slide off the plating."


    elder "Look well, all of you."

    elder "For years, we have lived in shadow."

    elder "We boarded our windows, whispered our prayers, and buried bodies without names."

    elder "The Yamakui haunted us longer than memory itself."

    elder "And yet..."

    elder "[player_name] climbed that mountain and came back. Where no one else could."

    n "The crowd claps, but they don't seem to be excited. Odd."

    elder "Never again will we light our fires with fear."

    elder "Never again will we sleep listening for footsteps."

    elder "Never again will our loved ones vanish under the Red Moon."

    elder "And never again will we... forget."

    girl "Speech, [player_name]!"

    n "A voice rises from the crowd. Shiori’s, maybe."

    show mc happy at midleft

    mc "Thank you, everyone. I didn’t do it alone."

    mc "I had your hopes, your prayers, {w}your bento."

    mc "Aaaand that weird old charm from our beloved shrine maiden..."

    mc "Still stuck in my pocket, by the way, thanks Shiori!"

    n2 "It stings."

    n "Don’t."

    n2 "Lets rip apart the shrine maiden next."

    n "Stop. Please."

    mc "...I..."

    mc "...I climbed that mountain."

    mc "...Faced it head-on...."

    mc "...And I, I won."

    mc "So let’s celebrate! No more fear!"

    m "They seem to believe you now."
    
    n "{cps=7}They believe you.{/cps}"

    n "The armor is still in your hand, the only proof that you killed Yamakui."

    n "As you step down from the shrine, the crowd parts."
    
    n2 "Hungry, hungry, hungry."

    n "You can still hear the scared whispers of the villagers ringing in your ears."

    "Man" "The next Red Moon’s coming soon, isn’t it?"

    "Woman" "Think we’ll be safe this time?"

    "Man" "I don't know, but..."

    "Man" "...there’s nothing left to hide from. Right?"

    n "...Right?"
    
    n2 "AhaHAHAhahaHa."

    n "You hear your name again."

    n "The armor still hangs limply from your hand."

    n "It feels...{w} heavier now."
    
    n "And that red ooze is still dripping."
    
label speechhh2noshiori:

    show bg shrine_day with fade
    show villagers_happy at center
    play music "bgm/festival_soft.ogg" fadein 1.5

    n "Later, they drag you toward the shrine steps."

    n "The Elder holds your arm, but you can’t tell whose hand is trembling. Yours, maybe."

    elder "Come. Let them see it clearly."

    show mc proud at midleft with dissolve

    n "You raise the armor."

    n "Sunlight catches the edges. Something {i}wet{/i} glistens. Red trails slide off the plating."

    elder "Look well, all of you."

    elder "For years, we have lived in shadow."

    elder "We boarded our windows, whispered our prayers, and buried bodies without names."

    elder "The Yamakui haunted us longer than memory itself."

    elder "And yet..."

    elder "[player_name] climbed that mountain and came back. Where no one else could."

    n "The crowd claps, but they don't seem to be excited. Odd."

    elder "Never again will we light our fires with fear."

    elder "Never again will we sleep listening for footsteps."

    elder "Never again will our loved ones vanish under the Red Moon."

    elder "And never again will we... forget."

    pause 0.5
    
    n "....."
    
    n "......"
    
    n "Silence."
    
    mc "....?"

    n "Wait, shouldn't someone say something by now?"

    n "Someone always says something here. A girl’s voice, I think her name was--"
    
    n "No, I can't remember her..."

    n "She should be laughing with her sweet voice by now, but you don't hear it."
    
    n "Someone should ask you to say a speech now, right?"
    
    n2 "That one's too stringy."

    n "..."

    n2 "Sounded shrill when devoured."

    n "I... don’t remember that."

    n2 "I do."

    n "...."
    
    n "Since no one asked you for a speech, it ends right there "

    with fade

    n "As you step down from the shrine, the crowd parts."
    
    n2 "Hungry, hungry, hungry."

    n "You can still hear the scared whispers of the villagers ringing in your ears."

    "Man" "The next Red Moon’s coming soon, isn’t it?"

    "Woman" "Think we’ll be safe this time?"

    "Man" "I don't know, but..."

    "Man" "...there’s nothing left to hide from. Right?"

    n "...Right?"
    
    n2 "AHahaHAHA."

    n "You hear your name again."

    n "The armor still hangs limply from your hand."

    n "It feels...{w} heavier now."
    
    n "And that red ooze is still dripping."
    
    
label LI_intro_noshiori:

    n "But of course, you don't get far."

    n "Because Yamato and Hikaru find you, they are your childhood friends--"
    
    n "Wait a second."

    n "Wasn’t there someone else?"

    n "You remember the rice paddies, the muddy sandals, the laughters and the paper effigies--"

    n "Someone used to hang those paper effigies."

    n "There were four of you. Weren’t there four?"

    play sound "sfx/grassstep.ogg"

    yamato "Tch. Look who finally shows up."

    hikaru "Welcome home, [player_name]-san."

    mc "Oi. That how you greet a hero?"

    yamato "Hero my ass. Ya ran off alone, idiot."

    mc "C’mon, tradition’s tradition. Oni slayer always goes solo."

    yamato "Fuckin' tradition..."

    n "Wait... There should be another voice now, someone who usually tease Yamato..."
    
    n "No, wait... Not Hikaru... Hikaru's a quiet person."

    n "..."

    hikaru "...Don’t you forget something, [player_name]?"

    mc "Huh? What, like a souvenir? I brought the armor, didn’t I?"

    hikaru "...I see."

    n "Hikaru’s voice lowers. Their eyes drift slowly to the armor."

    hikaru "...It's rather small for something like the Yamakui, isn’t it?"

    mc "...What?"

    yamato "Oi. What’s that supposed t' mean?"

    hikaru "...Forget it."

    n "The silence stretches again."
    
    n "Someone should occupy this space right now."
    
    n "Someone should've said something to fill the quit."

    n "But no one else is there but the three of you."

    n2 "...She is D E A D."

    n "Hikaru shrugs, turns and walks away."

    mc "...Hikaru?"

    yamato "Tch, whatever."

    n "Yamato follows. The empty space between you seems larger now."

    n "You look down at the armor, it feels heavier. Your fingers ache from holding it."

    n "You thought you cleaned it better."

    n2 "But we both know this is not mine."
    
    
label LI_intro_nohikaru:

    n "But of course, you don’t get far."

    n "Because Shiori and Yamato find you."

    n "Your childhood friends. {w}Two of them?"

    n "...Weren’t there more? You cared for them more than the others... didn't youMx

    n "Yes, you remember the rice paddies, muddy ankles, chasing cats and sparring...."

     n "Didn't one of you never talk much?"

    n "Who was it?"

    n2 "The mushy one."

    n "..."

    shiori "Ehehe~ [player_name]-samaaa~!"

    shiori "You came back~! I was so sure you'd get squished into pancake mochi~!"

    mc "Oi, rude. I’m not that easy to mash."

    yamato "Hnh. Coulda fooled me, dumbass. Leavin’ us without a word, ya promised ya'd being me along!"

    mc "C’mon, you know how it is. Oni slayer tradition."

    yamato "Tradition’s for corpses."

    shiori "Mou~ Yamato-kun's just mad he didn’t get to do anything cool~"

    yamato "Tch. I stayed behind t’guard the goddamn village."

    shiori "Did you now? Aren't you just sulky [player_name] didn't bring you along?"

    n "There should be someone cutting the conversation right now, someone who observe, someone who is--"

    n2 "--Tender "

    n "...What?"
    
    n2 "Soft around the ribs."

    n "..."

    shiori "Ne ne~ [player_name]-sama! You have to tell us what Yamakui looked like! Did it have fangs? Big claws? Did it talk?"

    mc "Uh... Big. Yeah. Bloody. And...."

    shiori "Beautiful?"
    
    n2 "Hah."

    mc "...What?"

    yamato "Oi, cut it out."

    shiori "What~? I’m just sayin’! Maybe Yamakui-sama's got a pretty face!"

    yamato "Damn Oni's got teeth, that's what."

    n "They laugh again, almost in harmony. But something is missing. Someone is missing."

    n "The hill you grew up on had four shadows. You’re sure of it."

    n "Right?"

    mc "Yeah, whatever they looked like now, it doesn't matter now."

    yamato "Tch. Ain’t like I’m complainin’. Ya came back in one piece."

    shiori "Especially not clean like that~ Not even a scratch!"

    yamato "Almost like you ain’t fought anything at all, eh?"
    
    mc "Ehh, just got Lucky's all!"
    
    yamato "What, oni bonked their head on a stone and dropped dead?"
    
    mc "Something like that, yeah...!"

    n "Yamato and Shiori says nothing else, but their smile fades as yours does."

    n "You look down at the armor."

    n "You thought you cleaned it better."

    n "The red stain slowly turns to black."
    
    n "You hope no one notices."
    
label LI_intro_noyamato:

    n "But of course, you don’t get far."

    n "Because Shiori and Hikaru, your childhood friends find you."

    n "You grew up together, train together, sit under the same tree together, and chase each other on the paddy fields."

    n "There were always four sets of muddy shoes by the door."

    n "Wait, four?"

    n "...Wasn’t there one more?"

    n2 "The loud one."

    n "..."
    
    n2 "All muscle, gamey."

    shiori "Ehehe~ [player_name]-samaaa~!"

    shiori "You came back~! You didn’t explode or get squashed or turned into jelly!"

    mc "Oi, rude. I’m tougher than I look."

    hikaru "Welcome home, [player_name]-san."

    n "There should be someone grumbling now, that you left them to fight the Yamakui all by yourself..."

    n2 "Stopped moving halfway down the throat."

    n "..."

    shiori "Ne ne~ Did Yamakui look like the legends? Big and scary? Lots of fangs? Or was it kinda cute~?"

    mc "I think it looked like it needed stabbing."

    shiori "Muuuu, why are you so stingy, [player_name]???"

    hikaru "..."

    n "Silence falls when Shiori stops talking."
    
    n "Someone should have said something by now..."

    n2 "Better this way..."
    
    n2 "All talk and no meat to back it up."

    shiori "You must be starving, [player_name]-sama. Shiori's gonna make alllll~ the food you want!"

    mc "How 'bout venison?"
    
    shiori "Eh...? I don't think I have... that...."

    hikaru "..."

    mc "What is it?"

    hikaru "...Do you feel like something’s missing?"

    mc "Huh?"

    hikaru "I don’t know. I keep thinking there should be..."

    hikaru "...four of us "
    
    mc "..."

    n "You-I... don’t know what to say."

    hikaru "...Forget it."

    shiori "Ah, mou... Let's go eat before Hikaru's making odd theories again!"
    
    mc "Yeah, agreed."

    n "The fourth voice still doesn’t come."

    n "The armor clinks in your hand as you carry around with you, footsteps behind Shiori and Hikaru."

    n "..."

    n "You wonder what venison tastes like, again."
    
label beforesecondloop:

    n "Time passes slowly, it happens when people wait."
    
    n2 "Hungry, hungry, hungry."

    n "You wake. You laugh. You sleep. You talk. {w=0.3}Repeat."

    n "You do all the things that safe people do."

    n "{cps=7}So you must be safe.{/cps}"

    n "The village tries to be more bright and cheery, but there's always this heavy feeling in the air."

    n "They greet you kindly, politely. A bit... rehearsed."
    
    n "And slightly afraid."

    n "No one speaks about the mountain anymore."

    n "Instead, they light incense more often, cose their doors faster..."
    
    n "...and never once stare at you in the eye "

    n "You never ask why."
    
    n2 "No need."

    n "..."

    n "Meanwhile, the moon is starting to shift again."

    n "They say it only turns red a few times a year."

    n "{i}That’s when the Yamakui comes down.{/i}"

    n "All the villagers can do now is waiting, wondering... If you've truly killed the Yamakui."
    
    n2 "You know the answer."

    n "{cps=7}T-The Yamakui is dead.{/cps}"

    n "There was a scream, a pool of blood, and... and... the weight of flesh, giving under your hand."

    n "You... You remember stabbing...."
    
    n "Me-You-We-It...?"

    n "Again. Again. Again."

    n2 "Again."

    n "You made sure a thousand times..."

    n "So the Red Moon shouldn’t mean anything this time."

    n "It should rise, and pass, and no one should vanish or be forgotten--"

    n "No one should{nw}"

    n2 "{fast}No one should remember.{/fast}"

    scene black

    centered "{color=#9a0000}5 DAYS UNTIL THE NEXT RED MOON{/color}"

    with fade

    pause 0.5