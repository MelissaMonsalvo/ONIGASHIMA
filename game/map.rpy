#########################
# Map 4:20 Mel v
############################

python early:
    def find_nearest_mandatory_event(time_block):
        """
        Returns a tuple: (event_label, character_name) of the nearest available mandatory event
        that matches the current time block (Day/Night).
        Prioritizes Yamato > Shiori > Hikaru if all else equal.
        Does NOT increment counters here!
        """
        current_loop = store.current_loop
        candidates = []
        for char in ["yamato", "shiori", "hikaru"]:
            is_dead = getattr(persistent, f"{char}_dies", False)
            if not is_dead and char in mandatory_events.get(current_loop, {}):
                events_completed = getattr(store, f"{char}_events_completed", 0)
                events_list = mandatory_events[current_loop][char]
                for idx in range(events_completed, len(events_list)):
                    next_event = events_list[idx]
                    if next_event["time"] == time_block:
                        candidates.append({
                            "char": char,
                            "idx": idx,
                            "event_label": next_event["event"]
                        })
                        break  # Only consider the next event for each character
        # Sort by order in event list (progress), then by preference: Yamato, Shiori, Hikaru
        # Sort by most events completed (progress) first, then preference
        candidates.sort(key=lambda c: (-getattr(store, f"{c['char']}_events_completed", 0), ["yamato", "shiori", "hikaru"].index(c["char"])))

        if candidates:
            selected = candidates[0]
            return (selected["event_label"], selected["char"])
        return (None, None)

default redirect_event_label = None
default redirect_event_char = None
default redirect_message = ""

image black_screen = "#000"
# Variables para el progreso del juego
default current_Day = 1
default current_time_block = "Day"  # "Day" o "Night"
default current_loop = 1
default visits_toDay = 0

# Variables para el progreso de los personajes
default yamato_events_completed = 0
default hikaru_events_completed = 0
default shiori_events_completed = 0

# Variables para los eventos fantasmas de los personajes
default shiori_ghost_events_completed = 0
default yamato_ghost_events_completed = 0
default hikaru_ghost_events_completed = 0

# define persistent.shiori_dies = False ## shiori dead
# define persistent.yamato_dies = False ## yamato dead
# define persistent.hikaru_dies = False ## hikaru ded

#! Quitar
#default preferences.skip_unseen=True

define locations = ["shrine", "forest", "dojo", "village","house"]

define location_positions = {
    "shrine": (820, 200),
    "forest": (350, 290),
    "dojo": (1420, 500),
    "village": (975, 850),
    "house": (325, 750)
}



#Eventos obligatorios por loop y personaje
define mandatory_events = {
    1: {
        "yamato": [
            {"location": "dojo", "time": "Day", "event": "loop1_yamato_mandatory1"},
            {"location": "dojo", "time": "Night", "event": "loop1_yamato_mandatory2"},
            {"location": "house", "time": "Night", "event": "loop1_yamato_mandatory3"},
            {"location": "village", "time": "Day", "event": "loop1_yamato_mandatory4"},
            {"location": "forest", "time": "Night", "event": "loop1_yamato_mandatory5"}
        ],
        "hikaru": [
            {"location": "forest", "time": "Day", "event": "loop1_hikaru_mandatory1"},
            {"location": "dojo", "time": "Day", "event": "loop1_hikaru_mandatory2"},
            {"location": "village", "time": "Night", "event": "loop1_hikaru_mandatory3"},
            {"location": "house", "time": "Day", "event": "loop1_hikaru_mandatory4"},
            {"location": "shrine", "time": "Day", "event": "loop1_hikaru_mandatory5"}
        ],
        "shiori": [
            {"location": "shrine", "time": "Day", "event": "loop1_shiori_mandatory1"},
            {"location": "shrine", "time": "Night", "event": "loop1_shiori_mandatory2"},
            {"location": "shrine", "time": "Day", "event": "loop1_shiori_mandatory3"},
            {"location": "shrine", "time": "Night", "event": "loop1_shiori_mandatory4"},
            {"location": "forest", "time": "Day", "event": "loop1_shiori_mandatory5"}
        ]
    },
    2: {
        "yamato": [
            {"location": "dojo", "time": "Day", "event": "loop2_yamato_mandatory1"},
            {"location": "dojo", "time": "Day", "event": "loop2_yamato_mandatory2"},
            {"location": "shrine", "time": "Night", "event": "loop2_yamato_mandatory3"},
            {"location": "forest", "time": "Night", "event": "loop2_yamato_mandatory4"}
        ],
        "hikaru": [
            {"location": "forest", "time": "Day", "event": "loop2_hikaru_mandatory1"},
            {"location": "shrine", "time": "Night", "event": "loop2_hikaru_mandatory2"},
            {"location": "shrine", "time": "Day", "event": "loop2_hikaru_mandatory3"},
            {"location": "house", "time": "Day", "event": "loop2_hikaru_mandatory4"}
        ],
        "shiori": [
            {"location": "village", "time": "Day", "event": "loop2_shiori_mandatory1"},
            {"location": "shrine", "time": "Day", "event": "loop2_shiori_mandatory2"},
            {"location": "shrine", "time": "Night", "event": "loop2_shiori_mandatory3"},
            {"location": "shrine", "time": "Night", "event": "loop2_shiori_mandatory4"}
        ]
    }
}


# Definir los eventos fantasmas
define ghost_events = {
    "shiori": ["ghost_shiori_1", "ghost_shiori_2", "ghost_shiori_3", "ghost_shiori_4", "ghost_shiori_5"],
    "yamato": ["ghost_yamato_1", "ghost_yamato_2", "ghost_yamato_3", "ghost_yamato_4", "ghost_yamato_5"],
    "hikaru": ["ghost_hikaru_1", "ghost_hikaru_2", "ghost_hikaru_3", "ghost_hikaru_4", "ghost_hikaru_5"]
}

####################################################################
#Labels for testing Map
####################################################################

#Dont Delete


# define mandatory_events = {
#     1: {
#         "yamato": [
#             {"location": "dojo", "time": "Day", "event": "loop1_yamato_mandatory1b"},
#             {"location": "dojo", "time": "Night", "event": "loop1_yamato_mandatory2b"},
#             {"location": "house", "time": "Night", "event": "loop1_yamato_mandatory3b"},
#             {"location": "village", "time": "Day", "event": "loop1_yamato_mandatory4b"},
#             {"location": "forest", "time": "Night", "event": "loop1_yamato_mandatory5b"}
#         ],
#         "hikaru": [
#             {"location": "forest", "time": "Day", "event": "loop1_hikaru_mandatory1b"},
#             {"location": "dojo", "time": "Day", "event": "loop1_hikaru_mandatory2b"},
#             {"location": "village", "time": "Night", "event": "loop1_hikaru_mandatory3b"},
#             {"location": "house", "time": "Day", "event": "loop1_hikaru_mandatory4b"},
#             {"location": "shrine", "time": "Day", "event": "loop1_hikaru_mandatory5b"}
#         ],
#         "shiori": [
#             {"location": "shrine", "time": "Day", "event": "loop1_shiori_mandatory1b"},
#             {"location": "shrine", "time": "Night", "event": "loop1_shiori_mandatory2b"},
#             {"location": "shrine", "time": "Day", "event": "loop1_shiori_mandatory3b"},
#             {"location": "shrine", "time": "Night", "event": "loop1_shiori_mandatory4b"},
#             {"location": "forest", "time": "Day", "event": "loop1_shiori_mandatory5b"}
#         ]
#     },
#     2: {
#         "yamato": [
#             {"location": "dojo", "time": "Day", "event": "loop2_yamato_mandatory1b"},
#             {"location": "dojo", "time": "Day", "event": "loop2_yamato_mandatory2b"},
#             {"location": "shrine", "time": "Night", "event": "loop2_yamato_mandatory3b"},
#             {"location": "forest", "time": "Night", "event": "loop2_yamato_mandatory4b"}
#         ],
#         "hikaru": [
#             {"location": "forest", "time": "Day", "event": "loop2_hikaru_mandatory1b"},
#             {"location": "shrine", "time": "Night", "event": "loop2_hikaru_mandatory2b"},
#             {"location": "shrine", "time": "Day", "event": "loop2_hikaru_mandatory3b"},
#             {"location": "house", "time": "Day", "event": "loop2_hikaru_mandatory4b"}
#         ],
#         "shiori": [
#             {"location": "village", "time": "Day", "event": "loop2_shiori_mandatory1b"},
#             {"location": "shrine", "time": "Day", "event": "loop2_shiori_mandatory2b"},
#             {"location": "shrine", "time": "Night", "event": "loop2_shiori_mandatory3b"},
#             {"location": "shrine", "time": "Night", "event": "loop2_shiori_mandatory4b"}
#         ]
#     }
# }


# # Definir los eventos fantasmas
# define ghost_events = {
#     "shiori": ["ghost_shiori_1b", "ghost_shiori_2b", "ghost_shiori_3b", "ghost_shiori_4b", "ghost_shiori_5b"],
#     "yamato": ["ghost_yamato_1b", "ghost_yamato_2b", "ghost_yamato_3b", "ghost_yamato_4b", "ghost_yamato_5b"],
#     "hikaru": ["ghost_hikaru_1b", "ghost_hikaru_2b", "ghost_hikaru_3b", "ghost_hikaru_4b", "ghost_hikaru_5b"]
# }


define character_icons_idle = {
    "shiori": "images/map/map_shiori_idle.webp",
    "yamato": "images/map/map_yamato_idle.webp",
    "hikaru": "images/map/map_hikaru_idle.webp"
}

define character_icons_red = {
    "shiori": "images/map/map_shiori_red_hover.webp",
    "yamato": "images/map/map_yamato_red_hover.webp",
    "hikaru": "images/map/map_hikaru_red_hover.webp"
}


define character_icons_yellow= {
    "shiori": "images/map/map_shiori_yellow_hover.webp",
    "yamato": "images/map/map_yamato_yellow_hover.webp",
    "hikaru": "images/map/map_hikaru_yellow_hover.webp"
}


label map:

    # Optional: update current_loop if needed, e.g.:
    # if persistent.loop1:
    #     $ current_loop = 1
    # elif persistent.loop2:
    #     $ current_loop = 2

    # Route jump if any character completed all mandatory events
    if yamato_events_completed >= 5 or shiori_events_completed >= 5 or hikaru_events_completed >= 5:
        $ check_rutes()

    if current_Day > 5:
        if persistent.trueendingunlocked and store.current_loop == 1:
            jump truend
        else:
            $ check_rutes()
        return

    # Call the map screen (player picks location)
    call screen map_screen
    # (After a location has been picked and handled...)

    # Check: is there any valid event for this time block?
    $ event_exists = False
    python:
        for char in ["yamato", "shiori", "hikaru"]:
            is_dead = getattr(persistent, f"{char}_dies", False)
            if not is_dead and char in mandatory_events.get(store.current_loop, {}):
                events_completed = getattr(store, f"{char}_events_completed", 0)
                events_list = mandatory_events[store.current_loop][char]
                for idx in range(events_completed, len(events_list)):
                    next_event = events_list[idx]
                    if next_event["time"] == current_time_block:
                        event_exists = True
                        break
                if event_exists:
                    break

    if not event_exists:
        # If there are no events for anyone at this time, auto-advance time block
        if current_time_block == "Day":
            $ current_time_block = "Night"
            "Nothing important happens during the day. Night falls."
        else:
            $ current_Day += 1
            $ current_time_block = "Day"
            "The night passes quietly. A new day begins."
        jump map

    # If at least one event exists for the current time block, allow normal progression
    jump map



default offset_x_a = 0

# Pantalla del mapa
screen map_screen():

    key "h" action NullAction()

    # if yamato_events_completed >= 5 or shiori_events_completed >= 5 or yamato_events_completed >= 5:
    #     timer 0.05 action Function(check_rutes) repeat True

    # if persistent.trueendingunlocked and current_Day > 5 and store.current_loop == 1:
    #     timer 0.05 action Function(truend) repeat True

    #BG
    #$ check_rutes()
    if current_time_block == "Day":
        add "images/map/map_day.webp"
    else:
        add "images/map/map_night.webp"
    #textbutton "" xsize 1920 ysize 1080 action Function (check_rutes)

    imagebutton auto "images/map/shrine_%s.webp" action Function(visit_location_func, "shrine") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 820 ypos 200
    imagebutton auto "images/map/forest_%s.webp" action Function(visit_location_func, "forest") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 350 ypos 290
    imagebutton auto "images/map/dojo_%s.webp" action Function(visit_location_func, "dojo") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 1420 ypos 500
    imagebutton auto "images/map/village_%s.webp" action Function(visit_location_func, "village") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 975 ypos 850
    imagebutton auto "images/map/house_%s.webp" action Function(visit_location_func, "house") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 325 ypos 750

    # Mostrar iconos de personajes según su ubicación y estado
    for i, character in enumerate(["shiori", "yamato", "hikaru"]):
        # === HIDE ICONS IF DEAD ===
        if getattr(persistent, f"{character}_dies", False):
            continue  # skip this character if dead

        $ char_location = get_character_location(character)
        if char_location:
            $ pos_x, pos_y = location_positions.get(char_location, (0, 0))
            $ icon_width = 120
            $ icon_height = 190
            $ button_width = 284
            $ icon_x = pos_x + (button_width // 2) - (icon_width // 2)
            $ offset_x = i * 50
            $ icon_x += offset_x
            $ icon_y = pos_y - icon_height - 2

            $ character_icons = character_icons_yellow if persistent.loop1 else character_icons_red
            $ icon = character_icons.get(character)

            add Transform(icon, size=(icon_width, icon_height)):
                xpos icon_x
                ypos icon_y


    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        xsize 600
        ysize 250
        background "map/question_frame.webp"   # <- This sets your custom image

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            #label "Day [current_Day] loop [current_loop]" xalign 0.5
            label "Day [current_Day]" xalign 0.5
            text "Where do you want to go?" xalign 0.5





# Función para verificar eventos obligatorios
python early:
    def visit_location_func(location):
        store.visits_toDay += 1
        current_mandatory = store.check_mandatory_events(location)
        event_to_call = None
        if current_mandatory:
            event_to_call = current_mandatory

        # Advance the time block for the next turn
        if store.visits_toDay >= 2:
            store.current_Day += 1
            store.visits_toDay = 0
            store.current_time_block = "Day"
        else:
            store.current_time_block = "Night" if store.current_time_block == "Day" else "Day"

        # Call event or empty label before advancing time block
        if event_to_call:
            renpy.call(event_to_call)
            renpy.jump("map")  # <---- ADD THIS to always go back to map after event
        else:
            nearest_event, nearest_char = find_nearest_mandatory_event(store.current_time_block)
            if nearest_event:
                store.redirect_event_label = nearest_event
                store.redirect_event_char = nearest_char
                store.redirect_message = "There is nothing interesting happening here, so you rest up and go somewhere else..."
                renpy.jump("redirect_to_event")
            else:
                renpy.call("location_empty", location)
                renpy.jump("map")  # <---- ADD THIS to always go back to map after empty




#Checa en la lista de eventos de vivos y muertos
    def check_mandatory_events(location):
        candidates = []
        characters = ["shiori", "yamato", "hikaru"]

        for char in characters:
            is_dead = getattr(persistent, f"{char}_dies", False)

            if is_dead:
                events_completed = getattr(store, f"{char}_ghost_events_completed", 0)
                events_list = ghost_events.get(char, [])

                # If you want ghost events to require location/time, uncomment below and adjust
                # if events_completed < len(mandatory_events[store.current_loop][char]):
                #     next_event = mandatory_events[store.current_loop][char][events_completed]
                #     if next_event["location"] == location and next_event["time"] == store.current_time_block:
                #         candidates.append({
                #             "char": char,
                #             "is_dead": True,
                #             "events_completed": events_completed,
                #             "event_label": events_list[events_completed]
                #         })

                # If ghost events can always be triggered, just check length
                if events_completed < len(events_list):
                    candidates.append({
                        "char": char,
                        "is_dead": True,
                        "events_completed": events_completed,
                        "event_label": events_list[events_completed]
                    })

            else:
                events_completed = getattr(store, f"{char}_events_completed", 0)
                events_list = mandatory_events[store.current_loop][char]

                if events_completed < len(events_list):
                    next_event = events_list[events_completed]
                    if (next_event["location"] == location and
                        next_event["time"] == store.current_time_block):
                        candidates.append({
                            "char": char,
                            "is_dead": False,
                            "events_completed": events_completed,
                            "event_label": next_event["event"]
                        })

        if not candidates:
            return None

        # Sort: most events completed first, then alive before dead
        candidates.sort(key=lambda c: (-c["events_completed"], c["is_dead"]))

        selected = candidates[0]

        # Progress their event counter
        if selected["is_dead"]:
            setattr(store, f"{selected['char']}_ghost_events_completed", selected["events_completed"] + 1)
        else:
            setattr(store, f"{selected['char']}_events_completed", selected["events_completed"] + 1)

        return selected["event_label"]


    #Funcion para obtener eventos fantasma
    def get_next_ghost_event(character):
        ghost_completed = getattr(store, f"{character}_ghost_events_completed", 0)
        events_list = ghost_events.get(character, [])

        if ghost_completed < len(events_list):
            return events_list[ghost_completed]
        return None


    def get_character_location(character):
        """
        Determina dónde debería estar un personaje basado en sus eventos pendientes
        """

        events_completed = getattr(store, f"{character}_events_completed", 0)
        current_loop = store.current_loop

        if current_loop == 1:
            maxevents = 5
        else:
            maxevents = 4

        dies = getattr(persistent, f"{character}_dies", False)
        # Para personajes muertos con eventos fantasma pendientes
        if dies:
            #print(f"{character} muerto")
            ghost_completed = getattr(store, f"{character}_ghost_events_completed", None)

            if ghost_completed < len(ghost_events.get(character, [])) and ghost_completed < maxevents:
                #print(f"ghost_completed: {ghost_completed}\n")
                next_event = mandatory_events[current_loop][character][ghost_completed]
                # Solo mostrar si el evento es para el tiempo actual
                if next_event["time"] == store.current_time_block:
                    #print(f"siguiente evento muerto: {next_event} para {store.current_time_block}\n")
                    #print (f"Return ghost from {character} in {next_event['location']}")
                    return next_event["location"]

        # Verificar si el personaje tiene eventos mandatorios pendientes
        if not dies and character in mandatory_events.get(current_loop, {}) and events_completed < len(mandatory_events[current_loop][character]) and events_completed < maxevents:

            next_event = mandatory_events[current_loop][character][events_completed]
            # Solo mostrar si el evento es para el tiempo actual
            if next_event["time"] == store.current_time_block:
                #print (f"Return alive from {character} in {next_event['location']}")
                return next_event["location"]


        return None  # No mostrar icono si no hay razón para estar en el mapa

    def nextloop():
        store.current_Day = 1
        store.current_loop += 1
        store.yamato_events_completed = 0
        store.shiori_events_completed = 0
        store.hikaru_events_completed = 0
        store.yamato_ghost_events_completed = 0
        store.shiori_ghost_events_completed = 0
        store.hikaru_ghost_events_completed = 0


    def check_rutes():
        print(f"Yamato {store.yamato_events_completed}")
        print(f"Shiori {store.shiori_events_completed}")
        print(f"hikaru {store.hikaru_events_completed}")

        if persistent.shiori_dies:
            if store.yamato_events_completed >= 5:
                label_name = f"loop{store.current_loop}_yamato"
                renpy.jump(label_name)
            elif store.hikaru_events_completed >= 5:
                label_name = f"loop{store.current_loop}_hikaru"
                renpy.jump(label_name)
            else:
                route_counts = [
                    ("yamato", store.yamato_events_completed),
                    ("hikaru", store.hikaru_events_completed),
                ]
                route_counts.sort(key=lambda x: (-x[1], x[0]))
                label_name = f"loop{store.current_loop}_{route_counts[0][0]}"
                renpy.jump(label_name)
        else:
            if store.yamato_events_completed >= 5:
                label_name = f"loop{store.current_loop}_yamato"
                renpy.jump(label_name)
            elif store.shiori_events_completed >= 5:
                label_name = f"loop{store.current_loop}_shiori"
                renpy.jump(label_name)
            elif store.hikaru_events_completed >= 5:
                label_name = f"loop{store.current_loop}_hikaru"
                renpy.jump(label_name)
            else:
                route_counts = [
                    ("yamato", store.yamato_events_completed),
                    ("shiori", store.shiori_events_completed),
                    ("hikaru", store.hikaru_events_completed),
                ]
                route_counts.sort(key=lambda x: (-x[1], x[0]))  # Highest progress, then order
                label_name = f"loop{store.current_loop}_{route_counts[0][0]}"
                renpy.jump(label_name)




    # def check_rutes():
    #     print(f"Yamato {store.yamato_events_completed}")
    #     print(f"Shiori {store.shiori_events_completed}")
    #     print(f"hikaru {store.hikaru_events_completed}")

    #     #If persistent.trueendingunlocked is true and you are in loop 1

    #     if store.yamato_events_completed >= 5:

    #         print("Rute Yamato")
    #         label_name = f"loop{store.current_loop}_yamatob"
    #         renpy.callt(label_name)


    #     elif store.shiori_events_completed >= 5:

    #         print("Rute Shiori")
    #         label_name = f"loop{store.current_loop}_shiorib"
    #         renpy.call(label_name)

    #     elif store.hikaru_events_completed >= 5:

    #         print("Rute Hikaru")
    #         label_name = f"loop{store.current_loop}_hikarub"
    #         renpy.call(label_name)




    def truend():
        renpy.call("truend")


label inter:
    jump map


# Label for when there are no events
label location_empty(location):
    "There is nothing interesting in [location]" # [locations[location]] at this moment."
    return


###########################


#Rutes

label loop1_yamatob:
    "Rute Yamato loop1_yamatob"
    "1"
    "2"
    "3"
    "4"
    "5"
    jump map
    return
label loop2_yamatob:
    "Rute Yamato loop2_yamatob"
    "1"
    "2"
    "3"
    "4"
    "5"
    jump map
    return

label loop1_shiorib:

    "Rute shiori loop1_shiorib"
    "1"
    "2"
    "3"
    "4"
    "5"
    jump map
    return

label loop2_shiorib:
    "Rute shiori loop2_shiorib"
    "1"
    "2"
    "3"
    "4"
    "5"
    jump map
    return

label loop1_hikarub:
    "Rute hikaru loop1_hikarub"
    "1"
    "2"
    "3"
    "4"
    "5"
    jump map
    return
label loop2_hikarub:
    "Rute hikaru loop2_hikarub"
    "1"
    "2"
    "3"
    "4"
    "5"
    jump map
    return

# MANDATORY EVENTS - LOOP 1

# Yamato - Loop 1
label loop1_yamato_mandatory1b:
    $ renpy.save("auto_save")
    "Yamato - Day - Dojo"
    "Tag: loop1_yamato_mandatory1b"
    #$ persistent.yamato_dies = True
    #$ print(f"dead: {persistent.yamato_dies}")
    jump map
    return

label loop1_yamato_mandatory2b:
    "Yamato - Night - Dojo"
    "Tag: loop1_yamato_mandatory2b"
    jump map
    return

label loop1_yamato_mandatory3b:
    "Yamato - Night - House"
    "Tag: loop1_yamato_mandatory3b"
    jump map
    return

label loop1_yamato_mandatory4b:
    "Yamato - Day - Town Square"
    "Tag: loop1_yamato_mandatory4b"
    jump map
    return

label loop1_yamato_mandatory5b:
    "Yamato - Night - Forest"
    "Tag: loop1_yamato_mandatory5b"
    $ persistent.yamato_dies = True
    #$ nextloop()
    jump map
    return

# Hikaru - Loop 1
label loop1_hikaru_mandatory1b:
    "Hikaru - Day - Forest"
    "Tag: loop1_hikaru_mandatory1b"
    jump map
    return

label loop1_hikaru_mandatory2b:
    "Hikaru - Day - Dojo"
    "Tag: loop1_hikaru_mandatory2b"
    jump map
    return

label loop1_hikaru_mandatory3b:
    "Hikaru - Night - Town Square"
    "Tag: loop1_hikaru_mandatory3b"
    jump map
    return

label loop1_hikaru_mandatory4b:
    "Hikaru - Day - House"
    "Tag: loop1_hikaru_mandatory4b"
    jump map
    return

label loop1_hikaru_mandatory5b:
    "Hikaru - Day - Shrine"
    "Tag: loop1_hikaru_mandatory5b"
    $ persistent.hikaru_dies = True
    #$ nextloop()
    jump map
    return

# Shiori - Loop 1
label loop1_shiori_mandatory1b:
    "Shiori - Day - Shrine"
    "Tag: loop1_shiori_mandatory1b"
    jump map
    return

label loop1_shiori_mandatory2b:
    "Shiori - Night - Shrine"
    "Tag: loop1_shiori_mandatory2b"
    jump map
    return

label loop1_shiori_mandatory3b:
    "Shiori - Day - Shrine"
    "Tag: loop1_shiori_mandatory3b"
    jump map
    return

label loop1_shiori_mandatory4b:
    "Shiori - Night - Shrine"
    "Tag: loop1_shiori_mandatory4b"
    jump map
    return

label loop1_shiori_mandatory5b:
    "Shiori - Day - Forest"
    "Tag: loop1_shiori_mandatory5b"
    $ persistent.shiori_dies = True
    jump map
    #$ nextloop()
    return

# MANDATORY EVENTS - LOOP 2

# Yamato - Loop 2
label loop2_yamato_mandatory1b:
    "Yamato - Day - Dojo"
    "Tag: loop2_yamato_mandatory1b"
    jump map
    return

label loop2_yamato_mandatory2b:
    "Yamato - Day - Dojo"
    "Tag: loop2_yamato_mandatory2b"
    jump map
    return

label loop2_yamato_mandatory3b:
    "Yamato - Night - Shrine"
    "Tag: loop2_yamato_mandatory3b"
    jump map
    return

label loop2_yamato_mandatory4b:
    "Yamato - Night - Forest"
    "Tag: loop2_yamato_mandatory4b"
    jump map
    return

# Hikaru - Loop 2
label loop2_hikaru_mandatory1b:
    "Hikaru - Day - Forest"
    "Tag: loop2_hikaru_mandatory1b"
    jump map
    return

label loop2_hikaru_mandatory2b:
    "Hikaru - Night - Shrine"
    "Tag: loop2_hikaru_mandatory2b"
    jump map
    return

label loop2_hikaru_mandatory3b:
    "Hikaru - Day - Shrine"
    "Tag: loop2_hikaru_mandatory3b"
    jump map
    return

label loop2_hikaru_mandatory4b:
    "Hikaru - Day - House"
    "Tag: loop2_hikaru_mandatory4b"
    jump map
    return

# Shiori - Loop 2
label loop2_shiori_mandatory1b:
    "Shiori - Day - Town Square"
    "Tag: loop2_shiori_mandatory1b"
    jump map
    return

label loop2_shiori_mandatory2b:
    "Shiori - Day - Shrine"
    "Tag: loop2_shiori_mandatory2b"
    jump map
    return

label loop2_shiori_mandatory3b:
    "Shiori - Night - Shrine"
    "Tag: loop2_shiori_mandatory3b"
    jump map
    return

label loop2_shiori_mandatory4b:
    "Shiori - Night - Shrine"
    "Tag: loop2_shiori_mandatory4b"
    jump map
    return

#

###########Ghost###
label ghost_shiori_1b:
    "ghost_shiori_1"

    return

label ghost_shiori_2b:
    "ghost_shiori_2"
    return

label ghost_shiori_3b:
    "ghost_shiori_3"
    return

label ghost_shiori_4b:
    "ghost_shiori_4"
    return

label ghost_shiori_5b:
    "ghost_shiori_5"
    return


label ghost_yamato_1b:
    "ghost_yamato_1"
    return

label ghost_yamato_2b:
    "ghost_yamato_2"
    return

label ghost_yamato_3b:
    "ghost_yamato_3"
    return

label ghost_yamato_4b:
    "ghost_yamato_4"
    return

label ghost_yamato_5b:
    "ghost_yamato_5"
    return


label ghost_hikaru_1b:
    "ghost_hikaru_1"
    return

label ghost_hikaru_2b:
    "ghost_hikaru_2"
    return

label ghost_hikaru_3b:
    "ghost_hikaru_3"
    return

label ghost_hikaru_4b:
    "ghost_hikaru_4"
    return

label ghost_hikaru_5b:
    "ghost_hikaru_5"
    return

label redirect_to_event:
    scene black_screen
    with fade
    "[redirect_message]"
    with dissolve

    # Actually increment event counter here, only if there IS an event
    if redirect_event_label is not None and redirect_event_char is not None:
        if redirect_event_char == "yamato":
            $ yamato_events_completed += 1
        elif redirect_event_char == "shiori":
            $ shiori_events_completed += 1
        elif redirect_event_char == "hikaru":
            $ hikaru_events_completed += 1

        # Also advance visit counters, day/time only if a real event played
        $ visits_toDay += 1
        if visits_toDay >= 2:
            $ current_Day += 1
            $ visits_toDay = 0
            $ current_time_block = "Day"
        else:
            $ current_time_block = "Night" if current_time_block == "Day" else "Day"

        call expression redirect_event_label

    $ redirect_event_label = None
    $ redirect_event_char = None
    $ redirect_message = ""
    jump map
