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
    $ tight_on_money = (money + food < 15000 and loan == "all") or (money + food  < 20000 and loan == "medium") or (money + food  < 25000 and loan == "small")
    "Good decision! Now that's all done with, so it's time to find your residence hall and meet your roommate!"
    scene picture_of_munger_hall
    "It looks like you're living in Munger Hall. That's the new housing building, so it's gotta be great right?"
    "Apparently there's 4500 students living here. More like 4500 potential friends! Let's have a look inside."
    scene inside_munger_hall
    "Hmmm, this is your room. I wonder if your roommate are here. You open the door and see what your room looks like."
    scene picture_of_room
    "Huh, it's a bit smaller than expected."

    show roommate
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
    hide roommate

    scene black_background
    "After sorting out everything in your room, you head to your first class. Unfortunately there's already assigned homework \
        Where would you like to study?"
    menu:
        "In your room":
            scene picture_of_room
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
    scene picture_of_lounge
    "You go to your dorm's lounge to start studying for a bit."
    "..."
    "There's too many people here and the lounge is too small, so there's no place for you to sit. \
        Maybe just go to the library."
    $ stress += 1
    jump study_library

label study_library:
    scene picture_of_library
    "You go to the library. It's quiet and there's a lot of space to sit."
    if roommate == 0:
        "You don't see anyone familiar, so you just sit alone."
    elif roommate == 1:
        "Oh look, it's your roommate."
        show roommate
        m "Hey, roommate!"
        "He looks at you and nods."
        m "Mind if I sit with you?"
        r "Sure."
        "You sit with your roommate, mostly in silence but with the occassional comment."
        $ stress -= 1
    elif roommate == 2:
        show roommate
        "Oh look, it's your roommate."
        r "Hello! What brings you here?"
        m "Oh hey! I just got some homework from my last class to do."
        r "Ah, starting early I see. Let's sit together."
        "You sit with your roommate and talk for a lot of the time (quietly of course, it's a library.)"
        $ stress -= 2
    hide roommate
    "..."
    "Eventually, you get your homework done, and you decide to head back to your dorm."


    # Maybe some other event here in your dorm that highlights another problem with Munger Hall
    # For example: the fire alarm goes off and it's really hard to get out, or the long and steep trek to the Hall,
    #   or 'strange placement of amenities' detailed in the Daily Nexus article, or just general feeling of isolation


    scene black_background
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
        "Your roommate situation is fantastic. He's already one of your best friends, which makes it \
            very easy to communicate and resolve disagreements."
    "Speaking of roommates, you've heard that housing is very competitive, and other students \
         have already started looking for housing for next year. Maybe you should start too."
    "At the same time, you're very busy studying for finals next week. What do you wanna do?"
    menu:
        "Start looking for housing":
            $ stress += 1
            if roommate == 0:
                "But who should you live with? You haven't had enough time to develop close enough friendships with anyone, \
                    and your current roommate is terrible. You decide to go random again."
                jump roommate_random
            elif roommate == 1:
                "But who should you live with? You haven't had enough time to develop close enough friendships with anyone. \
                    Your current roommate is decent; do you wanna ask him?"
                menu:
                    "Yes":
                        jump roommate_current
                    "No, go random again":
                        jump roommate_random
            elif roommate == 2:
                "But who should you live with? Probably your current roommate since you guys are great friends, \
                    and you haven't had enough time to develop close enough friendships with anyone else."
                jump roommate_current
        "Wait until later":
            jump end_of_year_no_housing

label roommate_current:
    scene picture_of_room
    "You go to your room and ask your roommate if he wants to live with you next year."
    $ live_with_roommate = True if renpy.random.random() > .33 else False
    if live_with_roommate:
        show roommate
        if roommate == 1:
            r "Okay, I guess."
            m "Awesome! Do you want to live in IV or on campus?"
            r "I don't care."
            m "I'll decide then."
        elif roommate == 2:
            r "Yeah sounds great!"
            m "Awesome! Do you want to live in IV or on campus?"
            r "I don't care, what ever is best for you."
        hide roommate
        "Do you want to live in IV or on campus? IV will be less expensive, but campus is easier and less problematic."
        menu:
            "IV":
                m "Let's live in IV. Apartments are already up for leases, so let's look now."
                jump live_IV
            "Campus":
                if tight_on_money:
                    "Actually, after examining your budgets and loan, you would rather live in IV."
                    jump live_IV
                m "Let's live on campus. Let's apply for housing now, that way we're more likely to get our top choice."
                jump live_campus
    else:
        "Do you want to live in IV or on campus? IV will be less expensive, but campus is easier and less problematic."
        menu:
            "IV":
                r "Actually I was gonna live on campus, sorry."
                "Looks like you'll have to go random after all."
                jump random_IV
            "Campus":
                if tight_on_money:
                    "Actually, after examining your budgets and loan, you would rather live in IV."
                    r "Actually I was gonna live on campus, sorry."
                    "Looks like you'll have to go random after all."
                    jump random_IV
                r "Actually I was gonna live in IV, sorry."
                "Looks like you'll have to go random after all."
                jump random_campus


label roommate_random:
    $ stress += 1
    "Do you want to live in IV or on campus? IV will be less expensive, but campus is easier and less problematic."
    menu:
        "IV":
            jump random_IV
        "Campus":
            if tight_on_money:
                "Actually, after examining your budgets and loan, you would rather live in IV."
                jump random_IV
            jump live_campus

label random_IV:
    scene looking_at_apartments
    "You hop on Facebook and start looking for people wanting to live in IV."
    "..."
    "After spending several weeks browsing and asking around, you are unable to find anyone to sign a lease with."
    if tight_on_money:
        "You decide to just default to living on campus, even though you are tight on money."
        $ stress += 1
    else:
        "You decide to just default to living on campus. At least you can afford it."
    jump live_campus

label live_IV:
    scene looking_at_apartments
    "You guys hop on google and start looking for double apartments in IV."
    "After a while, you have a pretty solid list of suitable places, and you apply to the top 3."
    "Now just wait for the property managers to respond."
    scene black_background
    "..."
    scene looking_at_email
    "Looks like you got one of your top choices!"
    show roommate
    r "Hooray!"
    m "Yay!"
    hide roommate
    "The lease is pretty long with a bunch of stuff you don't really understand, but assume is probably fine."
    "Huh, it looks like you need to put down a security deposit."
    if tight_on_money:
        m "Ugh, I wasn't really expecting an expense like that right now."
        "You can afford it, but you'll have to budget on other things you spend on."
        $ stress += 1
    else:
        "You have enough money or you didn't take out a large loan, so you have no problem expensing it."
        # Maybe there's a chance that your roommate can't afford it, and you need to loan it to him, which adds stress
    jump end_of_year_iv_housing

label live_campus:
    scene looking_at_campus_housing
    "You open a housing application, and rank the halls and dorm sizes according to your preference."
    "Now to just wait until the end of the year to find out what you'll get."
    jump end_of_year_campus_housing

label end_of_year_iv_housing:
    hide screen simple_stats_screen
    # You did very well and secured housing without many problems!

label end_of_year_campus_housing:
    $ stress += 0 # just so this compiles
    # There's a chance you don't get any housing, and resort to similar options as end_of_year_no_housing.
    # Otherwise, you successfully secured housing!

label end_of_year_no_housing:
    $ stress += 0 # just so this compiles
    # You waited until the end of the year to find housing. Talk with your roommate.
    # You can't live on campus, so you have to live in IV, hotels, or downtown. And there's a lot less options.
