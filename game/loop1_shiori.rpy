label loop1_shiori:

    ## SHIORI'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS OR DEFAULT ROUTE IF YOU DIDN'T UNLOCK YAMATO AND HIKARU

    $ persistent.shiori_dies = True

    ## at the end of the route shiori dies
    shiori "nuuuu"

    $ persistent.loop1 = True

    $ persistent.trueending.unlocked = False

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
