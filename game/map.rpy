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
default preferences.skip_unseen=True

define locations = ["shrine", "forest", "dojo", "village","house"]

# define location_positions = {
#     "shrine": (1500, 900),
#     "forest": (400, 425),
#     "dojo": (900, 1000),
#     "village": (1200, 425),
#     "house": (400, 1000)
# }
define location_positions = {
    "shrine": (850, 125),
    "forest": (350, 390),
    "dojo": (1620, 500),
    "village": (975, 950),
    "house": (325, 850)
}
# shrine
# xpos 850 ypos 25
# Forest
# xpos 350 ypos 290
# Dojo
# xpos 1620 ypos 400
# Village
# xpos 975 ypos 850
# House
# xpos 325 ypos 750

# Eventos obligatorios por loop y personaje
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


# define character_icons = {
#     "shiori": "images/map/shiori.png",
#     "yamato": "images/map/yamato.png",
#     "hikaru": "images/map/hikaru.png"
# }

define character_icons_idle = {
    "shiori": "images/map/map_shiori_idle.png",
    "yamato": "images/map/map_yamato_idle.png",
    "hikaru": "images/map/map_hikaru_idle.png"
}

define character_icons_red = {
    "shiori": "images/map/map_shiori_red_hover.png",
    "yamato": "images/map/map_yamato_red_hover.png",
    "hikaru": "images/map/map_hikaru_red_hover.png"
}


define character_icons_yellow= {
    "shiori": "images/map/map_shiori_yellow_hover.png",
    "yamato": "images/map/map_yamato_yellow_hover.png",
    "hikaru": "images/map/map_hikaru_yellow_hover.png"
}


label map:
    #show screen map_screen
    call screen map_screen
    pause


default offset_x_a = 0

# Pantalla del mapa
screen map_screen():



    #BG
    #$ check_rutes()
    if current_time_block == "Day":
        add "images/map/map_day.png"
    else:
        add "images/map/map_night.png"
    if yamato_events_completed >= 5 or shiori_events_completed >= 5 or yamato_events_completed >= 5:
        timer 0.1 action Function(check_rutes) repeat True
    #textbutton "" xsize 1920 ysize 1080 action Function (check_rutes)

    imagebutton auto "images/map/shrine_%s.png" action Function(visit_location_func, "shrine") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 850 ypos 25
    imagebutton auto "images/map/forest_%s.png" action Function(visit_location_func, "forest") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 350 ypos 290
    imagebutton auto "images/map/dojo_%s.png" action Function(visit_location_func, "dojo") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 1620 ypos 400
    imagebutton auto "images/map/village_%s.png" action Function(visit_location_func, "village") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 975 ypos 850
    imagebutton auto "images/map/house_%s.png" action Function(visit_location_func, "house") hover_sound "/sfx/hover_s.mp3" activate_sound "/sfx/active_s.mp3" xpos 325 ypos 750

    # Mostrar iconos de personajes según su ubicación y estado
    for i, character in enumerate(["shiori", "yamato", "hikaru"]):
    #for character in ["shiori"]:

        # Obtener la ubicación actual del personaje
        $ char_location = get_character_location(character)

        if char_location:
            #$ print(f"Sí hay char_location: {char_location}")

            # Obtener posición en el mapa
            $ pos_x, pos_y = location_positions.get(char_location, (0, 0))

            $ icon_x = pos_x + 150   # 284 = button width, 16 = margin

            # button height 122, icon height 150 so like
            $ icon_y = pos_y + (122 // 2) - (150 // 2)


            $ character_icons = character_icons_yellow if persistent.loop1 else character_icons_red

            #btener Icono
            $ icon = character_icons.get(character)

            # Determinar la imagen del icono según el estado
            if getattr(persistent, f"{character}_dies", False):

                # Icono fantasma (transparente o con efecto fantasma)
                add Transform(icon, size=(150, 150)):
                    xpos icon_x
                    ypos icon_y
                    alpha 0.7  # Más transparente para fantasmas
            else:
                # Icono normal
                add Transform(icon, size=(150, 150)):
                    xpos icon_x
                    ypos icon_y


    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        xsize 600
        ysize 250
        background "map/question_frame.png"   # <- This sets your custom image

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            label "Day [current_Day]" xalign 0.5
            text "Where do you want to go?" xalign 0.5





# Función para verificar eventos obligatorios
python early:


    import math


    #Función que se ejecuta al hacer click en alguna parte del mapa

    def visit_location_func(location):
        # Incrementar visitas
        store.visits_toDay += 1

        #check_rutes()

        # Verificar eventos obligatorios primero
        current_mandatory = store.check_mandatory_events(location)

        # Variable para el evento a ejecutar
        event_to_call = None

        if current_mandatory:
            event_to_call = current_mandatory

        # Avanzar el tiempo
        if store.visits_toDay >= 2:
            store.current_Day += 1
            store.visits_toDay = 0
            store.current_time_block = "Day"
        else:
            store.current_time_block = "Night" if store.current_time_block == "Day" else "Day"

        # Llamar al evento si existe
        if event_to_call:
            renpy.call_in_new_context(event_to_call)
        else:
            # Mostrar mensaje de ubicación vacía o algo por defecto
            #renpy.call_in_new_context("location_empty", location)
            time_block = "Night" if store.current_time_block == "Day" else "Day"

            label_name = f"empty_{location}_{time_block}"
            # Verificamos si existe
            if renpy.has_label(label_name):
                #renpy.jump(label_name)
                renpy.call_in_new_context(label_name)
            else:
                renpy.call_in_new_context("location_empty", location)

#Checa en la lista de eventos de vivos y muertos
    def check_mandatory_events(location):
        #print("\n\n\nBuscando nuevo evento")
        # Guardar candidatos vivos y muertos
        alive_candidates = []
        dead_candidates = []
        priority = []

        characters = ["shiori", "yamato", "hikaru"]
        priority = [char for char in characters if not getattr(persistent, f"{char}_dies", False)]
        priority.extend(char for char in characters if getattr(persistent, f"{char}_dies", False))

        for char in priority:

            if getattr(persistent, f"{char}_dies", False):
                events_completed = getattr(store, f"{char}_ghost_events_completed", 0)
                #print(f"{char} muerto")
            else:
                events_completed = getattr(store, f"{char}_events_completed", 0)
                #print(f"{char} vivo")


            #print(f"Eventos luego de dar click:  {events_completed}")
            #print(f"{char} eventos completos {events_completed}")

            if events_completed < len(mandatory_events[store.current_loop][char]):

                next_event = mandatory_events[store.current_loop][char][events_completed]

                #print(f"{char} next_event {next_event["event"]} in {next_event["location"]} at {next_event["time"]}")

                if (next_event["location"] == location and next_event["time"] == store.current_time_block):

                    if getattr(persistent, f"{char}_dies", False):
                        # Muerto → mandar a fantasma
                        ghost_event = get_next_ghost_event(char)
                        if ghost_event:
                            dead_candidates.append(ghost_event)
                    else:
                        # Vivo → evento normal
                        setattr(store, f"{char}_events_completed", events_completed + 1)
                        alive_candidates.append(next_event["event"])
                        #print(f"{char}_dies = False")

            # Prioridad: primero vivos, luego muertos
            if alive_candidates:
                #print(f"Evento vivo: {alive_candidates[0]}******************************************")
                return alive_candidates[0]
            elif dead_candidates:

                ghost_completed = getattr(store, f"{char}_ghost_events_completed", 0)
                setattr(store, f"{char}_ghost_events_completed", ghost_completed + 1)

                #print(f"Evento Muerto: {dead_candidates[0]}******************************************")
                return dead_candidates[0]

        return None


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

        if store.yamato_events_completed >= 5:
            #renpy.hide_screen("map")
            print("Rute Yamato")
            label_name = f"loop{store.current_loop}_yamatob"
            renpy.call_in_new_context(label_name)
            #renpy.call_in_new_context(label_name)

        elif store.shiori_events_completed >= 5:
            #renpy.hide_screen("map")
            print("Rute Shiori")
            label_name = f"loop{store.current_loop}_shiorib"
            renpy.call_in_new_context(label_name)
            #renpy.call_in_new_context(label_name)
        elif store.hikaru_events_completed >= 5:
            #renpy.hide_screen("map")
            print("Rute Hikaru")
            label_name = f"loop{store.current_loop}_hikarub"
            renpy.call_in_new_context(label_name)
            #renpy.call_in_new_context(label_name)



# Label for when there are no events
label location_empty(location):
    "There is nothing interesting in [location]" # [locations[location]] at this moment."
    return







###########################


#Rutes

label loop1_yamatob:
    "Rute Yamato loop1_yamatob"
    return
label loop2_yamatob:
    "Rute Yamato loop2_yamatob"
    return

label loop1_shiorib:
    "Rute shiori loop1_shiorib"
    return

label loop2_shiorib:
    "Rute shiori loop2_shiorib"
    return

label loop1_hikarub:
    "Rute hikaru loop1_hikarub"
    return
label loop2_hikarub:
    "Rute hikaru loop2_hikarub"
    return

# MANDATORY EVENTS - LOOP 1

# Yamato - Loop 1
label loop1_yamato_mandatory1b:
    "Yamato - Day - Dojo"
    "Tag: loop1_yamato_mandatory1b"
    #$ persistent.yamato_dies = True
    #$ print(f"dead: {persistent.yamato_dies}")
    return

label loop1_yamato_mandatory2b:
    "Yamato - Night - Dojo"
    "Tag: loop1_yamato_mandatory2b"
    return

label loop1_yamato_mandatory3b:
    "Yamato - Night - House"
    "Tag: loop1_yamato_mandatory3b"
    return

label loop1_yamato_mandatory4b:
    "Yamato - Day - Town Square"
    "Tag: loop1_yamato_mandatory4b"
    return

label loop1_yamato_mandatory5b:
    "Yamato - Night - Forest"
    "Tag: loop1_yamato_mandatory5b"
    $ persistent.yamato_dies = True
    #$ nextloop()
    return

# Hikaru - Loop 1
label loop1_hikaru_mandatory1b:
    "Hikaru - Day - Forest"
    "Tag: loop1_hikaru_mandatory1b"
    return

label loop1_hikaru_mandatory2b:
    "Hikaru - Day - Dojo"
    "Tag: loop1_hikaru_mandatory2b"
    return

label loop1_hikaru_mandatory3b:
    "Hikaru - Night - Town Square"
    "Tag: loop1_hikaru_mandatory3b"
    return

label loop1_hikaru_mandatory4b:
    "Hikaru - Day - House"
    "Tag: loop1_hikaru_mandatory4b"
    return

label loop1_hikaru_mandatory5b:
    "Hikaru - Day - Shrine"
    "Tag: loop1_hikaru_mandatory5b"
    $ persistent.hikaru_dies = True
    #$ nextloop()
    return

# Shiori - Loop 1
label loop1_shiori_mandatory1b:
    "Shiori - Day - Shrine"
    "Tag: loop1_shiori_mandatory1b"
    return

label loop1_shiori_mandatory2b:
    "Shiori - Night - Shrine"
    "Tag: loop1_shiori_mandatory2b"
    return

label loop1_shiori_mandatory3b:
    "Shiori - Day - Shrine"
    "Tag: loop1_shiori_mandatory3b"
    return

label loop1_shiori_mandatory4b:
    "Shiori - Night - Shrine"
    "Tag: loop1_shiori_mandatory4b"
    return

label loop1_shiori_mandatory5b:
    "Shiori - Day - Forest"
    "Tag: loop1_shiori_mandatory5b"
    $ persistent.shiori_dies = True
    #$ nextloop()
    return

# MANDATORY EVENTS - LOOP 2

# Yamato - Loop 2
label loop2_yamato_mandatory1b:
    "Yamato - Day - Dojo"
    "Tag: loop2_yamato_mandatory1b"
    return

label loop2_yamato_mandatory2b:
    "Yamato - Day - Dojo"
    "Tag: loop2_yamato_mandatory2b"
    return

label loop2_yamato_mandatory3b:
    "Yamato - Night - Shrine"
    "Tag: loop2_yamato_mandatory3b"
    return

label loop2_yamato_mandatory4b:
    "Yamato - Night - Forest"
    "Tag: loop2_yamato_mandatory4b"
    return

# Hikaru - Loop 2
label loop2_hikaru_mandatory1b:
    "Hikaru - Day - Forest"
    "Tag: loop2_hikaru_mandatory1b"
    return

label loop2_hikaru_mandatory2b:
    "Hikaru - Night - Shrine"
    "Tag: loop2_hikaru_mandatory2b"
    return

label loop2_hikaru_mandatory3b:
    "Hikaru - Day - Shrine"
    "Tag: loop2_hikaru_mandatory3b"
    return

label loop2_hikaru_mandatory4b:
    "Hikaru - Day - House"
    "Tag: loop2_hikaru_mandatory4b"
    return

# Shiori - Loop 2
label loop2_shiori_mandatory1b:
    "Shiori - Day - Town Square"
    "Tag: loop2_shiori_mandatory1b"
    return

label loop2_shiori_mandatory2b:
    "Shiori - Day - Shrine"
    "Tag: loop2_shiori_mandatory2b"
    return

label loop2_shiori_mandatory3b:
    "Shiori - Night - Shrine"
    "Tag: loop2_shiori_mandatory3b"
    return

label loop2_shiori_mandatory4b:
    "Shiori - Night - Shrine"
    "Tag: loop2_shiori_mandatory4b"
    return

# RANDOM EVENTS - LOOP 1

# Yamato - Random Loop 1
label loop1_yamato_nonmandatory1b:
    "Yamato - Night - Forest"
    "Tag: loop1_yamato_nonmandatory1b"
    return

label loop1_yamato_nonmandatory2b:
    "Yamato - Day - Shrine"
    "Tag: loop1_yamato_nonmandatory2b"
    return

label loop1_yamato_nonmandatory3b:
    "Yamato - Day - Village"
    "Tag: loop1_yamato_nonmandatory3b"
    return

# Hikaru - Random Loop 1
label loop1_hikaru_nonmandatory1b:
    "Hikaru - Night - Forest"
    "Tag: loop1_hikaru_nonmandatory1b"
    return

label loop1_hikaru_nonmandatory2b:
    "Hikaru - Day - Shrine"
    "Tag: loop1_hikaru_nonmandatory2b"
    return

label loop1_hikaru_nonmandatory3b:
    "Hikaru - Night - Shrine"
    "Tag: loop1_hikaru_nonmandatory3b"
    return

# Shiori - Random Loop 1
label loop1_shiori_nonmandatory1b:
    "Shiori - Day - Forest"
    "Tag: loop1_shiori_nonmandatory1b"
    return

label loop1_shiori_nonmandatory2b:
    "Shiori - Day - Shrine"
    "Tag: loop1_shiori_nonmandatory2b"
    return

label loop1_shiori_nonmandatory3b:
    "Shiori - Night - House"
    "Tag: loop1_shiori_nonmandatory3b"
    return

label loop1_shiori_nonmandatory4b:
    "Shiori - Night - Shrine"
    "Tag: loop1_shiori_nonmandatory4b"
    return



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
