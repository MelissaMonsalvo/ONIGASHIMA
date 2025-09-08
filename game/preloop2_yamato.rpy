############# LOOP 2 WHERE ONE DIED ###########################
label loop2_yamato_mandatory1:

    $ loop2_yamato_mandatory1 = True

    n "Hmm? Why is the path curved?"

    n "You don't remember it curving like this..."

    n2 "Or maybe the trees moved, because they don’t like what’s inside you now."

    play sound "sfx/grassstep.ogg"

    show yamato angry at midright

    yamato "Oi."

    yamato "I been lookin' for ya."

    MC "...Yamato."

    yamato "Tch. Don't gimme that voice."

    yamato "Ain’t here for pleasantries."

    MC "Okay...?"

    yamato "I got questions."

    MC "About...?"

    yamato "Don't fuckin’ play innocent."

    yamato "You went up that mountain and came back without a single scratch."

    yamato "There ain't no way that's happenin'."

    MC "..."

    n2 "Hah."

    yamato "So I’m askin’, what the hell happened up there?"

    n "Say something. Anything."

    MC "I got bit."

    yamato "Bit?"

    MC "Yeah, the damn Yamakui bit me. That’s why I--"

    yamato "Bullshit. Where?"

    MC "Here."

    play sound "sfx/clothes_rustle.ogg"

    n "You pull your collar down and shows a mark just below the neck."

    n "It looks like a bite, all right."

    n "But it's starting to rot at the edges..."

    play sound "sfx/slough_skin.ogg"

    n "Oh wait, it’s actually melting--"

    n2 "Mmmmnnnnh."

    yamato "The FUCK."

    yamato "What the hell is that?!"

    yamato "That ain’t a wound. That’s... That’s--"

    yamato "Shit, what ARE you?!"

    n "Yamato  unsheates his blades now."

    yamato "That ain’t--That's a corpse...!"

    MC "I thought you wanted proof?"

    yamato "Yeah?! Well, ya gave me a damn horror show!"

    n2 "Let him scream. I wanna see what his ribs sound like."

    n "Stop. Please stop. Don’t talk like that. Don’t even ASK.."

    MC "It’s only a wound, Yamato."

    MC "I mean it's a Yamakui, it's bound to leave a curse or something."

    yamato "Nah. That ain’t no wound I ever seen."

    yamato "That thing’s... That thing's crawling under your fuckin’ skin."

    n2 "It fits good."

    n2 "Tight."

    yamato "...You’re lyin'."

    yamato "If the fuckin' Yamakui's dead then the curse would fuck off!"

    MC "No--"

    yamato "Don’t you lie t’me!"

    yamato "I trusted ya!"

    n2 "So loud."

    n2 "Let's shut him up."

    n "DO NOT. Don’t touch him. Don’t even think about it--"

    yamato "Tch..."

    n "His hand is trembling. You have never seen Yamato this horrified before."

    play sound "sfx/step_back.ogg"

    yamato "Shit. I need t’think."

    yamato "Don’t even fuckin’ BREATHE near me right now, you get it!?"

    n "He’s gone."

    n2 "He’ll come back."

    n2 "They always do. {w}Meat don’t wander far."

    n "You look down at your shoulder."

    n "The skin wriggles, then closes itself again."

    MC "..."

    return

label loop2_yamato_mandatory2:

    yamato "Ah hell, what are you doing here!?"

    MC "Don't mind me, I just want to spar."

    yamato "Fuck off!"

    MC "What, the great Yamato is afraid of a little curse?"

    yamato "Wh--"

    MC "Can't believe the guy who used to shout he'd kill the Yamakui now run away with his tails between his legs."

    MC "What are you, coward?"

    yamato "Damn you--"

    n "Yamato grabs hid word then rushes towards you."

    n "He always had that fast and clean form, even sharper than you or Hikaru."

    n "You usually couldn't dodge because he's too{nw}"

    n2 "S l o w."

    n "You move without thinking."

    n "Parry, then twist."

    n "Your blade dances gracefully and you reappears behind him."

    n "Yamato swings backwards in desperation, as instict."

    n "But you're faster and trips his legs."

    yamato "Wha--!"

    n "You heard his knees popping."

    n2 "Again."

    n2 "Break it."

    n "You slam the sword forward--"

    n "He hits the ground. Hard."

    yamato "Ghk--! Fuck!"

    n "He’s kneeling on the dirt, wheezing and clutching his side."

    yamato "Y-you--"

    yamato "You’re not even breakin’ a sweat. Since when...?"

    yamato "No... What the fuck {b}are{/b} you?"

    ## make the menu txt distorted, mouse erratic

    menu:
        "K I L L K I L L K I L L":
            n "Are you insane!? Stop!"
        "E A T E A T E A T E A T":
            n "No! Please, stop!"

    n2 "Look at him shaking."

    n2 "Little animal is cornered."

    n "Stop. Stop thinking like that. That’s not--"

    mc "Yamato--"

    yamato "S-Stay back!"

    yamato "You ain’t foolin’ anyone anymore!"

    yamato "Whatever curse ya brought down that mountain--"

    yamato "Tch, damn it!"

    n "Yamato scrambles away frantically, but still heavily wounded."

    n "What are you doing...? He's going to tell the others and--"

    n2 "Let him, let them aaallllll come."

    n2 "I want to see what they taste like... one by one."

    $ loop2_yamato_mandatory2 = True

    return

label loop2_yamato_mandatory3:

    n "You see Yamato kneeling before the graves without names."

    n "He lights the incense, then presses both fists together... They're still shaking."

    yamato "Tch..."

    yamato "Didn’t think I’d be back here so soon."

    yamato "I still dunno what t’say."

    n2 "Hn? Something’s here."

    n2 "I can  smell it."


    ### SHIORI GHOST PATH
    if shiori_dead:

        n "You see her before you hear anything."

        n "She’s standing between the gravestones, her mouth stretches open, then splits slowly."

        n "Who...?"

        play sound "sfx/flesh_rip.ogg"

        n "Her face peeling open like a purse made of meat, from lip, to cheek, then her ears..."

        n2 "Ah. The stringy one."

        n "But Yamato can't seem to see her."

        yamato "Whoever you were, I remembered having ya as a friend..."

        yamato "Sometimes I dreamed of a girly voice in my sleep... Maybe it's ya."

        yamato "...I shoulda gone up there with ya."

        yamato "Tch. {w}Dunno if you hear me."

        yamato "But this is all I can give."

        n "The incense smoke trails toward her, as if she's inhaling it."

        n2 "HraHaHHAhHAhahhh"

        n2 "She followed us down the throat."

        n2 "Let her stay there forever."

    ### HIKARU GHOST PATH
    if hikaru_dead:

        n "There’s something standing by the incense..."

        n "Their mask has melted into the bone. You can see the skull beneath it."

        n "Ah... Who..."

        n "Why do I feel...?"

        n2 "That's your favorite."

        n "The eye sockets are dark. Empty. But you know they see you."

        n "You can feel it on your skin."

        yamato "Tch... I can't even remember how ya look like..."

        yamato "But I remembered I got another sparring partner other than [persistent.player_name]."

        yamato "I shoulda said goodbye properly."

        yamato "Now I gotta light this stupid stick and hope it gets to ya somehow."

        n2 "HUhhUhhhuHUHuHuuhh."

        n2 "You'll join them soon."

    ### COMMON ENDING

    n "Yamato bows one more time before leaving."

    n "Whatever that was... He didn't see it."

    n2 "But we do."

    n2 "Because the meat is always with us."

    $ loop2_yamato_mandatory3 = True

    return

label loop2_yamato_mandatory4:

    n "Why... Why are you in the forest this late?"

    n2 "Sshh... Listen. {w=0.2}Look."

    n "Yamato is on his knees, with his hands clawed into the dirt."

    yamato "HrghKKKK!"

    n "Black water floods from his mouth. It's thick, writhing... alive?"

    yamato "Haaah... Hhhhaaaaahh..."

    n "His face is contorting... No one should look likt THAT."

    n "His jaw unhinges far too wide, then his tongue slides out, twitching.."

    n "What is happening?!"

    n "You hear something pop, then followed by a wet crunch. It's as if... as if... something inside him is rearranging."

    n "The black water pools at his knees. It moves without touching him, having a mind of its own"

    yamato "Tch..."

    yamato "Knew you were watchin’..."

    mc "...Yamato?"

    yamato "Wanna laugh again, huh? Go on. Do it."

    yamato "I ain't scared anymore."

    yamato "NO NO NO. Not scared not scared not scared."

    yamato "Red moon's comin’... and I’m gonna peel the meat off your damn bones."

    yamato "When it rises... {w=0.2}you {i}fall{/i}."

    ## make the menu txt distorted, mouse erratic

    menu:
        "T H E R E D M O O N":
            n "No, no, no, stop--"
        "I S C O M I N G":
            n "No, no, no, stop--"


    n2 "AhhhhHHHhh... He SPEAKS now."

    n2 "Little boy thinks he's brave."

    n2 "HRAHaHAHaHaaa... oh, bite back, bite down, BITE OUT HIS TONGUE!"

    yamato "I’m stronger now. {w=0.2}Don’t need skin to hold me back anymore."

    yamato "You come near, [player_name], I’ll drag you through yer own blood.."

    n2 "Try. TRY. TRY. TRY TRY TRY TRY TRY--"

    yamato "Tch. WATCH me."

    n2 "I am."

    n2 "I A M {w=0.1}W A T C H I N G {w=0.1}Y O U."

    ## all characters vanish from map, but the ghost still appear
    return
