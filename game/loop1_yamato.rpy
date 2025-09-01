label loop1_yamato:

    ## YAMATO'S ROUTE GOES HERE FOR LOOP 1 AFTER CLEARING ALL MANDATORY EVENTS

    $ persistent.yamato_dies = True

    ## at the end of the route yamato dies

    $ persistent.loop1 = True

    $ persistent.trueending.unlocked = False

    yamato "I ded."

    ## if any character dies in loop 1, you are locked out of true ending and must play again until everyone is revived

    return
