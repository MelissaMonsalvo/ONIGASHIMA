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

screen config_dialogue():
    style_prefix "estilo"
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
                        left_bar "gui/game menu/left.png"  
                        right_bar "gui/game menu/right.png"  
                        ysize 68
                        thumb None

            ### Dialogue Size #############################################################################

            hbox:
                ysize cell_hight_4
                frame:
                    background None
                    xsize 100
                    $ prefs = persistent.dialogue_size
                    text "[prefs]"
                frame:
                    background None
                    xsize 524
                    bar value FieldValue(persistent, "dialogue_size", range=50, max_is_zero=False, offset=0, step=1):
                        range 50
                        left_bar "gui/game menu/left.png"
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
                        left_bar "gui/game menu/left.png"  
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
                    left_bar "gui/game menu/left.png"  
                    right_bar "gui/game menu/right.png"  
                    ysize 68
                    thumb None

            ### Sound #############################################################################
            frame:
                background None
                xsize 524
                ysize cell_hight_4
                bar value Preference("sound volume"): 
                    left_bar "gui/game menu/left.png"  
                    right_bar "gui/game menu/right.png"  
                    ysize 68
                    thumb None

            ### Voice #############################################################################
            frame:
                background None
                xsize 524
                ysize cell_hight_4
                bar value Preference("voice volume"): 
                    left_bar "gui/game menu/left.png"  
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






        #null width 50

# screen preferences():

#     tag menu

#     use game_menu(_("Preferences"), scroll="viewport"):

#         vbox:

#             hbox:
#                 box_wrap True

#                 if renpy.variant("pc") or renpy.variant("web"):

#                     vbox:
#                         style_prefix "radio"
#                         label _("Display")
#                         textbutton _("Window") action Preference("display", "window")
#                         textbutton _("Fullscreen") action Preference("display", "fullscreen")

#                 vbox:
#                     style_prefix "check"
#                     label _("Skip")
#                     textbutton _("Unseen Text") action Preference("skip", "toggle")
#                     textbutton _("After Choices") action Preference("after choices", "toggle")
#                     textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

#                 ## Additional vboxes of type "radio_pref" or "check_pref" can
#                 ## be added here, to add additional creator-defined preferences.

#             null height (4 * gui.pref_spacing)

#             hbox:
#                 style_prefix "slider"
#                 box_wrap True

#                 vbox:

#                     label _("Text Speed")

#                     bar value Preference("text speed")

#                     label _("Auto-Forward Time")

#                     bar value Preference("auto-forward time")

#                 vbox:

#                     if config.has_music:
#                         label _("Music Volume")

#                         hbox:
#                             bar value Preference("music volume")

#                     if config.has_sound:

#                         label _("Sound Volume")

#                         hbox:
#                             bar value Preference("sound volume")

#                             if config.sample_sound:
#                                 textbutton _("Test") action Play("sound", config.sample_sound)


#                     if config.has_voice:
#                         label _("Voice Volume")

#                         hbox:
#                             bar value Preference("voice volume")

#                             if config.sample_voice:
#                                 textbutton _("Test") action Play("voice", config.sample_voice)

#                     if config.has_music or config.has_sound or config.has_voice:
#                         null height gui.pref_spacing

#                         textbutton _("Mute All"):
#                             action Preference("all mute", "toggle")
#                             style "mute_all_button"