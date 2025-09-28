### GALLERY SCREEN ############################################################
##
##

############################################################
### PYTHON ###
############################################################
init python:
    ## NOTE: CGs defined in "define.rpy"

    ## First, some constants to speed up declarations

    ## The size of gallery buttons/thumbnails
    gallery_thumb_size = (415, 233)
    ## For convenience's sake: list off all the gallery image
    ## names we're going to use in this gallery
    gallery_buttons = [
        "shiori cg1",
        "shiori cg3",
        "yamato cg1",
        "yamato cg3",
        "hikaru cg1",
        "hikaru cg3",
        "cg final"
    ]

    ## Set up the gallery
    g = Gallery()
    g.locked_button = Composite(
        gallery_thumb_size,
        (0, 0), Transform("#000", xysize=gallery_thumb_size),
        (0.5, 0.5), Text("LOCKED", color=WHITE, font="NotoSerifJP-SemiBold.ttf", align=(0.5, 0.5))
    )

    ## And declare the various gallery images
    ## This file doesn't assume the presence of any GUI files, so I'm
    ## just using basic squares, declared as images below, but you will
    ## replace these with actual images.
    ## These use the names declared in the gallery_buttons list
    g.button("shiori cg1")
    g.unlock_image("cg_shioriloop1")

    g.button("shiori cg3")
    g.unlock_image("cg_loop3shiori")


    g.button("yamato cg1")
    g.unlock_image("cg_loop1yamato")

    g.button("yamato cg3")
    g.unlock_image("cg_loop3yamato")



    g.button("hikaru cg1")
    g.unlock_image("cg_loop1hikaru")

    g.button("hikaru cg3")
    g.unlock_image("cg_loop3hikarui")



    g.button("cg final")
    g.unlock_image("cg_trueending")

############################################################
### THUMBNAILS ###
############################################################
image cg final_thumb = "images/cg_trueending.png"
image shiori cg1_thumb = "images/cg_shioriloop1.png"
image hikaru cg1_thumb = "images/cg_loop1hikaru.png"
image yamato cg1_thumb = "images/cg_loop1yamato.png"
image hikaru cg3_thumb = "images/cg_loop3hikaru.png"
image shiori cg3_thumb = "images/cg_loop3shiori.png"
image yamato cg3_thumb = "images/cg_loop3yamato.png"
    
############################################################
### EXTRAS GALLERY ###
############################################################
screen extras_gallery():
    style_prefix "gal"

    grid 2 6:
  
        
        for btn in gallery_buttons:
            button:

                add g.make_button(btn, "{}_thumb".format(btn)) align (0.5, 0.5)

         

############################################################
### EXTRAS STYLES ###
############################################################
style gal_grid:
    spacing 50

style gal_button:
    xysize (480, 302)
    
    background "frame gal"
    hover_background "frame gal hover"
    insensitive_background Transform("frame gal", matrixcolor=ColorizeMatrix("#838383", "#838383"))

    padding (50, 50)

