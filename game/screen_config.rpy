default cell_hight_4 = 100               
default cell_hight_3 = cell_hight_4 * 4


#[DejaVuSans, Atkinson-Hyperlegible, OpenDyslexic, Noto-Serif (Default)]
# Definimos las fuentes disponibles
define fonts = ["DejaVuSans.ttf", "NotoSans-Regular.ttf", "TurretRoad-Regular.ttf"]
default font_index = 0  # Índice actual
define persistent.dialogue_font = "NotoSans-Regular.ttf"



# Ejemplo de estilo del diálogo usando la fuente seleccionada
init python:
    def update_dialogue_font():
        persistent.dialogue_font = fonts[font_index]
        #style.say_dialogue.font = fonts[font_index]
        #persistent.dialogue_font = fonts[font_index]
        #style.say_dialogue.font = fonts[font_index]


define bar_skin_yellow = "gui/game menu/left.png"
define bar_skin_red = "gui/game menu/left_red.png"


screen config_dialogue():
    style_prefix "estilo"

    $ bar_skin = bar_skin_yellow if persistent.loop1 else bar_skin_red

    hbox:
        xsize 1060
        yoffset 30
        #xoffset 250
        vbox:
            spacing 30
            xsize 500
            ysize cell_hight_3
            label _("Dialogue Speed") yalign 0.1 text_style "estilo_label"
            label _("Dialogue Size") yalign 0.1 text_style "estilo_label"
            label _("Auto-Delay Time") yalign 0.1 text_style "estilo_label"
            label _("Typeface") yalign 0.1 text_style "estilo_label"
        #null width 50

        vbox:
            ysize cell_hight_3
            spacing 10
            ### Dialogue Speed #############################################################################
            hbox:    
                ysize cell_hight_4

                frame:
                    background None
                    xsize 100
                    #text "[preferences.text_cps]"
                    $ prefs = preferences.text_cps  # valor de 0 a 200
                    $ display_value = int(prefs / 200.0 * 100)
                    text "[display_value]"
                frame:
                    background None
                    xsize 524
                    bar value FieldValue(preferences, "text_cps", range=200, max_is_zero=False, offset=0, step=1): #Preference("text speed"):
                        range 200
                        left_bar bar_skin  
                        right_bar "gui/game menu/right.png"  
                        ysize 68
                        thumb None

            ### Dialogue Size #############################################################################

            hbox:
                ysize cell_hight_4
                frame:
                    background None
                    xsize 100
                    $ preff = preferences.font_size
                    $ prefs = int(preff / 1.5 * 100)
                    text "[prefs]"
                frame:
                    background None
                    xsize 524
                    #bar value FieldValue(persistent, "dialogue_size", range=50, max_is_zero=False, offset=0, step=1):
                    bar value Preference("font size") yalign 0.5: #Preference("font size")
                        #range 50
                        left_bar bar_skin
                        right_bar "gui/game menu/right.png"
                        ysize 68
                        thumb None

            ### Auto-Delay Time #############################################################################

            hbox:
                ysize cell_hight_4
                frame:
                    background None
                    xsize 100
                    $ prefs = preferences.afm_time
                    $ display_value = int(prefs / 30.0 * 100)  # lo mostramos como porcentaje 0 - 100
                    text "[display_value]"
                    #text "[preferences.afm_time]"
                frame:
                    background None
                    xsize 524
                    bar value FieldValue(preferences, "afm_time", range=30.0, max_is_zero=False, offset=0, step=0.1):
                        left_bar bar_skin 
                        right_bar "gui/game menu/right.png"  
                        ysize 68
                        thumb None

            ### Dialogue Font #############################################################################
            hbox:    
                ysize cell_hight_4

                # Flecha izquierda
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"
                        hover "gui/settings/btn_left_arrow_hover.png"
                        action [
                            SetVariable("font_index", (font_index - 1) % len(fonts)),
                            Function(update_dialogue_font)
                        ]

                # Texto que muestra la fuente actual
                frame:
                    background None
                    xsize 300
                    text fonts[font_index]:
                        xalign 0.5

                # Flecha derecha
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_right_arrow_idle.png"
                        hover "gui/settings/btn_right_arrow_hover.png"
                        action [
                            SetVariable("font_index", (font_index + 1) % len(fonts)),
                            Function(update_dialogue_font)
                        ]





define persistent.dialogue_size = 0

default pref_muteall = False



screen config_audio():
    style_prefix "estilo"
    $ bar_skin = bar_skin_yellow if persistent.loop1 else bar_skin_red
    hbox:
        xsize 1060
        yoffset 30
        #xoffset 250
        vbox:
            spacing 10
            xsize 500
            ysize cell_hight_3
            label _("Music") yalign 0.1 text_style "estilo_label"
            label _("Sound") yalign 0.1 text_style "estilo_label"
            label _("Voice") yalign 0.1 text_style "estilo_label"
            label _("Mute All") yalign 0.1 text_style "estilo_label"

        vbox:
            ysize cell_hight_3
            spacing 10

            ### Music #############################################################################

            frame:
                background None
                xsize 524
                ysize cell_hight_4
                bar value Preference("music volume"): 
                    left_bar bar_skin 
                    right_bar "gui/game menu/right.png"  
                    ysize 68
                    thumb None

            ### Sound #############################################################################
            frame:
                background None
                xsize 524
                ysize cell_hight_4
                bar value Preference("sound volume"): 
                    left_bar bar_skin  
                    right_bar "gui/game menu/right.png"  
                    ysize 68
                    thumb None

            ### Voice #############################################################################
            frame:
                background None
                xsize 524
                ysize cell_hight_4
                bar value Preference("voice volume"): 
                    left_bar bar_skin  
                    right_bar "gui/game menu/right.png"  
                    ysize 68
                    thumb None


            ### Mute all #############################################################################
            hbox:
                ysize cell_hight_4
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"  
                        hover "gui/settings/btn_left_arrow_hover.png"  
                        xalign 1.0 
                        action [SetVariable("pref_muteall", True), Preference("all mute", "toggle")]
                        sensitive not pref_muteall  # Solo activa si las transiciones están habilitadas
                    
                frame:
                    background None
                    xsize 300
                    # Columna 3 - Texto
                    if pref_muteall:
                        text _("ON"):
                            xalign 0.5
                            
                    else:
                        text _("OFF"):
                            xalign 0.5
                            
                frame:
                    background None
                    xsize 100
                    # Flecha derecha (para activar - Skip)
                    imagebutton:
                        idle "gui/settings/btn_right_arrow_idle.png"  
                        hover "gui/settings/btn_right_arrow_hover.png"  
                        action [SetVariable("pref_muteall",False), Preference("all mute", "toggle")]
                        sensitive pref_muteall  # Solo activa si las transiciones están deshabilitadas



default self_voicing = False
default image_captions = False

screen config_accessibility():
    style_prefix "estilo"
    hbox:
        xsize 1060
        yoffset 30
        #xoffset 250
        vbox:
            spacing 30
            xsize 500
            ysize cell_hight_3
            # label _("Sound Captions") yalign 0.1 text_style "estilo_label"
            # label _("Image Captions") yalign 0.1 text_style "estilo_label"
            label _("Self-Voicing") yalign 0.1 text_style "estilo_label"
        vbox:


            ### self_voicing #############################################################################
            hbox:
                ysize cell_hight_4
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"  
                        hover "gui/settings/btn_left_arrow_hover.png"  
                        xalign 1.0 
                        action [SetVariable("self_voicing", True), Preference("self voicing", "toggle")]
                        sensitive not self_voicing  # Solo activa si las transiciones están habilitadas
                    
                frame:
                    background None
                    xsize 300
                    # Columna 3 - Texto
                    if self_voicing:
                        text _("ON"):
                            xalign 0.5
                            
                    else:
                        text _("OFF"):
                            xalign 0.5
                            
                frame:
                    background None
                    xsize 100
                    # Flecha derecha (para activar - Skip)
                    imagebutton:
                        idle "gui/settings/btn_right_arrow_idle.png"  
                        hover "gui/settings/btn_right_arrow_hover.png"  
                        action [SetVariable("self_voicing",False), Preference("self voicing", "toggle")]
                        sensitive self_voicing  # Solo activa si las transiciones están deshabilitadas



            # textbutton "Self-Voicing": # [onoff(renpy.self_voicing)]":
            #     action Preference("self voicing", "toggle")

            # textbutton "Image Captions": #[onoff(renpy.image_captions)]":
            #     action Preference("image captions", "toggle")

            # textbutton "Sound Captions": # [onoff(renpy.sound_captions)]":
            #     action Preference("sound captions", "toggle")