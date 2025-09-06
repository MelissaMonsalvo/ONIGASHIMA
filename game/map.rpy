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
            {"location": "dojo", "time": "day", "event": "loop1_yamato_mandatory1"},
            {"location": "dojo", "time": "night", "event": "loop1_yamato_mandatory2"},
            {"location": "house", "time": "night", "event": "loop1_yamato_mandatory3"},
            {"location": "town_square", "time": "day", "event": "loop1_yamato_mandatory4"},
            {"location": "forest", "time": "night", "event": "loop1_yamato_mandatory5"}
        ],
        "hikaru": [
            {"location": "forest", "time": "day", "event": "loop1_hikaru_mandatory1"},
            {"location": "dojo", "time": "day", "event": "loop1_hikaru_mandatory2"},
            {"location": "town_square", "time": "night", "event": "loop1_hikaru_mandatory3"},
            {"location": "house", "time": "day", "event": "loop1_hikaru_mandatory4"},
            {"location": "shrine", "time": "day", "event": "loop1_hikaru_mandatory5"}
        ],
        "shiori": [
            {"location": "shrine", "time": "day", "event": "loop1_shiori_mandatory1"},
            {"location": "shrine", "time": "night", "event": "loop1_shiori_mandatory2"},
            {"location": "shrine", "time": "day", "event": "loop1_shiori_mandatory3"},
            {"location": "shrine", "time": "night", "event": "loop1_shiori_mandatory4"},
            {"location": "forest", "time": "day", "event": "loop1_shiori_mandatory5"}
        ]
    },
    2: {
        "yamato": [
            {"location": "dojo", "time": "day", "event": "loop2_yamato_mandatory1"},
            {"location": "dojo", "time": "day", "event": "loop2_yamato_mandatory2"},
            {"location": "shrine", "time": "night", "event": "loop2_yamato_mandatory3"},
            {"location": "forest", "time": "night", "event": "loop2_yamato_mandatory4"}
        ],
        "hikaru": [
            {"location": "forest", "time": "day", "event": "loop2_hikaru_mandatory1"},
            {"location": "shrine", "time": "night", "event": "loop2_hikaru_mandatory2"},
            {"location": "shrine", "time": "day", "event": "loop2_hikaru_mandatory3"},
            {"location": "house", "time": "day", "event": "loop2_hikaru_mandatory4"}
        ],
        "shiori": [
            {"location": "town_square", "time": "day", "event": "loop2_shiori_mandatory1"},
            {"location": "shrine", "time": "day", "event": "loop2_shiori_mandatory2"},
            {"location": "shrine", "time": "night", "event": "loop2_shiori_mandatory3"},
            {"location": "shrine", "time": "night", "event": "loop2_shiori_mandatory4"}
        ]
    }
}


# Definir los eventos aleatorios
define random_events = {
    1: {
        "yamato": [
            {"location": "forest", "time": "night", "event": "loop1_yamato_nonmandatory1"},
            {"location": "shrine", "time": "day", "event": "loop1_yamato_nonmandatory2"},
            {"location": "village", "time": "day", "event": "loop1_yamato_nonmandatory3"}
        ],
        "hikaru": [
            {"location": "forest", "time": "night", "event": "loop1_hikaru_nonmandatory1"},
            {"location": "shrine", "time": "day", "event": "loop1_hikaru_nonmandatory2"},
            {"location": "shrine", "time": "night", "event": "loop1_hikaru_nonmandatory3"}
        ],
        "shiori": [
            {"location": "forest", "time": "day", "event": "loop1_shiori_nonmandatory1"},
            {"location": "shrine", "time": "day", "event": "loop1_shiori_nonmandatory2"},
            {"location": "house", "time": "night", "event": "loop1_shiori_nonmandatory3"},
            {"location": "shrine", "time": "night", "event": "loop1_shiori_nonmandatory4"}
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



# Función Python que reemplaza al label visit_location
init python:
    def visit_location_func(location):
        # Incrementar visitas

        store.visits_today += 1
        
        # Verificar eventos obligatorios
        current_mandatory = store.check_mandatory_events(location)
        
        # Avanzar el tiempo
        if store.visits_today >= 2:
            store.current_day += 1
            store.visits_today = 0
            store.current_time_block = "day"
        else:
            store.current_time_block = "night" if store.current_time_block == "day" else "day"

        #Llamar a la label
        if current_mandatory:
            #renpy.jump(current_mandatory)
            renpy.call_in_new_context(current_mandatory)
        else:
            print("random event")
            #renpy.call_in_new_context("get_random_event", location)
            current_mandatory = store.get_random_event(1,location)
        
        if current_mandatory:
            renpy.call_in_new_context(current_mandatory)
        else:
            print("Sin lugar")
        
       
        
        # Verificar rutas completadas
        # renpy.call_in_new_context("check_route_completion")



# # Función para visitar una ubicación
# label visit_location(location):
#     $ visits_today += 1
    
#     # Verificar si hay evento obligatorio
#     $ current_mandatory = check_mandatory_events(location)
#     $ print(location)
#     if current_mandatory:
#         call expression current_mandatory
#     # else:
#     #     # Evento aleatorio o ubicación vacía
#     #     call random_event(location)
    
#     # Avanzar el tiempo
#     if visits_today >= 2:
#         $ current_day += 1
#         $ visits_today = 0
#         $ current_time_block = "day"
#     else:
#         $ current_time_block = "night" if current_time_block == "day" else "day"
    
#     # Verificar si se completó alguna ruta
#     #call check_route_completion
    
#     return


# Función para verificar eventos obligatorios
python early:
    def check_mandatory_events(location):
        for char in ["yamato", "hikaru", "shiori"]:
            events_completed = getattr(store, f"{char}_events_completed", 0)
            if events_completed < len(mandatory_events[store.current_loop][char]):
                next_event = mandatory_events[store.current_loop][char][events_completed]
                if (next_event["location"] == location and next_event["time"] == store.current_time_block):
                    setattr(store, f"{char}_events_completed", events_completed + 1)
                    return next_event["event"]
        return None

    # Función para obtener un evento aleatorio de cualquier personaje
    def get_random_event(loop, location):
        """
        Obtiene un evento aleatorio disponible de cualquier personaje para la ubicación actual
        
        Args:
            loop: Número del loop actual
            location: Ubicación actual del jugador
        
        Returns:
            str: La etiqueta del evento a ejecutar, o None si no hay eventos disponibles
        """
        
        # Verificar si hay eventos para este loop
        if loop not in random_events:
            return None
        
        available_events = []
        
        # Revisar todos los personajes
        for character in random_events[loop]:
            # Verificar si el personaje tiene eventos
            if not random_events[loop][character]:
                continue
                
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
