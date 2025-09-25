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
    (0,0), "Shiori/brow/b_neutral.webp",

    )

image shi happy = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_smile.webp", .2, "Shiori/mouth/m_smile_open.webp", .2),
            "Shiori/mouth/m_smile.webp"
        ),
    (0,0), "Shiori/brow/b_happy.webp",

    )

image shi happyblush = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), "Shiori/eyes/e_closed.webp",
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_smile.webp", .2, "Shiori/mouth/m_smile_open.webp", .2),
            "Shiori/mouth/m_smile.webp"
        ),
    (0,0), "Shiori/extra/ex_blush.webp",)

image shi sad = LiveComposite(
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
    (0,0), "Shiori/ear_left2.png",
    (0,0), "Shiori/ear_right2.png",
    (0,0), "Shiori/bangs.png",
    (0,0), "Shiori/brow/b_sad.webp",
    (0,0), "Shiori/eyes/e_normal_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_half.webp", 4.25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_normal.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_serious.webp", .2, "Shiori/mouth/m_serious_open.webp", .2),
            "Shiori/mouth/m_serious.webp"
        ),
    (0,0), "Shiori/brow/b_happy.webp",

    )

image shi blush = LiveComposite(
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
    (0,0), "Shiori/ear_left2.png",
    (0,0), "Shiori/ear_right2.png",
    (0,0), "Shiori/bangs.png",
    (0,0), "Shiori/eyes/e_normal_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_half.webp", 4.25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_normal.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_smile.webp", .2, "Shiori/mouth/m_smile_open.webp", .2),
            "Shiori/mouth/m_smile.webp"
        ),
    (0,0), "Shiori/brow/b_sad.webp",
    (0,0), "Shiori/extra/ex_blush.webp",


    )

image shi worried = LiveComposite(
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
    (0,0), "Shiori/ear_left2.png",
    (0,0), "Shiori/ear_right2.png",
    (0,0), "Shiori/bangs.png",

    (0,0), "Shiori/eyes/e_normal_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), "Shiori/eyes/e_closed.webp",
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_serious.webp", .2, "Shiori/mouth/m_serious_open.webp", .2),
            "Shiori/mouth/m_serious.webp"
        ),
    (0,0), "Shiori/brow/b_fear.webp",
    (0,0), "Shiori/extra/ex_sweat.webp",

    )

image shi fear = LiveComposite(
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
    (0,0), "Shiori/ear_left2.png",
    (0,0), "Shiori/ear_right2.png",
    (0,0), "Shiori/bangs.png",

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_surprise.webp", .2, "Shiori/mouth/m_surprise_open.webp", .2),
            "Shiori/mouth/m_surprise_open.webp"
        ),
    (0,0), "Shiori/brow/b_fear.webp",
    (0,0), "Shiori/extra/ex_sweat.webp",

    )

image shi surprised = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_shout.webp", .2, "Shiori/mouth/m_shout_open.webp", .2),
            "Shiori/mouth/m_shout_open.webp"
        ),
    (0,0), "Shiori/brow/b_happy.webp",

    )
image shi shocked = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_angry.webp", .2, "Shiori/mouth/m_angry_open.webp", .2),
            "Shiori/mouth/m_angry_open.webp"
        ),
    (0,0), "Shiori/brow/b_fear.webp",

    )
image shi annoyed = LiveComposite(
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
            Animation("Shiori/mouth/m_serious.webp", .2, "Shiori/mouth/m_serious_open.webp", .2),
            "Shiori/mouth/m_serious_open.webp"
        ),
    (0,0), "Shiori/brow/b_anger.webp",

    )
image shi angry = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_angry.webp", .2, "Shiori/mouth/m_angry_open.webp", .2),
            "Shiori/mouth/m_angry_open.webp"
        ),
    (0,0), "Shiori/brow/b_anger.webp",

    )
image shi yansm = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_yandere.webp", .2, "Shiori/mouth/m_yandere_open.webp", .2),
            "Shiori/mouth/m_yandere.webp"
        ),
    (0,0), "Shiori/brow/b_fear.webp",

    )
image shi yan = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_neutral.webp", .2, "Shiori/mouth/m_neutral_open.webp", .2),
            "Shiori/mouth/m_neutral.webp"
        ),
    (0,0), "Shiori/brow/b_fear.webp",

    )
image shi yanbl = LiveComposite(
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

    (0,0), "Shiori/eyes/e_normal_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
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
            Animation("Shiori/mouth/m_surprise.webp", .2, "Shiori/mouth/m_surprise_open.webp", .2),
            "Shiori/mouth/m_surprise_open.webp"
        ),
    (0,0), "Shiori/brow/b_sad.webp",
    (0,0), "Shiori/extra/ex_blush.webp",

    )
image shi yansmbl = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
    (0,0), Animation(
            "Shiori/eyes/e_wide.webp", 4.5,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
            "Shiori/eyes/e_wide.webp", .75,
            "Shiori/eyes/e_half.webp", .25,
            "Shiori/eyes/e_closed.webp", .25,
        ),
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_yandere.webp", .2, "Shiori/mouth/m_yandere_open.webp", .2),
            "Shiori/mouth/m_yandere_open.webp"
        ),
    (0,0), "Shiori/brow/b_happy.webp",
    (0,0), "Shiori/extra/ex_blush.webp",

    )
image shi smug = LiveComposite(
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

    (0,0), "Shiori/eyes/e_wide_white.webp",              # whites
    (0,0), "Shiori/eyes/e_small_iris.webp",             # iris
    (0,0), "Shiori/eyes/e_closed.webp",
    (0,0), WhileSpeaking(
            "shio",
            Animation("Shiori/mouth/m_yandere.webp", .2, "Shiori/mouth/m_yandere_open.webp", .2),
            "Shiori/mouth/m_yandere.webp"
        ),
    (0,0), "Shiori/brow/b_Anger.webp",

    )
