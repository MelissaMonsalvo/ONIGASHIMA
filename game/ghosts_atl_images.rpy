#image ghost_hikaru_idle = "Ghosts/ghost_hikaru_idle.webp"

#scene here
image black_screen = "#000"

#hikaru image
image ghost_hikaru idle = Composite(
    (6118, 5846),
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_torso_idle.webp", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.webp", 4.25,
            "images/sprite_hikaru_ghost/ghost_torso_idle.webp", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.webp", .25,
        ),
    (0,0),"images/sprite_hikaru_ghost/ghost_legs.webp",
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_bang.webp", 4.25,
            "images/sprite_hikaru_ghost/ghost_bang2.webp", .25,
            "images/sprite_hikaru_ghost/ghost_bang.webp", .25,
            "images/sprite_hikaru_ghost/ghost_bang2.webp", .25,
        ))

image ghost_hikaru normal = Composite(
    (6118, 5846),
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_torso_idle.webp", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.webp", 4.25,
            "images/sprite_hikaru_ghost/ghost_torso_idle.webp", .25,
            "images/sprite_hikaru_ghost/ghost_torso_idle1.webp", .25,
        ),
    (0,0),"images/sprite_hikaru_ghost/ghost_legs.webp",
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_bang.webp", 4.25,
            "images/sprite_hikaru_ghost/ghost_bang2.webp", .25,
            "images/sprite_hikaru_ghost/ghost_bang.webp", .25,
            "images/sprite_hikaru_ghost/ghost_bang2.webp", .25,
        ),
)


image ghost_hikaru attack = Composite(
    (6118, 5846),
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_torso_attack0.webp", .25,
            "images/sprite_hikaru_ghost/ghost_torso_attack1.webp", 4.25,
            "images/sprite_hikaru_ghost/ghost_torso_attack0.webp", .25,
            "images/sprite_hikaru_ghost/ghost_torso_attack1.webp", .25,
        ),
    (0,0),"images/sprite_hikaru_ghost/ghost_legs.webp",
    (0,0), Animation(
            "images/sprite_hikaru_ghost/ghost_bang.webp", 4.25,
            "images/sprite_hikaru_ghost/ghost_bang2.webp", .25,
            "images/sprite_hikaru_ghost/ghost_bang.webp", .25,
            "images/sprite_hikaru_ghost/ghost_bang2.webp", .25,
        ),
)



#shiori image
image ghost_shiori normal = Composite(
    (4265, 5166),
    (0,0),"images/sprite_shiori_ghost/tail_spit.webp",
    (0,0),"images/sprite_shiori_ghost/tail_base.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.webp", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.webp", .25,
            "images/sprite_shiori_ghost/tail_mouth.webp", .5,
            "images/sprite_shiori_ghost/tail_mouth2.webp", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/ear_left.webp",
    (0,0),"images/sprite_shiori_ghost/ear_right.webp",
    (0,0),"images/sprite_shiori_ghost/body_idle.webp",

    (0,0), Animation(
            "images/sprite_shiori_ghost/mouth.webp", 4.5,
            "images/sprite_shiori_ghost/mouth1.webp", .25,
            "images/sprite_shiori_ghost/mouth2.webp", .25,
            "images/sprite_shiori_ghost/mouth1.webp", .25,
        ),
)

image ghost_shiori idle = Composite(
    (4265, 5166),
    (0,0),"images/sprite_shiori_ghost/tail_spit.webp",
    (0,0),"images/sprite_shiori_ghost/tail_base.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.webp", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.webp", .25,
            "images/sprite_shiori_ghost/tail_mouth.webp", .5,
            "images/sprite_shiori_ghost/tail_mouth2.webp", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/ear_left.webp",
    (0,0),"images/sprite_shiori_ghost/ear_right.webp",
    (0,0),"images/sprite_shiori_ghost/body_idle.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/mouth.webp", 4.5,
            "images/sprite_shiori_ghost/mouth1.webp", .25,
            "images/sprite_shiori_ghost/mouth2.webp", .25,
            "images/sprite_shiori_ghost/mouth1.webp", .25,
        ),
)

image ghost_shiori attack = Composite(
    (4265, 5166),
    (0,0),"images/sprite_shiori_ghost/tail_spit.webp",
    (0,0),"images/sprite_shiori_ghost/tail_base.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.webp", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.webp", .25,
            "images/sprite_shiori_ghost/tail_mouth.webp", .5,
            "images/sprite_shiori_ghost/tail_mouth2.webp", .25,
        ),

    (0,0),"images/sprite_shiori_ghost/ear_left.webp",
    (0,0),"images/sprite_shiori_ghost/ear_right.webp",
    (0,0),"images/sprite_shiori_ghost/body_attack.webp",
    (0,0),"images/sprite_shiori_ghost/attack_arm_hand.webp",
    (0,0),"images/sprite_shiori_ghost/attack_arm_left.webp",
    (0,0), Animation(
            "images/sprite_shiori_ghost/attack_arm_right.webp", 4.5,
            "images/sprite_shiori_ghost/attack_arm_right1.webp", .25,
            "images/sprite_shiori_ghost/attack_arm_right.webp", .5,
            "images/sprite_shiori_ghost/attack_arm_right1.webp", .25,
        ),


    (0,0), Animation(
            "images/sprite_shiori_ghost/mouth.webp", 4.5,
            "images/sprite_shiori_ghost/mouth1.webp", .25,
            "images/sprite_shiori_ghost/mouth2.webp", .25,
            "images/sprite_shiori_ghost/mouth1.webp", .25,
        ),
)



#yamato image

#image ghost_yamato_idle = "Ghosts/ghost_yamato_idle.webp"
image ghost_yamato idle = Composite(
    (6062, 7035),
    (0,0),"images/sprite_yamato_ghost/tendril_1.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_2.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_3.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_4.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_5.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/tail.webp", 4.5,
            "images/sprite_yamato_ghost/tail2.webp", .25,
            "images/sprite_yamato_ghost/tail.webp", .5,
            "images/sprite_yamato_ghost/tail2.webp", .25,
        ),
    (0,0),"images/sprite_yamato_ghost/torso_idle.webp",
    (0,0),"images/sprite_yamato_ghost/legs.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/arm_idle.webp", 4.5,
            "images/sprite_yamato_ghost/arm_idle1.webp", .25,
            "images/sprite_yamato_ghost/arm_idle.webp", .25,
            "images/sprite_yamato_ghost/arm_idle1.webp", .25,
        ),
)
image ghost_yamato normal = Composite(
    (6062, 7035),
    (0,0),"images/sprite_yamato_ghost/tendril_1.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_2.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_3.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_4.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_5.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/tail.webp", 4.5,
            "images/sprite_yamato_ghost/tail2.webp", .25,
            "images/sprite_yamato_ghost/tail.webp", .5,
            "images/sprite_yamato_ghost/tail2.webp", .25,
        ),
    (0,0),"images/sprite_yamato_ghost/torso_idle.webp",
    (0,0),"images/sprite_yamato_ghost/legs.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/arm_idle.webp", 4.5,
            "images/sprite_yamato_ghost/arm_idle1.webp", .25,
            "images/sprite_yamato_ghost/arm_idle.webp", .25,
            "images/sprite_yamato_ghost/arm_idle1.webp", .25,
        ),
)
image ghost_yamato attack = Composite(
    (6062, 7035),
    (0,0),"images/sprite_yamato_ghost/tendril_1.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_2.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_3.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_4.webp",
    (0,0),"images/sprite_yamato_ghost/tendril_5.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/tail.webp", 4.5,
            "images/sprite_yamato_ghost/tail2.webp", .25,
            "images/sprite_yamato_ghost/tail.webp", .5,
            "images/sprite_yamato_ghost/tail2.webp", .25,
        ),
    (0,0),"images/sprite_yamato_ghost/torso_attack.webp",
    (0,0),"images/sprite_yamato_ghost/mouth_attack.webp",
    (0,0),"images/sprite_yamato_ghost/legs.webp",
    (0,0), Animation(
            "images/sprite_yamato_ghost/arm_attack.webp", 4.5,
            "images/sprite_yamato_ghost/arm_attack2.webp", .25,
            "images/sprite_yamato_ghost/arm_attack.webp", .25,
            "images/sprite_yamato_ghost/arm_attack2.webp", .25,
        ),
)

## ATLS FOR GHOSTS ARE HERE ###
