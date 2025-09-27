## additionan screen ##

###### POSITIONS ######

transform c_show_1: #fade slowly at center
    delay 3.0
    xalign 0.5 yalign 0.5
    zoom 0.1
    alpha 0.1
    linear 0.5 alpha 1.0 zoom 0.17


transform c_show_2: #fade slowly at center
    linear 0.8 xalign 0.5 yalign 0.5  zoom 0.17

transform c_show_3: #fade and glitching
    xalign 0.5 yalign 0.5
    zoom 0.1
    alpha 0.1
    linear 0.5 alpha 1.0 zoom 0.13

    xzoom 0.2 yzoom 0.7 yalign 0.2
    pause 0.2
    xzoom 1.0 yzoom 1.0

    xzoom 0.3 yzoom 0.3 xalign 0.1 yalign 0.2
    pause 0.2
    xzoom 1.0 yzoom 1.0

    xzoom 0.5 yzoom 0.1 xalign 0.6 yalign 0.7
    pause 0.2
    xzoom 1.0 yzoom 1.0

    yzoom 0.7 xzoom 0.2 xalign 0.7
    pause 0.2
    yzoom 1.0 xzoom 1.0 xalign 0.5 yalign 0.5

transform c_show_4:
    xalign 0.5 yalign 0.5
    zoom 0.12
    alpha 1
    linear 1.2 zoom 1.2 alpha 0.0 yalign 0.06

transform c_show_5:
    linear 0.15 xalign 0.1 yalign 0.5 zoom 0.1

transform c_show_6:
    linear 0.15 xalign 0.7 yalign 0.5 zoom 0.13

transform c_show_7: #appear ad side
    xzoom 0.12 yzoom 0.12 yalign 0.7 blur 1 xpos config.screen_width-20

transform c_show_8:
    xzoom 0.12 yzoom 0.12 yalign 0.5 xpos config.screen_width-20
    linear 0.3 xpos -500 yalign 0.5

transform c_show_9:
    yzoom 0.01 xzoom 0.01 xalign 0.5 yalign 0.06
    linear 0.2 xzoom 1 yzoom 1 yalign 0.06 xalign 0.5
    pause(0.2)
    linear 0.15 alpha 0.0

transform c_show_10:
    xalign 0.5 ypos -2300 rotate 180 zoom 0.5
    alpha 0.1
    linear 0.4 alpha 1.0

transform c_show_11:
    linear 1.0 alpha 0.0

transform c_show_12:
    xalign 0.5 ypos -100
    linear 0.3 alpha 0.0

transform c_show_13: #blink
    xalign 0.5 yalign 0.5 alpha 0
    pause 1
    linear 0.7 alpha 1
    linear 0.7 alpha 0

transform c_show_14:
    xalign 0.5 yalign 0.5 zoom 0.16 alpha 0
    pause 1.5
    linear 1 alpha 1

transform c_show_15:
    zoom 0.16 alpha 0.0 xalign 0.5 yalign 0.5
    linear 1 alpha 1.0

transform c_show_16:
    linear 1 alpha 0.0

transform c_show_17:
    alpha 0.0 zoom 0.17 xalign 0.5 yalign 0.5
    pause 1.2
    linear 1 alpha 1.1 xalign 0.5 yalign 0.5

transform c_show_18:
    xalign 0.5 yalign 0.5 zoom 0.13 alpha 0.0
    linear 1.0 alpha 1.0

transform c_show_19:
    linear 1.0 zoom 0.16

transform c_show_20:
    linear 1.0 zoom 0.18

transform c_show_21:
    alpha 0.0 zoom 0.17 xalign 0.5 yalign 0.5
    linear 1 alpha 1

transform c_show_22:
    alpha 1.0 zoom 0.17 xalign 0.5 yalign 0.5

transform c_show_23:
    alpha 1.0 zoom 0.6 xalign 0.5 ypos 1080
    linear 4 ypos 200

transform c_show_24:
    alpha 0 zoom 0.17 yalign 0.5 xalign 0.75
    linear 1 alpha 1

transform c_show_25:
    linear 0.5 zoom 0.2 xalign 0.5 yalign 0.2

transform c_show_26:
    linear 0.4 yalign 0.0 zoom 0.9
    linear 0.5 alpha 0

transform c_show_27:
    linear 0.05 alpha 1
    linear 0.05 alpha 0
    linear 0.05 alpha 1
    linear 0.05 alpha 0
    linear 0.05 alpha 1
    linear 0.05 alpha 0
    linear 0.05 alpha 1
    linear 0.05 alpha 0
    linear 0.05 alpha 1
    linear 0.05 alpha 0
    repeat

transform c_show_28:
    xalign 0.5 yalign 0.8 zoom 0.13 alpha 0
    linear 1 alpha 0.6

transform c_show_29:
    linear 0.5 zoom 0.15 alpha 0.8

transform c_show_30:
    linear 0.5 zoom 0.20 alpha 1

transform c_show_31:
    xalign 0.5 yalign 0.2 zoom 0.18 alpha 1
    pause 0.3
    linear 0.1 zoom 1 xalign 0.5 yalign 0.1
    linear 0.2 alpha 0

transform c_show_32:
    zoom 0.6 yalign 0.06 xalign 0.5 alpha 0 xoffset -200
    linear 1 alpha 1


transform c_show_33:
    zoom 0.5 alpha 0
    linear 1 alpha 1

transform c_show_34:
    zoom 0.6 yalign 0.06 xalign 0.5 alpha 0 xoffset -200
    linear 1 alpha 1

transform c_show_35:
    linear 1 zoom 0.7  yalign 0.05 xalign 0.5 xoffset -200 yoffset -200

transform c_show_36:
    linear 1 zoom 0.8  yalign 0.06 xalign 0.5 alpha 0 xoffset -200

transform c_show_37:
    alpha 0 zoom 0.5 ypos -2000 xpos -700
    linear 1 alpha 1
    linear 3 ypos -1000

transform c_show_38:
    linear 3 ypos -400

transform c_show_39:
    linear 2 yalign 0.05

transform c_show_40:
    alpha 0 zoom 0.19 yalign 0.1 xalign 0.9
    linear 1 alpha 1

transform c_show_41:
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0
    pause 1
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    pause 1
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    pause 1
    repeat

transform c_show_42:
    linear 1.0 zoom 0.4 xalign 0.5 yalign 0.05
