image side main normal = Transform(
    LiveComposite(
        (800, 1400),
        (-20, -140), "MC/side_normal_background.png",
        (260, 0), "MC/mc/base.png",                        # base
        (260, 0), "MC/mc/brow/b_angry_01.webp",            # brows
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
        )
    ),
    zoom=0.31
)
