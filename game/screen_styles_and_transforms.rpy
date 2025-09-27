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

    NOTO_JP = "NotoSerifJP-VariableFont_wght.ttf"


############################################################
### DEFAULTS/DEFINES ###
############################################################
## CUSTOM EXIT CONFIRM PROMPT ##
define config.quit_action = Show("exit_game")

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

image frame black = Frame("gui/frame.webp", 100, 85)

define LONG_BTN_PADDING = (75, 30)

############################################################
### ENTER/EXIT ###
############################################################
transform ts_qm_fadein(dist):
    alpha 0.5
    yoffset dist

    ease 1.0 yoffset 0 alpha 1.0

transform ts_enterX(xoff, ts_speed=0.2):
    alpha 0.0
    xoffset xoff

    ease ts_speed xoffset 0 alpha 1.0

transform ts_enterY(yoff, ts_speed=0.2):
    alpha 0.3
    yoffset yoff

    linear ts_speed yoffset 0 alpha 1.0

