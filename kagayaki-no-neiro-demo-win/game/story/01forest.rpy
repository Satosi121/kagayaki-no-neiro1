
label _01forest:

    scene bg death_forest with fade
    call play_city ('city_calm')
    play sound run1
    with Pause(2.0)


    show ku nsei with moveinleft
    show bg death_forest darken with dissolve
    ku2 "I wonder if the iron witch is still following me."

    show ku nsei darken with dissolve
    na "The witch's obsession was troublesome."
    na "I have been chased by her countless times. I shook her off my trail every time."
    na "But only shaking her off is not enough."
    na "Until she gets what she wants, She will keep on chasing."


    show ku nsei with dissolve
    ku2 "I will NEVER hand over the Red Stone."
    window hide



    play sound run2
    show ku nsei at offscreenright with MoveTransition(0.2)
    stop music fadeout 1.0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
