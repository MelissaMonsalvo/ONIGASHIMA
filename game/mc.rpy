#####################################
#MC NORMAL
######################################3

image side main normal = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_open_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_neutral_01.webp",            # brows
    ),
    zoom=0.31
)

image side main yan = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_open_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
    ),
    zoom=0.31
)

image side main yansm = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_open_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_open_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
    ),
    zoom=0.31
)
image side main panic = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_open_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_angry_01.webp", .2, "MC/mc/mouth/m_open_angry_01.webp", .2),
            "MC/mc/mouth/m_open_angry_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_sad_01.webp",            # brows
    ),
    zoom=0.31
)
image side main happy = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_open_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_open_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
    ),
    zoom=0.31
)

image side main happycl = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
    ),
    zoom=0.31
)

image side main nervous = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_sad_01.webp",            # brows
    ),
    zoom=0.31
)

image side main sad = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_sad_01.webp",            # brows
    ),
    zoom=0.31
)

image side main sadcl = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_sad_01.webp",            # brows
    ),
    zoom=0.31
)

image side main annoyed = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
    ),
    zoom=0.31
)

image side main mad = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_angry_01.webp", .2, "MC/mc/mouth/m_open_angry_01.webp", .2),
            "MC/mc/mouth/m_open_angry_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
    ),
    zoom=0.31
)

image side main hurt = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_angry_01.webp", .2, "MC/mc/mouth/m_open_angry_01.webp", .2),
            "MC/mc/mouth/m_angry_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
    ),
    zoom=0.31
)

image side main surprised = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_open_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
    ),
    zoom=0.31
)

image side main shocked = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_angry_01.webp", .2, "MC/mc/mouth/m_open_angry_01.webp", .2),
            "MC/mc/mouth/m_open_angry_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
    ),
    zoom=0.31
)

image side main smug = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
    ),
    zoom=0.31
)

image side main smugcl = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_01.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_open_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
    ),
    zoom=0.31
)

image side main evil = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/mc/eyes/e_iris_sm_01.webp",             # iris
        (260, 0), Animation(
            "MC/mc/eyes/e_half_01.webp", 4.5,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
            "MC/mc/eyes/e_open_01.webp", .75,
            "MC/mc/eyes/e_half_01.webp", .25,
            "MC/mc/eyes/e_closed_01.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_open_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
    ),
    zoom=0.31
)
