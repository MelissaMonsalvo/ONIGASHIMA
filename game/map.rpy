# Variables para el progreso del juego
default current_day = 1
default current_time_block = "day"  # "day" o "night"
default current_loop = 1
default visits_today = 0

# Variables para el progreso de los personajes
default yamato_events_completed = 0
default hikaru_events_completed = 0
default shiori_events_completed = 0

#! Quitar
default preferences.skip_unseen=True

# Variable para llevar registro de eventos ya mostrados
default shown_random_events = {}


define locations = {
    "shrine": "Santuario",
    "forest": "Bosque",
    "dojo": "Dojo",
    "town_square": "Plaza del Pueblo",
    "house": "Casa"
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

label map:
    #show screen map_screen
    call screen map_screen
    pause



# Pantalla del mapa
screen map_screen():

    #BG
    add "images/map/bg.png"

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


    def check_mandatory_events(location):
        for char in ["yamato", "hikaru", "shiori"]:
            events_completed = getattr(store, f"{char}_events_completed", 0)
            print( f"{char}_events_complete : {events_completed}")
            if events_completed < len(mandatory_events[store.current_loop][char]):
                next_event = mandatory_events[store.current_loop][char][events_completed]
                if (next_event["location"] == location and next_event["time"] == store.current_time_block):
                    setattr(store, f"{char}_events_completed", events_completed + 1)
                    return next_event["event"]
        return None


# Función para obtener evento aleatorio (CORREGIDA - por personaje)
    def get_random_event(loop, location):
        """
        Obtiene un evento aleatorio disponible solo de personajes
        que hayan completado todos sus eventos obligatorios
        """
        # Verificar si hay eventos para este loop
        if loop not in random_events:
            return None
        
        available_events = []
        
        # Revisar todos los personajes
        for character in random_events[loop]:
            # Verificar si el personaje tiene eventos aleatorios
            if not random_events[loop][character]:
                continue
            
            # VERIFICAR SI EL PERSONAJE COMPLETÓ SUS EVENTOS OBLIGATORIOS
            events_completed = getattr(store, f"{character}_events_completed", 0)
            total_mandatory = len(mandatory_events[loop][character])
            
            # Solo considerar personajes que completaron todos sus eventos obligatorios
            if events_completed < total_mandatory:
                continue  # Saltar este personaje
                
            # Filtrar eventos que coincidan con ubicación y tiempo actual
            for event_data in random_events[loop][character]:
                if (event_data["location"] == location and 
                    event_data["time"] == store.current_time_block):
                    
                    # Verificar si el evento ya fue mostrado
                    event_key = f"{loop}_{character}_{event_data['event']}"
                    if event_key not in shown_random_events:
                        available_events.append((character, event_data))
        
        # Si no hay eventos disponibles
        if not available_events:
            return None
        
        # Elegir un evento aleatorio
        chosen_character, chosen_event = renpy.random.choice(available_events)
        
        # Marcar como mostrado
        event_key = f"{loop}_{chosen_character}_{chosen_event['event']}"
        shown_random_events[event_key] = True
        
        return chosen_event["event"]


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