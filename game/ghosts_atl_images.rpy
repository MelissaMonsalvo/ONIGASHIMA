#image ghost_hikaru_idle = "Ghosts/ghost_hikaru_idle.png"

#scene here
image black_screen = "images/black_screen.png"

#hikaru image
image ghost_hikaru_idle = "Ghosts/ghost_hikaru_idle.png"
image ghost_hikaru normal = Live Composite(
    (6118, 5846),
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughostdefault_body.PNG",
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughost_legs.PNG",
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughost_hairbang.PNG",
)

image ghost_hikaru attack = Live Composite(
    (6118, 5846),
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughostattack_body.PNG",
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughost_legs.PNG",
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughost_arm.PNG",
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughost_hairbang.PNG",
)

image ghost_hikaru idle = Live Composite(
    (4161, 5846),
    (0,0),"Ghosts/ghost_hikaru_idle.png",
)

image ghost_hikaru normal shadow = Live Composite(
    (6118, 5846),
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughostdefault_body_black.PNG",
    (0,0),"images/sprite_hikaru_ghost/sprite_hikarughost_legs_black.PNG",
)

image normal_hikaru normal = Live Composite(
    (3139, 6112),
    (0,0), "images/hikaru_rough1.png",
)

#shiori image
image ghost_shiori normal = Live Composite(
    (4265, 5166),
    (-2200,0), Animation(
            "images/sprite_shiori_ghost/tail_mouth.PNG", 4.5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
            "images/sprite_shiori_ghost/tail_mouth.PNG", .5,
            "images/sprite_shiori_ghost/tail_mouth2.PNG", .25,
        ),
    (0,0),"images/sprite_shiori_ghost/tail_base.PNG",
    (0,0),"images/sprite_shiori_ghost/body_idle.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighost_foxearleft.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighost_foxearright.PNG",
)

image ghost_shiori attack = Live Composite(
    (4265, 5166),
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighost_tail.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighostattack_body.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighost_foxearleft.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighost_foxearright.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighostattack_hand.PNG",
    (0,0),"images/sprite_shiori_ghost/sprite_shiorighost_mouth.PNG",
)



#image ghost_shiori_idle = "Ghosts/ghost_shiori_idle.png"
image ghost_shiori_idle = "Ghosts/ghost_shiori_idle.png"

#yamato image

#image ghost_yamato_idle = "Ghosts/ghost_yamato_idle.png"
image ghost_yamato_idle = "Ghosts/ghost_yamato_idle.png"




## ATLS FOR GHOSTS ARE HERE ###
