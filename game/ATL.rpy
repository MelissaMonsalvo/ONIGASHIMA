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