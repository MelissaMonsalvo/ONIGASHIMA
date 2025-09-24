transform shiori_zoom:
    zoom 0.26
    xanchor 0.5
    xalign 0.5
    yalign -0.60
    yoffset 0
    xzoom 1.0
    yzoom 1.0

image shi normal = LiveComposite(
    (2000,5637),
    (-2200,0), Animation(
            "Shiori/tail1.png", 4.5,
            "Shiori/tail2.png", .25,
            "Shiori/tail3.png", .25,
            "Shiori/tail4.png", 2.25,
            "Shiori/tail3.png", .25,
            "Shiori/tail2.png", .25,
            "Shiori/tail1.png", 2.25,
        ),

    (0,0), "Shiori/body.png",
    (0,0), Animation(
            "Shiori/ear_left.png", 4.5,
            "Shiori/ear_left2.png", .1,
            "Shiori/ear_left.png", .1,
            "Shiori/ear_left.png", 2.25,
            "Shiori/ear_left2.png", .1,
            "Shiori/ear_left.png", .1,
            "Shiori/ear_left2.png", .25,
        ),
    (0,0), Animation(
            "Shiori/ear_right.png", 4.5,
            "Shiori/ear_right2.png", .1,
            "Shiori/ear_right.png", .1,
            "Shiori/ear_right.png", 2.25,
            "Shiori/ear_right2.png", .1,
            "Shiori/ear_right.png", .1,
            "Shiori/ear_right2.png", .25,
        ),
    (0,0), "Shiori/bangs.png",
    (0,0), "Shiori/brow/b_neutral.webp",
    (0,0), "Shiori/eyes/e_normal_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_normal.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_normal.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_neutral.webp", .2, "Shiori/mouth/m_neutral_open.webp", .2),
            "Shiori/mouth/m_neutral.webp"
        ),

    )
