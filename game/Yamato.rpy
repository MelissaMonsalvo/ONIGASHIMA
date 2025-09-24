transform yamato_zoom:
    zoom 0.23
    xanchor 0.5
    yalign -0.04
    xzoom 1.0
    yzoom 1.0
    yoffset 0

image yam normal = LiveComposite(
    (3638,6926),
    (0,0), Animation(
            "Yamato/tail/tail_raised1.png", 4.5,
            "Yamato/tail/tail_raised2.png", .25,
            "Yamato/tail/tail_raised3.png", 2.25,
            "Yamato/tail/tail_raised2.png", .25,
            "Yamato/tail/tail_raised1.png", .25,
            "Yamato/tail/tail_Raised2.png", 2.25,
        ),

    (0,0), "Yamato/body.webp",
    (0,0), Animation(
            "Yamato/ear_left.png", 4.5,
            "Yamato/ear_left1.png", .1,
            "Yamato/ear_left.png", .1,
            "Yamato/ear_left.png", 2.25,
            "Yamato/ear_left1.png", .1,
            "Yamato/ear_left.png", .1,
            "Yamato/ear_left1.png", .25,
        ),
    (0,0), Animation(
            "Yamato/ear_right.png", 4.5,
            "Yamato/ear_right1.png", .1,
            "Yamato/ear_right.png", .1,
            "Yamato/ear_right.png", 2.25,
            "Yamato/ear_right1.png", .1,
            "Yamato/ear_right.png", .1,
            "Yamato/ear_right1.png", .25,
        ),
    (0,0), "Yamato/bangs1.png",
    (0, 0), ConditionSwitch(
    "ysword == False", "Yamato/sword/sword_hilted.webp",
    "True", "Yamato/sword/sword_drawn.webp"),
    (0,0), "Yamato/eye/e_normal_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_normal.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_neutral.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_serious.webp", .2, "Yamato/mouth/m_serious_open.webp", .2),
            "Yamato/mouth/m_serious.webp"
        ),

    )

image yam glitched:
    glitch("yam normal") # reliable slicing
    pause 1.0
    glitch("yam normal", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat
