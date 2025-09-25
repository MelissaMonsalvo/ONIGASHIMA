transform yamato_zoom:
    zoom 0.23
    xanchor 0.5
    yalign -0.04
    xzoom 1.0
    yzoom 1.0
    yoffset 0
image yam serious = LiveComposite(
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
    (0,0), "Yamato/brow/b_angry.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_serious.webp", .2, "Yamato/mouth/m_serious_open.webp", .2),
            "Yamato/mouth/m_serious.webp"
        ),

    )
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
image yam happycl = LiveComposite(
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
    (0,0), "Yamato/eye/e_closed.webp",
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_smile.webp", .2, "Yamato/mouth/m_smile_open.webp", .2),
            "Yamato/mouth/m_smile_open.webp"
        ),

    )
image yam smug = LiveComposite(
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
    (0,0), "Yamato/eye/e_closed.webp",
    (0,0), "Yamato/brow/b_angry.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_smile.webp", .2, "Yamato/mouth/m_smile_open.webp", .2),
            "Yamato/mouth/m_smile_open.webp"
        ),

    )
image yam happy = LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_smile.webp", .2, "Yamato/mouth/m_smile_open.webp", .2),
            "Yamato/mouth/m_smile.webp"
        ),

    )
image yam annoyed= LiveComposite(
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
    (0,0), "Yamato/brow/b_angry.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_angry.webp", .2, "Yamato/mouth/m_angry_open.webp", .2),
            "Yamato/mouth/m_angry.webp"
        ),
    (0,0), "Yamato/extra/ex_angrymark.webp"

    )
image yam angry= LiveComposite(
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
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_normal.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_angry.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_shout.webp", .2, "Yamato/mouth/m_shout_open.webp", .2),
            "Yamato/mouth/m_shout_open.webp"
        ),
    (0,0), "Yamato/extra/ex_angrymark.webp"

    )
image yam rage= LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_rage.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_rage.webp", .2, "Yamato/mouth/m_rage_open.webp", .2),
            "Yamato/mouth/m_rage_open.webp"
        ),
    (0,0), "Yamato/extra/ex_angrymark.webp"

    )
image yam annoyedbl= LiveComposite(
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
            "Yamato/eye/e_half.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_angry.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_angry.webp", .2, "Yamato/mouth/m_angry_open.webp", .2),
            "Yamato/mouth/m_angry.webp"
        ),
    (0,0), "Yamato/extra/ex_angrymark.webp",
    (0,0), "Yamato/extra/ex_blush2.webp"

    )
image yam panic = LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_fear.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_panic.webp", .2, "Yamato/mouth/m_panic_open.webp", .2),
            "Yamato/mouth/m_panic_open.webp"
        ),

    )
image yam panicbl = LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_panic.webp", .2, "Yamato/mouth/m_panic_open.webp", .2),
            "Yamato/mouth/m_panic_open.webp"
        ),
    (0,0), "Yamato/extra/ex_blush3.webp"

    )
image yam surprised = LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_surprised.webp", .2, "Yamato/mouth/m_surprised_open.webp", .2),
            "Yamato/mouth/m_surprised_open.webp"
        ),

    )
image yam evil = LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_rage.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_smile.webp", .2, "Yamato/mouth/m_smile_open.webp", .2),
            "Yamato/mouth/m_smile_open.webp"
        ),

    )
image yam shocked = LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_panic.webp", .2, "Yamato/mouth/m_panic_open.webp", .2),
            "Yamato/mouth/m_panic.webp"
        ),

    )
image yam sad = LiveComposite(
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
    (0,0), "Yamato/ear_left1.png",
    (0,0), "Yamato/ear_right1.png",
    (0,0), "Yamato/bangs1.png",
    (0, 0), ConditionSwitch(
    "ysword == False", "Yamato/sword/sword_hilted.webp",
    "True", "Yamato/sword/sword_drawn.webp"),
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), "Yamato/eye/e_closed.webp",
    (0,0), "Yamato/brow/b_sad.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_serious.webp", .2, "Yamato/mouth/m_serious_open.webp", .2),
            "Yamato/mouth/m_serious.webp"
        ),

    )
image yam ngh= LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), "Yamato/eye/e_closed.webp",
    (0,0), "Yamato/brow/b_rage.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_rage.webp", .2, "Yamato/mouth/m_rage_open.webp", .2),
            "Yamato/mouth/m_rage.webp"
        ),

    )
image yam blush = LiveComposite(
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
    (0,0), "Yamato/ear_left1.png",
    (0,0), "Yamato/ear_right1.png",
    (0,0), "Yamato/bangs1.png",
    (0, 0), ConditionSwitch(
    "ysword == False", "Yamato/sword/sword_hilted.webp",
    "True", "Yamato/sword/sword_drawn.webp"),
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_half.webp", 4.25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_sad.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_serious.webp", .2, "Yamato/mouth/m_serious_open.webp", .2),
            "Yamato/mouth/m_serious.webp"
        ),
    (0,0), "Yamato/extra/ex_blush2.webp"

    )
image yam drunk = LiveComposite(
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
    (0,0), "Yamato/ear_left1.png",
    (0,0), "Yamato/ear_right1.png",
    (0,0), "Yamato/bangs1.png",
    (0, 0), ConditionSwitch(
    "ysword == False", "Yamato/sword/sword_hilted.webp",
    "True", "Yamato/sword/sword_drawn.webp"),
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_half.webp", 4.25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_surprised.webp", .2, "Yamato/mouth/m_surprised_open.webp", .2),
            "Yamato/mouth/m_surprised.webp"
        ),
    (0,0), "Yamato/extra/ex_blush2.webp"

    )
image yam drunk2 = LiveComposite(
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
    (0,0), "Yamato/ear_left1.png",
    (0,0), "Yamato/ear_right1.png",
    (0,0), "Yamato/bangs1.png",
    (0, 0), ConditionSwitch(
    "ysword == False", "Yamato/sword/sword_hilted.webp",
    "True", "Yamato/sword/sword_drawn.webp"),
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Yamato/eye/e_half.webp", 4.25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_smile.webp", .2, "Yamato/mouth/m_smile_open.webp", .2),
            "Yamato/mouth/m_smile.webp"
        ),
    (0,0), "Yamato/extra/ex_blush2.webp"

    )
image yam kiss = LiveComposite(
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
    (0,0), "Yamato/ear_left1.png",
    (0,0), "Yamato/ear_right1.png",
    (0,0), "Yamato/bangs1.png",
    (0, 0), ConditionSwitch(
    "ysword == False", "Yamato/sword/sword_hilted.webp",
    "True", "Yamato/sword/sword_drawn.webp"),
    (0,0), "Yamato/eye/e_wide_white.webp",              # whites
    (0,0), "Yamato/eye/e_iris_small.webp",             # iris
    (0,0), "Yamato/eye/e_closed.webp",
    (0,0), "Yamato/brow/b_sad.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_surprised.webp", .2, "Yamato/mouth/m_surprised_open.webp", .2),
            "Yamato/mouth/m_surprised.webp"
        ),
    (0,0), "Yamato/extra/ex_blush2.webp"

    )
image yam eldritch= LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_angry.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_shout.webp", .2, "Yamato/mouth/m_shout_open.webp", .2),
            "Yamato/mouth/m_shout.webp"
        ),
    (0,0), "Yamato/extra/ex_eldritch.webp"

    )

image yam eldritch= LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_smile.webp", .2, "Yamato/mouth/m_smile_open.webp", .2),
            "Yamato/mouth/m_smile.webp"
        ),
    (0,0), "Yamato/extra/ex_eldritch.webp"

    )

image yam eldritch1= LiveComposite(
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
    (0,0), "Yamato/eye/e_wide_white.webp",
    (0,0), Animation(
            "Yamato/eye/e_wide.webp", 4.5,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
            "Yamato/eye/e_normal.webp", .75,
            "Yamato/eye/e_half.webp", .25,
            "Yamato/eye/e_closed.webp", .25,
        ),
    (0,0), "Yamato/brow/b_happy.webp",
    (0,0), WhileSpeaking(
            "yama",
            Animation("Yamato/mouth/m_shout.webp", .2, "Yamato/mouth/m_shout_open.webp", .2),
            "Yamato/mouth/m_shout_open.webp"
        )

    )
image yam glitched:
    glitch("yam eldritch") # reliable slicing
    pause 1.0
    glitch("yam eldritch", offset=100, randomkey=None) # bigger and always-random slicing
    pause 0.1
    repeat
