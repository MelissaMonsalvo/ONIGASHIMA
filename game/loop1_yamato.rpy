label loop1_yamato:

    scene black
    with fade

    scene white_bg
    with out_182

    show petals_dense2
    show petals_scatter2

    n "These past few days have been odd, to say the least."

    n "You spent your days with Yamato the most."

    n "...Wait, where is Yamato right now?"

    scene black

    with fade

    $ ysword = False

    ## YAMATO'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS

    ## STILL IN DAY 5, HAPPENS AT THE END OF DAY 5

    scene forest night:
        zoom 0.5

    show yam drunk:
        zoom 0.3
        xalign 0.55
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

    n "Yamato's hunched, a half-empty bottle of sake in his right hand. Eyes lidded, gaze unfocused, and a bit woozy."

    MC surprised "...Drinking alone?"

    yamato "{cps=14}Didn't ask for a damn audience.{/cps}"

    MC smugcl "Guess you got one anyway."

    yamato "Figures."

    n "He tips the bottle towards his mouth, the liquid inside sloshes..."

    n "But then his eyes meet yours, and he puts the bottle down again."

    yamato "This thing's{w=0.2} *hic* {w=0.1}got more memory than I do."

    MC annoyed "You're drunk."

    yamato "{w=0.2}No shit."

    n "He pulls back his sleeve, and you see a long gash on his arm. The scars look old but it's pulsing."

    yamato "This thing still goddamn burns. {w=0.2}You remember how I got it?"

    menu:
        "I gave it to you":
            MC nervous "Did I give it to you during sparring?"
            yamato "Ya? {w=0.15}Hah, nah."
        "You got bitten by a wolf":
            MC surprised "Did you get bitten by a wolf during patrol?"
            yamato "{cps=13}What'cha mean? All the wolves around here got eaten by the damn Yamakui.{/cps}"

    yamato "{w=0.2}Can't believe you forgot..."

    MC sad "...Yamato–"

    yamato "Tch... {w=0.1}We were, what, eleven?"

    yamato "{cps=13}Said we'd climb the mountain together. Remember that?{/cps}"

    yamato "{w=0.2}Kill the Yamakui. Be heroes 'n shit."

    n "Yamato no longer sounds bitter, it seems like he is merely... tired. Or maybe sad? Disappointed?"

    yamato "Got as far as the first cliff. I slipped and arm caught a rock."

    yamato "Split clean open, blood everywhere. {w=0.2}Thought my fightin' days are done for."

    MC sad "..."

    yamato "You screamed like hell broke loose. Said I was gonna die or somethin'."

    n "Ohh right, you {b}DID{/b} scream."

    yamato "{cps=12}You were the one who dragged me all the way back. I woke up t' yer dumb snot in my face.{/cps}"

    MC sadcl "..."

    yamato "Then you bawled your eyes out in front o' the whole damn village."

    n "Oh yes, I remember that too..."

    MC nervous "...That was a long time ago, right?"

    show yam drunk2
    with dissolve

    yamato "Heh."

    n "He drops the sake bottle beside him."

    show yam drunk
    with dissolve

    yamato "{w=0.1}Yeah. Long enough for ya t' forget."

    yamato "{cps=12}Long enough for ya...{w=0.1} t' go climb it y'self. Guess I don't matter anymore.{/cps}"

    yamato "{w=0.1}Then, {w=0.1}bam, suddenly came back with that damn armor."

    MC sadcl "I just-I didn't want anyone else getting hurt."

    yamato "So what, ya think we're weak? Think I can't take a hit?"

    MC hurt "...I didn't mean to–"

    show yam annoyedbl
    with dissolve

    yamato "{w=0.15}Shut it."

    yamato "{cps=14}Ain't about what ya meant.{/cps}"

    yamato "Ya talk like yer some lone wolf hero from the damn stories."

    yamato "{w=0.1}But ya don't even remember who the hell ya were fightin' for."

    yamato "Tch."

    yamato "{cps=13}Now everything's weird since ya came back.{/cps}"

    yamato "Feels like I'm gonna open my mouth and someone else's voice is gonna crawl out."

    MC "...Is that a figure of speech, or–"

    stop music fadeout 1.0

    n "He looks up, his eyes are glassy. You wonder if it's because he is drunk... or something else is shifting beneath those eyes."

    yamato "Like th–{nw}"

    play sound "sfx/jumpscare.mp3"

    scene forest night:
        zoom 0.5
        xalign 0.5
        yalign 0.5
        linear 0.2 zoom 0.6
        linear 0.1 zoom 0.75
        linear 0.01 zoom 0.9

    show yam eldritch:
        zoom 0.3
        xalign 0.55
        yalign 0
        yoffset 50
        xoffset 50
        xzoom 1.0
        yzoom 1.0


        linear 0.2 zoom 0.38 yalign 0.13 yoffset 310
        linear 0.1 zoom 0.49 yalign 0.21 yoffset 400
        linear 0.01 zoom 0.7 yalign 0.28 yoffset 850


        linear 0.04 xoffset 100
        linear 0.03 xoffset 140
        linear 0.03 xoffset 170
        linear 0.03 xoffset 185
        linear 0.03 xoffset 200
    pause 0.5

    show yam eldritch:
        zoom 0.7
        xalign 0.55
        yalign 0.28
        yoffset 850
        xoffset 200
        xzoom 1.0
        yzoom 1.0

        parallel:
            pause 0.03
            linear 0.02 xoffset 215 yoffset 860
            pause 0.06
            linear 0.02 xoffset 185 yoffset 790
            pause 0.04
            linear 0.01 xoffset 225 yoffset 800
            pause 0.08
            linear 0.03 xoffset 200 yoffset 790
            pause 0.02
            linear 0.02 xoffset 192 yoffset 860
            pause 0.09
            linear 0.01 xoffset 205 yoffset 850
            pause 0.04
            linear 0.03 xoffset 200 yoffset 850
            pause 0.4
            repeat

    show darken2
    play music "sfx/forest night.wav"
    yamato "{cps=180}Teeth in the dark, teeth in the mud, teeth in the spine–{w=0.2}gotta eat, gotta chew, gotta tear, gotta bite, gotta bite–{/cps}{nw}"

    yamato "{cps=150}Names {w=0.1}slide down the throat–{w=0.2}they don't come back up, {i}not once{/i} {w=0.15}names go soft and sweet in the belly, {k=2}rotten with memory{/k}–{/cps}{nw}"

    yamato "{cps=140}Stomachs full of holes, empty, always {sc=4}empty{/sc}, {w=0.1}hunger's a song in my bones {w=0.2}can't stop can't stop can't–{/cps}{nw}"

    yamato "{cps=100}Mouths in the walls, eyes in the roots, {sc=3}who are you when you're all eaten up?{/sc} {i}Who am I?{/i}–{/cps}{nw}"

    MC surprised "Yamato–"

    yamato "{cps=100}Feed it, {w=0.1}feed it, {w=0.1}feed it, never full, never done–{k=2}starving starving always starving {/k}{/cps}{nw}"

    yamato "{cps=50}mouthsinthewatermouthsinthetreesmouthsundertheskininthe{/cps}{cps=10}SKIIIIIIIN–{/cps}{nw}"


    n "What is happening!? That doesn't sound like Yamato at all...!?"

    MC annoyed "Yamato."

    play sound "sfx/suzu.mp3"

    show yam panic:
        zoom 0.6
        xalign 0.55
        yalign 0.28
        yoffset 700
        xoffset 200
        xzoom 1.0
        yzoom 1.0

        ease 0.2 zoom 0.55 yoffset 750
    hide darken2
    with sshake

    yamato "....!"

    yamato "Haah.... {w}Haaaah...."

    show yam ngh
    with dissolve

    yamato "...Shit."

    MC annoyed "You alright?"

    yamato "No."

    MC yan "..."

    n "You pat Yamato's back, saying nothing as he tried to compose himself."

    MC yansm "There, there..."

    MC yansm "You're gonna be {glitch}okay.{/glitch}"

    n "Why–"

    n "Why are you so calm about this?"

    scene black

    with fade

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}TWO DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

    with fade

    pause 0.5

    scene moon4
    with fade
    pause 0.2
    scene moon5
    with fade

    stop sound

    scene black
    with fade

    pause 0.5

    scene dojo day with in_182:
        zoom 0.5

    pause 1.0



    n "You dropped Yamato at his house yesterday, he looked a lot better after his 'drunk' ramblings when you left him."

    n "So naturally you want to check up on him again today."

    show yam serious:
        zoom 0.3
        xalign 0.4
        yalign 0
        yoffset 0
        xzoom -1
        yzoom 1.0
        matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

        pause 0.8

        ease 0.2 xzoom 1 matrixcolor None xoffset 120

    play music "Idle.mp3"


    yamato "Oi. Ya showed up. Thought ya'd be late again."

    MC surprised "{k=2}...Yamato?{/k}"

    yamato "What? Ya lookin' funny. Grab a sword, will ya?"

    n "...Wait. Where's the Yamato from last night? Does he even remember what happened?"

    MC nervous "Are you okay?"

    show yam annoyed
    with dissolve

    yamato "Haaa? What'd ya mean?"

    MC nervous "{sc=1}It's just... You were drunk last night and I–{/sc}"

    yamato "Tch, I don't get ya. Red Moon's tomorrow, remember? I ain't lettin' ya slack off."

    MC normal "{i}...You're... in a good mood today.{/i}"

    show yam annoyedbl
    with dissolve

    yamato "{k=1}H-Hah? Dumbass, don't say it like that.{/k}"

    yamato "{sc=1}I'm just... y'know. Tryin' t' be less of a pain in the ass today, 's all.{/sc}"

    n "The corner of his mouth twitches. Yamato struggles to smile, but his face isn't used to it."

    MC happycl "{i}...Thanks.{/i}"

    yamato "D-Don't thank me, idiot. I'm doin' it for the village, not for ya."


    scene black

    play sound "swing.wav"

    show slash_arc

    pause 1

    scene dojo day:
        zoom 0.5

    show yam serious:
        zoom 0.3
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1
        yzoom 1.0

        # Rapid, small side-to-side shakes (as if shouting)
        linear 0.06 xoffset 154
        linear 0.06 xoffset 134
        linear 0.06 xoffset 149
        linear 0.05 xoffset 139
        linear 0.07 xoffset 144
    with hpunch


    n "He swings lightly this time. A soft tap into your side instead of a full-blown strike, you feel that he's holding back."

    MC smugcl "You're going easy on me."

    show yam annoyedbl
    with dissolve

    yamato "{sc=1}Wha–hell I am!{/sc} If ya think this is easy, yer gettin' soft.."

    n "He looks everywhere else but your eyes, focusing on your stance, a soft blush creeping to his ears."

    yamato "...I just don't wanna see ya keel over, alright?"

    MC smugcl "Really~?"

    scene black

    play sound "swing.wav"
    show slash_vertical
    $ renpy.pause(0.1, hard=True)
    with vpunch

    scene dojo day:
        zoom 0.5

    show yam annoyedbl:
        zoom 0.47
        align (0.5, 0.005)


        linear 0.01 xalign 0.5 yalign 0.1

        linear 0.16 zoom 0.4 xalign 0.41 yalign -0.09 xoffset 122

        linear 0.12 zoom 0.35 xalign 0.4 yalign 0 xoffset 144 yoffset 0

        linear 0.07 yoffset 8
        linear 0.09 yoffset 0

    pause 0.05




    yamato "Ngh, shaddap."

    n "He swings again, you feel no weight on it as you parry."

    n "This isn't the same Yamato who broke down in front of you yesterday."

    n "What is going on? {k=-1}Which one's the real Yamato?{/k}"

    n "And why doesn't that scare you...?"

    n "You're done sparring now. Yamato taps his side as you sit down."

    show yam serious
    with dissolve

    yamato "Lemme see yer blade, [persistent.player_name]."

    MC surprised "Why...?"

    yamato "Just gimme."

    n "You hand him your blade without protest, he turns it around in his hand."

    show yam annoyed
    with dissolve

    yamato "Tch. What the hell did ya hit, {i}a boulder?{/i}"

    yamato "Look at this edge. Disrespectful,{w=0.1} that's what this is."

    MC annoyed "*scoff* {w=0.1}'Scuse me?"

    show yam annoyedbl
    with dissolve

    yamato "Lemme sharpen it for ya."

    n "He brings it to the whetstone he used to keep at the dojo."

    MC surprised "Oi, there's no need–"

    yamato "Shut it. Just don't want the damn thing falling apart on ya mid-swing and me havin' to pick up yer pieces."

    MC happycl "...Thanks."

    show yam serious
    with dissolve

    n "You say nothing else and listen to the whetstone whisper against steel."

    play muzak "sfx/whetstone.mp3"

    n "One stroke."

    n "Then another."

    n "Then another."

    # transition to heartbeat sound

    stop muzak

    show darken

    $ decrease_music_volume(0.3)
    $ renpy.block_rollback()

    play sound "sfx/heartbeat.mp3"

    n "..."

    pause 0.3

    $ decrease_music_volume(0.3)
    $ renpy.block_rollback()

    play sound "sfx/heartbeat.mp3"

    n "..."

    pause 0.3

    $ decrease_music_volume(0.3)
    $ renpy.block_rollback()

    play sound "sfx/heartbeat.mp3"

    n "..."

    pause 0.3


    n "Wait, you're not listening to the steel anymore are you."

    n "That's–"

    n "...Wait."

    n "You're listening to his pulse?"

    n "Why?"

    play sound "sfx/heartbeat.mp3"

    n "{size=+3}Thump.{/size}"

    MC "..."

    play sound "sfx/heartbeat.mp3"

    n "{size=+6}Thump.{/size}"

    scene black
    with out_eye
    show darken2

    n "You lean back and close your eyes, focusing."

    n "He's talking now, rambling about something you don't care about."

    yamato "–and the look on his face, swear to hell, like the noodles betrayed him–"

    play sound "sfx/heartbeat.mp3"

    n "All you hear is the thing behind his ribs."

    n "You feel like if you tapped back, it'd answer."

    play sound "sfx/heartbeat.mp3"

    MC yan "..."

    play sound "sfx/heartbeat.mp3"

    n "You try to stop listening, but your whole body's tuned to it now."

    $ restore_music_volume()
    $ restore_music_volume()
    $ restore_music_volume()

    yamato "Oi. Ya sleeping or somethin'?"

    scene dojo day with in_eye:
        zoom 0.5


    show yam surprised with dissolve:
        zoom 0.26
        align (0.5, 0.005)
        yoffset 0

    MC surprised "...Huh?"

    yamato "What were you staring at?"

    MC yan "Nothing."

    show yam annoyed
    with dissolve

    yamato "Tch. Sleepyhead."

    show yam happycl
    with dissolve

    yamato "...Anyway. Done."

    yamato "Here ya go."

    MC happycl "...Thanks."

    show yam blush
    with dissolve

    yamato "{bt=h1-s0.5-p1.0}Ughhh.{/bt}"

    MC smug "What?"

    yamato "Wipe that smug grin off yer face, already."

    MC smug "Mmmm, not a chance."

    show yam blush:
        zoom 0.26
        align (0.5, 0.005)
        yoffset 0

        ease 0.4 zoom 0.35 yoffset -20 xoffset 10

    n "He hands it back, knuckles brushing your grip, somehow... {w=0.1}they feel longer than they need to."

    show yam panicbl:
        zoom 0.35
        align (0.5, 0.005)
        yoffset -20
        xoffset 10

        ease 0.1 zoom 0.25 yoffset 0 xoffset 0

    n "Then he pulls away with a jerk, as if he feels this is bordering on inappropriate."

    yamato "See ya around–{w}Uh, {w=0.2}umm..."

    show yam annoyedbl
    with dissolve

    yamato "Yer goin' on patrol tonight, right?"

    MC normal "Yeah, obviously, the red moon is coming."

    show yam blush
    with dissolve

    yamato "Great, see ya tonight then."

    show yam blush:
        zoom 0.26
        align (0.5, 0.005)
        yoffset 0

        ease 0.3 xzoom -1
    pause 0.3

    hide yam blush
    with easeoutleft

    play sound "sfx/doorslam.wav"
    with hpunch

    n "Yamato leaves immediately, clearly flustered for some reason."

    stop music fadeout 1.0

    n "The heartbeat isn't there anymore, but you're still listening."

    scene black

    with out_182

    pause 0.2

    play sound "sfx/knock.wav"

    with vpunch
    pause 0.01
    with vpunch
    pause 0.01
    with vpunch
    pause 0.01

    n "You were getting ready for tonight's patrol when you hear a soft knock."

    MC normal "...Come in."

    play sound "sfx/sliding door.mp3"

    pause 0.3

    scene house night:
        zoom 0.5

    show yam serious:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    with dissolve

    pause 0.2

    stop sound

    play muzak "sfx/forest night.wav"

    yamato "Yo. Ya already for patrol or ya still nappin'?"

    MC normal "You're early."

    show yam smug
    with dissolve

    yamato "No, yer lazy. Ya hav' eaten yet?"

    show frame2:
        zoom 0.4
        xanchor 0.5
        xalign 0.5
        yalign 0.3
    show bento:
        zoom 0.5
        xanchor 0.5
        xalign 0.5
        yalign 0.33
    with dissolve

    n "He takes out two bento boxes."

    MC surprised "What's that?"

    show yam blush
    with dissolve

    yamato "Bento. Made too much."

    MC happy "For me?"

    show yam annoyedbl
    with dissolve

    yamato "Don't start smilin', dumbass. I ain't tryna marry you."

    MC happycl "Actually, I haven't eaten–"

    n "Now that I think of it, you haven't eaten for DAYS, have you?"

    show yam smug
    with dissolve

    yamato "Heh. Of course. Can't trust ya to prep yer own damn lungs."

    show yam annoyedbl
    with dissolve

    yamato "Get some before ya go and ya die hungry or somethin'."

    n "He starts unwrapping the bento and shoves one into your hand."

    yamato "Half's yours. Don't drop it or I'll kick yer spine straight."

    MC normal "...Thanks."

    yamato "Shut up and eat."

    show yam blush
    with dissolve

    n "Yamato just stands there as he waits for you to begin eating."

    n "It actually looks... {w=0.1}decent. MORE then decent, even."

    MC nervous "{k=2}I-{w=0.1}Itadakimasu...{/k}"

    scene black

    show darken2
    with dissolve

    play music "sfx/eatfood.mp3"

    n "..."

    n "The first bite sinks in. Your teeth drag slow, {i}pulling{/i} instead of tearing."

    n "It feels {sc=3}gummy{/sc} in places, and {i}slippery{/i} in others. Bound to your molars like glue stretched thin."

    n "The act of chewing itself spreads it across your tongue in layers. Tastes like...{w}damp cloth?{w}{sc=2} Sour milk?{/sc}"

    MC sadcl "{sc=3}...Nn...{/sc}"

    with hpunch
    with flashred

    n "You eat the boiled egg next and feel the yolk bursts in your mouth. There's a sudden {sc=2}grit{/sc} against your gums, followed by a hollow crunch that melts the moment you notice it."

    with flashred

    n "You try to push it down, no, you {i}struggle{/i} to swallow. Your throat now feels like there are nails trying to force its way through it."

    with flashred

    n "It passes only because of sheer will."

    MC nervous "...Tastes good."

    yamato "Damn right. I seasoned it myself."

    pause 0.3

    scene house night:
        zoom 0.5

    show yam serious:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    show darken2
    with dissolve

    n "Yamato begins unwrapping his own bento and eats without a care in the world."

    n "You don't understand how he manages to do that."

    n "You take another bite, the seaweed {sc=3}lashes{/sc} the inside of your cheek. A sharp crack, followed by a wet snap."

    with flashred

    n "Your stomach {i}twists{/i} hard against your ribs, a feeling of nausea trying to crawl upward. You snap your jaws shut and hold still."

    play sound "sfx/gag2.mp3"

    with hpunch

    MC hurt "{k=2}...Ngh.{/k}"

    show yam panicbl
    with dissolve

    yamato "Oi. 'S that bad?"

    MC hurt "{sc=3}No, no–It's really good! I'm actually not...{w} really hungry.{/sc}"

    n "You nod as your gut {i}sloshes{/i}. The taste lingers, you want to drink something to wash it off since swallowing doesn't clear it and chewing doesn't help."

    show yam blush
    with dissolve

    yamato "Ya don't have to force yerself t' eat it, ya know..."

    n "You glance at your box."

    n "One piece left...."

    play sound "sfx/gag1.mp3"

    with vpunch

    MC hurt "{k=2}I-Uh...{/k}"

    n "Your hand's frozen halfway now, chopsticks floating."

    n "...You never liked eating, did you?"

    n "Wait."

    n "That's wrong."

    n "When's the last time you ate something {sc=2}decent{/sc}?"

    n "..."

    n "No, that's not–"

    play sound "sfx/stomp.mp3"
    stop music
    stop muzak

    scene house night:
        zoom 0.5

    show yam shocked:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    with vpunch



    MC yan "Yeah, I'm done."

    show yam normal
    with dissolve

    yamato "Let's go, then."

    scene black
    with out_212

    stop music

    n "He walks out first, not realizing you're trailing behind with a hand to your gut."

    n "You want to gag. Badly."

    n "Maybe find something to drink later."

    scene black

    pause 0.3

    stop music

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}ONE DAY UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

    with fade

    pause 0.5

    scene moon5
    with fade
    pause 0.2
    scene moon6
    with fade

    stop sound

    pause 0.5

    n "The sky's almost fully red tonight, so is the moon."

    scene forest night with fade:
        xpos 0
        blur 2
        linear 15 xpos -1920  # Move left by one screen width over 8 seconds (adjust speed)
        repeat
    show yam serious:
        zoom 0.5
        xalign 0.4
        yalign -0.15
        yoffset -400
        xzoom 1
        yzoom 1.0

        yoffset -400
        linear 0.5 yoffset -420
        linear 0.5 yoffset -400
        repeat


    with dissolve

    play music "Night.mp3"

    yamato "Tch... This kinda quiet 's the worst."

    MC normal "Why? Is peaceful bad now?"

    yamato "It's the waitin' I hate."

    MC normal "Still think something is out here?"

    yamato "Maybe."

    n "You both keep walking. You can hear your steps and his, Yamatos's always heavier than yours."

    n "Nothing else. No one else. No one's following you, at least... {w}not tonight."

    yamato "...Maybe ya actually pulled it off."

    MC smug "Mm, 'course I did."

    n "He rubs the back of his neck."

    show yam blush
    with dissolve

    yamato "Say we live past tomorrow."

    yamato "I was thinkin' maybe we–"

    yamato "{cps=10}Hnh...{/cps}"

    MC surprised "...Yeah?"

    show yam panicbl
    with dissolve

    yamato "Tch. {w}Forget it."

    MC happycl "–wanna go cherry blossom viewing?"

    show yam annoyedbl
    with dissolve

    yamato "Was gonna say drink 'till dawn, but that works too."

    MC smugcl "I would consider it since you're blushing so hard I almost want to pity you."

    show yam panicbl
    with dissolve

    yamato "{sc=2}{size=+2}The hell I am!{/size}{/sc}"

    MC smugcl "Ohh, you totally are. {cps=10}Wooow.{/cps} Do you like me, Yamato?"

    yamato "{sc=1}K-Keep talkin' and I-'ll... {w=0.2}I'll...{/sc}"

    show yam blush
    with dissolve

    yamato "{w=0.1}Argh, whatever."

    MC happy "So that's a yes."


    show yam panicbl:
        zoom 0.5
        xalign 0.4
        yalign -0.15
        yoffset -400
        xzoom 1
        yzoom 1.0

        ease 0.5 xzoom -1
    with dissolve
    pause 0.1
    hide yam with easeoutleft

    pause 0.1

    scene black
    with fade

    n "He turns quick, stomping ahead as if he can walk the embarrassment off."

    n "The patrol ends early and peacefully."

    n "It might end permanently once tomorrow comes."

    stop music

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THE RED MOON IS HERE{/color}{/atl}{/color}"

    with fade

    pause 0.5

    scene moon6
    with fade
    pause 0.2
    scene moon7
    with fade

    stop sound

    pause 0.5

    scene black

    with out_182

    pause 0.2

    play sound "sfx/knock.wav"

    with vpunch
    pause 0.01
    with vpunch
    pause 0.01
    with vpunch
    pause 0.01

    n "You're used to Yamato's knocking pattern by now."

    MC normal "Come in."

    play sound "sfx/sliding door.mp3"

    pause 0.3

    scene house day:
        zoom 0.5

    show yam serious:
        zoom 0.3
        xanchor 0.5
        xalign 0.5
        yalign 0
        yoffset 40
        xoffset 0
    with dissolve

    pause 0.2

    stop sound
    yamato "...Yo."

    MC normal "You're up early."

    show yam ngh
    with dissolve

    yamato "Couldn't get a damn sleep."

    n "He leans against the frame, arms crossed, eyes tired. Clearly he had been thinking too much and didn't like any of it."

    yamato "That time of th' year again. Damn red moon and all."

    MC sad "Yeah..."

    show yam sad
    with dissolve

    yamato "{sc=2}Though maybe...{/sc}"

    pause(0.4)

    show yam annoyedbl
    with dissolve

    yamato "{k=1}...Tch. Whatever. Ain't like I believe in fate 'n shit.{/k}"

    MC surprised "What is it?"

    yamato "{k=2}Ya wanna be on guard with me?{/k}"

    MC happycl "{i}Of course!{/i}"

    yamato "Heh. Figures. Ya'd say yes even if I told ya we'd both die tonight."

    MC happy "Well, I'm just looking out for you, that's all."

    pause(0.3)

    yamato "..."

    show yam ngh
    with dissolve

    yamato "If nothin' happens and the red moon passes..."

    yamato "...Then maybe I'll believe ya for {i}real{/i} this time."

    MC surprised "...Yamato."

    show yam surprised
    with dissolve

    yamato "What?"

    MC smugcl "{i}That almost sounded like a compliment, you know.{/i}"

    show yam annoyedbl
    with hpunch

    yamato "{k=2}{sc=1}Wh-Shut the hell up!{/sc}{/k}"

    show yam blush
    with dissolve

    yamato "{sc=1}Ergh...{/sc}"

    yamato "I ain't good at sayin' soft shit."

    yamato "{k=1}I just mean–{/k}"

    yamato "{i}–Guess I'd be glad.{/i}{w} If ya really killed the damn thing."

    MC happy "Same with me."

    yamato "Anyway. {w=0.1}Let's not die."


    scene black

    with dissolve

    MC happy "...."

    MC yansm "...." ## expression changes

    scene moon7
    with in_212
    show yam serious:
        zoom 0.5
        xalign 0.8
        yalign 0.2
        xoffset 0
        yoffset 400


        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    play music "Love.mp3"

    n "You sit next to Yamato on the shrine roof. He's sitting really close that your knees keep bumping to each other."

    n "He's twirling an unopened bottle of sake."

    yamato "I'm keepin' it for after the red moon."

    MC normal "Can't wait."

    show yam sad
    with dissolve

    yamato "{i}...Sigh...{/i}"

    yamato "{k=1}Look... I was a dick. Ya know it, I know it.{/k}"

    yamato "Ya came back alive, did everything right. And I couldn't stop actin' like a jealous lil' shit."

    yamato "I kept barkin' at'cha 'cause I didn't know what else to do."

    MC normal "Yeah, but I did forget our promise. Understandable."

    show yam ngh
    with dissolve

    yamato "{i}I know. Not an excuse, though.{/i}"

    MC normal "...Yamato."

    show yam sad
    with dissolve

    yamato "{w=0.2}So... all I can think is–if ya die out there and I never said any of this, I'd never forgive myself."

    show yam blush
    with dissolve

    yamato "'Cause I care about ya, dumbass."

    yamato "{i}That ain't new. I just-{w=0.1}I was too busy actin' tough t' notice.{/i}"

    MC normal "...You really mean that?"

    show yam drunk2
    with dissolve

    yamato "{i}Yeah.{/i}"

    yamato "So... {w=0.2}if somethin' happens, I need ya t' remember that."

    yamato "{k=1}I... {w=0.3}didn't hate ya. Never did.{/k}"

    MC normal "..."

    MC normal "{i}I don't hate you too, Yamato.{/i}"

    yamato "That so?"

    yamato "{w=0.2}If we live... {w=0.2}maybe we figure this out."

    show yam blush
    with dissolve

    yamato "Y'know, what the hell this is between us."

    MC normal "That would be nice."

    n "None of you talk again in a while."

    n "So you wait."

    with fade

    n "And wait."

    with fade

    n "And wait."

    with fade

    n "But nothing comes out tonight."

    n "The night is almost over, you both open the bottle of sake he promised you both will drink after the red moon has passed."

    n "Yamato has already started drinking, but you hesitate on yours."

    show yam happycl
    with dissolve

    yamato "...Heh."

    yamato "So that's it, guess you really did it."

    pause(0.3)

    yamato "Guess an apology is overdue, for everything I spat at ya."

    yamato "And for actin' like I wanted ya gone."

    show yam blush
    with dissolve

    yamato "I..."

    n "Yamato fully turns towards you now, eyes darting left and right, slight tremors in his lips."

    yamato "So..."

    yamato "Wasn't sure if I was gonna say it tonight, 'cause I didn't know if we'd make it."

    n "The smell of the sake hits you stronger now."

    n "You don't know why your stomach knots in the inside."

    play sound "sfx/gag2.mp3"


    MC hurt "...Urk..."

    yamato "Oi. Ya alright?"

    n "You nod before thinking as the heat behind your eyes pulses again."

    n "You're shaking now, there's a crawling itch in the inside of your skin."

    yamato "Look, if this ain't what you want–"

    n "He waits, searching for an answer in your face. And yet you stay silent, never once shaking your head, so Yamato takes it as a yes."

    show yam kiss:
        zoom 0.5
        xalign 0.8
        yalign 0.2
        xoffset 0
        yoffset 400


        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

        ease 0.4 zoom 0.6 yoffset 450 xoffset 250


    n "He leans in, slowly, then again, still waiting for rejection. You still don't move."

    n "His breath brushes your cheek now, you're frozen in place."

    n "You feel the world tilt again faster."

    scene black

    with dissolve

    stop music fadeout 1.0

    scene cg_loop1yamato:
        zoom 0.5
    with dissolve

    stop music
    play sound "sfx/hahh.mp3"

    n "And finally, finally, softly, his lips find yours. His hands slowly holding your shoulder, {sc=5}shaking, trembling.{/sc} He doesn't know what he's doing."

    play sound "sfx/heartbeat.mp3"

    n "Right at that moment, {i}something underneath your skin wants to get out.{/i}"

    n "You kiss him back because that's what happens next. That's the part you know."

    n "{cps=14}That's what people do–{/cps}"

    n "{sc=4}Wait, what? You really think that?{/sc}"

    n "Something inside you is folding inward..."

    play sound "sfx/heartbeat.mp3"

    n "... a {i}hunger{/i} that wasn't there before."

    n "{cps=13}And Yamato chokes on you. You hear that gurgle caught in his throat.{/cps}"

    play sound "sfx/struggle.mp3"
    with flashred

    scene black

    yamato "{sc=5}–mmgh–!{/sc}"

    n "But his hands are gripping your arms now, tightly, then tighter, then he starts clawing."

    n "{w}You hold him in place."

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    play sound "sfx/sticky.mp3"

    n "{cps=11}There's a pull in your mouth–no, from your mouth–that feels wet, deep and wrong.{/cps}"

    n "{sc=4}His mouth won't leave yours... You're still kissing–why are you still kissing..!?{/sc}"

    n "You feel his body jerk once, then shake violently."

    scene flesh:
        matrixcolor BrightnessMatrix(-0.5)

        parallel:
            linear 1.2 zoom 1.02 blur 2
            linear 1.2 zoom 1.0 blur 1
            repeat

        parallel:
            linear 0.1 matrixcolor BrightnessMatrix(-1)
            linear 0.1 matrixcolor BrightnessMatrix(-0.5)
            pause 2.0
            repeat

        parallel:
            linear 0.05 xoffset -5 yoffset 3
            linear 0.05 xoffset 5 yoffset -2
            linear 0.05 xoffset 0 yoffset 0
            pause 1.5
            repeat

        parallel:
            linear 0.2 blur 6
            linear 0.4 blur 2
            pause 3.0
            repeat

    play sound "sfx/squelch.mp3"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    stop sound

    n "{i}Something is inside him now.{w} Wait, no. you're inside him–{/i}"

    play sound "sfx/yamato_eaten.wav"

    yamato "{sc=6}GHHHH–HHAKK–HHHHH!!{/sc}"

    n "{sc=5}He's screaming.{/sc}"

    n "He's... trying to scream through the kiss."

    n "{sc=5}I-Oh kami-sama–{/sc}"

    n "{cps=12}You can hear it in his throat. In your teeth...{/cps}"

    n "{cps=15}INSIDE YOUR STOMACH.{/cps}"

    yamato "{sc=6}NNNRRGHH–!–LET–LET–HHHHH–{/sc}"

    n "{i}...Let him go.{/i}"

    n "{sc=4}Please–let him go–!{/sc}"

    n "{w}Please–!"

    play sound "sfx/tearflesh.wav"

    show darken2
    with dissolve
    pause 0.3
    hide blood
    with dissolve

    n "..."

    n "T-The red moon is over now."

    n "{k=2}Yamato was–{/k}"

    n "...He is–"

    n "...He–"

    play sound "sfx/slurrp.mp3"

    n "{cps=14}Gone?{/cps}"

    n "{sc=3}You–{/sc}"

    MC yan "Yeah, he's gone now. Don't pretend you didn't see that."

    n "{w}You're supposed to be–"

    n "{sc=4}You were–{/sc}"

    MC yan "..."

    n "–the hero, right?"

    n "{i}Oh no.{/i}"

    n "{w}But just now you–Why? Why did you do that?"

    MC yansm "Eh."

    n "{cps=12}No, no, no way...{/cps}"

    n "{sc=4}...Let me out!{/sc}"

    MC yansm "Too late, you're stuck with me now until you're gone or I die."

    n "..."

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}YAMATO IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}T W O M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound


    n2 "...."

    n2 "Let's go back to the entrance... and start again."

    n2 "Still hungry."

    pause 0.5

    $ persistent.yamato_dies = True

    ## at the end of the route yamato dies

    $ persistent.loop1 = True

    if persistent.trueendingunlocked:
        $ persistent.trueendingunlocked = False
    $ MainMenu(confirm=False)()

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    $ renpy.full_restart()

    return
