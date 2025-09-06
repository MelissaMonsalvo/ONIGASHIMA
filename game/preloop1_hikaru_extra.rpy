### CONTAINS NON MANDATORY EVENTS FOR LOOP 1

label loop1_hikaru_nonmandatory1:

    n "You are wandering in the forest at night, because Ymakui's dead, so why not?"

    n "But then something stops you."

    n "You hear a slow, shaking breath..."

    n "Then... {w}a strangled sob?"

    n "You follow it, of course, because you don't have a sense of self-preservation."

    n "You see something crouched down on the ground."

    pause 1.0

    n "It isn't moving."

    show crouched_shadow at center with dissolve

    n "You get closer."

    pause 1.0

    n "It's moving--"

    hikaru "...Why...?"

    n "Oh, that's just hikaru."

    hikaru "What's going on...?"

    hikaru "What's happening to [persistent.player_name]?"

    ## TWIG SNAP LOL

    hikaru "...!"

    MC "...Hikaru, it's me--"

    hikaru "Get back!"

    MC "A-Are you okay?"

    n "Hikaru stares at you for a few moments, hands hovering over their sai, calculating..."

    hikaru "...I’m... fine."

    hikaru "Just needed a moment."

    MC "You're crying."

    hikaru "Tired."

    n "They leap back without another word and dissapears into the trees like smoke."

    n "What was that about...?"

    return

label loop1_hikaru_nonmandatory2:

    n "There are a lot of tombstones on the shrine."

    n "All of them are blank tombstones, some said those are the victims of Yamakui."

    n "Now they're just nameless and faceless souls that dissolves from memory once they got eaten."

    n "Hikaru stands in front of the grave, with their hands folded in prayer."

    n "They clearly are too absorbed in their own thoughts."

    hikaru "...[persistent.player_name]."

    n "..."

    hikaru "....mine..."

    n "Was that a prayer for you...?"

    MC "...Did you say my name?"

    hikaru "...Hm? Oh! Didn't realize you're here."

    MC "What are you praying about?"

    hikaru "Ah, nothing really... Just health and prosperity and mundane things."

    MC "You said \"mine\", you said my name."

    hikaru "Are you sure you are not mishearing things?"

    MC "..."

    n "Hmm... Maybe you do. Everyone hears things wrong sometimes."

    n "You glance toward the stones without names."

    n "Their names might be forgotten, but you don't forget your own."

    n "Your name...{w} is..."

    $ loop1_hikaru_nonmandatory2 = True

    return

label loop1_hikaru_nonmandatory3:

    n "You see Hikaru is helping Shiori with making talismans, they seem to be too occupied to realize you are there "

    shiori "You’ve gotten better, Hikaru~"

    hikaru "I... had practice."

    shiori "Mhm. I noticed~"

    n "Hikaru ties off the charm’s final knot and stack it with the others."

    shiori "Cuz you made a lot for [persistent.player_name] before leaving, riiight?"

    hikaru "..."

    hikaru "I didn’t know what else to do."

    shiori "Aww, Hikaru~ Deep down you really care, don't you?"

    hikaru "That's... That's just because [persistent.player_name] didn’t say goodbye, so I thought--"

    hikaru "I... I just didn’t know if [persistent.player_name] would come back."

    hikaru "Or...{w} if anything would be left when it was over."

    shiori "So you made tons of charms instead, huh?"

    hikaru "Yes."

    shiori "Mm, you even made variations."

    shiori "..."

    shiori "Ah, by the way [persistent.player_name] asked me and Yamato something earlier."

    hikaru "Hmm?"

    shiori "Are you two, like, in looove or something~?"

    hikaru "..."

    hikaru "...That’s not..."

    shiori "Ara~ You’re not denying it."

    hikaru "I’m not confirming it either."

    shiori "Then what is it, Hikaru?"

    hikaru "..."

    hikaru "It’s nothing."

    hikaru "I just... {w}wanted [persistent.player_name] to be safe."

    shiori "So safe you etched their name into seven different protection spells~"

    hikaru "..."

    shiori "You know, when people are afraid to name what they feel... {W}it usually means it’s important."

    hikaru "...Shiori-chan, stop."

    shiori "Hmm~"

    hikaru "I mean it."

    shiori "Mmkay, if you said so."

    shiori "If you're truly in love with [persistent.player_name], though. You shoud say it before it's too late..."

    hikaru "..."

    hikaru "I already have."

    shiori "Hm?"

    hikaru "Nothing."

    n "Shiori didn't hear that last sentence, but you did."

    n "You don't want to deal with it, at least for now, so you decide to leave instead."

    $ loop1_hikaru_nonmandatory3 = True

    return
