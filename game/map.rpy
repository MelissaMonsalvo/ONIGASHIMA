# Variables para el progreso del juego
default current_day = 1
default current_time_block = "day"  # "day" o "night"
default current_loop = 1
default visits_today = 0

# Variables para el progreso de los personajes
default yamato_events_completed = 0
default hikaru_events_completed = 0
default shiori_events_completed = 0

# Variables para los eventos fantasmas de los personajes
define shiori_ghost_events_completed = 0
define yamato_ghost_events_completed = 0
define hikaru_ghost_events_completed = 0


#! Quitar
default preferences.skip_unseen=True

# Variable para llevar registro de eventos ya mostrados
default shown_random_events = {}


define locations = ["shrine", "forest", "dojo", "town_square","house"]

define location_positions = {
    "shrine": (1500, 900),
    "forest": (400, 425),
    "dojo": (900, 1000),
    "town_square": (1200, 425),
    "house": (400, 1000)
}
# Eventos obligatorios por loop y personaje
define mandatory_events = {
    1: {
        "yamato": [
            {"location": "dojo", "time": "day", "event": "loop1_yamato_mandatory1b"},
            {"location": "dojo", "time": "night", "event": "loop1_yamato_mandatory2b"},
            {"location": "house", "time": "night", "event": "loop1_yamato_mandatory3b"},
            {"location": "town_square", "time": "day", "event": "loop1_yamato_mandatory4b"},
            {"location": "forest", "time": "night", "event": "loop1_yamato_mandatory5b"}
        ],
        "hikaru": [
            {"location": "forest", "time": "day", "event": "loop1_hikaru_mandatory1b"},
            {"location": "dojo", "time": "day", "event": "loop1_hikaru_mandatory2b"},
            {"location": "town_square", "time": "night", "event": "loop1_hikaru_mandatory3b"},
            {"location": "house", "time": "day", "event": "loop1_hikaru_mandatory4b"},
            {"location": "shrine", "time": "day", "event": "loop1_hikaru_mandatory5b"}
        ],
        "shiori": [
            {"location": "shrine", "time": "day", "event": "loop1_shiori_mandatory1b"},
            {"location": "shrine", "time": "night", "event": "loop1_shiori_mandatory2b"},
            {"location": "shrine", "time": "day", "event": "loop1_shiori_mandatory3b"},
            {"location": "shrine", "time": "night", "event": "loop1_shiori_mandatory4b"},
            {"location": "forest", "time": "day", "event": "loop1_shiori_mandatory5b"}
        ]
    },
    2: {
        "yamato": [
            {"location": "dojo", "time": "day", "event": "loop2_yamato_mandatory1b"},
            {"location": "dojo", "time": "day", "event": "loop2_yamato_mandatory2b"},
            {"location": "shrine", "time": "night", "event": "loop2_yamato_mandatory3b"},
            {"location": "forest", "time": "night", "event": "loop2_yamato_mandatory4b"}
        ],
        "hikaru": [
            {"location": "forest", "time": "day", "event": "loop2_hikaru_mandatory1b"},
            {"location": "shrine", "time": "night", "event": "loop2_hikaru_mandatory2b"},
            {"location": "shrine", "time": "day", "event": "loop2_hikaru_mandatory3b"},
            {"location": "house", "time": "day", "event": "loop2_hikaru_mandatory4b"}
        ],
        "shiori": [
            {"location": "town_square", "time": "day", "event": "loop2_shiori_mandatory1b"},
            {"location": "shrine", "time": "day", "event": "loop2_shiori_mandatory2b"},
            {"location": "shrine", "time": "night", "event": "loop2_shiori_mandatory3b"},
            {"location": "shrine", "time": "night", "event": "loop2_shiori_mandatory4b"}
        ]
    }
}


# Definir los eventos aleatorios
define random_events = {
    1: {
        "yamato": [
            {"location": "forest", "time": "night", "event": "loop1_yamato_nonmandatory1b"},
            {"location": "shrine", "time": "day", "event": "loop1_yamato_nonmandatory2b"},
            {"location": "village", "time": "day", "event": "loop1_yamato_nonmandatory3b"}
        ],
        "hikaru": [
            {"location": "forest", "time": "night", "event": "loop1_hikaru_nonmandatory1b"},
            {"location": "shrine", "time": "day", "event": "loop1_hikaru_nonmandatory2b"},
            {"location": "shrine", "time": "night", "event": "loop1_hikaru_nonmandatory3b"}
        ],
        "shiori": [
            {"location": "forest", "time": "day", "event": "loop1_shiori_nonmandatory1b"},
            {"location": "shrine", "time": "day", "event": "loop1_shiori_nonmandatory2b"},
            {"location": "house", "time": "night", "event": "loop1_shiori_nonmandatory3b"},
            {"location": "shrine", "time": "night", "event": "loop1_shiori_nonmandatory4b"}
        ]
    },
    2: {
        # Puedes agregar eventos random para el loop 2 aquí cuando los necesites
        "yamato": [],
        "hikaru": [],
        "shiori": []
    }
}

# Definir los eventos fantasmas
define ghost_events = {
    "shiori": ["ghost_shiori_1b", "ghost_shiori_2b", "ghost_shiori_3b", "ghost_shiori_4b", "ghost_shiori_5b"],
    "yamato": ["ghost_yamato_1b", "ghost_yamato_2b", "ghost_yamato_3b", "ghost_yamato_4b", "ghost_yamato_5b"],
    "hikaru": ["ghost_hikaru_1b", "ghost_hikaru_2b", "ghost_hikaru_3b", "ghost_hikaru_4b", "ghost_hikaru_5b"]
}



define character_icons = {
    "shiori": "images/map/shiori.png",
    "yamato": "images/map/yamato.png",
    "hikaru": "images/map/hikaru.png"
}


label map:
    #show screen map_screen
    call screen map_screen
    pause



# Pantalla del mapa
screen map_screen():

    #BG
    add "images/map/bg.png"
        # Se calcula una sola vez
    #default icon_data = build_icon_data(store.current_loop, store.current_time_block)

    #Shrine
    imagebutton auto "images/map/shrine_%s.png" focus_mask True action Function(visit_location_func, "shrine") hover_sound "/audio/buttons/hover_s.mp3" activate_sound "/audio/buttons/active_s.mp3"
    #Forest
    imagebutton auto "images/map/forest_%s.png" focus_mask True action Function(visit_location_func, "forest") hover_sound "/audio/buttons/hover_s.mp3" activate_sound "/audio/buttons/active_s.mp3"
    #Dojo
    imagebutton auto "images/map/dojo_%s.png" focus_mask True action Function(visit_location_func, "dojo") hover_sound "/audio/buttons/hover_s.mp3" activate_sound "/audio/buttons/active_s.mp3"
    #town_square
    imagebutton auto "images/map/village_%s.png" focus_mask True action Function(visit_location_func, "town_square") hover_sound "/audio/buttons/hover_s.mp3" activate_sound "/audio/buttons/active_s.mp3"
    #house
    imagebutton auto "images/map/house_%s.png" focus_mask True action Function(visit_location_func, "house") hover_sound "/audio/buttons/hover_s.mp3" activate_sound "/audio/buttons/active_s.mp3"

    # Dibujar íconos en un solo for
    # for (pos, char) in icon_data:
    #     add Transform(character_icons[char], size=(50, 50)) xpos pos[0] ypos pos[1]


    # Mostrar iconos de personajes en sus ubicaciones
    $ icon_data = build_icon_data(store.current_loop, store.current_time_block)
    
    for location, characters in icon_data.items():
        $ pos = location_positions.get(location, (0, 0))
        $ x_pos, y_pos = pos
        
        # Mostrar iconos de personajes vivos
        for character in characters.get("alive", []):
            $ icon = character_icons.get(character)
            if icon:
                # Ajustar posición para múltiples personajes en la misma ubicación
                $ offset_x = characters["alive"].index(character) * 50  # Espaciado horizontal
                imagebutton:
                    idle Transform(icon, size=(150, 150))
                    hover Transform(icon, size=(150, 150))
                    xpos x_pos + offset_x
                    ypos y_pos - 30  # Levantar un poco el icono sobre la ubicación
                    action NullAction()
                    tooltip character.capitalize()
        
        # Mostrar iconos de personajes fantasmas (en tono gris/transparente)
        for character in characters.get("ghost", []):
            $ icon = character_icons.get(character)
            if icon:
                $ offset_x = characters["ghost"].index(character) * 50
                imagebutton:
                    idle Transform(im.Grayscale(icon), size=(50, 50))   # Convertir a escala de grises
                    hover Transform(im.Grayscale(icon), size=(50, 50)) 
                    xpos x_pos + offset_x
                    ypos y_pos - 30
                    #alpha 0.7  # Hacerlo semi-transparente
                    action NullAction()
                    tooltip character.capitalize() + " (Fantasma)"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 50
        
        vbox:
            label "Map - Día [current_day] - [current_time_block]"
            text "Where do you want to go?"





# Función para verificar eventos obligatorios
python early:


    import math

    def get_circle_positions(center_x, center_y, radius, count):
        positions = []
        if count == 0:
            return positions
        angle_step = 2 * math.pi / count
        for i in range(count):
            angle = i * angle_step
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            positions.append((x, y))
        return positions

    #Función que se ejecuta al hacer click en alguna parte del mapa

    def visit_location_func(location):
        # Incrementar visitas
        store.visits_today += 1
        # Verificar eventos obligatorios primero
        current_mandatory = store.check_mandatory_events(location)
        
        # Variable para el evento a ejecutar
        event_to_call = None
        
        if current_mandatory:
            # Hay evento obligatorio
            event_to_call = current_mandatory
        else:
            # Buscar eventos aleatorios solo de personajes que hayan completado sus obligatorios
            event_to_call = store.get_random_event(store.current_loop, location)
        
        # Avanzar el tiempo
        if store.visits_today >= 2:
            store.current_day += 1
            store.visits_today = 0
            store.current_time_block = "day"
        else:
            store.current_time_block = "night" if store.current_time_block == "day" else "day"

        # Llamar al evento si existe
        if event_to_call:
            renpy.call_in_new_context(event_to_call)
        else:
            # Mostrar mensaje de ubicación vacía o algo por defecto
            renpy.call_in_new_context("location_empty", location)

#Checa en la lista de eventos de vivos y muertos
    def check_mandatory_events(location):
        # Guardar candidatos vivos y muertos
        alive_candidates = []
        dead_candidates = []

        for char in ["yamato", "hikaru", "shiori"]:
            events_completed = getattr(store, f"{char}_events_completed", 0)
            if events_completed < len(mandatory_events[store.current_loop][char]):
                next_event = mandatory_events[store.current_loop][char][events_completed]
                if (next_event["location"] == location and next_event["time"] == store.current_time_block):
                    if getattr(persistent, f"{char}_dies", False):
                        # Muerto → mandar a fantasma
                        ghost_event = get_next_ghost_event(char)
                        print(f"{char}_dies = True")
                        if ghost_event:
                            dead_candidates.append(ghost_event)
                    else:
                        # Vivo → evento normal
                        setattr(store, f"{char}_events_completed", events_completed + 1)
                        alive_candidates.append(next_event["event"])
                        print(f"{char}_dies = False")

        # Prioridad: primero vivos, luego muertos
        if alive_candidates:
            return alive_candidates[0]
        elif dead_candidates:
            return dead_candidates[0]

        return None

    # funcion random para eventos    
    def get_random_event(loop, location):
        if loop not in random_events:
            return None
        
        alive_events = []
        dead_events = []

        for character in random_events[loop]:
            if not random_events[loop][character]:
                continue
            
            events_completed = getattr(store, f"{character}_events_completed", 0)
            total_mandatory = len(mandatory_events[loop][character])
            if events_completed < total_mandatory:
                continue  

            if getattr(persistent, f"{character}_dies", False):
                # Muerto → usar evento fantasma
                ghost_event = get_next_ghost_event(character)
                if ghost_event:
                    dead_events.append(ghost_event)
            else:
                # Vivo → revisar randoms normales
                for event_data in random_events[loop][character]:
                    if (event_data["location"] == location and 
                        event_data["time"] == store.current_time_block):
                        
                        event_key = f"{loop}_{character}_{event_data['event']}"
                        if event_key not in shown_random_events:
                            alive_events.append((character, event_data))
        
        # Prioridad: primero vivos, luego muertos
        if alive_events:
            chosen_character, chosen_event = renpy.random.choice(alive_events)
            event_key = f"{loop}_{chosen_character}_{chosen_event['event']}"
            shown_random_events[event_key] = True
            return chosen_event["event"]
        
        if dead_events:
            return dead_events[0]  # Fantasma en orden

        return None


    #Funcion para obtener eventos fantasma

    def get_next_ghost_event(character):
        ghost_completed = getattr(store, f"{character}_ghost_events_completed", 0)
        events_list = ghost_events.get(character, [])

        if ghost_completed < len(events_list):
            setattr(store, f"{character}_ghost_events_completed", ghost_completed + 1)
            return events_list[ghost_completed]
        return None



    def build_icon_data(current_loop, current_time_block):
        icon_data = {}
        
        # Inicializar estructura para cada ubicación
        for location in locations:
            icon_data[location] = {"alive": [], "ghost": []}
        
        # Determinar el número máximo de eventos obligatorios por loop
        if current_loop == 1:
            max_mandatory_events = 5
        else:
            max_mandatory_events = 4
        
        # Verificar eventos obligatorios para personajes vivos y fantasmas
        for character in ["yamato", "hikaru", "shiori"]:
            # Determinar si el personaje está vivo usando las variables persistentes
            if character == "shiori":
                alive = not persistent.shiori_dies
            elif character == "yamato":
                alive = not persistent.yamato_dies
            elif character == "hikaru":
                alive = not persistent.hikaru_dies
            else:
                alive = True
            
            print(f"{character} alive: {alive}")

            
            # Obtener eventos completados del personaje
            events_completed = globals().get(f"{character}_events_completed", 0)

            
            # Verificar si todos los eventos obligatorios del loop están completados
            all_mandatory_completed = (events_completed >= max_mandatory_events)

            print(f"events_completed: {events_completed}, Todos los eventos completados? : {all_mandatory_completed}")




            # Buscar en eventos obligatorios (solo si no están todos completados)
            if not all_mandatory_completed and current_loop in mandatory_events and character in mandatory_events[current_loop]:
                
                print("\n\nbuscando eventos obligatorios**********")
                
                next_event = mandatory_events[current_loop][character][events_completed]

                if (next_event["time"] == current_time_block and 
                    next_event["location"] in icon_data and
                    not event_completed(next_event["event"])):
                    
                    if alive:
                        if character not in icon_data[next_event["location"]]["alive"]:
                            icon_data[next_event["location"]]["alive"].append(character)
                            print(f"Evento de {next_event['event']} alive, en {next_event['location']} at {next_event['time']}")
                    else:
                        if character not in icon_data[next_event["location"]]["ghost"]:
                            icon_data[next_event["location"]]["ghost"].append(character)
                            print(f"Evento de {next_event['event']} ghost, en {next_event['location']} at {next_event['time']}")

            #Buscar en eventos aleatorios (solo para personajes vivos Y después de completar todos los obligatorios)
            #if True:
            if (alive and all_mandatory_completed and 
                current_loop in random_events and character in random_events[current_loop]):
            
                for event in random_events[current_loop][character]:
                    if (event["time"] == current_time_block and 
                        event["location"] in icon_data and
                        not event_completed(event["event"])):
                        if character not in icon_data[event["location"]]["alive"]:
                            icon_data[event["location"]]["alive"].append(character)
                            print(f"Evento de {event['event']} ghost, en {event['location']} at {event['time']}")
            
            # Buscar en eventos fantasmas (solo para personajes muertos, sin importar eventos completados)
            if (not alive and current_loop in mandatory_events and 
                character in mandatory_events[current_loop]):
                
                next_ghost_event_index = globals().get(f"{character}_ghost_events_completed", 0)
                next_event = mandatory_events[current_loop][character][next_ghost_event_index]
                    
                if (next_event["time"] == current_time_block and 
                        next_event["location"] in icon_data and
                        not event_completed(next_event["event"])):
                        
                        if character not in icon_data[next_event["location"]]["ghost"]:
                            icon_data[next_event["location"]]["ghost"].append(character)
                            print(f"-----------------Evento de {next_event['event']} ghost, en {next_event['location']} at {next_event['time']}")
        


                # for event in mandatory_events[current_loop][character]:
                #     if (event["time"] == current_time_block and 
                #         event["location"] in icon_data and
                #         not event_completed(event["event"])):
                        
                #         if character not in icon_data[event["location"]]["ghost"]:
                #             icon_data[event["location"]]["ghost"].append(character)
        
        return icon_data

        # Función auxiliar para verificar si un evento ya fue completado
    def event_completed(event_name):
        # Esta función debería verificar en tu sistema de guardado si el evento ya ocurrió
        # Puedes usar variables persistentes o otro sistema de tracking
        # Por ejemplo: return persistent.event_tracker.get(event_name, False)
        return False  # Cambiar según tu implementación

    #Funcaion para dibujar personajes en mapa

    # def get_characters_in_location(loop, location, time_block):
    #     present_chars = []

    #     for char in ["yamato", "hikaru", "shiori"]:
    #         # PERSONAJE MUERTO → usa fantasma
    #         if getattr(persistent, f"{char}_dies", False):
    #             ghost_completed = getattr(store, f"{char}_ghost_events_completed", 0)
    #             events_list = ghost_events.get(char, [])
    #             if ghost_completed < len(events_list):
    #                 # Si quieres que fantasma aparezca SIEMPRE en el mapa:
    #                 present_chars.append(char)
    #                 # Si quieres que fantasma dependa de location/time,
    #                 # necesitarías guardar esos datos también en ghost_events
    #         else:
    #             # OBLIGATORIOS
    #             events_completed = getattr(store, f"{char}_events_completed", 0)
    #             if events_completed < len(mandatory_events[loop][char]):
    #                 next_event = mandatory_events[loop][char][events_completed]
    #                 if next_event["location"] == location and next_event["time"] == time_block:
    #                     present_chars.append(char)
    #                     continue
                
    #             # RANDOMS
    #             for event_data in random_events[loop][char]:
    #                 if (event_data["location"] == location and event_data["time"] == time_block):
    #                     event_key = f"{loop}_{char}_{event_data['event']}"
    #                     if event_key not in shown_random_events:
    #                         present_chars.append(char)
    #                         break  # Evitar duplicados

    #     print("present_chars: ", present_chars, "\n")
    #     return present_chars




    # def build_icon_data(loop, time_block):
    #     result = []
    #     for location in locations:
    #         print("location: ", location, "*************************************\n")

    #         chars_here = get_characters_in_location(loop, location, time_block)
    #         print("chars_here: ", chars_here, "\n")
            
    #         center_x, center_y = location_positions[location]
    #         print("Center: ", location_positions[location], "\n")

    #         positions = get_circle_positions(center_x, center_y, 50, len(chars_here))
    #         print("positions: ", positions, "\n")

    #         for (pos, char) in zip(positions, chars_here):
    #             result.append((pos, char))

    #         #print("result: ", result, "\n")
    #     return result



# Label para cuando no hay eventos
label location_empty(location):
    "No hay nada interesante en [location]" #[locations[location]] en este momento."
    return


###########################

# EVENTOS OBLIGATORIOS - LOOP 1

# Yamato - Loop 1
label loop1_yamato_mandatory1b:
    "Yamato - Día - Dojo"
    "Etiqueta: loop1_yamato_mandatory1b"
    #$ persistent.yamato_dies = True
    #$ print(f"muerto: {persistent.yamato_dies}")
    return

label loop1_yamato_mandatory2b:
    "Yamato - Noche - Dojo"
    "Etiqueta: loop1_yamato_mandatory2b"
    return

label loop1_yamato_mandatory3b:
    "Yamato - Noche - Casa"
    "Etiqueta: loop1_yamato_mandatory3b"
    return

label loop1_yamato_mandatory4b:
    "Yamato - Día - Plaza del Pueblo"
    "Etiqueta: loop1_yamato_mandatory4b"
    return

label loop1_yamato_mandatory5b:
    "Yamato - Noche - Bosque"
    "Etiqueta: loop1_yamato_mandatory5b"
    $ persistent.yamato_dies = True
    return

# Hikaru - Loop 1
label loop1_hikaru_mandatory1b:
    "Hikaru - Día - Bosque"
    "Etiqueta: loop1_hikaru_mandatory1b"
    return

label loop1_hikaru_mandatory2b:
    "Hikaru - Día - Dojo"
    "Etiqueta: loop1_hikaru_mandatory2b"
    return

label loop1_hikaru_mandatory3b:
    "Hikaru - Noche - Plaza del Pueblo"
    "Etiqueta: loop1_hikaru_mandatory3b"
    return

label loop1_hikaru_mandatory4b:
    "Hikaru - Día - Casa"
    "Etiqueta: loop1_hikaru_mandatory4b"
    return

label loop1_hikaru_mandatory5b:
    "Hikaru - Día - Santuario"
    "Etiqueta: loop1_hikaru_mandatory5b"
    return

# Shiori - Loop 1
label loop1_shiori_mandatory1b:
    "Shiori - Día - Santuario"
    "Etiqueta: loop1_shiori_mandatory1b"
    return

label loop1_shiori_mandatory2b:
    "Shiori - Noche - Santuario"
    "Etiqueta: loop1_shiori_mandatory2b"
    return

label loop1_shiori_mandatory3b:
    "Shiori - Día - Santuario"
    "Etiqueta: loop1_shiori_mandatory3b"
    return

label loop1_shiori_mandatory4b:
    "Shiori - Noche - Santuario"
    "Etiqueta: loop1_shiori_mandatory4b"
    return

label loop1_shiori_mandatory5b:
    "Shiori - Día - Bosque"
    "Etiqueta: loop1_shiori_mandatory5b"
    $ persistent.shiori_dies = True
    return

# EVENTOS OBLIGATORIOS - LOOP 2

# Yamato - Loop 2
label loop2_yamato_mandatory1b:
    "Yamato - Día - Dojo"
    "Etiqueta: loop2_yamato_mandatory1b"
    return

label loop2_yamato_mandatory2b:
    "Yamato - Día - Dojo"
    "Etiqueta: loop2_yamato_mandatory2b"
    return

label loop2_yamato_mandatory3b:
    "Yamato - Noche - Santuario"
    "Etiqueta: loop2_yamato_mandatory3b"
    return

label loop2_yamato_mandatory4b:
    "Yamato - Noche - Bosque"
    "Etiqueta: loop2_yamato_mandatory4b"
    return

# Hikaru - Loop 2
label loop2_hikaru_mandatory1b:
    "Hikaru - Día - Bosque"
    "Etiqueta: loop2_hikaru_mandatory1b"
    return

label loop2_hikaru_mandatory2b:
    "Hikaru - Noche - Santuario"
    "Etiqueta: loop2_hikaru_mandatory2b"
    return

label loop2_hikaru_mandatory3b:
    "Hikaru - Día - Santuario"
    "Etiqueta: loop2_hikaru_mandatory3b"
    return

label loop2_hikaru_mandatory4b:
    "Hikaru - Día - Casa"
    "Etiqueta: loop2_hikaru_mandatory4b"
    return

# Shiori - Loop 2
label loop2_shiori_mandatory1b:
    "Shiori - Día - Plaza del Pueblo"
    "Etiqueta: loop2_shiori_mandatory1b"
    return

label loop2_shiori_mandatory2b:
    "Shiori - Día - Santuario"
    "Etiqueta: loop2_shiori_mandatory2b"
    return

label loop2_shiori_mandatory3b:
    "Shiori - Noche - Santuario"
    "Etiqueta: loop2_shiori_mandatory3b"
    return

label loop2_shiori_mandatory4b:
    "Shiori - Noche - Santuario"
    "Etiqueta: loop2_shiori_mandatory4b"
    return

# EVENTOS ALEATORIOS - LOOP 1

# Yamato - Aleatorios Loop 1
label loop1_yamato_nonmandatory1b:
    "Yamato - Noche - Bosque"
    "Etiqueta: loop1_yamato_nonmandatory1b"
    return

label loop1_yamato_nonmandatory2b:
    "Yamato - Día - Santuario"
    "Etiqueta: loop1_yamato_nonmandatory2b"
    return

label loop1_yamato_nonmandatory3b:
    "Yamato - Día - Pueblo"
    "Etiqueta: loop1_yamato_nonmandatory3b"
    return

# Hikaru - Aleatorios Loop 1
label loop1_hikaru_nonmandatory1b:
    "Hikaru - Noche - Bosque"
    "Etiqueta: loop1_hikaru_nonmandatory1b"
    return

label loop1_hikaru_nonmandatory2b:
    "Hikaru - Día - Santuario"
    "Etiqueta: loop1_hikaru_nonmandatory2b"
    return

label loop1_hikaru_nonmandatory3b:
    "Hikaru - Noche - Santuario"
    "Etiqueta: loop1_hikaru_nonmandatory3b"
    return

# Shiori - Aleatorios Loop 1
label loop1_shiori_nonmandatory1b:
    "Shiori - Día - Bosque"
    "Etiqueta: loop1_shiori_nonmandatory1b"
    return

label loop1_shiori_nonmandatory2b:
    "Shiori - Día - Santuario"
    "Etiqueta: loop1_shiori_nonmandatory2b"
    return

label loop1_shiori_nonmandatory3b:
    "Shiori - Noche - Casa"
    "Etiqueta: loop1_shiori_nonmandatory3b"
    return

label loop1_shiori_nonmandatory4b:
    "Shiori - Noche - Santuario"
    "Etiqueta: loop1_shiori_nonmandatory4b"
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
