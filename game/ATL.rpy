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

### SHOW FOG ####
image tiledFog = im.Tile(im.Scale("fog.png", 1600, 600), size=(2400, 800))
image particleFog = SnowBlossom("fog-particle.png", count=80, border=600, xspeed=50, yspeed=0, start=5, fast=True, horizontal=True)



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

##### YAMATO'S ATLS ######

##### SHIORI'S ATLS ######
transform shiori_skipp:
    zoom 0.25
    xanchor 0.5
    xalign 0.5
    yalign -0.45   # face zoom

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

transform shiori_tilt:
    zoom 0.25
    xanchor 0.5
    xalign 0.5
    yalign -0.45
    yoffset 0
    xzoom 1.0
    yzoom 1.0

    # Lean in (upper body moves toward camera)
    parallel:
        easein 0.4 zoom 0.29
        easeout 0.4 zoom 0.26

    parallel:
        easein 0.4 yoffset -100
        easeout 0.4 yoffset 0

    # Final resting bounce (subtle)
    parallel:
        pause 0.8
        easein 0.1 yoffset -12
        easeout 0.1 yoffset 0
        easein 0.08 yoffset -6
        easeout 0.08 yoffset 0

transform shiori_think:
    zoom 0.26
    xanchor 0.5
    yanchor 0.1   # anchor the "neck"
    xalign 0.5
    yalign -0.30
    xzoom 1.0
    yzoom 1.0
    yoffset 0
    rotate 0
    rotate_pad True

    easein 0.3 rotate -2
    ease 0.4 rotate 2
    easeout 0.3 rotate 0

transform shiori_stomp:
    zoom 0.26
    xanchor 0.5
    yanchor 0.1   # anchor the "neck"
    xalign 0.5
    yalign -0.30
    xzoom 1.0
    yzoom 1.0
    yoffset 0
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
