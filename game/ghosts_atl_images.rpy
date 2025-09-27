#image ghost_hikaru_idle = "Ghosts/ghost_hikaru_idle.png"

#scene here
image black_screen = "images/black_screen.png"

#hikaru image
image ghost_hikaru idle = Live Composite(
    (6118, 5846),
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_torso_idle.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.PNG", 4.25,
            "images/sprite_hikaru_ghost/ghost_torso_idle.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.PNG", .25,
        ),
    (0,0),"images/sprite_hikaru_ghost/ghost_legs.webp"
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_bang.PNG", 4.25,
            "images/sprite_hikaru_ghost/ghost_bang2.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_bang.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_bang2.PNG", .25,
        )
image ghost_hikaru normal = Live Composite(
    (6118, 5846),
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_torso_idle.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.PNG", 4.25,
            "images/sprite_hikaru_ghost/ghost_torso_idle.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.PNG", .25,
        ),
    (0,0),"images/sprite_hikaru_ghost/ghost_legs.webp"
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_bang.PNG", 4.25,
            "images/sprite_hikaru_ghost/ghost_bang2.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_bang.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_bang2.PNG", .25,
        ),
)


image ghost_hikaru attack = Live Composite(
    (6118, 5846),
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_torso_attack0.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_torso_attack1.PNG", 4.25,
            "images/sprite_hikaru_ghost/ghost_torso_attack2.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_torso_attack1.PNG", .25,
        ),
    (0,0),"images/sprite_hikaru_ghost/ghost_legs.webp"
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_bang.PNG", 4.25,
            "images/sprite_hikaru_ghost/ghost_bang2.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_bang.PNG", .25,
            "images/sprite_hikaru_ghost/ghost_bang2.PNG", .25,
        ),
)



#shiori image
image ghost_shiori normal = Live Composite(
    (4265, 5166),
    (0,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
            "images/sprite_shiori_ghost/tail_mouth.PNG", .5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/tail_base.webp",
    (0,0),"images/sprite_shiori_ghost/body_idle.webp",
    (0,0),"images/sprite_shiori_ghost/ear_left.webp",
    (0,0),"images/sprite_shiori_ghost/ear_right.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/mouth1.PNG", .25,
            "images/sprite_shiori_ghost/mouth2.PNG", .25,
            "images/sprite_shiori_ghost/mouth1.PNG", .25,
        ),
)

image ghost_shiori idle = Live Composite(
    (4265, 5166),
    (0,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
            "images/sprite_shiori_ghost/tail_mouth.PNG", .5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/tail_base.webp",
    (0,0),"images/sprite_shiori_ghost/body_idle.webp",
    (0,0),"images/sprite_shiori_ghost/ear_left.webp",
    (0,0),"images/sprite_shiori_ghost/ear_right.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/mouth1.PNG", .25,
            "images/sprite_shiori_ghost/mouth2.PNG", .25,
            "images/sprite_shiori_ghost/mouth1.PNG", .25,
        ),
)

image ghost_shiori attack = Live Composite(
    (4265, 5166),
    (0,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
            "images/sprite_shiori_ghost/tail_mouth.PNG", .5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/tail_base.webp",
    (0,0),"images/sprite_shiori_ghost/body_attack.webp",
    (0,0),"images/sprite_shiori_ghost/attack_arm_hand.webp",
    (0,0),"images/sprite_shiori_ghost/attack_arm_left.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/attack_arm_right.PNG", 4.5,
            "images/sprite_shiori_ghost/attack_arm_right1.PNG", .25,
            "images/sprite_shiori_ghost/attack_arm_right.PNG", .5,
            "images/sprite_shiori_ghost/attack_arm_right1.PNG", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/ear_left.webp",
    (0,0),"images/sprite_shiori_ghost/ear_right.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/mouth1.PNG", .25,
            "images/sprite_shiori_ghost/mouth2.PNG", .25,
            "images/sprite_shiori_ghost/mouth1.PNG", .25,
        ),
)



#yamato image

#image ghost_yamato_idle = "Ghosts/ghost_yamato_idle.png"
image ghost_yamato idle = Live Composite(
    (6062, 7035),
    (0,0),"images/sprite_yamato_ghost/tendril_1.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_2.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_3.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_4.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_5.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/tail.PNG", 4.5,
            "images/sprite_yamato_ghost/tail2.PNG", .25,
            "images/sprite_yamato_ghost/tail.PNG", .5,
            "images/sprite_yamato_ghost/tail2.PNG", .25,
        ),
    (0,0),"images/sprite_yamato_ghost/torso_idle.webp",
    (0,0),"images/sprite_yamato_ghost/legs.webp",

    (0,0), Animation(
            "images/sprite_yamato_ghost/mouth.PNG", 4.5,
            "images/sprite_yamato_ghost/mouth1.PNG", .25,
            "images/sprite_yamato_ghost/mouth2.PNG", .25,
            "images/sprite_yamato_ghost/mouth1.PNG", .25,
        ),
    (0,0), Animation(
            "images/sprite_yamato_ghost/arm_idle1.PNG", 4.5,
            "images/sprite_yamato_ghost/arm_idle2.PNG", .25,
            "images/sprite_yamato_ghost/arm_idle1.PNG", .25,
            "images/sprite_yamato_ghost/arm_idle2.PNG", .25,
        ),
)
image ghost_yamato normal = Live Composite(
    (6062, 7035),
    (0,0),"images/sprite_yamato_ghost/tendril_1.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_2.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_3.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_4.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_5.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/tail.PNG", 4.5,
            "images/sprite_yamato_ghost/tail2.PNG", .25,
            "images/sprite_yamato_ghost/tail.PNG", .5,
            "images/sprite_yamato_ghost/tail2.PNG", .25,
        ),
    (0,0),"images/sprite_yamato_ghost/torso_idle.webp",
    (0,0),"images/sprite_yamato_ghost/legs.webp",

    (0,0), Animation(
            "images/sprite_yamato_ghost/mouth.PNG", 4.5,
            "images/sprite_yamato_ghost/mouth1.PNG", .25,
            "images/sprite_yamato_ghost/mouth2.PNG", .25,
            "images/sprite_yamato_ghost/mouth1.PNG", .25,
        ),
    (0,0), Animation(
            "images/sprite_yamato_ghost/arm_idle1.PNG", 4.5,
            "images/sprite_yamato_ghost/arm_idle2.PNG", .25,
            "images/sprite_yamato_ghost/arm_idle1.PNG", .25,
            "images/sprite_yamato_ghost/arm_idle2.PNG", .25,
        ),
)
image ghost_yamato attack = Live Composite(
    (6062, 7035),
    (0,0),"images/sprite_yamato_ghost/tendril_1.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_2.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_3.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_4.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_5.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/tail.PNG", 4.5,
            "images/sprite_yamato_ghost/tail2.PNG", .25,
            "images/sprite_yamato_ghost/tail.PNG", .5,
            "images/sprite_yamato_ghost/tail2.PNG", .25,
        ),
    (0,0),"images/sprite_yamato_ghost/torso_attack.webp",
    (0,0),"images/sprite_yamato_ghost/mouth_attack.webp",
    (0,0),"images/sprite_yamato_ghost/legs.webp",

    (0,0), Animation(
            "images/sprite_yamato_ghost/mouth.PNG", 4.5,
            "images/sprite_yamato_ghost/mouth1.PNG", .25,
            "images/sprite_yamato_ghost/mouth2.PNG", .25,
            "images/sprite_yamato_ghost/mouth1.PNG", .25,
        ),
    (0,0), Animation(
            "images/sprite_yamato_ghost/arm_attack1.PNG", 4.5,
            "images/sprite_yamato_ghost/arm_attack2.PNG", .25,
            "images/sprite_yamato_ghost/arm_attack1.PNG", .25,
            "images/sprite_yamato_ghost/arm_attack2.PNG", .25,
        ),
)

## ATLS FOR GHOSTS ARE HERE ###
