label prologue_loop3:

    ### this has the prologue after everyone has devoured

    n "Everyone are dead."

    menu:
        "Repent?"

        "Yes":
            $ persistent.trueending.unlocked = True

            ### EVERYTHING IS HARD RESET
            $ persistent.shiori_dies = False
            $ persistent.yamato_dies = False
            $ persistent.hikaru_dies = False

            $ persistent.loop1 = False
            $ persistent.loop2 = False
            $ persistent.loop3 = False 

            $ persistent.loop2_shiori_ghost1 = False
            $ persistent.loop2_shiori_ghost2 = False
            $ persistent.loop2_shiori_ghost3 = False
            $ persistent.loop2_shiori_ghost4 = False
            $ persistent.loop2_shiori_ghost5 = False

            $ persistent.loop2_yamato_ghost1 = False
            $ persistent.loop2_yamato_ghost2 = False
            $ persistent.loop2_yamato_ghost3 = False
            $ persistent.loop2_yamato_ghost4 = False
            $ persistent.loop2_yamato_ghost5 = False

            $ persistent.loop2_hikaru_ghost1 = False
            $ persistent.loop2_hikaru_ghost2 = False
            $ persistent.loop2_hikaru_ghost3 = False
            $ persistent.loop2_hikaru_ghost4 = False
            $ persistent.loop2_hikaru_ghost5 = False

            n "Repent! Repent!"
            return
            ## after this, you are kicked to main menu and everyone are alive again
        "No.":
            n "........."
            ## crckets chirping, the village is empty for a long time
            jump uncomfortable_silence


    return

label uncomfortable_silence:

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    pause 0.3

    n "......"

    jump prologue_loop3
