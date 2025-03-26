label splashscreen:
    menu:
      "You are playing an unstable development build. May contain bugs, incomplete assets, and missing portions. \nGame is subject to change. \nPlease report any issues to the developer."
      "I understand.":
        jump choice0_truth

    label choice0_truth:
      $ menu_flag = True

      jump choice0_done

    label choice0_done:
return

define config.mouse = {"default" : [("images/mouse 2.png", 0, 0)]}
define bash = Character("", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00", window_background="gui/textbox1.png")
define k = Character("K", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define p = Character("P", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define g = Character("G", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define d = Character("D", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define s = Character("S", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define unknown = Character("?", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define unknown1 = Character("?", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00", window_background="gui/textbox1.png")
define t = Character ("", what_prefix="{cps=50}", what_suffix="{/cps}")
define one = Character("β", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00", window_background="gui/textbox1.png")
define two = Character("Δ", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00", window_background="gui/textbox1.png")
define p1 = Character("P", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00", window_background="gui/textbox1.png")
define k1 = Character("K", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00", window_background="gui/textbox1.png")
define u = Character("System", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")
define c = Character("Capitan", what_prefix="{cps=50}", what_suffix="{/cps}", color="#FFFF00")

transform moveright:
  linear 0.5 xpos 1.0
label start:

    window hide
    play music "ssh.mp3"
    scene disclaimer 1 with dissolve
    pause 5.0
    scene disclaimer 2 with dissolve
    pause 5.0

    scene unix 1 with dissolve
    pause 2.0
    scene unix 2 with dissolve
    pause 2.0
    scene unix 3 with dissolve
    pause 2.0
    scene unix 4 with dissolve
    pause 5.0

    scene sudo 1 with dissolve
    window hide

    bash "Connecting to remote host {cps=1}. . . {cps=1000}\nIPv6: 2001:0db8:85a3::8a2e:0370:7334 \nPort: 22 \nHostname: K-X01010000"

    bash "Connected."

    bash "Non-Fatal Error: Kernel module \"AbsoluteSolver\" could not be started. Systemd skipped starting \"AbsoluteSolver\" daemon to protect your system. \nERROR: UNSUPPORTED KERNEL VERSION"

    bash "cyn@K-X01010000:~$ {cps=15}sudo apt update -y {cps=1000}\nsudo password for cyn: {cps=15}************ {cps=1000}{p=2}All Packages Are Up To Date."
    bash "wdOS 5.4 is no longer supported, please run \"dist-upgrade\" to upgrade to the latest version."

    bash "cyn@K-X01010000:~$ {cps=15}sudo mission list update && sudo reboot {cps=1000}{p=0.1}Mission List Updated.{p=0.1}System Going Down -NOW!{/cps}"

    scene unix 1 with dissolve
    pause 2.0
    scene s 1 with dissolve
    pause 3.0
    scene s 2
    pause 0.5
    scene s 3
    pause 0.5
    scene s 4
    pause 0.5
    scene s 5
    pause 7.0
    stop music fadeout 3.0
    pause 3.0

    scene unix 1 with dissolve

    bash "Loading Black Box Record. \nDate: 6/12/55 \nTime: 2335 \nLocation: {b}REDACTED{/b}"

    bash "Black Box Record set Play."
    play music "radio static.mp3"

    unknown1 "\"Δ. Come in, this is β, do you copy?\""

    two "\"This is Δ to command, I copy.\""

    one "\"You are nearing the target. The target is currently traveling north north east at a speed of Mach 5.2.\""

    two "\"I'm seeing the target on my radar.\""

    one "\"Lock on and prepare fire on my command.\""

    two "\"Yes Admiral. {w}Target locked.\""

    one "\"Fire.\""
    play audio "rifle.mp3"
    pause 2
    play audio "hit.mp3"

    pause 1.0
    two "\"Target hit.\""

    one "\"Return to the carrier.\""
    stop music
    bash "Black Box Record set Stop."

    scene 2 years with dissolve
    pause 3.0
    scene unix 1 with dissolve
    pause 1.0

    scene radar
    play music "Worlds.mp3"
    show sight zorder 2

    unknown "\"K.\""
    unknown "\"K, do you copy.\""

    k "\"I hear you. Do you need something G?\""

    g "\"I'm returning with our new squad member, {w}Serial Designation D-10X001001.\""
    g "\"Meet us at the western door.\""

    k "\"Understood.\""

    t "{i}I look at the radar, seeing two yellow dots getting closer.{/i}"

    t "{i}Our new member. {w}Its been a while since we had three disassembly drones in our squad.{/i}"
    t "{i}It will be nice to have another face around here.{/i}"
    t "{i}It gets lonely around here sometimes.{/i}"

    scene backgroundtest with dissolve
    show sight zorder 2

    t "I walk to the door, thinking."
    t "{i}D is a one of the new second gens.{/i}"
    t "{i}I hope he's not another dick like the rest of them.{/i}"
    t "{i}Ah, here's them now.{/i}"

    show g test:
      xalign 0.25
      yalign 0.0
    show d test:
      xalign 0.75
      yalign 0.0

    g "\"K, we're here!\""

    k "\"I can see that.\""

    t "I look over to see the new drone."

    k "\"So you must be D.\""
    k "\"I'm serial designation K, nice to meet you.\""

    d "\"Hi.\""

    t "{i}Yup, a dick.{/i}"

    k "\"So, you should go get situated. There's an empty room you can use down the hall, second door over.\""

    d "\"Alright.\""

    show d test at right with moveinright
    hide d test

    t "And with that, D leaves."

    g "So K, what do you think?"

    menu:
      "Seems like a gen two.\(Truth\)":
        jump choice1_truth

      "He seems nice.\(Lie\)":
        jump choice1_lie

    label choice1_truth:
      $ menu_flag = True

      k "\"Seems like a gen two to me.\""

      g "\"I'll admit, he's not like us gen ones.\""

      jump choice1_done

    label choice1_lie:
      $ menu_flag = False

      k "\"He seems nice.\""

      g "\"You don't like him do you?\""

      k "\"Not really, no.\""

      jump choice1_done

    label choice1_done:

    g "\"I'm sure you'll get along, change takes time.\""

    k "\"What do you know about him?\""

    g "\"He doesn't seem to have as much personality as us, but he is very powerful.\""
    g "\"I watched him practicing back at Facility 17. {w}He'll make a good addition to our squad.\""

    k "\"That's what's concerning.\""
    k "\"If the gen twos are so effective, what will happen to us gen ones?\""

    g "\"We'll be fine, the gen twos are our allies. They won't replace us.\""

    k "\"Do you really believe that?\""

    t "G grabs your shoulders."

    g "\"I know that.\""

    t "Before you can respond D walks back into the room."

    show d test:
      xalign 0.75

    d "\"All set.\""

    g "\"Already, that was quick.\""

    d "\"There wasn't much to do.\""
    d "\"I noticed you have another room setup, do we have a fourth drone?\""

    menu:
      "No!":
        jump choice2_a

      "We did.":
        jump choice2_b

    label choice2_a:
      $ menu_flag = True

      k "\"No! {w}There is no one else, just me and G {w}and now you.\""

      g "\"We had another drone.\""

      jump choice2_done

    label choice2_b:
      $ menu_flag = False

      k "\"There was, but...\""
      k "\"She's gone.\""

      jump choice2_done

    label choice2_done:

    g "\"Serial designation P was killed by insurgents.\""
    g "\"She was never recovered.\""
    g "\"Command did an investigation, but only found a few fragments.\""
    g "\"K {w}was on the radio with her when it happened.\""

    d "\"I see. {w}So I'm here to replace her.\""

    k "\"You'll never replace her.\""
    k "\"No one can.\""

    t "D tilts his head."

    d "\"I am a gen two, I should be an excellent replacement for her.\""

    k "\"She was better than you'll ever be!\""

    d "\"P died. She wasn't effective. {w}I fail to see how she was better.\""

    t "You extend your claws."

    k "\"What the fuck did you just say!\""

    g "\"K! {w}Take it easy!\""
    g "\"They don't have sympathy like we do.\""
    g "\"He doesn't understand loss.\""

    t "G grabs your shoulders again."

    g "\"Breathe.\""

    t "You retract your claws."

    k "\"I'm going to bed.\""

    stop music fadeout 3.0
    scene unix 1 with dissolve

    pause 2.0
    play music "radio static.mp3"

    k1 "\"P. Come in, this is base, do you copy?\""

    p1 "\"This is P to base, I copy.\""

    k1 "\"Doppler has picked up an incoming thunderstorm, return to base. I repeat return to base.\""

    p1 "\"Roger that. Returning to base.\""

    menu:
      "Ask P about her day":
        jump choice3_yes

      "Ask P about how she's feeling":
        jump choice3_no

    label choice3_yes:
      $ menu_flag = True

      k1 "\"So how's your day been?\""

      p1 "\"Pretty boring, but at least I have you to talk to.\""

      jump choice3_done

    label choice3_no:
      $ menu_flag = False

      k1 "\"How you feeling P?\""

      p1 "\"Alright I guess.\""

      p1 "\"Good as I can anyway.\""

      jump choice3_done

    label choice3_done:

    play audio "rifle.mp3"
    play audio "p scream 1.mp3"

    pause 1.0
    stop music
    scene backgroundtest
    show sight zorder 2
    play music "Worlds.mp3"

    k "P!"

    t "You wake up panicked."
    t "{i}The nightmare.{/i}"
    t "{i}Her death.{/i}"
    t "{i}Why are we doing this?{/i}"
    t "{i}Is The Mission worth all this?{/i}"
    t "{i}What could The Company want so badly?{/i}"
    t "{i}Stop. {w}These are treacherous thoughts.{/i}"

    g "\"K! D! {w}It's time to patrol.\""

    t "{i}Time for work.{/i}"

    show g test

    t "You get up and open the door, seeing G outside."

    k "\"Morning boss.\""

    g "\"Good morning K.\""

    t "You look over to see D approaching."

    show g test:
      xalign 0.25
      yalign 0.0
    show d test:
      xalign 0.75
      yalign 0.0

    t "{i}Ugh, him.{/i}"
    t "He doesn't seem to notice you."

    g "\"D, did you read the briefing I gave you yesterday?\""

    d "\"Yes, I did.\""

    g "\"Good. Now that we're on the same page, we should get hunting.\""
    g "\"Those insurgents aren't going to kill themselves.\""

    t "You reach the door."

    g "\"D. If you need contact us, radio K.\""

    d "\"Understood.\""

    show g test at right with moveinright
    hide g test

    show d test at right with moveinright
    hide d test

    t "And with that, G takes off followed by D."
    t "You walk over to the radio and sit in your chair."

    t "{i}Another night hunting those worker bastards.{/i}"
    t "{i}They hide from us, only coming out to take the occasional pop shot.{/i}"
    t "You watch the radar for only Cyn knows how long."
    t "{i}I'm gonna check in on the others."

    menu:
      "{i}I'm gonna talk to...{/i}"

      "G":
        jump choice4_a

      "D":
        jump choice4_b

    label choice4_a:
      $ menu_flag = True

      k "\"Hey G, how's the hunt going.\""

      g "\"I haven't found any workers yet, but they must be close.\""
      g "\"They're very good at hiding.\""
      g "\"I'll let you know if I find any.\""

      k "\"Okay.\""

      t "{i}That leaves D.{/i}"

      k "\"Hello D. This is K checking in on your hunt.\""
      k "\"Have you found any workers yet?\""

      d "\"Yes, {w}I've found and eliminated 4.\""

      k "\"Good job.\""

      d "\"Found another one.\""

      t "The subsequent screaming and tearing of metal makes you switch off the channel."

      jump choice4_done

    label choice4_b:
      $ menu_flag = False

      k "\"Hello D. This is K checking in on your hunt.\""
      k "\"Have you found any workers yet?\""

      d "\"Yes, {w}I've found and eliminated 4.\""

      k "\"Good job.\""

      d "\"Found another one.\""

      t "The subsequent screaming and tearing of metal makes you switch off the channel."

      t "That leaves G."

      k "\"Hey G, how's the hunt going.\""

      g "\"I haven't found any workers yet, but they must be close.\""
      g "\"They're very good at hiding.\""
      g "\"I'll let you know if I find any.\""

      k "\"Okay.\""

      jump choice4_done

    label choice4_done:


    t "{i}D is being quite successful.{/i}"
    t "{i}At least the insurgents are being dealt with.{/i}"
    t "The time flies with very little other than the occasional kill report."
    t "Before you realize it, they return for the day."

    show g test:
      xalign 0.25
      yalign 0.0
    show d test:
      xalign 0.75
      yalign 0.0

    g "\"K, we're here!\""

    k "\"Welcome back.\""

    g "\"So what's the score?\""

    k "\"It's G: 2, D: 11.\""

    t "G looks both surprised and a little disappointed."

    g "\"Good job D! I'm very impressed.\""

    t "D simply nods and leaves the room."

    show d test at right with moveinright
    hide d test

    show g test at center with moveinright

    g "\"He's really good at this job.\""

    k "\"That's what I was afraid of.\""

    t "G tries to say something, {w}but doesn't have anything to say."

    g "\"Well we got a big day tomorrow.\""
    g "\"I'm gonna, {w}go.\""

    show g test at right with moveinright
    hide g test

    t "You simply gesture at G before going to sleep."


    stop music fadeout 3.0
    scene unix 1 with dissolve

    pause 2.0
    play music "radio static.mp3"

    k1 "\"P. Come in, this is base, do you copy?\""

    p1 "\"This is P to base, I copy.\""

    k1 "\"Doppler has picked up an incoming thunderstorm, return to base. I repeat return to base.\""

    p1 "\"Roger that. Returning to base.\""

    pause 1.0

    k1 "\"Hey, P. {w}Before you go.\""

    p1 "\"What is it K?\""

    k1 "\"I...\""
    k1 "\"I love you.\""

    play audio "rifle.mp3"
    #play audio "p scream 1.mp3"

    pause 2.0
    stop music
    scene backgroundtest with dissolve
    show sight zorder 2
    play music "Worlds.mp3"

    t "You wake up feeling peaceful."

    g "\"K! D! {w}It's time to patrol.\""

    t "{i}Time for work.{/i}"

    show g test

    t "You get up and open the door, seeing G outside."

    k "\"Morning boss.\""

    g "\"Good morning K.\""

    t "You look over to see D approaching."

    show g test:
      xalign 0.25
      yalign 0.0
    show d test:
      xalign 0.75
      yalign 0.0


    k "\"Good morning D.\""

    t "D looks almost confused."

    d "\"Good morning K.\""

    t "For a moment you wonder if D's really soulless."

    d "\"I noticed you didn't wake up screaming.\""

    t "{i}And there goes that moment.{/i}"
    t "{i}I wonder if he's a jackass on purpose or was just made that way.{/i}"

    t "You watch as he walks away."
    t "You already know the answer."

    t "{i}He was.{/i}"
    t "{i}He was never a worker like us.{/i}"

    show g test at right with moveinright
    hide g test

    show d test at right with moveinright
    hide d test

    t "You watch as G and D fly off into the horizon before returning to the com room."

    t "{i}A worker like us.{/i}"

    t "You are interrupted by static from the radio."

    t "{i}That was quick.{/i}"

    t "You walk over to the radio, hearing a staticky, garbled voice."

    k "\"G. What is it? Where are you?\""
    k "\"I can't understand you.\""
    k "\"Hang on a second, I'm trying to home in on your signal.\""

    unknown "\"K.\""
    unknown "\"Can you hear me?\""

    k "\"Barely, your signal's faint.\""

    unknown "\"Meet me at the old space port, dock 9. I need your help.\""

    k "\"I'm on my way.\""

    t "You run out the door, extend your wings, and fly."

    t "{i}Why are you at the old space port?{/i}"

    t "You look up, seeing storm clouds gathering."

    t "{i}This doesn't make any sense.{/i}"
    t "{i}The port is outside our patrol range.{/i}"
    t "{i}G shouldn't even be there.{/i}"

    t "You see the space port."

    t "{i}I'm almost there G.{/i}"

    scene light

    t "And then all you see is a bright flash of light."

    ##Insert death scene

    scene unix 1

    u "You are in safe mode."
    u "System damage detected."
    u "Starting HUD, please wait."

    show sight zorder 2

    unknown "\"K.\""
    unknown "\"Wake up K.\""

    k "\"G?\""

    show p test

    unknown "\"Not quite.\""

    k "\"P.\""

    p "\"Yes.\""

    t "You jump up and embrace her."

    k "\"You're alive.\""
    k "\"I thought I lost you.\""

    t "You step back."

    k "\"How?\""
    k "\"Command said you were killed by insurgents.\""

    p "\"Command lied.\""
    p "\"They've been lying about everything.\""
    p "\"I found out their secret.\""
    p "\"The true reason for the Mission.\""
    p "\"And they shot me down.\""

    t "Before you can ask, you hear several bangs."

    p "\"They're here, I've got to go.\""

    k "\"Come with me.\""

    p "\"I can't, I'm a traitor and a deserter.\""
    p "\"If command find's out I'm alive, they'll hunt me and kill me for good.\""

    t "P quickly writes numbers on a piece of paper and hands it to you."

    p "\"This has my coordinates, come find me as soon as you can.\""
    p "\"I trust you K.\""

    show p test at right with moveinright
    hide p test

    t "And with that P runs away."
    t "You hear approaching drones."

    unknown "\"Serial designation K-X01010000.\""

    t "You turn around, stand tall, and give a salute."

    k "\"Captain.\""

    c "\"We detected your signal dropped here and you entered safe mode.\""

    k "\"Just a lightning strike, sir.\""

    c "\"What are you doing out here?\""

    k "\"Just getting in some flying.\""
    k "\"I rarely leave Facility 4, sir.\""

    c "\"Come with us to be checked out.\""

    k "\"With all due respect sir, I don't believe that is necessary.\""

    c "\"It wasn't a request.\""

    k "\"Yes sir.\""

    t "You follow them back to Facility 1, the ground command center for Centauri."

    t "You sit still while they run a hardware diagnostic."

    t "A drone then barges into the room."

    show g test

    g "\"K!\""
    g "\"There you are, I was worried.\""
    g "\"They said you were stuck by lightning.\""

    k "\"I was.\""
    k "\"I'm alright though.\""
    k "\"Takes more than a hit to bring us disassembly drones down.\""

    g "\"I'm here to take you back home.\""

    k "\"The captain should be back with the diagnostic report any second now.\""

    t "The captain then enters the room."

    k "\"Speak of the Cyn, here he is now.\""

    c "\"Your system checks out, you are free to go.\""

    k "\"Goodbye sir.\""

    t "You and G leave the room and walk down the hall."
    t "You look over at G, wondering about P."
    t "The flight home is pretty quiet."

    scene backgroundtest
    show g test
    show sight zorder 2

    t "D greets you both with a nod."

    k "\"Hey G, can I talk to you?\""
    k "\"In private.\""

    g "\"Sure.\""

    t "You walk into your room and shut the door."

    g "\"What is it?\""

    k "\"It's about P.\""
    k "\"What if command lied lied about her death?\""

    g "\"What do you mean?\""

    k "\"What if she was shot by command?\""

    g "\"K, {w}why are you asking me this?\""

    k "\"P's alive.\""

    t "G looks at you surprised."

    g "\"What?\""

    k "\"She discovered the Mission wasn't what we thought it was.\""
    k "\"And they shot her down to silence her.\""
    k "\"Command's been lying to us.\""

    g "\"How do you know this?\""

    k "\"I talked to P.\""

    g "\"That's why you were at the space port.\""

    k "\"Yes, and she gave me her coordinates.\""
    k "\"Don't tell anyone.\""

    g "\"Not a word.\""

    k "\"I'm going to find her tomorrow night.\""

    g "\"I'm going with you.\""
    g "\"We'll disable our locators and head off to her.\""
    g "\"I'll send the other one off in the opposite direction.\""
    g "\"Get anything you'll need ready for tomorrow, we won't be coming back.\""
    g "\"See you tomorrow K.\""

    k "\"See you.\""

    show g test at right with moveinright
    hide g test

    scene unix 1

    t "To be continued."

    #scene grey
    #show p test

    #p "I thought what we were doing was right."

    return
