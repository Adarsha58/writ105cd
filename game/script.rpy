screen simple_stats_screen:
    frame:
        xpos 0.1 ypos 0.05
        vbox:
            text "Food" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value food
                    range 100
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[food]% full" size 16

    frame:
        xpos 0.1 ypos 0.15
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
        xpos 0.1 ypos 0.25
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
        xpos 0.1 ypos 0.35
        vbox:
            text "Wallet: $[money]" size 22 xalign 0.5



define m = Character(_("Me"), color="#3d4dff")
define r = Character(_("Roommate"), color="#ff503d")


# The game starts here.
label start:
    $ money = renpy.random.randint(10, 30) * 1000 # between 10,000 and 30,000
    $ food = 100
    $ mental_health = 100
    $ gpa = 4.0
    $ loan = ""
    $ food_expense = 0
    $ roommate = renpy.random.randint(0, 2) # 0, 1, or 2 (2 is the best score)
    $ stress = 3

    show screen simple_stats_screen

    "It's your first day of college! Before beginning your academic life, you must figure out a few logistics first."
    "It appears you have $[money] budgeted for college, and you need to decide how to divy that up between tuition, loans, and food."
    "Tuition costs $4000 per year. Would you like to take out a loan?"
    menu:
        "No thanks":
            $ loan = "none"
        "Yes, $1500":
            $ loan = "small"
        "Yes, $3500":
            $ loan = "medium"
        "Yes, all $5000":
            $ loan = "all"
    "Good decision! Now how much do you want to spend on a meal plan?"
    menu:
        "I'll get the large meal plan for $1000 per year":
            $ food_expense = 1000
        "I'll get the small meal plan for $500 per year":
            $ food_expense = 500
        "None. I'll just eat out for $250 per year":
            $ food_expense = 250
        "None. I'll just cook at home for $100 per year":
            $ food_expense = 100
    "Good decision! Now that's all done with, so it's time to find your residence hall and meet your roommate!"
    # scene picture_of_munger_hall
    "It looks like you're living in Munger Hall. That's the new housing building, so it's gotta be great right?"
    "Apparently there's 4500 students living here. More like 4500 potential friends! Let's have a look inside."
    # scene inside_of_munger_hall
    "Hmmm, this is your room. I wonder if your roommate are here. You open the door and see what your room looks like."
    # scene picture_of_room
    "Huh, it's a bit smaller than expected."

    if roommate == 0:
        r "Hey, man!"
        m "Hey, I think we're roommates!"
        r "Yeah, that really sucks. Haha, just playing around."
        "Was he really playing around though?"
        r "Hey dude, I hope it's no problem, but I have a really big monitor so it's gonna have to take up both of our desks. \
            There's plenty of space on your bed or in the library if you wanna study."
        m "Uhh, yeah, no, um... that's not okay."
        r "Sorry dude, gamer's gotta game!"
        "Looks like this might be a problem."
    elif roommate == 1:
        m "Hey I think we're roommates!"
        r "Oh, cool."
        m "What's your major?"
        r "Undeclared."
        m "Oh nice, I'm Computer Science. Do you know what you wanna switch to?"
        r "No."
        "..."
        m "Okay then."
        "Looks like he's a little quiet, but at least his belongings are clean and organized."
    else:
        r "Hello!"
        m "Hey I think we're roommates!"
        r "Awesome, it's great to meet you. What's your major?"
        m "Computer Science, how about you?"
        r "No way, me too! We're probably gonna have a lot of the same classes so we should totally study together."
        m "Yeah for sure!"
        "Looks like you got very lucky with your roommate."

    # scene black_background
    "After sorting out everything in your room, you head to your first class. Unfortunately there's already assigned homework \
        Where would you like to study?"
    menu:
        "In your room":
            # scene picture_of_room
            "You go to your room and start studying for a bit."
            "..."
            "Quickly you encounter a few problems. There's no natural lighting so you can't see your notebook, \
                and it's really stuffy due to the lack of windows. It's really hard to study here."
            $ stress += 1
            if roommate == 0:
                "On top of that, you have to study on your bed since your roommate is taking up both desks, \
                    and you can hear him cursing at whatever dumb game he's playing."
                $ stress += 1
            "Maybe you wanna study somewhere else?"
            menu:
                "In the study lounge area":
                    jump study_lounge
                "In the library":
                    jump study_library
        "In the study lounge area":
            jump study_lounge
        "In the library":
            jump study_library

label study_lounge:
    # scene picture_of_lounge
    "You go to your dorm's lounge to start studying for a bit."
    "..."
    "There's too many people here and the lounge is too small, so there's no place for you to sit. \
        Maybe just go to the library."
    $ stress += 1
    jump study_library

label study_library:
    # scene picture_of_library
    "You go to the library. It's quiet and there's a lot of space to sit."
    if roommate == 0:
        "You don't see anyone familiar, so you just sit alone."
    elif roommate == 1:
        "Oh look, it's your roommate."
        m "Hey, roommate!"
        "He looks at you and nods."
        m "Mind if I sit with you?"
        r "Sure."
        "You sit with your roommate, mostly in silence but with the occassional comment."
        $ stress -= 1
    elif roommate == 2:
        "Oh look, it's your roommate."
        r "Hello! What brings you here?"
        m "Oh hey! I just got some homework from my last class to do."
        r "Ah, starting early I see. Let's sit together."
        "You sit with your roommate and talk for a lot of the time (quietly of course, it's a library.)"
        $ stress -= 2
    "..."
    "Eventually, you get your homework done, and you decide to head back to your dorm."


    # Maybe some other event here in your dorm that highlights another problem with Munger Hall
    # For example: the fire alarm goes off and it's really hard to get out, or the long and steep trek to the Hall,
    #   or 'strange placement of amenities' detailed in the Daily Nexus article, or just general feeling of isolation


    # scene black_background
    "Several weeks go by."
    if stress >= 2:
        "School is already pretty stressful."
    elif stress >= 0:
        "School is starting to stress you out just a little bit."
    else:
        "School is very easy, and you're not really stressed."
    "Your dorm isn't that great, as you've discovered from talking to others who live closer to campus."
    if roommate == 0:
        "Your roommate sitation isn't good either. You've tried to resolve some of the problems, \
            but he's just blantantly inconsiderate."
    elif roommate == 1:
        "Your roommate sitation is decent. He's a quiet guy, but at least he doesn't get in the way \
            and is relatively agreeable."
    else:
        "Your roommmate situation is fantastic. He's already one of your best friends, which makes it \
            very easy to communicate and resolve disagreements."
    "Speaking of roommates, you've heard that housing is very competitive, and other students \
         have already started looking for housing for next year. Maybe you should start too."
    "At the same time, you're very busy studying for finals next week. What do you wanna do?"
    menu:
        "Start looking for housing":
            $ stress += 1
            # Talk with your roommate. You don't wanna live with bad roommate, you do wanna live with good roommate,
            # and you're given a choice to live with medium roommate. There is a chance that your roommate has also
            # already decided where they're living.

            # Pick between living in IV or campus housing. If IV, choose housing now and require security deposit.
            # If housing, wait until later in year before revealing where you live. There is a chance you don't get
            # a housing contract, which jumps to the "Wait until later" option.
        "Wait until later":
            $ stress = 0 # just so this compiles for now
            # Similar talk with roommate. Now you have to live in IV, hotels, or downtown. And there's a lot less options



    hide screen simple_stats_screen

    "bye"
