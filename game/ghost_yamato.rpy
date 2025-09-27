############# GHOST ENCOUNTERS ###########################
label ghost_yamato_1:

    # yamato jumpscares you while you are walking in the woods, like appearing to nowhere zooms in to the player pov then dissapears

    $ ghost_yamato_1 = True

    play music "sfx/forest night.wav"

    show forest day:
        zoom 0.5
    show particleFog with dissolve:
        ypos 0.4
    with fade



    n "..."

    n "...."

    n "What's with all these mist?"

    $ renpy.pause(1.0)

    window hide

    # Yamato ghost jumpscare
    # show yamato_ghost_attack >> appears, zoomos in to your face, then dissapears

    play sound "sfx/jumpscare.mp3"

    show ghost_yamato normal at c_show_31

    $ renpy.pause(1.2)

    #hide yamato_ghost_attack with dissolve
    stop sound fadeout 0.5
    stop music fadeout 1.5

    window show

    n "W-What was that?"

    MC yansm2 "Ha. Ha. Verry funny."

    return

label ghost_yamato_2:

    scene dojo day:
        zoom 0.8
        yalign 0.6
    play music "Friends.mp3"

    # Yamato’s ghost slowly slides from behind screen, his limbs first, then his head comes to view ,
    # unsettlign crawl onamotopeia text, squelch squelch, black liquid drips from his mouth

    $ ghost_yamato_2 = True

    n "So quiet..."

    window hide
    $ renpy.pause(1.5)

    # Limb 1 slides in
    play sound "sfx/splurt.mp3"
    show ghost_yamato attack at c_show_37
    with flashred
    n"{cps=5}{size=+10}Squelch...{/size}"
    $ renpy.pause(3.5)
    hide text

    # Limb 2 slides in
    play sound "sfx/splurt.mp3"
    show ghost_yamato attack at c_show_38
    with flashred
    n "{cps=5}{size=+10}Squelch...{/size}"
    $ renpy.pause(2.5)
    hide text

    # Head slides into view
    play sound "sfx/splurt.mp3"
    show ghost_yamato attack at c_show_39
    with flashred
    n "{cps=4}{size=+12}Sssqqquueellchh...{/size}"
    $ renpy.pause(1.5)
    hide text

    n "Something is dripping from his mouth..."

    $ renpy.pause(2.0)

    ### everything dissapears

    scene black with fade
    hide ghost_yamato with fade
    $ renpy.pause(1.0)

    n "You don’t want to know what it tasted like."
    return

label ghost_yamato_3:

    # MC sleeps and something starts choking them
    # players must free themselves by clicking the screen several times (advancing dialogue)
    # show zoomed in to yamato ghost face but it's veyr blurry and shakey

    play music "spooky.mp3"

    scene house night:
        zoom 0.5
    with fade

    n "The night is young."

    n "You close your eyes."

    show black_screen with fade

    $ renpy.pause(1.0)

    n "..."

    $ renpy.pause(2.0)

    n "..."

    $ choke_clicks = 0

    # First moment: panic starts
    ## you open your eyes, yamato's ghost face is zoomed in and shakey

    hide black_screen with fade

    show ghost_yamato normal at c_show_32

    ## first click
    play sound "sfx/shiori_eaten.wav"
    MC "{size=+10}{cps=6}Ghhk--{/cps}"

    ## second click
    show ghost_yamato with vpunch
    n "{cps=7}Y-You--can’t--breathe--{/cps}"

    ## third click
    MC "Ah--Haaaa--!!!!"

    ## fourth click
    show ghost_yamato with vpunch
    n "{cps=6}WHO ARE YOU--{/cps}"

    ## fifth click
    MC "{color=#111}{size=+12}Gghkh--!!{/size}{/color}"

    ### sicth click
    show ghost_yamato with vpunch
    MC "MOVE--{w}MOVE--{w}Get--off--"

    hide ghost_yamato normal with fade

    ## yamato dissapears

    MC shocked2 "Haa... {w}Ha... {w}Haa..."

    stop sound

    MC yan2 "Tch, persistent even in death."

    $ ghost_yamato_3 = True

    return

label ghost_yamato_4:

    # the day of the red moon and you are forced to relieve your betrayal,
    # with Yamato about to kiss you, but in his ghostly form, everything melts, his mouth starts dripping in

    play music "noinomai.mp3"

    $ ghost_yamato_4 = True

    scene village night:
        zoom 0.5
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    with fade

    n "..."

    n "Where is it? is it a dream?"

    n "The moon's already red..."

    ## yamato's ghost sprite is right in front of you
    show ghost_yamato normal at c_show_34:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))
    $ renpy.pause(1.0)

    yamato "{cps=14}LoOk... iF ThIs iSN’t wHaT yA wANt...{/cps}"

    n "He waits."

    n "Always, always."



    show ghost_yamato attack at c_show_35:
        matrixcolor TintMatrix(Color(rgb=(0.9, 0.12, 0.12), alpha=0.8))

    n "Then he leans in..."

    n "His breath brushes your cheek., but it no longer smells like sake..."

    n "...but rotting flesh."

    n "His lips meet yours. Hesitant, tender..."

    n "...just like before."


    play sound "sfx/swallow.mp3"

    n "Odd, has this happened before?"

    n "But he didn't look like this, he didn't look this..."

    n "{w=0.1}...D E A D."

    play sound "sfx/mmph.mp3"
    with sshake

    yamato "{cps=8}{size=+6}--mghh--{/size}{/cps}"

    with hpunch

    ## the screen shakes with red and black, frantic

    $ renpy.pause(0.3)

    with vpunch

    n "His mouth widens far past what mouths should, black ooze filling your lungs."



    n "Your own throat stretches to welcome it--"

    ## RETCHING SOUND

    play sound "sfx/gag2.mp3"

    show black_screen with sshake
    ## black

    n "Then darkness."

    n "Was that a dream?"

    return

label ghost_yamato_5:

    ## code in pulsating effect or heartbeat effect, or shaking every time mc eats

    $ ghost_yamato_5 = True

    play music "spooky.mp3"

    scene house night:
        zoom 0.5
    with fade
    show darken2

    n "You’re sitting...{w} Wait."

    ## show your home and yamato's ghost sprite

    show ghost_yamato normal behind darken2 at c_show_40
    pause 1.0
    show ghost_yamato normal at c_show_41

    n "Yamato has prepared a meal."

    ## yamato's ghost sprite is twitching in this whole scene

    n "Steam coils in the wrong direction, looks like it is crawling back into the food."

    yamato "{cps=12}Oi, pRettYfaCE. SiT Up.{/cps}"

    n "You move forward but your limbs are dragging as if they belong to someone else."

    ## camera zooms in to yamato's ghost

    show ghost_yamato normal at c_show_42
    pause 0.5
    show ghost_yamato normal at c_show_41
    yamato "{size=+6}{cps=7}Heh... THat’S bEttER.{/cps}{/size}"


    yamato "{cps=10}AiN’t yA hUnGRy?{w=0.2} WhAt, fOrgOt aLL aBouT dInNeR?{w=0.3} YoU'rE wItH uS nOw, ReMeMbEr?{/cps}"

    n "He pushes the bowl forward, the sweet smell hits you and makes you nauseous."

    MC "Urk--"

    yamato "EaT."

    n "The bite scrapes your teeth. Dry, slick... {w}Grainy? {w}The texture keeps cycling, over and over, you're not even sure what it is."

    play sound "sfx/slurrp.mp3"
    with flashred
    n "SKRCHCH-SSSPPTH"

    yamato "{size=+8}{cps=6}Awwww, {w=0.1}LoOk aT yA.{/cps}{/size}"

    yamato "{cps=12}LiTTle mONsteR wiTh a GoUrMeT mOuTh, eh? {/cps}"

    play sound "sfx/splurt.mp3"
    with flashred

    n "You swallow as it wriggles down your throat."

    play sound "sfx/tearflesh.wav"
    with flashred
    n "GLRK—kkkkkKRRPH"

    yamato "{cps=9}eAt aNoThEr bIT.{w=0.2} CoME oN.{w=0.2} oPEn WiiiIIIiiiDe~{/cps}"

    play sound "sfx/splurt.mp3"
    with flashred
    $ renpy.pause(0.3)

    n "He forces another spoon down on your mouth, your jaw splits open wide."

    play sound "sfx/stretch.mp3"
    with flashred
    n "GLRRCHHHH-SPLTK."

    n "Smething fat and wet slaps your tongue."

    yamato "{cps=8}DiD ya liKE ThaT oNE~?{w=0.2} hUH?{w=0.2} wAS iT tAsTy?{/cps}"

    play sound "sfx/tearflesh.wav"
    with flashred
    n "KRRRSHK-KHH—SPPLLT"

    n "It looks like a normal dinner... then why do you want to gag so bad?"

    yamato "{size=+10}{cps=5}SwALLoW iT.{/cps}{/size}"

    MC shocked2 "GAH--"

    MC "Hahh... {w=0.2}Hahh..."
    hide ghost_yamato normal with fade
    hide darken2
    n "You open your eyes and your room is back to normal."

    stop music
    play sound "sfx/gag1.mp3"

    MC "Blerghhhhh--"

    ## mc retches

    n "Your stomach is empty, but you're starving and full at the same time."


    return
