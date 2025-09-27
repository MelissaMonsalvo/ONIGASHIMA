# ===========================
# AFTER LOAD HOOK
# ===========================
label after_load:

    # Allow everything if true ending seen
    if persistent.seen_true_end:
        return

    $ should_block_label = None
    $ block_scheduled = False

    if persistent.shiori_dies and shiori_alive:
        $ should_block_label = "saveprohibiteded_shiori"
    elif persistent.yamato_dies and yamato_alive:
        $ should_block_label = "saveprohibiteded_yamato"
    elif persistent.hikaru_dies and hikaru_alive:
        $ should_block_label = "saveprohibiteded_hikaru"

    return


# ===========================
# AUTO SCREEN TO REDIRECT AFTER LOAD
# ===========================
screen safe_block_redirect():
    if should_block_label and not block_scheduled:
        timer 0.01 action [
            SetVariable("block_scheduled", True),
            Function(renpy.call_in_new_context, should_block_label)
        ]

# Make the screen always active
init -1 python:
    config.overlay_screens.append("safe_block_redirect")
label saveprohibiteded_hikaru:
    scene black
    show text "You can't save Hikaru." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()

label saveprohibiteded_yamato:
    scene black
    show text "You can't save Yamato." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()

label saveprohibiteded_shiori:
    scene black
    show text "You can't save Shiori." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()
