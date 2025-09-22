label loop2_hikaru:

    play music "Battora.mp3"

    scene house night:
        zoom 0.5

    show hik normal:
        zoom 0.24
        xalign 0.4
        xoffset 120
        yoffset 0
        xzoom 1
        yzoom 1.0

        matrixcolor BrightnessMatrix(-0.8) * TintMatrix("#111111")

        ease 0.5 matrixcolor None zoom 0.3
    pause 0.1
    with sshake

    play music "Battora.mp3"

    n "You wake up to see hikaru already barging in into your house."

    hikaru "I don’t care if it's forbidden{w=0.2} or if it kills me..."

    hikaru "You-{w=0.2} you took [persistent.player_name] from me."

    hikaru "{glitch=8}Yamakui...!{/glitch}"

    with sshake

    n "They’re sweating,{w=0.2} hands shaking,{w=0.3} smearing salt across the floor in thick,{w=0.2} frantic lines."

    show magic_circle behind hik:
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        zoom 1.0
        xoffset 0
        yoffset 0

        # Endless rotation
        linear 2.5 rotate 360
        repeat

    n "It's... {w=0.1}a binding circle?"

    n "How does Hikaru know something like this?"

    n2 "This again."

    n2 "It's {i}useless.{/i}"

    hikaru "{sc=5}Y-you stole [player_name]'s face, you monster...{/sc}"

    hikaru "You dare use {i}that mouth{/i} to kiss me!"

    n "Wait--"

    n "{sc=6}Wait--{w=0.2} Hikaru--{/sc}"

    n "Please--{w=0.3} don’t do this--"

    n2 "{b}HeheHAHAHAHEHhehe.{w=0.2} Let them try.{/b}"

    n "Hikaru,{w=0.2} it’s me--{w=0.2} it's really me in here--"

    n "I’m still here!{w=0.2} I’m--"

    n2 "{b}{i}D E A D.{/i}{/b}"

    n "{color=#ff002e}DON’T!{/color}"

    play sound "sfx/pulse.ogg"

    n "You feel the ground vibrate,{w=0.2} no,{w=0.3} wait,{w=0.2} it's your bones that are vibrating."

    hikaru "Why are you still smiling,{w=0.2} damn you!?"

    MC "You’re cute when you’re desperate."

    n "{i}No, stop this madness at once! Let me speak--{/i}"

    n "Hikaru,{w=0.2} I love you.{w=0.3} I’ve always--"

    n "{cps=15}...Run.{/cps}"

    MC "Why? As long as it's me,{w=0.2} you don't mind... Do you, Hikaru?"

    hikaru "{sc=7}SHUT UP!{/sc}"

    play sound "sfx/salt_flare.ogg"

    n "The circle glows.{w=0.3} You feel it {sc=5}*cutting*{/sc} into you."

    n2 "{b}{i}AhhhHH--{w=0.2} hhghghGHH--{w=0.3} YES--{/i}{/b}"

    hikaru "{cps=13}Give me back [player_name]!{/cps}"

    MC "What do you mean?{w=0.2} I'm [player_name]."

    n "With one simple swoosh of your hand,{w=0.2} the whole binding circle {glitch=8}shatters{/glitch}."

    hikaru "{i}No--{/i}"

    hikaru "{cps=14}No, please--{/cps}"

    hikaru "{sc=6}I did everything right...{/sc}"

    n2 "{b}Is that all?{/b}"

    MC "Time to say goodbye, Hikaru~"

    n "{color=#ff002e}No--{/color}"

    n2 "{b}They smell ripe.{/b}"

    n "Please...{w=0.2} don’t touch them."

    hikaru "{sc=7}Noooo...!{/sc}"


    ## hikaru's sprites stumbles back and then runs

    ## shaking image of hikaru running frantically to the village

    hikaru "{sc=8}SOMEONE--PLEASE--!!{/sc}"

    play sound "sfx/village_murmur.ogg"

    "Man" "...Hikaru?"

    "Woman" "What’s all the noise?"

    hikaru "{glitch=12}It’s Yamakui--IT’S STILL HERE--{/glitch}"

    hikaru "It’s wearing [player_name]’s face--{w=0.2} YOU HAVE TO LISTEN!"

    "Man" "...What?"

    hikaru "{sc=7}WE HAVE TO KILL THAT THING--THAT THING WEARING [player_name]!{/sc}"

    hikaru "Please...{w=0.3} please, believe me--"

    n2 "{b}Foolish.{w=0.2} Foolish.{w=0.2} FOOLISH.{/b}"

    "Man" "How dare you accuse [persistent.player_name] like that, Hikaru!"

    "Woman" "They saved the village! They brought the armor back!"

    "Man" "Unlike your father, who ran into the mist and never returned!"

    hikaru "{color=#ff002e}NO!{/color}"

    hikaru "My father wasn’t a coward--{w=0.2} HE WAS TRYING TO FIND A WAY OUT--{w=0.2} YOU KNOW THAT!"

    n2 "{b}No one listens to the traitor’s child.{/b}"

    n "Hikaru's voice {sc=6}starts to crack{/sc} from screaming.{w=0.2} Their fists clench until the nails cut skin and bleeds..."

    n2 "{b}There it is...{w=0.2} Your blood.{/b}"

    n2 "{b}I can't wait...{/b}"

    hikaru "You're all going to {glitch=10}DIE!{/glitch}"

    hikaru "{sc=7}DON’T YOU UNDERSTAND?!{w=0.3} IT’S IN [player_name]! IT’S WEARING [player_name]'S SKIN!{/sc}"

    n2 "{b}They’ll scream so well.{w=0.3} One by one.{w=0.2} One by--{/b}"

    hikaru "I’M TRYING TO SAVE YOU!"

    play sound "sfx/village_stepback.ogg"
    $ renpy.pause(0.5)

    n "The man {sc=5}shoves{/sc} Hikaru back like swatting a mad dog."

    "Man" "Enough!"

    "Man" "Look at yourself, Hikaru!{w=0.2} You’ve lost your mind!"

    "Woman" "You should be ashamed, screaming like this in front of the children!"

    n "{i}No...{/i}"

    MC "Sorry for the trouble...{w=0.2} Hikaru’s not well."

    n "{color=#ff002e}No!{/color}"

    MC "Hikaru's been talking nonsense for days,{w=0.2} barely sleeping...{w=0.2} Seeing things in the woods, you know."

    n "{glitch=8}Hikaru's not wrong!{/glitch}"

    MC "I tried to help."

    MC "But...{w=0.2} I think Hikaru's gone mad. Just like Karasuma-san."

    n "{cps=13}Hikaru turns to you, completely betrayed and broken.{/cps}"

    n "I'm sorry...{w=0.3} Hikaru..."

    hikaru "...You..."

    hikaru "{sc=6}You LIAR--{/sc}"

    MC "Go home, Hikaru.{w=0.3} Before you hurt someone."


    play sound "sfx/fabric_grab.ogg"

    man "{sc=6}Let's go before you make a ruckus again!{/sc}"

    n "The man grabs Hikaru’s arm roughly{w=0.2} and pulls Hikaru away,{w=0.2} too stunned to struggle against him."

    hikaru "{i}...No one’s listening...{/i}"

    hikaru "{cps=14}...You all deserve what’s coming.{/cps}"

    hikaru "You all--"

    hikaru "{glitch=9}You all deserve to be devoured...{/glitch}"

    centered "{color=#9a0000}RED MOON{/color}"

    n "{sc=5}The red moon is coming...{/sc}"

    n "It's here...{w=0.3}"

    n "{glitch=7}And so are you--{/glitch}"

    hikaru "{sc=6}Hahh--hahh--hahhh--{/sc}"

    n2 "{b}I can hear it.{/b}"

    n2 "{b}Step.{w=0.2} Step.{w=0.2} Step.{w=0.3} FLEE.{/b}"

    hikaru "No--no--please--"

    n2 "{b}{i}Delicious.{/i}{/b}"

    n "{size=*1.2}{sc=9}THUMP.{/sc} {size=*1.0}THUMP.{/size} {size=*1.1}THUMP.{/size}"

    n "Hikaru's heartbeat now turns into a drumbeat of panic,{w=0.2} echoing in your ears."

    n2 "{b}Run, little thing.{/b}"

    n2 "{b}I’ll follow the footprints made in your blood.{/b}"

    stop sound fadeout 1.0

    hikaru "...You!"

    ## shing sai draw

    n "Hikaru draws their sai now,{w=0.2} ready to fight to the death{w=0.3} and bring you down with them."

    n2 "{b}Like that will help.{/b}"

    hikaru "I don’t care if I die."

    hikaru "{sc=8}I’ll drag you down screaming if it’s the last thing I do!{/sc}"

    mc "Why don't you try...?"

    hikaru "Kami-sama should’ve struck you down--"

    hikaru "But they didn’t.{w=0.2} Just like the rest of them--those cowards back in the village."

    hikaru "They turned their backs on me--"

    hikaru "Let you walk free--"

    hikaru "{color=#ff002e}They left me ALONE--!{/color}"

    hikaru "{sc=8}A L O N E--!!{/sc}"

    hikaru "{glitch=12}WHILE YOU ATE MY LOVER!!{/glitch}"

    n "Hikaru--{w=0.2} please--"

    n "{sc=6}RUN--{/sc}"

    n "{sc=7}RUN BEFORE I CAN’T STOP THIS--{/sc}"

    n "{cps=15}I’m still here--inside--I still love you--{/cps}"

    n2 "{b}Shut up.{/b}"

    n2 "{b}I’m hungry.{/b}"

    mc "You were always the softest one."

    hikaru "You want me?"

    hikaru "{sc=7}Come and TRY!!!{/sc}"

    n2 "{b}{i}Y e s .{/i}{/b}"

    n2 "{b}Let’s dance with your bones,{w=0.2} little ninja.{/b}"

    n "{color=#ff002e}STOP--{/color}"

    n "Metal {sc=6}screams{/sc} against clawed hands."

    n "Their arm twists back{w=0.2} and you catch it easily,{w=0.2} snaps it."

    ## crack

    hikaru "{sc=7}Aahh--ghhk--{/sc}"

    n "They stumble unto the ground,{w=0.2} their sai is gone.{w=0.3} One arm lies limp beside them..."

    n "But their other hand {sc=4}claws{/sc} the ground, still trying to reach you."

    n "{cps=13}You're over them now.{/cps}"

    n2 "{b}Easy prey.{/b}"

    show hikaru broken at center with dissolve
    play sound "sfx/heartbeat_slow.ogg"

    hikaru "Ngh...{w=0.3} ha...{w=0.3} hah..."

    hikaru "{i}You’re... still inside, right?{/i}"

    hikaru "{cps=14}I know you're watching.{/cps}"

    hikaru "[player_name]..."

    n "{color=#ff002e}Hikaru... No...{/color}"

    n2 "{b}I’m starving.{/b}"

    n "{sc=8}PLEASE--{/sc}"

    n2 "{b}I’m going to tear them open.{/b}"

    ## erratic mouse

    menu:
        "Save them save them save them save them":
            n2 "{b}No.{/b}"

        "Eat":
            n2 "{b}Yes.{/b}"

    play sound "sfx/tackle.ogg"
    play sound "sfx/struggle_cloth.ogg"

    n2 "{b}Hold still.{/b}"

    hikaru "{i}I’ll see them again soon...{/i}"

    hikaru "Under the tree..."

    hikaru "When...{w=0.3} the sakura...{w=0.2} blooms--"

    n "{sc=8}HIKARU--!!{/sc}"

    n2 "{b}Open wide.{/b}"

    play sound "sfx/mouth_open.ogg"
    $ renpy.pause(0.5)

    ## Eating onomatopoeia (non-graphic)
    play sound "sfx/eat_slurp1.ogg"
    n "{cps=10}Sllk... ghhk... nrrrh...{/cps}"

    play sound "sfx/eat_crunch.ogg"
    n "{sc=6}Gkkk--chk--krRRSHK.{/sc}"

    play sound "sfx/gulp.ogg"
    n "Ghhhlk... glkk...{w=0.2} *gulp*."

    play sound "sfx/eat_slurp2.ogg"
    n "{cps=11}Nghh--skrrk--ssLLLK... ah...{/cps}"

    n2 "{b}...It's done.{/b}"

    n "..."

    n "They’re gone."

    n "{i}...no.{/i}"

    pause(1.0)

    n "...No."

    n "{sc=5}No no no no--{/sc}"

    n "{glitch=10}What did you--{/glitch}"

    n "{sc=7}WHAT DID YOU DO--{/sc}"

    n "{glitch=11}HIKARU WAS--{/glitch}"

    pause(1.0)

    n "{cps=15}Hikaru was my--{/cps}"

    n2 "{b}Ah, you remember now that Hikaru's inside us?{w=0.2} About who you are?{/b}"

    n "{sc=8}I DIDN'T WANT THIS!{/sc}"

    n "{size=+6}{color=#ff002e}YOU WEREN’T SUPPOSED TO KILL HIKARU!{/color}"

    n "{w=0.3}.{w=0.3}.{w=0.3}You weren't supposed to...{w=0.3} I was trying to..."

    n "I thought if I just..."

    pause(0.5)

    n "...forgot about Hikaru, then you won't eat--"

    pause(1.0)

    n2 "Too late."

    scene black

    pause 0.3

    play sound "sfx/day change.mp3"

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}HIKARU IS DEVOURED{/size}{/font}{/color}{/atl}{/color}"

    pause 0.2

    centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}{font=LibreBaskerville-Regular.ttf}{size=40}O N E M O R E T O G O{/size}{/font}{/color}{/atl}{/color}"

    with fade

    pause 0.5

    stop sound

    $ persistent.hikaru_dies = True

    $ persistent.loop2 = True

    return
