############# LOOP 2 WHERE ONE DIED ###########################
label loop2_shiori_mandatory1:

    n "Shiori is already waiting for you as you walk towards her, as if she'd already knew you're coming."

    shiori "[persistent.player_name]-sama~!"

    n "She’s smiling again."

    shiori "Did you sleep well~?"

    MC "Yeah, definitely!"

    shiori "That’s good~ That’s very good."

    shiori "I thought you'd dream of killing the Yamakui."

    n2 "Hoo?"

    MC "Why would I dream of that?"

    shiori "Oh, woow~ You just defeated the big scary oni and you're unfazed?"

    MC "Guess I'm awesome like that!"

    shiori "Ne, [persistent.player_name]-sama?"

    shiori "Will you tell me how you killed the Yamakui?"

    n  "Why would she ask that?"

    MC "Why."

    shiori "I just... I want to understand. I want to know how you get to kill the fearsome oni~"

    shiori "Where did you strike first? Did it bleed a lot? Did it scream?"

    n "That voice is far too soft for someone asking something that gruesome."

    shiori "Did you see its eyes when it died?"


    menu:
        "I stabbed it in the chest":
            MC "I snapped it's spine in half."
        "I decapitated it.":
            MC "I snapped it's spine in half."

    n2 "Gouge it, rip it, tear it apart."

    n "Wait, what? That's not even what you thought of--"


    n2 "I say what I want."

    shiori "Ara~ That sounds...{w} painful."

    shiori "But are you sure it's really dead?"

   MC "Definitely."

    menu:
            "‘I burned it.’":
                MC "I tore the arms off."
            "‘I watched it bleed out.’":
                MC "I tore the arms off."



    MC "Bent the legs backwards so it'll be on the wrong angle."

    MC "It looked like a beautiful flower~"

    n "What the hell are you saying."

    n2 "Heh. Heh. HeHeHAHAHAHa."

    shiori "...."

    shiori "And did it... say anything before it died?"

    menu:
        "It cursed me before dying.":
            MC "It didn’t say anything, Shiori. Just gurgling noises. Probably because I stabbed it in this neck to kill it."
        "It cried like a child.":
            MC "It didn’t say anything, Shiori. Just gurgling noises. Probably because I stabbed it in this neck to kill it."


    shiori "...I thought so."

    n "She looks relieved now, pleased even."

    shiori "[persistent.player_name]-sama, you forgot your own story~"

    MC "Eh?"

    shiori "You said you snapped its spine. Now it’s a stab in the neck?"

    shiori "Ehehe~ You really should keep your lies straight."

    n2  "Slipped up, ahHahHaha."

    n "What--"

    n2 "This mouth. {w}So much fun."

    shiori "You didn’t kill the Yamakui, didn't you~"

    shiori "It’s still alive, isn’t it?"

    n "Oh no--"

    shiori "But that's okay, Shiori will keep your secrets. I won't tell anyone, promise."

    shiori "Because if you’re lying... it means my precious Yamakui is still breathing somewhere~"

    shiori "And if it’s still alive... maybe it’s listening right now?"

    n "Don’t say anything. Don’t respond. Please--"

    MC "..."

    shiori "Ne, [persistent.player_name]-sama..."

    shiori "If you see the Yamakui again..."

    shiori "...will you tell it something for me?"

    MC "What is it?"

    shiori "Tell it... it was never a monster to me."

    n "She leans closer that you feel her breath on your face."

    shiori "Tell it that if it feels hungry, [persistent.player_name]-sama..."

    shiori "...come find me first."

    n "She turns around and leaves, mumbling a song you haven't heard before."

    n "Shiori...?"

    n "Have she always been like this?"

    n "Or am I the one losing grip on reality?"

    $ loop2_shiori_mandatory1 = True

    return

label loop2_shiori_mandatory2:

## during this scene Shiori 's sprite leans closer very slowly almost unnoticeable and her eyes follow your mouse tracking

    n "You see her again, waiting on the same spot, wearing the same smile."

    n "She's being normal... {w}Yesterday doesn't mean anything. {w}She was just being curious, is all...."

    shiori "[persistent.player_name]-sama~ Did you sleep well again?"

    MC "...Yeah."

    shiori "I am so happy you get enough sleep!"

    n "She’s inching closer again."

    shiori "Ne... Can I ask more today?"

    MC "...What now?"

    shiori "About the mountain. I mean, no one went there and returned alive like you did."

    shiori "What did its lair look like?"

    shiori "I always imagined something awful. Or beautiful. Maybe a bit of both~"

    MC "It’s just a cave filled with rotten meat and bones."

    shiori "Oh~? That sounds horrifying. Must be lonely."

    n2 "Meat's always in storage."

    n "Shut up."

    shiori "Was it surrounded by mist?"

    shiori "Everyone says that leaving the village is impossible because there's mist that swallow people."

    shiori "I wonder if the mist is Yamakui itself~"

    MC "No, but it hides the cliffside... And there are bodies inside it, probably those who fell."

    MC "They aren't intact, some are half-eaten."

    shiori "Ara~"

    n2 "We don't waste."

    n "Stop."

    shiori "But it doesn’t eat too often, right?"

    shiori "Otherwise it will... run out of food."

    MC "Exactly."

    MC "The Yamakui is a patient hunter."

    n2 "Patient enough to talk like this with prey."

    shiori "Then, does that mean Red Moon is a feast?"

    MC "..."

    shiori "Like... when it actually eats normally and not just snacking?"

    MC "Yesl That is when it feeds off something fresh and not rotten."

    MC "Food that has its own soul and memories."

    MC "Basically, yes, a feast."

    n "What are you saying? How do you know this--"

    MC "I--I mean, that’s what I heard."

    MC "That’s what it did. {w}Not me. {w}I mean--"

    n "Why is your mouth running off by itself? Get a grip already!"

    shiori "Ehehe~"

    shiori "You talk as if you’ve known it for years."

    MC "I was there, remember? I KILLED it."

    MC "That's why I know."

    shiori "Mm... but you talk like it’s still alive."

    MC "..."

    shiori "So, the Yamakui is hungry, right?"

    shiori "But maybe... it was lonely too?"

    n "Don’t answer that."

    MC "...I don’t think it works like that for Onis. Do they even have feelings?"

    n2 "Hungry, hungry, hungry."

    shiori "Are you sure?"

    MC "Yeah."

    shiori "Well~"

    shiori "Thanks for the story again today, [persistent.player_name]-sama."

    n "She bows then literally skips away cheerfully."

    n "Your throat feels dry. You are parched."

    n "You haven't eaten or drunk anything since--"

    n2 "Say one more word."

    n2 "And I’ll use the tongue for something else."

    n "..."

    $ loop2_shiori_mandatory2 = True
    return

label loop2_shiori_mandatory3:

    n "Shiori’s here again, kneeling. You don't know for how long."

    n "There's a new offering box in front of the unnamed graves."

    shiori "...Kami-sama..."

    shiori "...Protect [persistent.player_name]-sama, okay? And um... everyone else. Please."

    shiori "And--and someone else. I think."

    shiori "There was a friend of mine who died..."

    shiori "But I can't remember who..."

    n "She rubs her eyes but the tears keeps flowing down."

    shiori "There were four of us, I swear!"

    if persistent.hikaru_dead:
        shiori "Me, [persistent.player_name]-sama, and Yamato-kun, and--and..."
        shiori "Who else?"
        shiori "It’s right there. Like, on the tip of my tongue, you know?"
        shiori "They... they used to walk with us. I think."
        shiori "They always glared when I teased Yamato too hard. Or maybe they just never smiled much?"
    if persistent.yamato_dead:
        shiori "Me, [persistent.player_name]-sama, and Hikaru-san and--and..."
        shiori "Who else?"
        shiori "It’s right there. Like, on the tip of my tongue, you know?"
        shiori "They... they used to teach us how to use a sword. I think."
        shiori "They're louder than me, and I think of them like an older sibling..."
    shiori "They sat under the sakura tree with us! Right?"

    n "Your chest aches."

    n2 "..."

    play sound "sfx/sniffle.ogg"

    shiori "I keep seeing a shadow next to me when I walk, and then I turn and there’s no one."

    shiori "...I miss someone I don’t even know."

    shiori "Isn’t that the dumbest thing ever?"

    ## ghost flicker

    #if persistent.hikaru_dead:
        #show hikaru sad at farleft with dissolve
    #if persistent.yamato_dead:
        #show yamato sad at farleft with dissolve

    n "Wait, was that--"

    pause 0.5

    n "Ah, it's gone."

    shiori "...I just..."

    shiori "If you’re out there, and I forgot you..."

    shiori "I’m really sorry."

    shiori "You were probably annoying sometimes, and I probably yelled at you a lot, but..."

    shiori "I think I loved you too."

    shiori "So... wherever you are, I hope you’re in peace now."

    n "If she remembered who they were--"

    n2 "She’d never look at us again."

    n2 "Or maybe she would, and still smile about it."

    $ loop2_shiori_mandatory3 = True
    return

label loop2_shiori_mandatory4:

    shiori "Good night, [persistent.player_name]-sama~!"

    shiori "Can't sleep?"

    m=n2 "I don't sleep."

    MC "Yeah. The red moon is coming, so I--"

    shiori "Nee, nee, would you want to talk with me? Maybe you'd get sleepy."

    shiori "Umm... I was wondering..."

    shiori "I have more questions. Don't laugh, okay?"

    MC "Yeah?"

    shiori "When the Yamakui wasn’t eating... {w}what did it do?"

    shiori "Did it nap in a corner or crawl somewhere quiet?"

    shiori "Do you think it ever looked up at the sky and watch the stars?"

    shiori "Did it ever just... wonder what it's like outside the mountain?"

    n "The yamakui is not a dog."

    MC "What the hell, Shiori?"

    shiori "I-I mean! It's been alone all these time, right?"

    shiori "That must’ve been scary."

    shiori "But also kind of... I dunno. {w}Sad?"

    MC "Sad?"

    shiori "Yeah... Even if it’s a scary Oni, it must’ve been lonely, right?"

    MC "..."

    shiori "Didn’t it ever want someone to talk to?"

    MC "You're weird, Shiori."

    shiori "...Eh?"

    MC "Every time we talk, it’s about the Oni."

    MC "You never asked if I was okay, if I was scared, or if I was injured..."

    MC "And I think you're hoping that it managed to survive somehow."

    shiori "No! That’s not--I mean--"

    shiori "I care if you’re okay!"

    shiori "...But I-um, also just..."

    shiori "...I keep thinking about it. The Yamakui."

    shiori "It was probably awful and scary and hurt people, but..."

    shiori "I don’t think that means it didn’t feel things."

    MC "You think it had feelings?"

    shiori "M-Maybe!"

    shiori "Don’t you?"

    MC "..."

    shiori "At least it was hurt when you killed it, right?"

    MC "..."

    shiori "...I just think..."

    shiori "...Everyone should be loved. Even monsters."

    shiori "I hope someone hugs it before it dies, just once..."

    pause 0.4

    play sound "sfx/glitch_laugh.ogg"

    n2 "LOVE?"

    n2 "{fast}HHHHRRAKkkKhh--HHHHK! HhA!--KKAHhHAAHH!{/fast}"

    n2 "LOVE? You wanna love the crawl-thing?!"

    n2 "Stroke the throat, kiss the chewing holes?!"

    n2 "Hold the GULLET while it feeds?!"

    n2 "BAHAHA--"

    MC "Mmmph!"

    n "The laugh explodes out of your chest."

    n "Your hands twitch. Your spine locks."

    MC "That’s... ngh--"

    shiori "...[persistent.player_name]-sama?"

    MC "I’m fine."

    MC "Kh.{w} I’m--fine."

    n2 "This girl. So warm when she talks."

    n2 "Makes me wanna peel the skin and see where the softness comes from~"

    shiori "A-Are you laughing!?"

    shiori "You're so cruel!"

    MC "No, sorry, I just--!"

    shiori "Hmph! I can't believe you laughed when I was trying to be nice!"

    shiori "YOU BAKA!"

    n "She’s gone."

    n2 "See if she still says that when the hugging arm’s missing."

    n "Shut up."

    n "Shut up shut up shut up--"

    $ loop2_shiori_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear
    return
