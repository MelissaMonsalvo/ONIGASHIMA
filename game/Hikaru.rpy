transform hikaru_zoom:
    zoom 0.231
    xanchor 0.5
    yalign -0.09
    xzoom 1.0
    yzoom 1.0
    yoffset 460

image hik normal = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
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
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )

image hik happy = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
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
    (0,0), "Hikaru/brow/b_happy.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_smile.webp", .2, "Hikaru/mouth/m_smile_open.webp", .2),
            "Hikaru/mouth/m_smile_open.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )
image hik happycl = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), "Hikaru/eye/e_closed.webp",
    (0,0), "Hikaru/brow/b_happy.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_smile.webp", .2, "Hikaru/mouth/m_smile_open.webp", .2),
            "Hikaru/mouth/m_smile.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )
image hik smilesad = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_normal.webp", .5,
            "Hikaru/eye/e_half.webp", 4.25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_sad.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_smile.webp", .2, "Hikaru/mouth/m_smile_open.webp", .2),
            "Hikaru/mouth/m_smile.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )
image hik smileblush = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_normal.webp", .5,
            "Hikaru/eye/e_half.webp", 4.25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_happy.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_smile.webp", .2, "Hikaru/mouth/m_smile_open.webp", .2),
            "Hikaru/mouth/m_smile.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),
    (0,0), "Hikaru/extra/ex_blush.webp"

    )
image hik sad = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), "Hikaru/eye/e_closed.webp",
    (0,0), "Hikaru/brow/b_sad.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_neutral.webp", .2, "Hikaru/mouth/m_neutral_open.webp", .2),
            "Hikaru/mouth/m_neutral.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )

image hik blush = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_wide.webp", .5,
            "Hikaru/eye/e_half.webp", 4.25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_sad.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_neutral.webp", .2, "Hikaru/mouth/m_neutral_open.webp", .2),
            "Hikaru/mouth/m_neutral.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )

image hik cry = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_normal_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), "Hikaru/eye/e_closed.webp",
    (0,0), "Hikaru/brow/b_fear.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_angry.webp", .2, "Hikaru/mouth/m_angry_open.webp", .2),
            "Hikaru/mouth/m_angry.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),
    (0,0), "Hikaru/extra/ex_tears.webp"

    )

image hik madcry = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_wide.webp", 4.5,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_angry.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_angry.webp", .2, "Hikaru/mouth/m_angry_open.webp", .2),
            "Hikaru/mouth/m_angry_open.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),
    (0,0), "Hikaru/extra/ex_tears.webp"

    )
image hik worried = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), Animation(
            "Hikaru/eye/e_normal.webp", 4.5,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), "Hikaru/eye/e_closed.webp",
    (0,0), "Hikaru/brow/b_sad.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_surprised.webp", .2, "Hikaru/mouth/m_surprised_open.webp", .2),
            "Hikaru/mouth/m_surprised.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        ),

    )
image hik surprised = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_wide.webp", 4.5,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_happy.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_neutral.webp", .2, "Hikaru/mouth/m_neutral_open.webp", .2),
            "Hikaru/mouth/m_neutral_open.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
image hik shocked = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_wide.webp", 4.5,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_fear.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_shout.webp", .2, "Hikaru/mouth/m_shout_open.webp", .2),
            "Hikaru/mouth/m_shout.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
image hik serious = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_normal.webp", .5,
            "Hikaru/eye/e_half.webp", 4.45,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_angry.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_neutral.webp", .2, "Hikaru/mouth/m_neutral_open.webp", .2),
            "Hikaru/mouth/m_neutral.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
image hik angry = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_normal.webp", 4.5,
            "Hikaru/eye/e_half.webp", .45,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_angry.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_angry.webp", .2, "Hikaru/mouth/m_angry_open.webp", .2),
            "Hikaru/mouth/m_angry.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
image hik angry2 = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris_small.webp",             # iris
    (0,0), "Hikaru/eye/e_closed.webp",
    (0,0), "Hikaru/brow/b_angry.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_angry.webp", .2, "Hikaru/mouth/m_angry_open.webp", .2),
            "Hikaru/mouth/m_angry.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
image hik rage = Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_wide.webp", 4.5,
            "Hikaru/eye/e_half.webp", .45,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_angry.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_shout.webp", .2, "Hikaru/mouth/m_shout_open.webp", .2),
            "Hikaru/mouth/m_shout_open.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
image hik panic= Composite(
    (3139,6112),
    (-200,0), Animation(
            "Hikaru/wings/wing_left1.webp", 4.5,
            "Hikaru/wings/wing_left2.webp", .25,
            "Hikaru/wings/wing_left3.webp", .25,
            "Hikaru/wings/wing_left2.webp", 2.25,
            "Hikaru/wings/wing_left1.webp", .25,
            "Hikaru/wings/wing_left2.webp", .25,
        ),
    (-200,0), Animation(
            "Hikaru/wings/wing_right1.webp", 4.5,
            "Hikaru/wings/wing_right2.webp", .25,
            "Hikaru/wings/wing_right3.webp", .25,
            "Hikaru/wings/wing_right2.webp", 2.25,
            "Hikaru/wings/wing_right1.webp", .25,
            "Hikaru/wings/wing_right2.webp", .25,
        ),

    (0,0), "Hikaru/body.webp",

    (0,0), "Hikaru/eye/e_wide_white.webp",              # whites
    (0,0), "Hikaru/eye/e_iris_small.webp",             # iris
    (0,0), Animation(
            "Hikaru/eye/e_wide.webp", 4.5,
            "Hikaru/eye/e_half.webp", .45,
            "Hikaru/eye/e_closed.webp", .25,
            "Hikaru/eye/e_normal.webp", .75,
            "Hikaru/eye/e_half.webp", .25,
            "Hikaru/eye/e_closed.webp", .25,
        ),
    (0,0), "Hikaru/brow/b_fear.webp",
    (0,0),  ConditionSwitch(
    "hmask == False", WhileSpeaking(
            "hika",
            Animation("Hikaru/mouth/m_panic.webp", .2, "Hikaru/mouth/m_panic_open.webp", .2),
            "Hikaru/mouth/m_panic_open.webp"
        ),
    "True", "Hikaru/items/mask.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_bottom.webp"),
    (0,0),  ConditionSwitch(
    "hsword == False", "Hikaru/items/empty.webp",
    "True", "Hikaru/items/weapon_top.webp"),
    (0,0), Animation(
            "Hikaru/bangs1.webp", 4.5,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs3.webp", 2.25,
            "Hikaru/bangs2.webp", .25,
            "Hikaru/bangs1.webp", .25,
            "Hikaru/bangs2.webp", .25,
        )

    )
