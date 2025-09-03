############# LOOP 2 WHERE ONE DIED ###########################
label loop2_hikaru_mandatory1:

    n " loop 2 hikaru m1 Location: Forest Day"

    $ loop2_hikaru_mandatory1 = True

    return

label loop2_hikaru_mandatory2:

    n " loop 2 hikaru m2 Location: Shrine Night"

    $ loop2_hikaru_mandatory2 = True

    return

label loop2_hikaru_mandatory3:

    n " loop 2 hikaru m3 Location: Shrine Day"

    $ loop2_hikaru_mandatory3 = True

    return

label loop2_hikaru_mandatory4:

    n " loop 2 hikaru m4 Location: Your House Day"

    $ loop2_hikaru_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear

    return
