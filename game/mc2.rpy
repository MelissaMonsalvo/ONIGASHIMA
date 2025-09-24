#####################################
#MC LOOP2
######################################3

image side main normal2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main yan2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main yansm2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)
image side main panic2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)
image side main happy2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main happycl2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_happy_01.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main nervous2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/mc/brow/b_sad_01.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main sad2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main sadcl2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_neutral_01.webp", .2, "MC/mc/mouth/m_open_neutral_01.webp", .2),
            "MC/mc/mouth/m_neutral_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_sad_01.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main annoyed2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main mad2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main hurt2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_angry_01.webp", .2, "MC/mc/mouth/m_open_angry_01.webp", .2),
            "MC/mc/mouth/m_angry_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main surprised2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main shocked2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main smug2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main smugcl2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_2.webp",             # iris
        (260, 0), "MC/mc/eyes/e_closed_01.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/mc/mouth/m_smile_01.webp", .2, "MC/mc/mouth/m_open_smile_01.webp", .2),
            "MC/mc/mouth/m_open_smile_01.webp"
        ),
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)

image side main evil2 = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base

        (260, 0), "MC/mc/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_sm_2.webp",             # iris
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
        (260, 0), "MC/horn_shadow.webp",
    ),
    zoom=0.31
)
