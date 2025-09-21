# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    define config.layers = [ 'background', 'master', 'transient', 'screens', 'overlay', 'custom_layer' ]

define original_music_volume = None

init python:
    def decrease_music_volume(percent=0.2):
        global original_music_volume
        # Save original only if not saved yet
        if original_music_volume is None:
            original_music_volume = _preferences.volumes["music"]
        cur_vol = _preferences.volumes["music"]
        new_vol = max(0.05, cur_vol * (1.0 - percent))
        _preferences.volumes["music"] = new_vol

    def restore_music_volume():
        global original_music_volume
        if original_music_volume is not None:
            _preferences.volumes["music"] = original_music_volume
            original_music_volume = None  # Reset for next use

default persistent.player_name = None

define MC = Character("[persistent.player_name]", color="#d40000", window_left_padding=100, image="main")  # Player-named character
define n = Character(None, what_color="#fffafa") ## mc sama narrator
define n2 = Character(None, what_color="#ff5277", what_font="LibreBaskerville-Regular.ttf", what_size=34) ## yamakui narrator

define shiori = Character("Shiori", color="#c78b12")
define yamato = Character("Yamato", color="#00d44a")
define hikaru = Character("Hikaru", color="#092a43")

image flesh = "BG/Flesh.png"
image flesh2 = "BG/Flesh2.png"
image darken = "BG/darken.png"
image darken2 = "BG/darken2.png"
image blood = "BG/blood.png"

image gore = "images/gore.png"

image terumc = "images/terumc.webp"
image terumc_left = "images/terumc_left.png"
image terumc_right = "images/terumc_right.png"

image shrine2 = "BG/Shrine2.jpg"

image dojo day = "BG/Dojo.jpg"
image house day = "BG/House.jpg"
image forest day = "BG/Forest.jpg"
image shrine day = "BG/Shrine.jpg"
image village day = "BG/Village.jpg"

image dojo night = "BG/Dojo.jpg"
image house night = "BG/House.jpg"
image forest night = "BG/Forest.jpg"
image shrine night = "BG/Shrine.jpg"
image village night = "BG/Village.jpg"

image child = "NPC/npc_child.webp"
image man = "NPC/npc_man.webp"
image oldman = "NPC/npc_oldman.webp"
image oldwoman = "NPC/npc_oldwoman.webp"
image elder = "NPC/npc_villageelder.webp"
image woman = "NPC/npc_woman.webp"

image white_bg = "#FFFFFF"

# define persistent.loop1 = False ## player has cleared loop1
# define persistent.loop2 = False ## player has cleared loop2
# define persistent.loop3 = False ## player has cleared loop3
# define persistent.loop4 = False ## player has cleared loop4
# define persistent.trueending.unlocked = False ## player has picked all requirements to get the true ending

# define persistent.shiori_dies = False ## shiori dead
# define persistent.yamato_dies = False ## yamato dead
# define persistent.hikaru_dies = False ## hikaru ded

#### GHOST WILL APPEAR IN EMPTY SPACES RANDOMLY DURING LOOP2, THE GHOSTS WILL ONLY APPEAR IF THE PERSON IS DEVOURED
## GHOSTS THAT DOESN'T APPEAR IN LOOP2 WILL APPEAR IN SOMEONE'S ROUTE IN LOOP 3 (I'LL SEE WHAT WE CAN DO TO ADD TIME)
## if any persistent data has been unlocked, then that certain ghost jumpscare scene will not happen

#define persistent.loop2_shiori_ghost1 = False
#define persistent.loop2_shiori_ghost2 = False
#define persistent.loop2_shiori_ghost3 = False
#define persistent.loop2_shiori_ghost4 = False
#define persistent.loop2_shiori_ghost5 = False

#define persistent.loop2_yamato_ghost1 = False
#define persistent.loop2_yamato_ghost2 = False
#define persistent.loop2_yamato_ghost3 = False
#define persistent.loop2_yamato_ghost4 = False
#define persistent.loop2_yamato_ghost5 = False

#define persistent.loop2_hikaru_ghost1 = False
#define persistent.loop2_hikaru_ghost2 = False
#define persistent.loop2_hikaru_ghost3 = False
#define persistent.loop2_hikaru_ghost4 = False
#define persistent.loop2_hikaru_ghost5 = False

## this one below is for you to only be able to rename MC after the true end is unlocked

# define persistent.seen_true_end = False

## this is to check if this is player's first playthrough

#define persistent.first_playthrough = True
