transform hikaru_zoom:
    zoom 0.231
    xanchor 0.5
    yalign -0.09
    xzoom 1.0
    yzoom 1.0
    yoffset 460

image hik normal = LiveComposite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.png", 4.5,
            "Hikaru/wings/wing_left2.png", .25,
            "Hikaru/wings/wing_left3.png", .25,
            "Hikaru/wings/wing_left2.png", 2.25,
            "Hikaru/wings/wing_left1.png", .25,
            "Hikaru/wings/wing_left2.png", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.png", 4.5,
            "Hikaru/wings/wing_right2.png", .25,
            "Hikaru/wings/wing_right3.png", .25,
            "Hikaru/wings/wing_right2.png", 2.25,
            "Hikaru/wings/wing_right1.png", .25,
            "Hikaru/wings/wing_right2.png", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_normal.webp", 4.5,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_neutral.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_neutral.webp", .2, "Hikaru/mouth/m_neutral_open.webp", .2),
            "Hikaru/mouth/m_neutral.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/weapon_bottom.webp",
    "True", "Hikaru/items/empty.png"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/weapon_top.webp",
    "True", "Hikaru/items/empty.png"),
    (0,0), Animation(
            "Hikaru/bangs1.png", 4.5,
            "Hikaru/bangs2.png", .25,
            "Hikaru/bangs3.png", 2.25,
            "Hikaru/bangs2.png", .25,
            "Hikaru/bangs1.png", .25,
            "Hikaru/bangs2.png", .25,
        ),

    )
