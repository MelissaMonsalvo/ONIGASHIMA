label loop1_hikaru:

    ## HIKARU'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS

    $ persistent.hikaru_dies = True

    ## at the end of the route shiori dies

    hikaru "Blerrrrgh I die."

    $ persistent.loop1 = True

    $ persistent.trueending.unlocked = False

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
