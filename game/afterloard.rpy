label after_load:

    if not persistent.hikaru_dies and hikaru_alive:
        $ load_redirect = "saveprohibiteded_hikaru"
        $ just_loaded = True

    elif not persistent.yamato_dies and yamato_alive:
        $ load_redirect = "saveprohibiteded_yamato"
        $ just_loaded = True

    elif not persistent.shiori_dies and shiori_alive:
        $ load_redirect = "saveprohibiteded_shiori"
        $ just_loaded = True

    return

label saveprohibiteded_hikaru:
    scene black
    show text "You can't save Hikaru eyyyy." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()

label saveprohibiteded_yamato:
    scene black
    show text "You can't save Yamato booo." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()

label saveprohibiteded_shiori:
    scene black
    show text "You can't save Shiori nyaaa~." at truecenter
    with dissolve
    pause 3
    $ renpy.full_restart()
