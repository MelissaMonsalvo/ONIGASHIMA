### SCREEN STYLES & TRANSFORMS ############################################################
##
## Define list of screen styles & transforms.
##

############################################################
### PYTHON ###
############################################################
init python early:
    BLACK = "#000000"
    WHITE = "#ffffff"

    YELLOW = "#E1BE3E"
    RED = "#860C01"

    NOTO_JP_BOLD = "NotoSerifJP-SemiBold.ttf"
    NOTO_JP = "NotoSerifJP-VariableFont_wght.ttf"


init python:
    def save_choices(caption, chosen=None):
        """A function which will save the choice caption to the History log."""
        # Create an entry for the history list. kind="choice" so we can
        # differentiate it on the history screens.
        store.narrator.add_history(kind="choice", who=None,
            what=renpy.substitute((">>> " + caption)))


############################################################
### DEFAULTS/DEFINES ###
############################################################
## CUSTOM EXIT CONFIRM PROMPT ##
define config.quit_action = Show("exit_game")

image logo = "gui/window_icon.png"

image mm_background = ConditionSwitch(
    "current_route == 'route1'", "gui/mm_background1.webp",
    "current_route == 'route2'", "gui/mm_background2.webp"
)



image screen overlay = ConditionSwitch(
    "current_route == 'route1'", "gui/overlay/yellow_overlay.webp",
    "current_route == 'route2'", "gui/overlay/red_overlay.webp"
)


image long_btn_hover = ConditionSwitch(
    "current_route == 'route1'", Frame("gui/button/yw_btn.webp", 70, 25),
    "current_route == 'route2'", Frame("gui/button/red_btn.webp", 70, 25)
)

image long_btn_hover_no_frame = ConditionSwitch(
    "current_route == 'route1'", "gui/button/yw_btn.webp",
    "current_route == 'route2'", "gui/button/red_btn.webp"
)

image gm_btn_hover = ConditionSwitch(
    "current_route == 'route1'", Frame("gui/game menu/btn_hover_background.png", 20, 10),
    "current_route == 'route2'", Frame("gui/game menu/btn_red_hover_background.png", 20, 10)
)

image frame black = Frame("gui/frame.webp", 100, 85)

image frame gal = Transform("gui/frame.webp", xysize=(480, 302))
image frame gal hover = ConditionSwitch(
    "current_route == 'route1'", Transform("gui/frame.webp", xysize=(480, 302), matrixcolor=ColorizeMatrix(YELLOW, YELLOW)),
    "current_route == 'route2'", Transform("gui/frame.webp", xysize=(480, 302), matrixcolor=ColorizeMatrix(RED, RED))
)

image gm bg1 = "gui/menu_background.jpg"

define LONG_BTN_PADDING = (75, 30)
define GM_LONG_BTN_PADDING = (20, 30, 75, 30)

define GM_XMIN_FRAME = 400
define GM_TITLE_POS = (55, 42)
define GM_TITLE_SIZE = 80
define GM_BUTTON_SIZE = (411, 60)
define GM_SPACING = 30
define GM_VP_SIZE = (1100, 550)
define GM_VP_POS = (670, 332)
image gm navline = Transform("gui/game menu/nav_line.png", pos=(90, 215))


### SAVE/LOAD ###
image sl_thumb = Transform("frame black", xysize=(758, 476))
define SL_BTN_PADDING = (300, 111, 415, 113)



############################################################
### ENTER/EXIT ###
############################################################
transform ts_fadein():
    on show:
        alpha 0.0

        linear 1.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 1.0 alpha 0.0

transform ts_qm_fadein(dist):
    alpha 0.5
    yoffset dist

    ease 1.0 yoffset 0 alpha 1.0

transform ts_enterX(xoff, ts_speed=0.3):
    alpha 0.0
    xoffset xoff
    linear ts_speed xoffset 0 alpha 1.0


transform ts_enterY(yoff, ts_speed=0.5):
    alpha 0.3
    yoffset yoff
    linear ts_speed yoffset 0 alpha 1.0
    

transform ts_text_fade():
    alpha 0.3
    block:
        linear 1.5 alpha 1.0
        linear 1.5 alpha 0.3
        repeat

