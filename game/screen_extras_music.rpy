### MUSIC SCREEN ############################################################
##
##

############################################################
### PYTHON ###
############################################################


init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("Main Menu.mp3", always_unlocked=True)
    mr.add("MainMenu2.mp3", always_unlocked=True)
    mr.add("Ambient.mp3")
    mr.add("Battora.mp3")
    mr.add("Blood Ritual.mp3")
    mr.add("Dark.mp3")
    mr.add("Doubt.mp3")
    mr.add("Ending.mp3")
    mr.add("Final Battle.mp3")
    mr.add("Goodbye.mp3")
    mr.add("Hikaru.mp3")
    mr.add("Love.mp3")
    mr.add("Hope.mp3")
    mr.add("Hope2.mp3")
    mr.add("Idle.mp3")
    mr.add("Narukami.mp3")
    mr.add("Night.mp3")
    mr.add("noinomai.mp3")
    mr.add("Shiori.mp3")
    mr.add("Somber.mp3")
    mr.add("spooky.mp3")
    mr.add("Tense.mp3")
    mr.add("Yamato.mp3")


    MUSIC_DICT = {
        "Main Menu": "Main Menu.mp3",
        "Main Menu 2": "MainMenu2.mp3",
        "Ambient": "Ambient.mp3",
        "Battora": "Battora.mp3",
        "Blood Ritual": "Blood Ritual.mp3",
        "Dark": "Dark.mp3",
        "Doubt": "Doubt.mp3",
        "Ending": "Ending.mp3",
        "Final Battle": "Final Battle.mp3",
        "Goodbye": "Goodbye.mp3",
        "Hikaru": "Hikaru.mp3",
        "Love": "Love.mp3",
        "Hope": "Hope.mp3",
        "Hope 2": "Hope2.mp3",
        "Idle": "Idle.mp3",
        "Narukami": "Narukami.mp3",
        "Night": "Night.mp3",
        "Noinomai": "noinomai.mp3",
        "Shiori": "Shiori.mp3",
        "Somber": "Somber.mp3",
        "Spooky": "spooky.mp3",
        "Tense": "Tense.mp3",
        "Yamato": "Yamato.mp3"
    }


############################################################
### MUSIC SCREEN ###
############################################################
screen extras_music(selected_song):
    style_prefix "music"
    if not persistent.loop1:
        $ tt_color = BLACK
    else:
        $ tt_color = WHITE
        

    $ slot = 1
    for track_name, track in MUSIC_DICT.items(): 
        button:
            frame:
                if mr.is_unlocked(track):
                        
                    text "Track #{}  -  {}".format(slot, track_name):
                        xalign 0.0
                        selected_color tt_color
                        hover_color tt_color

                    if renpy.music.get_playing() == track:
                        text "Playing...":
                            xalign 1.0
                            selected_color tt_color
                            hover_color tt_color
                else:
                    text "Track #{}  -  ???".format(slot):
                        xalign 0.0
                        selected_color tt_color
                        hover_color tt_color

            action SetScreenVariable("selected_song", track)

        $ slot += 1




                

############################################################
### MUSIC STYLES ###
############################################################
style music_button:
    xysize (1084, 121)

    background None
    hover_background "long_btn_hover_no_frame"
    selected_background "long_btn_hover_no_frame"


style music_frame:
    background None
    xsize 860
    ysize 50
    align (0.5, 0.5)

style music_text:
    size 30
    color BLACK
    font NOTO_JP

