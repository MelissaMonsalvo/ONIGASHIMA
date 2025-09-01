############# LOOP 2 WHERE ONE DIED ###########################
label loop2_hikaru_mandatory1:

    n " Location: Forest Day"

    $ loop2_hikaru_mandatory1 = True

    return

label loop2_hikaru_mandatory2:

    n " Location: Shrine Night"

    $ loop2_hikaru_mandatory2 = True

    return

label loop2_hikaru_mandatory3:

    n " Location: Shrine Day"

    $ loop2_hikaru_mandatory3 = True

    return

label loop2_hikaru_mandatory4:

    n " Location: Your House Day"

    $ loop2_hikaru_mandatory4 = True

    ## all characters vanish from map, but the ghost still appear

    return
