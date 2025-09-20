label loop1_yamato:

    ## YAMATO'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS

    ## STILL IN DAY 5, HAPPENS AT THE END OF DAY 5

    scene forest night:
        zoom 0.5

    show yam normal:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 50
        xzoom 1.0
        yzoom 1.0

        parallel:
            linear 1.1 xoffset 6
            linear 1.2 xoffset -6
            linear 1.1 xoffset 0
            repeat

    play music "Night.mp3"


    n "You find him at the forest again, alone."

    n "The sun's almost gone, with a blood-colored light sinking into the current."

    n "Yamato's hunched, a half-empty bottle of sake in his right arm. Eyes liddled, gaze unfocused, and a bit woozy."

    MC "...Drinking alone?"

    yamato "{cps=14}Didn't ask for a damn audience.{/cps}"

    MC "Guess you got one anyway."

    yamato "Figures."

    n "He tips the bottle towards his mouth, the liquid inside sloshes..."

    n "But then his eyes meet yours, and he puts the bottle down again."

    yamato "This thing's{w=0.2} *hic* {w=0.1}got more memory than I do."

    MC "You're drunk."

    yamato "{w=0.2}No shit.{/w}"

    n "He pulls back his sleeve, and you see a long gash on his arm. The scars look old but it's pulsing."

    yamato "This thing still goddamn burns. {w=0.2}You remember how I got it?"

    menu:
        "Did I give it to you?":
            MC "Did I give it to you during sparring?"
            yamato "Ya? {w=0.15}Hah, nah."
        "Did you get bitten by a wolf during patrol?":
            MC "Did you get bitten by a wolf during patrol?"
            yamato "{cps=13}What'cha mean? All the wolves around here got eaten by the damn Yamakui.{/cps}"

    yamato "{w=0.2}Can't believe you forgot....{/w}"

    MC "...Yamato--"

    yamato "Tch... {w=0.1}We were, what, eleven?"

    yamato "{cps=13}Said we'd climb the mountain together. Remember that?{/cps}"

    yamato "{w=0.2}Kill the Yamakui. Be heroes 'n shit."

    n "Yamato no longer sounds bitter, it seems like he is merely... tired. Or maybe sad? Disappointed?"

    yamato "Got as far as the first cliff. I slipped and arm caught a rock."

    yamato "Split clean open, blood everywhere. {w=0.2}Thought my fightin' days are done for."

    MC "..."

    yamato "You screamed like hell broke loose. Said I was gonna die or somethin'."

    n "Ohh right, you {b}DID{/b} scream."

    yamato "{cps=12}You were the one who dragged me all the way back. I woke up t' yer dumb snot in my face.{/cps}"

    MC "..."

    yamato "Then you bawled your eyes out in front o' the whole damn village."

    n "Oh yes, I remember that too..."

    MC "...That was a long time ago, right?"

    yamato "Heh."

    play sound "sfx/bottle_thud.ogg"

    n "He drops the sake bottle beside him."

    yamato "{w=0.1}Yeah. Long enough for ya t' forget."

    yamato "{cps=12}Long enough for ya...{w=0.1} t' go climb it y'self. Guess I don't matter anymore{/cps}"

    yamato "{w=0.1}Then, {w=0.1}bam, suddenly came back with that damn armor "

    MC "I just-I didn't want anyone else getting hurt."

    yamato "So what, ya think we're weak? Think I can't take a hit?"

    MC "...I didn't mean to--"

    yamato "{w=0.15}Shut it."

    yamato "{cps=14}Ain't about what ya meant.{/cps}"

    yamato "Ya talk like yer some lone wolf hero from the damn stories."

    yamato "{w=0.1}But ya don't even remember who the hell ya were fightin' for."

    yamato "Tch."

    yamato "{cps=13}Now everything's weird since ya came back.{/cps}"

    yamato "Feels like I'm gonna open my mouth and someone else's voice is gonna crawl out."

    MC "...Is that a figure of speech, or--"

    n "He looks up, his eyes are glassy. You wonder if it's because he is drunk... or something else is shifting beneath those eyes."

    yamato "Like th--{nw}"

    yamato "Spine to root, bone to dirt, meat to mouth to mud to skin to teeth to skin--"

    yamato "Names in the mud, names we chewed, names we swallowed, chewed through our sleep, through your sleep--"

    yamato "Hollow boy full of eyes, mirror cracked with hairline mouths, singin' backwards--"

    yamato "River's throat opens open open open the jaw stretches wider when you breathe for too long don't breathe too long don't breathe don't--"

    MC "Yamato--"

    yamato "We are born wet and blind and screaming and that's the only time we ever get it right--"

    yamato "mouthsinthewatermouthsinthetreesmouthsundertheskinintheSKIIIIIIIN--"

    play sound "sfx/distortion_warp.ogg"
    $ renpy.pause(0.5)

    n "What is happening!? That doesn't sound like Yamato at all...!?"

    MC "Yamato."

    yamato "....!"

    yamato "Haah.... {w}Haaaah...."

    yamato "...Shit."

    MC "You alright?"

    yamato "No."

    MC "..."

    n "You pat Yamato's back, saying nothing as he tried to compose himself."

    MC "Tgere, there..."

    MC "You're gonna be okay."

    n "Why--"

    n "Why are you so calm about this?"

    scene black

    with fade

    ## TWO DAYS BEFORE THE RED MOON

    centered "TWO DAYS BEFORE THE RED MOON."

    n "You left Yamato alone yesterday, he looked a lot better then."

    n "So naturally you want to check up on him again today."

    play sound "sfx/wooden_sword_draw.ogg"

    show yamato neutral at midright

    yamato "Oi. Ya showed up. Thought ya'd be late again."

    MC "...Yamato?"

    yamato "What? Ya lookin' funny. Grab a sword, will ya?"

    n "...Wait. Where's the Yamato last night? Does he even remember what happened?"

    MC "Are you okay?"

    yamato "Haaa? What'd ya mean?"

    MC "It's just... You were drunk last night and I--"

    yamato "Tch, I don't get ya. Red Moon's tomorrow, remember? I ain't lettin' ya slack off."

    MC "...You're... in a good mood today."

    yamato "H-Hah? Dumbass, don't say it like that."

    yamato "I'm just... y'know. Tryin' t' be less of a pain in the ass today, 's all."

    n "The corner of his mouth twitches. Yamato struggles to smile, but his face isn't used to it."

    MC "...Thanks."

    yamato "D-Don't thank me, idiot. I'm doin' it for the village, not for ya."

    n "He swings lightly this time. A soft tap in your side instead of a full-blown strike, you feel he's holding back."

    MC "You're going easy on me."

    yamato "Wha--hell I am! If ya think this is easy, yer gettin' soft.."

    n "He looks everywhere else but your eyes, focusing on your stance, a soft blush creeping to his ears."

    yamato "...I just don't wanna see you keel over, alright?"

    MC "Really~?"

    yamato "Ngh, shaddap."

    n "He swings again, you feel no weight on ti as you parry."

    n "This isn't the same Yamato who broke in front of you yesterday."

    n "What is gping on? Which one's the real Yamato?"

    n "And why don't that scare you...?"

    n "You're done sparring now. Yamato taps his side as you sit down."

    yamato "Lemme see yer blade, [persistent.player_name]."

    MC "Why...?"

    yamato "Just gimme."

    sn "You hand him your blade without protest, he turns it around in his hand."

    yamato "Tch. What the hell did ya hit, a boulder?"

    yamato "Look at this edge. Disrespectful, that's what this is."

    MC "*scoff* 'Scuse me?"

    yamato "Lemme sharpen it for ya."

    n "He brings it to the  whetstone he used to keep at the dojo."

    MC "Oi, there's no need--"

    yamato "Shut it. Just don't want the damn thing falling apart on ya mid-swing and me havin' to pick up yer pieces."

    MC "...Thanks."

    n "You say nothing else and listen to the whetstone whispers against steel."

    # sharpening sound

    n "One stroke."

    n "Then another."

    n "Then another."

    # transition to heartbeat sound

    play sound "sfx/heartbeat_soft.ogg"

    n "Wait, you're not listening to the steel anymore are you."

    n "That's--"

    n "...Wait."

    n "You're listening to his pulse?"

    n "Why?"

    n "Thump. {w}Thump."

    MC "..."

    n "Thump.{w} Thump"

    n "You lean back and close your eyes, focusing."

    n "He's talking now, rambling about something you don't care about."

    yamato "--and the look on his face, swear to hell, like the noodles betrayed him--"

    n "All you hear is the thing behind his ribs."

    n "You feel like if you tapped back, it'd answer."

    MC "..."

    n "You try to stop listening, but your whole body's tuned to it now."

    yamato "Oi. Ya sleeping or somethin'?"

    MC "...Huh?"

    yamato "What were you staring at?"

    MC "Nothing."

    yamato "Tch. Sleepyhead."

    yamato "...Anyway. Done."

    play sound "sfx/sword_slide.ogg"

    yamato "Here ya go."

    MC "...Thanks."

    yamato "Ughhh."

    MC "What?"

    yamato "Wipe that smug grin off yer face, already."

    MC "Mmmm, not a chance."

    n "He hands it back, knuckles brushing your grip, somehow... they feel longer than they need to."

    n "Then he pulls away with a jerk, as if he feels this is bordering on inappropriate."

    yamato "See ya around--Uh, umm..."

    yamato "Yer goin' in patrol tonight, right?"

    MC "Yeah, obviously, the red moon is coming."

    yamato "Great, see ya tonight then."

    n "Yamato leaves immediately, clearly flustered for some reason."

    n "The heartbeat isn't there anymore, but you're still listening."

    ## STILL 2 DAYS BEFORE RED MOON

    n "You were getting ready for tonight's patrol when you hear a soft knock."

    MC "...Come in."

    yamato "Yo. Ya aready for patrol or ya still nappin'?"

    MC "You're early."

    yamato "No, yer lazy. Ya eatin' yet?"

    n "He takes out two packs of bento."

    MC "What's that?"

    yamato "Bento. Made too much."

    MC "For me?"

    yamato "Don't start smilin', dumbass. I ain't tryna marry you."

    MC "Actually, I haven't eaten--"

    n "Now that I think of it, you haven't eaten for DAYS, have you?"

    yamato "Heh. Of course. Can't trust ya to prep yer own damn lungs."

    yamato "Get some before ya go and ya die hungry or somethin'"

    n "He starts unwrapping the bento and shoves some to your hand."

    yamato "Half's yours. Don't drop it or I'll kick yer spine straight."

    MC "...Thanks."

    yamato "Shut up and eat."

    play sound "sfx/eat_crunch.ogg"

    n "Yamato just stands there as he waits for you to begin eating."

    n "It actually looks... decent. MORE then decent, even."

    MC "I-Itadakimatsu..."

    play sound "sfx/eat_softbite.ogg"

    n "..."

    n "The first bite sinks. Your teeth drag slow, pulling instead of tearing."

    n "It feels gummy in places, and slippery in others. Binds to your molars like glue stretched thin."

    n "The act of chewing itself spreads it across your tongue in layers. Tastes like... {w}damp cloth? {w}Sour milk?"

    MC "...Nn..."

    n "You eat the boiled egg next and feel the yolk bursts in your mouth. There's a sudden grit against your gums, followed by a hollow crunch that meltsthe moment you notice it."

    n "You try to push it down, no, you {i}struggle{/i} to swallow. Your throat now feels like there are nails trying to force its way through it."

    n "It passes only because of sheer will."

    MC "...Tastes good."

    yamato "Damn right. I seasoned it myself."

    n "Yamato begins unwrapping his own bento and eats without a care in the world."

    n "You don't understand how he manage to do that."

    play sound "sfx/eat_crunch.ogg"

    n "You take another bite, the seaweed lashes the inside of your cheek. A sharp crack, followed by a wet snap."

    n "Your stomach tuwists hard against your ribs, yourlike nausea trying to crawl upward. You snap your jaws shut and hold still."

    play sound "sfx/gulp_painful.ogg"

    MC "...Ngh."

    yamato "Oi. 'S that bad?"

    MC "No, no--It's really good! I'm actually not... {w} really hungry."

    n "You nod as your gut sloshes. The taste lingers, you want to drink something to wash it off since swallowing doesn't clear it and chewing doesn't help."

    yamato "Ya don't have to force yerself t' eat it, ya know..."

    n "You glance at your box."

    n "One piece left...."

    MC "I-Uh..."

    n "Your hand's frozen halfway now, chopsticks floating."

    n "...You never liked eating, did you?"

    n "Wait."

    n "That's wrong."

    n "When's the last time you ate something decent?"

    n "..."

    n "No, that's not--"

    MC "Yeah, I'm done."

    yamato "Let's go, then."

    n "He walks out first, not realizing you're trailing behind with a hand to your gut."

    n "You want to gag. Badly."

    n "Maybe find something to drink later."

    ## ONE DAY BEFORE THE RED MOON

    centered "ONE DAY BEFORE THE RED MOON."

    n "The sky's almost fully red tonight, so is the moon."

    yamato "Tch... This kinda quiet's the worst."

    MC "Why? Peaceful's bad now?"

    yamato "It's the waitin' I hate."

    MC "Still think something's out here?"

    yamato "Maybe."

    n "You both keep walking. You can hear your steps and his, Yamatos's always heavier than yours."

    n "Nothing else. No one else. No one's following you, at least... {w}not tonight."

    yamato "...Maybe ya actually pulled it off."

    MC "Mm, 'course I did."

    n "He rubs the back of his neck."

    yamato "Say we live past tomorrow."

    yamato "I was thinkin' maybe we--"

    yamato "Hnh..."

    MC "...Yeah?"

    yamato "Tch. {w}Forget it."

    MC "--wanna go cherry blossom viewing?"

    yamato "Was gonna say drink 'till dawn, but that works too."

    MC "I would conisder it since you're blushing so hard I almost want to pity you."

    yamato "The hell I am!"

    MC "Ohh, you totally are. Wooow. Do you like me, Yamato?"

    yamato "K-Keep talkin' and I-'ll... {w=0.2}I'll..."

    yamato "Argh, whatever."

    MC "So that's a yes."

    n "He turns quick, stomping ahead as if he can walk the embarrassment off."

    n "The patrol ends early and peacefully."

    n "It might end permanently once tomorrow comes."

    centered "DAY OF RED MOON."

    n "You're used to Yamato's knocking pattern by now."

    MC "Come in."

    play sound "sfx/door_open.ogg"

    yamato "...Yo."

    MC "You're up early."

    yamato "Couldn't get a damn sleep."

    n "He leans on the frame, arms crossed, eyes tired. Clearly he had been thinking too much and didn't like any of it."

    yamato "That time of th' year again. Damn red moon and all. "

    MC "Yeah..."

    yamato "Thought maybe..."

    pause(0.4)

    yamato "...Tch. Whatever. Ain't like I believe in fate 'n shit."

    MC "What is it?"

    yamato "Ya wanna be on guard with me?"

    MC "Of course!"

    yamato "Heh. Figures. Ya'd say yes even if I told ya we'd both die tonight."

    MC "Well, I'm just looking out for you, that's all."

    pause(0.3)

    yamato "..."

    yamato "If nothin' happens and the red moon passes..."

    yamato "Then maybe I'll believe ya for real this time."

    MC "...Yamato."

    yamato "What?"

    MC "That almost sounded like a compliment, you know."

    yamato "Wh-Shut the hell up!"

    yamato "Ergh..."

    yamato "I ain't good at sayin' soft shit."

    yamato "I just mean--"

    yamato "--Guess I'd be glad. If ya really killed the damn thing."

    MC "Same with me."

    yamato "Anyway. Let's not die."

    play sound "sfx/door_close.ogg"

    MC "...."

    MC "...." ## expression changes

    centered "RED MOON IS TONIGHT."

    n "The next day, you sit next to Yamato under the shrine roof. He's sitting really close that your knees keep bumping to each other."

    n "He's twirling an unopened bottle of sake."

    Yamato "I'm keepin' it for after the red moon."

    MC "Can't wait."

    yamato "...Sigh..."

    yamato "Look... I was a dick. Ya know it, I know it."

    yamato "Ya came back alive, did everything right. And I couldn't stop actin' like a jealous little shit."

    yamato "I kept barkin' at'cha 'cause I didn't know what else to do."

    MC "Yeah, but I did forgot our promise. Understandable."

    Yamato "I know. Not an excuse, though."

    MC "...Yamato."

    yamato "So... all I can think is--if ya die out there and I never said any of this, I'd never forgive myself."

    yamato "'Cause I care about ya, dumbass."

    yamato "That ain't new. I just-I was too busy actin' tough t' notice."

    MC "...You really mean that?"

    yamato "Yeah."

    yamato "So... {w=0.2}if somethin' happens, I need ya t' remember that."

    yamato "I... {w=0.3}didn't hate ya. Never did."

    MC "..."

    MC "I don't hate you too, Yamato."

    yamato "That so?"

    yamato "If we live... {W}maybe we figure this out."

    yamato "Y'know, what the hell this is between us."

    MC "That would be nice."

    n "None of you talk again in a while, until Yamato finally stands up."

    yamato "...I'm done talkin'. Ya remember the good parts, yeah?"

    MC "Yeah."

    yamato "A'ight. See ya again tonight."

    centered "RED MOON."

    n "The moon is bleeding now."

    n "You both are waiting for anything to appear, any sign of the Yamakui or the armor coming back alive "

    n "So you wait "

    n "And wait."

    n "And wait."

    n "But nothing comes out tonight."

    n "The night is almost over, you both open the bottle of sake he promised you both will drink after the red moon has passed."

    n "Yamato has already started drinking, but you hesitate on yours."

    yamato "...Heh."

    play sound "sfx/exhale.ogg"

    yamato "So that's it, guess you really did it."

    pause(0.3)

    yamato "Guess an apology is overdue, for everything I spat at ya."

    yamato "And for actin' like I wanted ya gone."

    yamato "I..."

    n "Yamato fully turns towards you now, eyes darting left and right, slight tremors in his lips."

    yamato "So..."

    yamato "Wasn't sure if I was gonna say it tonight, 'cause I didn't know if we'd make it."

    n "The smell of the sake hits you stronger now."

    n "You don't know why your stomach knots in the inside."

    MC "...Urk..."

    yamato "Oi. Ya alright?"

    n "You nod before thinking as the heat behind your eyes pulses again."

    n "You're shaking now, there's a crawling itch in the inside of your skin."

    yamato "Look, if this ain't what you want--"

    n "He waits, searching for an answer in your face. And yet you stay silent, never once shaking your head, so yamato takes it as a yes."

    play sound "sfx/shift_closer.ogg"

    n "He leans in, slowly, then again, still waiting for rejection. You still don't move."

    n "His breath brushes your cheek now, you're frozen in place."

    n "You feel the world tilts again faster."

    n "And finally, finally, softly, his lips find yours. His hands slowly holding your shoulder, shaking, trembling. He doesn't know what he's doing."

    n "Right at that moment, something underneath your skin wants out."

    n "You kiss him back because that's what happens next. That's the part you know."

    n "That's what people does--"

    n "Wait, what? You really think that?"

    n "Something inside you is folding inward..."

    ## ba dump ba dump

    n "... a hunger that wasn't there before."

    n "And Yamato chokes at you. You hear that gurgle caught in his throat."

    yamato "--mmgh--!"

    n "But his hands are gripping your arms now, tightly, then thighter, then he starts clawing."

    n "You hold him in place."

    play sound "sfx/flesh_pull1.ogg"

    n "There's a pull in your mouth--no, from your mouth--that feels wet, deep and wrong."

    n "His mouth won't leave yours... You're still kissing--why are you still kissing..!?"

    n "You feel his body jerk once, then shakes violently."

    play sound "sfx/wet_tangle.ogg"

    n "Something is inside him now.{w} Wait, no. you're inside him--"

    yamato "GHHHH--HHAKK--HHHHH!!"

    ## screaaaammmmmmmmm

    n "He's screaming."

    n "He's... trying to scream through the kiss."

    n "I-Oh kami-sama--"

    n "You can hear it in his throat. In your teeth..."

    n "INSIDE YOUR STOMACH."

    yamato "NNNRRGHH--!--LET--LET--HHHHH--"

    play sound "sfx/heartbeat_fast.ogg"

    n "...Let him go."

    n "Please--let him go--!"

    n "Please--!"

    n "..."

    n "T-The red moon is over now."

    n "Yamato was--"

    n "...He was--"

    n "...He--"

    n "Gone?"

    n "You--"

    MC "Yeah, he's gone now. Don't pretend you didn't see that."

    n "You're supposed to be--"

    n "You were--"

    MC "..."

    n "--the hero, right?"

    n "Oh no."

    n "But just now you--Why? Why did you do that?"

    MC "Eh."

    n "No, no, no way..."

    n "...Let me out!"

    MC "Too late, you're stuck with me now until you're gone or I die."

    n "..."

    centered "YAMATO IS DEVOURED"

    centered "TWO MORE TO GO."

    $ persistent.yamato_dies = True

    ## at the end of the route yamato dies

    $ persistent.loop1 = True

    $ persistent.trueending.unlocked = False

    yamato "I ded."

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
