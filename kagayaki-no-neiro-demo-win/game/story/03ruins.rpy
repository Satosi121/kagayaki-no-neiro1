
label _03ruins:

    scene bg haikyo darken with dissolve
    with Pause(1.0)

    show ku at left3 with dissolve
    with Pause(0.5)
    ku2 "However, did the Aecet tribe really exist?"

    show ku darken with dissolve
    call update_volume ('ocarina', 0.8, 0)
    call update_volume ('city_calm', 0.5, 2.0)
    play ocarina '1' noloop
    na "I kept walking around, and I heard the beautiful sound of an ocarina."


    na "That soothing song was the Song of Life."
    na "The special Aecet tribe's song that activated the Red Stone."




    show ae black at right1 with moveinright
    na "I stopped walking."
    stop ocarina fadeout 2.0
    call update_volume ('city_calm', 1.0, 2.0)
    with Pause(1.0)
    call update_volume ('ocarina', 1.0, 2.0)

    show ae black at right2 with move
    show ae
    show ku openm
    with dissolve
    na "The moment I saw that girl's back and white hair, I thought... No way."




    show bg haikyo with dissolve

    show ae odoroi
    show ku surprised1
    ae "A person! Are they human!?"

    show bg haikyo darken
    show ku openm darken
    show ae odoroi darken
    with dissolve
    na "I looked again closely."




    show ku openm with dissolve
    ku2 "An Aecet! It's an Aecet girl,{w=1.0} with an ocarina hanging by a thread on her neck."

    show ku openm darken with dissolve
    na "The Aecet tribe is a race that resembles humans, but with pure white skin, pure white hair, and crimson eyes."

    na "But, I thought something was strange."
    na "For religious reasons, Aecets tattooed their children's bodies with red markings shortly after birth."
    na "They think feelings like hatred, jealousy and greed are bad for their spirits."
    na "Negative energies are constantly floating through the air."
    na "Aecets say they gradually invade the body and pollute the spirit."
    na "Since they consider the mind holy, they give their children a sacred tattoo to protect it from these evils."

    show ku with dissolve
    ku2 "But there are no tattoos on this girl. Not on the face, not on the arms, and not on the legs."


    call update_volume ('city_per', 0.5, 2.0)
    show ae stance at right2
    show ku openm at left3
    with dissolve
    ae "An enemy of our people! I will not forgive you!"

    na "Although this was our first time meeting, her reaction was just natural."
    na "A long time ago, Humans killed her people."
    na "Mankind is the enemy of the Aecets... It was unavoidable."

    window hide
    with Pause(0.2)

    play sound swing_first
    show ae attack:
        right2
        easeout 0.3 left2

    show ku openm behind ae:
        left3
        pause 0.1
        "ku surprised1"
        xzoom -1.0
        easeout_quad 0.3 right3
    with Pause(0.2)
    with flash
    ae "Ggraaaah!!"

    show ae stance darken:
        left3
        xzoom -1.0
    show ku surprised1 darken:
        right3
        xzoom -1.0
    with dissolve

    na "The girl approached with a strike and swung her weapon repeatedly at me."
    na "I swiftly avoided the attacks."
    play sound swing_several
    na "She kept repeatedly striking me with hostility,{w=1.0} without being able to land a hit."

    play sound swing_last
    call city_toggle ('city_calm')
    scene cg ruins with fade
    na "After avoiding her many times, I am finally able to grab her by her wrist."


    ku "Wait! I didn't do anything!"

    na "Since she then reached out to the sword on my waist, I had to thrust her away, and she ended up falling to the ground."
    play sound thud

    scene bg haikyo
    show ku at left3
    with fade

    show ae hurt:
        pos (0.8, 2.0)
    show ae hurt at right2 with MoveTransition(1.5)
    ae "Ugh..."

    show bg haikyo darken
    show ae hurt darken
    show ku darken
    with dissolve
    na "The hostility could not simply disappear."
    na "Grabbing her arm, I kept staring at her burning eyes."
    na "Somehow I want us to understand each other."
    na "I may have finally found one of the Aecets that I was looking for."
    na "But I don't know how we could do that."
    na "An angry minded girl will not listen to any words."
    show ku hazu with dissolve
    na "--{w=0.5}It was then that I became embarrassed."


    show ku openm with dissolve
    call update_volume ('city_calm', 0.0, 2.0)
    play ocarina '2'
    na "Suddenly, like a groaning, ghostly moan, a creepy melody sounded throughout the ruins."


    show ae ears at shaking(right2)
    show bg haikyo zawarudo
    show ku zawarudo
    with za_warudo
    with Pause(0.2)

    show bg haikyo
    show ku surprised1
    with za_warudo
    ae "Urk...!"

    na "The girl, trembling on the spot, blocked her ears."

    ku "What's wrong?! Are you okay?!"


    ae "Stop it...... Stop it......."

    play sound thud
    show ae ears:
        pos (0.8, 2.0)
    with move
    show bg haikyo darken
    show ku openm darken
    with dissolve
    na "She crouched and collapsed to the ground."


    scene c_black with fade
    stop ocarina fadeout 1.0
    call stop_city
    with Pause(1.0)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
