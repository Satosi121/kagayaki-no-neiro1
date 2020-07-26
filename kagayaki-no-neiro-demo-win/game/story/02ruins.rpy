
label _02ruins:

    scene bg haikyo with Fade(0.5, 1.0, 1.0)
    show ku at left3 with moveinleft

    show bg haikyo darken
    show ku darken
    with dissolve
    na "I earnestly ran through the trees."
    na "And I stumbled across some large ruins."

    na "Several collapsed buildings stand side by side, with countless trees growing around it. Weeds growing through the rough, forgotten sidewalk."

    show ku with dissolve
    ku2 "Looking around, there seems to be no signs of people."

    show bg haikyo
    show ku surprised1
    with dissolve
    ku "These ruins... where am...?"

    show bg haikyo darken
    show ku openm
    with dissolve
    ku2 "I remembered. I've read about this in a book, a long time ago."

    hide ku

    call update_volume ('city_quiet', 0.4, 2.0)
    nvl clear

    nv "Although these are now ruins, this is the city of the Aecets." with dissolve
    nv "The Aecet people had features very similar to those of humans."
    nv "They were an indigenous tribe of this island, and their culture was very strongly tied to music. They were very advanced, and could use various sounds to create miracles."
    nv "They were conservative, and lived quietly here."
    nvl clear
    nv "But when humans came to the island, a war broke out."
    nv "And although the Aecets were very intelligent, the humans were far superior in number. They couldn't even scratch them. The humans have won that battle."
    nv "With the war, the Aecets became extinct."
    nvl clear

    call city_toggle ('city_calm')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
