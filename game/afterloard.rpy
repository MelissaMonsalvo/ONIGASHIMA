image afterloadhik = "cgsaveblock/hikaru_idle.webp"
image afterloadshi = "cgsaveblock/shiori_idle.webp"
image afterloadyam = "cgsaveblock/yamato_idle.webp"

image afterloadhik glitched:
    glitch("afterloadhik") # reliable slicing
    pause 1.0
    glitch("afterloadhik", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat

image afterloadshi glitched:
    glitch("afterloadshi") # reliable slicing
    pause 1.0
    glitch("afterloadshi", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat

image afterloadyam glitched:
    glitch("afterloadyam") # reliable slicing
    pause 1.0
    glitch("afterloadyam", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat

init python:
    import random

label after_load:
    $ should_block_label = None
    $ block_scheduled = False

    if persistent.trueending_unlocked:
        return

    python:
        dead_labels = []

        if persistent.loop3 and loopflag < 4:
            if persistent.hikaru_dies:
                dead_labels.append("saveprohibiteded_hikaru")
            if persistent.shiori_dies:
                dead_labels.append("saveprohibiteded_shiori")
            if persistent.yamato_dies:
                dead_labels.append("saveprohibiteded_yamato")
            if dead_labels:
                should_block_label = random.choice(dead_labels)

        elif persistent.loop2 and loopflag < 3:
            if persistent.hikaru_dies:
                dead_labels.append("saveprohibiteded_hikaru")
            if persistent.shiori_dies:
                dead_labels.append("saveprohibiteded_shiori")
            if persistent.yamato_dies:
                dead_labels.append("saveprohibiteded_yamato")
            if dead_labels:
                should_block_label = random.choice(dead_labels)

        elif persistent.loop1 and loopflag < 2:
            if persistent.hikaru_dies:
                dead_labels.append("saveprohibiteded_hikaru")
            if persistent.shiori_dies:
                dead_labels.append("saveprohibiteded_shiori")
            if persistent.yamato_dies:
                dead_labels.append("saveprohibiteded_yamato")
            if dead_labels:
                should_block_label = random.choice(dead_labels)

    return

# screens.rpy
screen safe_block_redirect():
    if should_block_label and not block_scheduled:
        timer 0.01 action [
            SetVariable("block_scheduled", True),
            Function(renpy.call_in_new_context, should_block_label)
        ]
init -1 python:
    config.overlay_screens.append("safe_block_redirect")




label saveprohibiteded_hikaru:
    scene black
    play sound "sfx/jumpscare.mp3"
    show afterloadhik glitched
    with vpunch
    pause 0.1
    hide afterloadhik glitched
    show text "You can't save Hikaru." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()

label saveprohibiteded_yamato:
    scene black
    play sound "sfx/jumpscare.mp3"
    show afterloadyam glitched
    with vpunch
    pause 0.1
    hide afterloadyam glitched
    show text "You can't save Yamato." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()

label saveprohibiteded_shiori:
    scene black
    play sound "sfx/jumpscare.mp3"
    show afterloadshi glitched
    with vpunch
    pause 0.1
    hide afterloadshi glitched
    show text "You can't save Shiori." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()
