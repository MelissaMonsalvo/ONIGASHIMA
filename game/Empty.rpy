label empty_village_Day:
    scene village day:
        zoom 0.5
    n "No one is here..."
    jump map
    return

label empty_village_Night:
    scene village night:
        zoom 0.5
    n "No one is here..."
    stop music
    scene black
    with fade
    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    jump map
    return

label empty_house_Day:
    scene house day:
        zoom 0.5
    n "No one is here..."
    jump map
    return

label empty_house_Night:
    scene house night:
        zoom 0.5
    n "No one is here..."
    stop music
    scene black
    with fade
    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    jump map
    return

label empty_forest_Day:
    scene forest day:
        zoom 0.5
    n "No one is here..."
    jump map
    return

label empty_forest_Night:
    scene forest night:
        zoom 0.5
    n "No one is here..."
    stop music
    scene black
    with fade
    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    jump map
    return

label empty_shrine_Day:
    scene shrine day:
        zoom 0.5
    n "No one is here..."
    jump map
    return

label empty_shrine_Night:
    scene shrine night:
        zoom 0.5
    n "No one is here..."
    stop music
    scene black
    with fade
    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    jump map
    return

label empty_dojo_Day:
    scene dojo day:
        zoom 0.5
    n "No one is here..."
    jump map
    return

label empty_dojo_Night:
    scene dojo night:
        zoom 0.5
    n "No one is here..."
    stop music
    scene black
    with fade
    if current_Day == 1:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}SIX DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon1
        with fade
        pause 0.2
        scene moon2
        with fade

        stop sound
    if current_Day == 2:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FIVE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon2
        with fade
        pause 0.2
        scene moon3
        with fade

        stop sound
    if current_Day == 3:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}FOUR DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    if current_Day == 4:
        pause 0.3

        play sound "sfx/day change.mp3"

        centered "{color=#9a0000}{atl=0.3,drop_text~#~ 1.5, bounce_text~5}{color=#FF0000}THREE DAYS UNTIL THE NEXT RED MOON{/color}{/atl}{/color}"

        with fade

        pause 0.5

        scene moon3
        with fade
        pause 0.2
        scene moon4
        with fade

        stop sound
    jump map
    return
