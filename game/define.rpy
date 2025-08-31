# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[player_name]", kind=adv)  # Player-named character
define n = Character(None, kind=narrator) ## mc sama narrator
define n2 = Character(None, kind=narrator) ## yamakui narrator

define shiori = Character("Shiori", color="#FFB6C1")
define yamato = Character("Yamato", color="#FF5555")
define hikaru = Character("Hikaru", color="#88CCFF")

# define persistent.loop1 = False ## player has cleared loop1
# define persistent.loop2 = False ## player has cleared loop2
# define persistent.loop3 = False ## player has cleared loop3
# define persistent.trueending.unlocked = False ## player has picked all requirements to get the true ending

# define persistent.shiori_dies = False ## shiori dead
# define persistent.yamato_dies = False ## yamato dead
# define persistent.hikaru_dies = False ## hikaru ded

#### GHOST WILL APPEAR IN EMPTY SPACES RANDOMLY DURING LOOP2, THE GHOSTS WILL ONLY APPEAR IF THE PERSON IS DEVOURED
## GHOSTS THAT DOESN'T APPEAR IN LOOP2 WILL APPEAR IN SOMEONE'S ROUTE IN LOOP 3 (I'LL SEE WHAT WE CAN DO TO ADD TIME)

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
