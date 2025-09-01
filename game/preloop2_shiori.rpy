############# LOOP 2 WHERE ONE DIED ###########################
label loop2_shiori_mandatory1:

    n "loop 2 shiori m1 Location : Village Morning."

    $ loop2_shiori_mandatory1 = True

    return

label loop2_shiori_mandatory2:

    n "loop 2 shiori m2 Location : Shrine Morning."

    $ loop2_shiori_mandatory2 = True
    return

label loop2_shiori_mandatory3:

    n "loop 2 shiori m3 Location : Shrine Day."
    $ loop2_shiori_mandatory3 = True
    return

label loop2_shiori_mandatory4:

    n "loop 2 shiori m4 Location : Shrine Night."
    $ loop2_shiori_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear
    return
