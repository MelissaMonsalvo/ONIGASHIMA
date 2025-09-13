############# GHOST ENCOUNTERS ###########################
label ghost_yamato_1:

    # yamato jumpscares you while you are walking in the woods, like appearing to nowhere zooms in to the player pov then dissapears

    $ ghost_yamato_1 = True

    n "..."

    n "...."

    n "The forest sure is dark lately..."

    n "And what's with all these mist?"

    $ renpy.pause(1.0)

    window hide

    # Yamato ghost jumpscare
    # show yamato_ghost_attack >> appears, zoomos in to your face, then dissapears


    $ renpy.pause(0.4)

    hide yamato_ghost_attack with dissolve
    stop sound fadeout 0.5
    stop music fadeout 1.5

    window show

    n "W-What was that?"

    MC "Ha. Ha. Verry funny."

    return

label ghost_yamato_2:

    # Yamato’s ghost slowly slides from behind screen, his limbs first, then his head comes to view , unsettlign crawl onamotopeia text, squelch squelch, black liquid drips from his mouth

    $ ghost_yamato_2 = True

    n "So quiet..."

    window hide
    $ renpy.pause(1.5)

    # Limb 1 slides in
    show text "{cps=5}{size=+10}{color=#222}Squelch...{/color}{/size}" at Position(xpos=0.65, ypos=0.75) zorder 100
    $ renpy.pause(1.2)
    hide text

    # Limb 2 slides in
    show text "{cps=5}{size=+10}{color=#111}Squelch...{/color}{/size}" at Position(xpos=0.6, ypos=0.78) zorder 100
    $ renpy.pause(1.0)
    hide text

    # Head slides into view
    show text "{cps=4}{size=+12}{color=#000000}Sssqqquueellchh...{/color}{/size}" at Position(xpos=0.58, ypos=0.74) zorder 101
    $ renpy.pause(1.5)
    hide text

    n "Something is dripping from his mouth..."

    $ renpy.pause(2.0)

    ### everything dissapears

    scene black with fade
    $ renpy.pause(1.0)

    n "You don’t want to know what it tasted like."
    return

label ghost_yamato_3:

    # MC sleeps and something starts choking them
    # players must free themselves by clicking the screen several times (advancing dialogue)
    # show zoomed in to yamato ghost face but it's veyr blurry and shakey

    n "The night is young."

    n "You close your eyes."

    $ renpy.pause(1.0)

    n "..."

    $ renpy.pause(2.0)

    n "..."

    $ choke_clicks = 0

    # First moment: panic starts
    ## you open your eyes, yamato's ghost face is zoomed in and shakey

    ## first click
    play sound "sfx/gasp1.ogg"
    MC "{size=+10}{cps=6}Ghhk--{/cps}"

    ## second click
    n "{cps=7}Y-You--can’t--breathe--{/cps}"

    ## third click
    MC "Ah--Haaaa--!!!!"

    ## fourth click
    n "{cps=6}WHO ARE YOU--{/cps}"

    ## fifth click
    MC "{color=#111}{size=+12}Gghkh--!!{/size}{/color}"

    ### sicth click
    MC "MOVE--{w}MOVE--{w}Get--off--"

    ## yamato dissapears

    MC "Haa... Ha... Haa..."

    MC "Tch, persistent even in death."

    $ ghost_yamato_3 = True

    return

label ghost_yamato_4:

    # the day of the red moon and you are forced to relieve your betrayal, with Yamato about to kiss you, but in his ghostly form, everything melts, his mouth starts dripping in

    $ ghost_yamato_4 = True

    n "..."

    n "Where is it? is it a dream?"

    n "The moon's already red..."

    ## yamato's ghost sprite is right in front of you
    $ renpy.pause(1.0)

    yamato "{cps=14}LoOk... iF ThIs iSN’t wHaT yA wANt...{/cps}"

    n "He waits."

    n "He always waits."

    n "Your mouth stays closed. {w}Head tilts slightly. {w}Fingers lie frozen."

    play sound "sfx/shift_closer.ogg"

    n "He leans in..."

    n "His breath brushes your cheek., but it no longer smells like sake..."

    n "The smell of rot envelopes your nose."

    n "His lips meet yours--hesitant, tender--"

    MC "Mm."

    play sound "sfx/wet_snap.ogg"

    n "--as you return the kiss."

    n "Odd, has this happened before?"

    n "But he didn't look like this, he didn't look this..."

    n "...D E A D."

    play sound "sfx/gurgle_choke.ogg"

    yamato "{cps=8}{size=+6}--mghh--{/size}{/cps}"

    ## the screen shakes with red and black, frantic

    $ renpy.pause(0.3)

    n "His body jerks, and scrapes against yours. Nails searching for escape."

    n "His mouth widens far past what mouths should, black ooze filling your lungs."

    play sound "sfx/drip_thick.ogg"

    n "Your own throat stretches to welcome it--"

    ## RETCHING SOUND

    ## black

    n "Then darkness."

    n "Was that a dream?"

label ghost_yamato_5:

    ## code in pulsating effect or heartbeat effect, or shaking every time mc eats

    $ ghost_yamato_5 = True

    n "You’re sitting...{w} Wait."

    n "Did the floor rise up, or did your knees fold without asking?"

    ## show your home and yamato's ghost sprite

    n "Yamato has prepared a meal."

    ## yamato's ghost sprite is twitching in this whole scene

    n "Steam coils in the wrong direction, looks like it is crawling back into the food."

    yamato "{cps=12}Oi, pRettYfaCE. SiT Up.{/cps}"

    n "You move forward but your limbs are dragging as if they belong to someone else."

    ## camera zooms in to yamato's ghost

    yamato "{size=+6}{cps=7}Heh... THat’S bEttER.{/cps}{/size}"

    play sound "sfx/bowl_placed.ogg"

    yamato "{cps=10}AiN’t yA hUnGRy?{w=0.2} WhAt, fOrgOt aLL aBouT dInNeR?{w=0.3} YoU'rE wItH uS nOw, ReMeMbEr?{/cps}"

    n "He pushes the bowl forward, the sweet smell hits you and makes you nauseous."

    MC "Urk--"

    yamato "EaT."

    n "The bite scrapes your teeth. Dry, slick... {w}Grainy? {w}The texture keeps cycling, over and over, you're not even sure what it is."

    play sound "sfx/slop_squish1.ogg"
    n "SKRCHCH-SSSPPTH"

    yamato "{size=+8}{cps=6}Awwww, {w=0.1}LoOk aT yA.{/cps}{/size}"

    yamato "{cps=12}LiTTle mONsteR wiTh a GoUrMeT mOuTh, eh? {/cps}"

    play sound "sfx/gulp.ogg"

    n "You swallow as it wriggles down your throat."

    #play sound "sfx/wet_clench.ogg"
    n "GLRK—kkkkkKRRPH"

    yamato "{cps=9}eAt aNoThEr bIT.{w=0.2} CoME oN.{w=0.2} oPEn WiiiIIIiiiDe~{/cps}"

    #play sound "sfx/spoon_clink.ogg"
    $ renpy.pause(0.3)

    n "He forces another spoon down on your mouth, your jaw splits open wide."

    #play sound "sfx/slime_glop.ogg"
    n "GLRRCHHHH-SPLTK."

    n "Smething fat and wet slaps your tongue."

    yamato "{cps=8}DiD ya liKE ThaT oNE~?{w=0.2} hUH?{w=0.2} wAS iT tAsTy?{/cps}"

    #play sound "sfx/chew_guts.ogg"
    n "KRRRSHK-KHH—SPPLLT"

    n "It looks like a normal dinner... then why do you want to gag so bad?"

    yamato "{size=+10}{cps=5}SwALLoW iT.{/cps}{/size}"

    MC "GAH--"

    MC "Hahh... Hahh..."

    n "You open your eyes and your room is back to normal."

    MC "Blerghhhhh--"

    ## mc retches

    n "Your stomach is empty, but you're starving and full at the same time."


    return
