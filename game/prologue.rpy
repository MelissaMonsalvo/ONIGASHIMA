label prologue:

    $ loop1_shiori_mandatory1 = True
    $ loop1_shiori_mandatory2 = True
    $ loop1_shiori_mandatory3 = True
    $ loop1_shiori_mandatory4 = True
    $ loop1_shiori_mandatory5 = True

    $ loop1_yamato_mandatory1 = True
    $ loop1_yamato_mandatory2 = True
    $ loop1_yamato_mandatory3 = True
    $ loop1_yamato_mandatory4 = True
    $ loop1_yamato_mandatory5 = True

    $ loop1_hikaru_mandatory1 = True
    $ loop1_hikaru_mandatory2 = True
    $ loop1_hikaru_mandatory3 = True
    $ loop1_hikaru_mandatory4 = True
    $ loop1_hikaru_mandatory5 = True

    ### this has the prologue before

    n "This is the very first prologue."

    ### there's a name input here, please also code the name input screen when the UI is made later

label get_player_name:

    ## player name is persistent
    ## you only name player ONLY ONCE, that name is used all across all loops until true ending is unlocked
    ## you can rename mc again after you have seen the true ending
    ## let me know if this logic breaks

    # Name input screen logic
    if persistent.player_name and not persistent.seen_true_end:
        # Skip input, already set and no good ending yet
        n "..."
    else:
        # Name input only if first time or after good ending
        $ player_name = renpy.input("Say your name out loud.", length=8)
        $ player_name = player_name.strip()
        if player_name == "":
            $ player_name = "Kagami"

        $ persistent.player_name = player_name
        $ persistent.seen_true_end = False  # Reset good_end status on new game

        n "Understood, [persistent.player_name]. That's your name."

    mc "Hi, I'm [persistent.player_name]!"


    ## jump to loop 1 map system

    return
