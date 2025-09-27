init python:
    import random
    import time

    BASE_X = 960
    BASE_Y = 540
    JITTER_RANGE = 42
    JITTER_INTERVAL = 0.07

    mouse_jittering = False

    def start_mouse_jitter():
        global mouse_jittering
        mouse_jittering = True
        renpy.invoke_in_thread(jitter_mouse)

    def stop_mouse_jitter():
        global mouse_jittering
        mouse_jittering = False

    def jitter_mouse():
        while mouse_jittering:
            dx = random.randint(-JITTER_RANGE, JITTER_RANGE)
            dy = random.randint(-JITTER_RANGE, JITTER_RANGE)
            renpy.set_mouse_pos(BASE_X + dx, BASE_Y + dy)
            time.sleep(JITTER_INTERVAL)




init:


    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # centreal position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

init:
        $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
        $ timeleft = 180

init:
    image haze_effect = "images/blur.png"

    transform haze_transform:
        parallel:
            linear 1.5 xoffset -4 yoffset 4 zoom 1.01
            linear 1.5 xoffset 4 yoffset -4 zoom 0.99
            repeat
        parallel:
            linear 1.5 alpha 0.25 blur 3
            linear 1.5 alpha 0.35 blur 5
            linear 1.5 alpha 0.25 blur 3
            repeat

    image magic_circle = "images/magic_circle.png"
    image magic_circle_red = "images/magic_circle_red.png"
transform spin_forever:
    rotate 0
    linear 2.5 rotate 360
    repeat
screen magic_circle_spin:
    add "magic_circle" at spin_forever anchor (0.5, 0.5) pos (0.5, 0.5)

init python:

    haze_active = False

    def drunk_haze_overlay():
        if haze_active:
            renpy.show("haze_effect", at_list=[haze_transform], layer="overlay")
        else:
            renpy.hide("haze_effect", layer="overlay")

    config.overlay_functions.append(drunk_haze_overlay)


screen multi_click_button(total_clicks=10, next_label="after_many_clicks"):
    default current_click = 0
    $ clicks_left = total_clicks - current_click

    # Clickable area covers entire screen
    button:
        action [
            SetScreenVariable("current_click", current_click + 1),
            Function(renpy.transition, sshake),
            If(current_click + 1 >= total_clicks, Jump(next_label), NullAction())
        ]
        xysize (config.screen_width, config.screen_height)
        style "transparent_button"

        text ">> S T RU G G L E !!!! <<" xalign 0.5 yalign 0.5 size 40 color "#ff2222" outlines [(2, "#0008", 0, 0)]

style transparent_button is default
style transparent_button:
    background None
    foreground None
    hover_background None
    insensitive_background None
    padding (0, 0)

screen struggle_qte_end:
    timer 0.1 action [Hide("struggle_qte"), Return()]

transform bg_run_shake:
    zoom 0.5

    linear 0.07 xoffset -24 yoffset 7 zoom 0.505
    linear 0.08 xoffset 18 yoffset -11 zoom 0.52
    linear 0.07 xoffset -13 yoffset 5 zoom 0.5
    linear 0.06 xoffset 10 yoffset -9 zoom 0.507
    linear 0.09 xoffset -20 yoffset 2 zoom 0.514
    pause 0.05
    repeat

transform walkinn:
        linear 0.3 xoffset 34 yoffset 12
        linear 0.3 xoffset -28 yoffset 0
        linear 0.3 xoffset 21 yoffset 11
        linear 0.3 xoffset 0 yoffset 0
        repeat
screen drunk_haze():
    add "haze_overlay" at haze_loop:
        xalign 0.5
        yalign 0.5
        xysize (config.screen_width, config.screen_height)
        alpha 0.3
        blur 4

transform haze_loop:
    parallel:
        linear 1.5 xoffset -4 yoffset 4 zoom 1.01
        linear 1.5 xoffset 4 yoffset -4 zoom 0.99
        repeat
    parallel:
        linear 1.5 alpha 0.25 blur 3
        linear 1.5 alpha 0.35 blur 5
        linear 1.5 alpha 0.25 blur 3
        repeat
transform camera_tilt:
    rotate 0
    easein 0.1 rotate 5   # quick tilt right
    easeout 0.15 rotate -4  # swing past center
    easein 0.1 rotate 2   # wobble correction
    easeout 0.15 rotate 0 # settle back to normal

###### POSITIONS ######

transform midleft:
    xalign 0.25
transform midleft2:
    xalign 0.36
transform left2:
    xalign -0.1
transform left:
    xalign 0.03
transform midright:
    xalign 0.75

transform midright2:
    xalign 0.6

### colors ###

transform blacku:
    matrixcolor (BrightnessMatrix(-0.5) * TintMatrix("#1A1A1A"))

define flashred = Fade(0.1, 0.0, 0.5, color="#ff002b")

screen horror_forced_menu(items):
    timer 0.1 repeat True action MouseMove(960, 440)

    vbox:
        spacing 40
        xalign 0.5
        yalign 0.5

        for idx, (caption, action, chosen) in enumerate(items):

            button:
                action action
                xalign 0.5
                xsize 1301
                ysize 426
                background None

                hovered SetVariable("hovered_choice", idx)
                unhovered SetVariable("hovered_choice", -1)

                fixed:
                    xysize (1301, 426)

                    # Your animation code as before:
                    if idx == 0:
                        add (
                            "top_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "top_half_idle_r1" if current_route == "route1" else
                            "top_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "top_half_idle_r2"
                        ) xpos 0 ypos 0 at button_top_anim
                    else:
                        add (
                            "bottom_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "bottom_half_idle_r1" if current_route == "route1" else
                            "bottom_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "bottom_half_idle_r2"
                        ) xpos 0 ypos 0 at button_bottom_anim

                    if idx == 0:
                        add "mask_top" xpos 0 ypos 0 at mask_top_anim
                    else:
                        add "mask_bottom" xpos 0 ypos 0 at mask_bottom_anim

                    text caption style "choice_text" xalign 0.5 yalign 0.6 at choice_text_fadein

transform horror_jitter:
    # Use renpy.random.randint for ATL expressions!
    linear 0.05 xoffset renpy.random.randint(-22, 22) yoffset renpy.random.randint(-16, 16)
    linear 0.05 xoffset renpy.random.randint(-10, 10) yoffset renpy.random.randint(-7, 7)
    linear 0.05 xoffset renpy.random.randint(-18, 18) yoffset renpy.random.randint(-11, 11)
    linear 0.05 xoffset renpy.random.randint(-6, 6) yoffset renpy.random.randint(-6, 6)
    repeat


transform menu_blur_dark:
    blur 8     # change blur strength here; try 12 for heavier blur
    alpha 0.7  # 0.7 = very dark, 0.5 = more transparent

screen horror_forced_menu_shaking(items):

    # Dark blurry overlay behind menu
    add Solid("#0008") xysize (1920, 1080) at menu_blur_dark

    vbox:
        spacing 40
        xalign 0.5
        yalign 0.5

        for idx, (caption, action, chosen) in enumerate(items):

            button:
                action action
                xalign 0.5
                xsize 1301
                ysize 426
                background None
                at horror_jitter    # <<<<<<<<<<<< jitter the button!
                hovered SetVariable("hovered_choice", idx)
                unhovered SetVariable("hovered_choice", -1)

                fixed:
                    xysize (1301, 426)
                    # Your animation code as before...
                    # (unchanged)
                    if idx == 0:
                        add (
                            "top_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "top_half_idle_r1" if current_route == "route1" else
                            "top_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "top_half_idle_r2"
                        ) xpos 0 ypos 0 at button_top_anim
                    else:
                        add (
                            "bottom_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "bottom_half_idle_r1" if current_route == "route1" else
                            "bottom_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "bottom_half_idle_r2"
                        ) xpos 0 ypos 0 at button_bottom_anim

                    if idx == 0:
                        add "mask_top" xpos 0 ypos 0 at mask_top_anim
                    else:
                        add "mask_bottom" xpos 0 ypos 0 at mask_bottom_anim

                    text caption style "choice_text" xalign 0.5 yalign 0.6 at choice_text_fadein

screen horror_forced_menu_jitter(items):
    on "show" action Function(start_mouse_jitter)
    on "hide" action Function(stop_mouse_jitter)

    vbox:
        spacing 40
        xalign 0.5
        yalign 0.5

        for idx, (caption, action, chosen) in enumerate(items):

            button:
                action action
                xalign 0.5
                xsize 1301
                ysize 426
                background None

                hovered SetVariable("hovered_choice", idx)
                unhovered SetVariable("hovered_choice", -1)

                fixed:
                    xysize (1301, 426)

                    # Your animation code as before:
                    if idx == 0:
                        add (
                            "top_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "top_half_idle_r1" if current_route == "route1" else
                            "top_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "top_half_idle_r2"
                        ) xpos 0 ypos 0 at button_top_anim
                    else:
                        add (
                            "bottom_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "bottom_half_idle_r1" if current_route == "route1" else
                            "bottom_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "bottom_half_idle_r2"
                        ) xpos 0 ypos 0 at button_bottom_anim

                    if idx == 0:
                        add "mask_top" xpos 0 ypos 0 at mask_top_anim
                    else:
                        add "mask_bottom" xpos 0 ypos 0 at mask_bottom_anim

                    text caption style "choice_text" xalign 0.5 yalign 0.6 at choice_text_fadein

screen black_flicker:
    zorder 1000
    add Solid("#000") at horror_flicker

transform horror_flicker:
    alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.05 alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.05 alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.05 alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.05 alpha 0.0
    alpha 0.0


screen horror_forced_menu_two(items):
    timer 0.1 repeat True action MouseMove(960, 880)

    vbox:
        spacing 40
        xalign 0.5
        yalign 0.5

        for idx, (caption, action, chosen) in enumerate(items):

            button:
                action action
                xalign 0.5
                xsize 1301
                ysize 426
                background None

                hovered SetVariable("hovered_choice", idx)
                unhovered SetVariable("hovered_choice", -1)

                fixed:
                    xysize (1301, 426)

                    # Your animation code as before:
                    if idx == 0:
                        add (
                            "top_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "top_half_idle_r1" if current_route == "route1" else
                            "top_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "top_half_idle_r2"
                        ) xpos 0 ypos 0 at button_top_anim
                    else:
                        add (
                            "bottom_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "bottom_half_idle_r1" if current_route == "route1" else
                            "bottom_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "bottom_half_idle_r2"
                        ) xpos 0 ypos 0 at button_bottom_anim

                    if idx == 0:
                        add "mask_top" xpos 0 ypos 0 at mask_top_anim
                    else:
                        add "mask_bottom" xpos 0 ypos 0 at mask_bottom_anim

                    text caption style "choice_text" xalign 0.5 yalign 0.6 at choice_text_fadein

## images

image frame2 = "images/frame.png"
image matcha = "images/matcha.png"
image wine = "images/wine.png"
image charm = "images/charm.png"
image charm2 = "images/charm2.png"
image bento = "images/bento.png"
image bone = "images/bone.png"

image moon1 = "MOON/moon1.jpg"
image moon2 = "MOON/moon2.jpg"
image moon3 = "MOON/moon3.jpg"
image moon4 = "MOON/moon4.jpg"
image moon5 = "MOON/moon5.jpg"
image moon6 = "MOON/moon6.jpg"
image moon7 = "MOON/moon7.jpg"

image moon7 glitched:
    glitch("moon7") # reliable slicing
    pause 1.0
    glitch("moon7", offset=50, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat

transform red_moon:
    matrixcolor TintMatrix(Color(rgb=(0.60, 0.20, 0.20))) * BrightnessMatrix(-0.1)

image red_flash_slow:
    Solid("#C00000")
    alpha 0.0
    on show:
        linear 1.0 alpha 0.75
        pause 1.0
        linear 1.3 alpha 0.0
### SHOW FOG ####
image tiledFog = im.Tile(im.Scale("fog.png", 1600, 600), size=(2400, 800))
image particleFog = SnowBlossom("fog-particle.png", count=80, border=600, xspeed=50, yspeed=0, start=5, fast=True, horizontal=True)
image petals_dense = SnowBlossom(
    "ppetal.png",
    count=40,             # More particles for density
    xspeed=(-10, 10),     # Not much horizontal movement
    yspeed=(-60, -110),   # Gentle, slow rise
    start=0.85,           # Lower part of screen (0.0 = top, 1.0 = bottom)
    border=40
)
image petals_scatter = SnowBlossom(
    "ppetal.png",
    count=20,             # Fewer particles
    xspeed=(-50, 50),     # More horizontal spread
    yspeed=(-150, -230),  # Faster upward movement
    start=0.0,            # Start near the top, so they scatter as they rise
    border=40
)
image petals_dense2 = SnowBlossom(
    "ppetal2.png",
    count=40,             # More particles for density
    xspeed=(-10, 10),     # Not much horizontal movement
    yspeed=(-60, -110),   # Gentle, slow rise
    start=0.85,           # Lower part of screen (0.0 = top, 1.0 = bottom)
    border=40
)
image petals_scatter2 = SnowBlossom(
    "ppetal2.png",
    count=20,             # Fewer particles
    xspeed=(-50, 50),     # More horizontal spread
    yspeed=(-150, -230),  # Faster upward movement
    start=0.0,            # Start near the top, so they scatter as they rise
    border=40
)


### horror circle

image circle_ghost:
    "Ghosts/Circle/1.jpg"
    0.04
    "Ghosts/Circle/2.jpg"
    0.04
    "Ghosts/Circle/3.jpg"
    0.04
    "Ghosts/Circle/4.jpg"
    0.04
    "Ghosts/Circle/5.jpg"
    0.04
    "Ghosts/Circle/6.jpg"
    0.04
    "Ghosts/Circle/7.jpg"
    0.04
    "Ghosts/Circle/8.jpg"
    0.04
    "Ghosts/Circle/9.jpg"
    0.04
    "Ghosts/Circle/10.jpg"
    0.04
    "Ghosts/Circle/11.jpg"
    0.04
    "Ghosts/Circle/12.jpg"
    0.04
    "Ghosts/Circle/13.jpg"
    0.04
    "Ghosts/Circle/14.jpg"
    0.04
    "Ghosts/Circle/15.jpg"
    0.04
    "Ghosts/Circle/16.jpg"
    0.04
    "Ghosts/Circle/17.jpg"
    0.04
    "Ghosts/Circle/18.jpg"
    0.04
    "Ghosts/Circle/19.jpg"
    0.04
    "Ghosts/Circle/20.jpg"
    0.04
    "Ghosts/Circle/21.jpg"
    0.04
    "Ghosts/Circle/22.jpg"
    0.04
    "Ghosts/Circle/23.jpg"
    0.04
    "Ghosts/Circle/24.jpg"
    0.04
    "Ghosts/Circle/25.jpg"
    0.04
    repeat


###EYEEESSSS####

transform blink_eye(delay=0.0, speed=0.4):
    alpha 1.0
    pause delay
    linear speed alpha 0.0
    linear speed alpha 1.0
    pause speed * 2
    repeat

screen eyessss:
    add "eyes/eye1.png" at blink_eye(delay=0.1, speed=0.3) xpos 0.1 ypos 0.2 zoom 0.3
    add "eyes/eye2.png" at blink_eye(delay=0.6, speed=0.5) xpos 0.8 ypos 0.1 zoom 0.3
    add "eyes/eye3.png" at blink_eye(delay=0.2, speed=0.6) xpos 0.4 ypos 0.7 zoom 0.3
    add "eyes/eye4.png" at blink_eye(delay=0.0, speed=0.2) xpos 0.3 ypos 0.5 zoom 0.3
    add "eyes/eye5.png" at blink_eye(delay=0.7, speed=0.3) xpos 0.6 ypos 0.8 zoom 0.3
    add "eyes/eye1.png" at blink_eye(delay=0.4, speed=0.5) xpos 0.15 ypos 0.6 zoom 0.3
    add "eyes/eye2.png" at blink_eye(delay=0.8, speed=0.4) xpos 0.85 ypos 0.3 zoom 0.3
    add "eyes/eye3.png" at blink_eye(delay=0.5, speed=0.7) xpos 0.55 ypos 0.2 zoom 0.3
    add "eyes/eye4.png" at blink_eye(delay=0.3, speed=0.3) xpos 0.2 ypos 0.85 zoom 0.3
    add "eyes/eye5.png" at blink_eye(delay=0.6, speed=0.6) xpos 0.75 ypos 0.65 zoom 0.3



##### CHARACTER MOVEMENTS ########
transform blink:
    linear 1.0 alpha 0.0
    linear 1.0 alpha 1.0
    repeat

transform shakey:
    ease 0.1 xoffset 16
    ease 0.1 xoffset -16
    ease 0.09 xoffset 12
    ease 0.09 xoffset -12
    ease 0.08 xoffset 8
    ease 0.08 xoffset -8
    ease 0.07 xoffset 4
    ease 0.07 xoffset -4
    ease 0.07 xoffset 0
    pass



transform bounci:
    parallel:  # Vertical bounce
        ease 0.2 yoffset -10
        ease 0.2 yoffset 0
    parallel:  # Squish effect
        ease 0.2 xzoom 1.1 yzoom 0.9
        ease 0.2 xzoom 1.0 yzoom 1.0

transform bowey:
    pause .15
    yoffset 0
    easein .2 yoffset 10
    easeout .2 yoffset 5
    easein .2 yoffset -5
    easeout .2 yoffset -2
    yoffset 0
    pass

####  HORROR ATL ######
transform scary_flicker:
    # zoom
    zoom 1.01
    matrixcolor BrightnessMatrix(0.0)


    parallel:
        # Flicker effect
        linear 0.8 alpha 0.9
        linear 0.5 alpha 0.8
        linear 0.8 alpha 1.0
        linear 1.0 alpha 0.85
        repeat

    parallel:
        # brightness
        linear 0.8 matrixcolor BrightnessMatrix(-0.2)
        linear 0.5 matrixcolor BrightnessMatrix(0.1)
        linear 0.8 matrixcolor BrightnessMatrix(-0.1)
        linear 1.0 matrixcolor BrightnessMatrix(0.0)
        repeat


    parallel:
        # Slow shaking
        linear 0.5 xoffset -5 yoffset -3
        linear 0.5 xoffset 3 yoffset 4
        linear 0.5 xoffset -2 yoffset -2
        linear 0.5 xoffset 0 yoffset 0
        repeat

transform red_squelch:
    alpha 0.18
    yoffset 0
    yzoom 1.0
    block:
        ease 0.19 yzoom 1.07 yoffset 8 alpha 0.22
        ease 0.08 yzoom 0.95 yoffset 2 alpha 0.14
        ease 0.14 yzoom 1.12 yoffset 17 alpha 0.26
        ease 0.11 yzoom 0.99 yoffset 0 alpha 0.18
        pause 0.06
        ease 0.20 yzoom 1.09 yoffset 12 alpha 0.21
        ease 0.12 yzoom 0.97 yoffset 4 alpha 0.12
        ease 0.13 yzoom 1.10 yoffset 14 alpha 0.25
        ease 0.11 yzoom 1.0 yoffset 0 alpha 0.18
        pause 0.10

screen red_squelch_overlay():
    add Solid("#ff2323") at red_squelch
        # Or, if you want to use an image of a blood splotch:
        # add "gui/bloodsplotch.png" at red_squelch
##### YAMATO'S ATLS ######

##### SHIORI'S ATLS ######
transform shiori_skipp:
    zoom 0.25
    xanchor 0.5
    xalign 0.5
    yalign -0.60   # face zoom

    parallel:
        linear 1.2 zoom 0.26

    parallel:
        easein 0.15 yoffset -40
        easeout 0.15 yoffset 0
        easein 0.13 yoffset -30
        easeout 0.13 yoffset 0
        easein 0.11 yoffset -20
        easeout 0.11 yoffset 0

    parallel: ## bouncy
        easein 0.15 yzoom 0.95 xzoom 1.05
        easeout 0.15 yzoom 1.0 xzoom 1.0
        easein 0.13 yzoom 0.97 xzoom 1.03
        easeout 0.13 yzoom 1.0 xzoom 1.0

transform shiori_skipp2:
    zoom 0.18
    xalign 0.4
    yalign 0
    yoffset 100    # Increase if still too low

    parallel:
        linear 1.0 zoom 0.5 yoffset 0

    parallel:
        easein 0.18 yzoom 0.97 xzoom 1.05
        easeout 0.18 yzoom 1.00 xzoom 1.00

transform shiori_tilt:
    zoom 0.26
    xanchor 0.5
    xalign 0.5
    yalign -0.60
    yoffset 0

    parallel:
        easein 0.4 zoom 0.4 yoffset -1
        easeout 0.4 zoom 0.26 yoffset 0




transform shiori_stomp:
    # === ANIMATION PHASE: Use anchor for natural squash/stretch ===
    zoom 0.5
    xanchor 0.5
    yanchor 0.1
    xalign 0.125
    yalign -0.261
    yoffset 0
    xzoom 1.0
    yzoom 1.0
    rotate 0
    rotate_pad True

    parallel:
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
        easein 0.08 yoffset -10
        easeout 0.08 yoffset 0

    parallel:
        easein 0.1 yzoom 0.95 xzoom 1.05
        easeout 0.1 yzoom 1.0 xzoom 1.0
        easein 0.08 yzoom 0.97 xzoom 1.03
        easeout 0.08 yzoom 1.0 xzoom 1.0

    ease 0.2 rotate -3
    ease 0.2 rotate 0

    # === SNAP TO FINAL, PIXEL-PERFECT END POSE ===
    anchor (0, 0)
    xalign 0.4
    yalign 0
    yoffset 0
    xzoom 1.0
    yzoom 1.0
    rotate 0
