screen simple_stats_screen:
    frame:
        xalign 0.15 yalign 0.05
        vbox:
            text "Food" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value food
                    range 100
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[food]% full" size 16

    frame:
        xalign 0.15 yalign 0.15
        vbox:
            text "Mental Heath" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value mental_health
                    range 100
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[mental_health]%" size 16

    frame:
        xalign 0.15 yalign 0.25
        vbox:
            text "GPA" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value gpa
                    range 4
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[mental_health] out of 4.0" size 16

    frame:
        xalign 0.15 yalign 0.35
        vbox:
            text "Wallet: $[money]" size 22 xalign 0.5

# The game starts here.
label start:
    $ money = 10000
    $ food = 100
    $ mental_health = 100
    $ gpa = 4.0



    show screen simple_stats_screen

    "hello"

    hide screen simple_stats_screen

    "bye"
