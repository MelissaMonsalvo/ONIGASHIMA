

image slash1 = "vfx/slash1.png"
image slash2 = "vfx/slash2.png"
image slash3 = "vfx/slash3.png"

image slash_anim:
    Solid("#FFFFFF")         # Pure white slash — change color if needed
    rotate 45                # Diagonal from bottom-left to top-right
    size (80, 2500)          # Wide and long enough to cross full HD diagonally
    alpha 1.0
    xpos 960 ypos 540        # Center of 1920x1080 screen
    anchor (0.5, 0.5)        # Center anchor for correct rotation
    linear 0.2 alpha 0.0     # Quick fade out

image slash_fx_horizontal:
    Solid("#FFFFFF")         # White slash — change if needed
    size (1920, 10)           # Long and thin, like a sword slash
    alpha 1.0
    xpos -200 ypos 540       # Start off-screen to the left, vertical center
    anchor (0.0, 0.5)        # Anchor left-middle
    linear 0.2 xpos 2120 alpha 0.0  # Move across screen and fade out

image combo_slash_1:
    Solid("#FFFFFF")
    rotate 45
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    alpha 1.0
    linear 0.15 alpha 0.0

image combo_slash_2:
    Solid("#FFFFFF")
    rotate -45
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    alpha 1.0
    linear 0.15 alpha 0.0

image combo_slash_3:
    Solid("#FFFFFF")
    rotate 60
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    alpha 1.0
    linear 0.15 alpha 0.0

image slash_animred:
    Solid("#FF3333")        
    rotate 45                
    size (80, 2500)         
    alpha 1.0
    xpos 960 ypos 540        
    anchor (0.5, 0.5)        
    linear 0.2 alpha 0.0     

image slash_fx_horizontalred:
    Solid("#FF3333")         
    size (1920, 10)          
    alpha 1.0
    xpos -200 ypos 540       
    anchor (0.0, 0.5)        
    linear 0.2 xpos 2120 alpha 0.0  


image slash_fx_zigzagred:
    # Segment 1: top-left to upper-right
    Solid("#FF3333")
    size (500, 16)
    xpos 120 ypos 70
    anchor (0.0, 0.5)
    rotate 18

    # Segment 2: upper-right to left-mid
    Solid("#FF3333")
    size (530, 16)
    xpos 540 ypos 270
    anchor (0.0, 0.5)
    rotate -25

    # Segment 3: left-mid to right-lower
    Solid("#FF3333")
    size (580, 16)
    xpos 120 ypos 450
    anchor (0.0, 0.5)
    rotate 16

    # Segment 4: right-lower to left-bottom
    Solid("#FF3333")
    size (610, 16)
    xpos 650 ypos 700
    anchor (0.0, 0.5)
    rotate -19

    # Segment 5: left-bottom to right-bottom
    Solid("#FF3333")
    size (690, 16)
    xpos 110 ypos 900
    anchor (0.0, 0.5)
    rotate 12
image combo_slash_1red:
    Solid("#FF3333")
    rotate 45
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    alpha 1.0
    linear 0.15 alpha 0.0

image combo_slash_2red:
    Solid("#FF3333")
    rotate -45
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    alpha 1.0
    linear 0.15 alpha 0.0

image combo_slash_3red:
    Solid("#FF3333")
    rotate 60
    size (60, 2000)
    anchor (0.5, 0.5)
    xpos 960 ypos 540
    alpha 1.0
    linear 0.15 alpha 0.0

image slash_critical_red:
    Solid("#FF3333")
    size (1920, 50)
    xpos 0 ypos 540
    alpha 1.0
    linear 0.1 alpha 0.0

image slash_vertical:
    Solid("#FFFFFF")
    size (90, 1080)
    xpos 960 ypos -1080
    anchor (0.5, 0)
    linear 0.15 ypos 1080 alpha 0.0

image slash_arc:
    Solid("#FF3333")
    size (3080, 50)
    xpos 800 ypos 600
    anchor (0.5, 0.5)
    linear 0.05 xpos 850 ypos 580
    linear 0.05 xpos 900 ypos 560
    linear 0.05 xpos 950 ypos 540 alpha 0.0

image slash_giant_arc:
    Solid("#FF0000")
    size (150, 2500)
    rotate 0
    xpos 500 ypos -600
    anchor (0.5, 0.0)
    alpha 1.0
    zoom 1.0

    easeout 0.01 ypos 600 zoom 1.05 alpha 0.8
    linear 0.01 alpha 0.0



image red_flash:
    Solid("#FF0000")
    size (1920, 1080)
    alpha 0.0
    linear 0.05 alpha 0.6
    linear 0.2 alpha 0.0


image slash_fast:
    Solid("#FFFFFF")
    size (200, 2)
    xpos -200 ypos 520
    anchor (0.0, 0.5)
    linear 0.05 xpos 2120 alpha 0.0

image slash_x1:
    Solid("#FFFFFF")
    rotate 45
    size (50, 2000)
    xpos 960 ypos 540
    anchor (0.5, 0.5)
    linear 0.2 alpha 0.0

image slash_x2:
    Solid("#FFFFFF")
    rotate -45
    size (50, 2000)
    xpos 960 ypos 540
    anchor (0.5, 0.5)
    linear 0.2 alpha 0.0

image slash_x2red:
    Solid("#FF0000")
    rotate -45
    size (50, 2000)
    xpos 960 ypos 540
    anchor (0.5, 0.5)
    linear 0.2 alpha 0.0

