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
    linear 1.2 zoom 1.2 alpha 0.0

transform c_show_5:
    linear 0.15 xalign 0.1 yalign 0.5 zoom 0.1

transform c_show_6:
    linear 0.15 xalign 0.7 yalign 0.5 zoom 0.13

transform c_show_7: #appear ad side
    xzoom 0.12 yzoom 0.12 yalign 0.7 blur 1 xpos config.screen_width-20

transform c_show_8:
    xzoom 0.12 yzoom 0.12 yalign 0.5 xpos config.screen_width-20
    linear 0.4 xpos -500 yalign 0.5

transform c_show_9:
    yzoom 0.01 xzoom 0.01 xalign 0.5 yalign 0.06
    linear 0.2 xzoom 1 yzoom 1 yalign 0.06 xalign 0.5
    pause(0.2)
    linear 0.15 alpha 0.0

transform c_show_10:
    xalign 0.5 ypos -100 rotate 180 zoom 0.13
    alpha 0.1
    linear 0.4 alpha 1.0

transform c_show_11:
    linear 1.0 alpha 0.0

