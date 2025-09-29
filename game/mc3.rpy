#####################################
#MC LOOP3
######################################3

image side main normal3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_open_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_neutral_1.webp", .2, "MC/oni/mouth/m_open_neutral_1.webp", .2),
            "MC/oni/mouth/m_neutral_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_neutral_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main yan3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_open_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_neutral_1.webp", .2, "MC/oni/mouth/m_open_neutral_1.webp", .2),
            "MC/oni/mouth/m_neutral_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_happy_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main yansm3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_open_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_open_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_happy_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)
image side main panic3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_open_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_angry_1.webp", .2, "MC/oni/mouth/m_open_angry_1.webp", .2),
            "MC/oni/mouth/m_open_angry_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_sad_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)
image side main happy3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_open_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_open_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_happy_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main happycl3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), "MC/oni/eyes/e_closed_1.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_happy_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main nervous3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_sad_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main sad3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_neutral_1.webp", .2, "MC/oni/mouth/m_open_neutral_1.webp", .2),
            "MC/oni/mouth/m_neutral_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_sad_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main sadcl3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), "MC/oni/eyes/e_closed_1.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_neutral_1.webp", .2, "MC/oni/mouth/m_open_neutral_1.webp", .2),
            "MC/oni/mouth/m_neutral_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_sad_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main annoyed3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_neutral_1.webp", .2, "MC/oni/mouth/m_open_neutral_1.webp", .2),
            "MC/oni/mouth/m_neutral_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_angry_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main mad3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_angry_1.webp", .2, "MC/oni/mouth/m_open_angry_1.webp", .2),
            "MC/oni/mouth/m_open_angry_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_angry_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main hurt3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), "MC/oni/eyes/e_closed_1.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_angry_1.webp", .2, "MC/oni/mouth/m_open_angry_1.webp", .2),
            "MC/oni/mouth/m_angry_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_angry_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main surprised3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_neutral_1.webp", .2, "MC/oni/mouth/m_open_neutral_1.webp", .2),
            "MC/oni/mouth/m_open_neutral_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_happy_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main shocked3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_angry_1.webp", .2, "MC/oni/mouth/m_open_angry_1.webp", .2),
            "MC/oni/mouth/m_open_angry_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_happy_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main smug3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_angry_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main smugcl3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), "MC/oni/eyes/e_closed_1.webp",
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_open_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_angry_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)

image side main evil3 = Transform(
    Composite(
        (800, 1400),
        (-20, -140), "MC/side_oni_background.png",
        (260, 0), "MC/oni/base.png",                        # base

        (260, 0), "MC/oni/eyes/e_whites.webp",              # whites
        (260, 0), "MC/oni/eyes/e_iris_3.png",             # iris
        (260, 0), Animation(
            "MC/oni/eyes/e_half_1.webp", 4.5,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
            "MC/oni/eyes/e_open_1.webp", .75,
            "MC/oni/eyes/e_half_1.webp", .25,
            "MC/oni/eyes/e_closed_1.webp", .25,
        ),
        (260, 0), WhileSpeaking(
            "main",
            Animation("MC/oni/mouth/m_smile_1.webp", .2, "MC/oni/mouth/m_open_smile_1.webp", .2),
            "MC/oni/mouth/m_open_smile_1.webp"
        ),
        (260, 0), "MC/oni/brow/b_angry_1.webp",            # brows
        (260, 0), "MC/horn_shadow.webp",
        (260, 0), "MC/melt.webp",
    ),
    zoom=0.31
)
