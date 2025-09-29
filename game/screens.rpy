init python:
    style.choice_text = Style(style.default)
    style.choice_text.size = 60
    style.choice_text.bold = True
    style.choice_text.color = "#232323" # Set color
    style.choice_text.outlines = [(2, "#fff", 0, 0)] # White outline
    style.choice_text.xalign = 0.5
    style.choice_text.yalign = 0.9
    style.choice_text.ypadding = 100

init python:
    def restore_all_volumes():
        if hasattr(store, "original_music_volume") and store.original_music_volume is not None:
            _preferences.volumes["music"] = store.original_music_volume
            store.original_music_volume = None


### CURSOR ###
define config.mouse = { }
define config.mouse['default'] = [ ( "gui/cursor.png", 0, 0) ]
################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize 68
    xsize 525
    left_bar Frame("gui/game menu/left.webp", 20, 5, tile=False)
    right_bar Frame("gui/game menu/right.webp", 20, 5, tile=False)
    #left_bar "gui/game menu/left.png"
    #right_bar "gui/game menu/right.png"

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize 29
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", 5, 5, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", 5, 5, tile=False)

    thumb_offset 10
    unscrollable 'hide'

style vscrollbar:
    xsize 29
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", 5, 5, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", 5, 5, tile=False)

    thumb_offset 10
    unscrollable 'hide'

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what":
            line_spacing persistent.dialogue_line_spacing
            font persistent.dialogue_font
            size persistent.dialogue_text_size


    ## If there's a side image, display it above the text. Do not display on
    ## the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    #properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

# =========================
# MASK IMAGES (dynamic per route)
# =========================

# Top masks
image mask_top = ConditionSwitch(
    "current_route == 'route1'", "gui/choices/yellow_mask.webp",
    "current_route == 'route2'", "gui/choices/red_mask.webp"
)

# Bottom masks
image mask_bottom = ConditionSwitch(
    "current_route == 'route1'", "gui/choices/yellow_mask.webp",
    "current_route == 'route2'", "gui/choices/red_mask.webp"
)

# =========================
# ANIMATIONS FOR CHOICES
# =========================
transform mask_top_anim:
    xpos -100
    alpha 0.0
    zoom 0.7
    parallel:
        linear 0.4 alpha 1.0
    parallel:
        linear 0.2 zoom 1.0
    linear 0.2 xpos 1000

transform mask_bottom_anim:
    xpos 1100
    alpha 0.0
    zoom 0.7
    parallel:
        linear 0.4 alpha 1.0
    parallel:
        linear 0.2 zoom 1.0
    linear 0.2 xpos -100


transform button_top_anim:
    crop (0, 0, 0, 426)
    alpha 0.0
    zoom 0.7

    parallel:
        linear 0.4 alpha 1.0
    parallel:
        linear 0.2 zoom 1.0
    linear 0.2 crop (0, 0, 1301, 426)
transform button_bottom_anim:
    crop (1301, 0, 0, 426)
    xpos 1301
    alpha 0.0
    zoom 0.7

    parallel:
        linear 0.5 alpha 1.0
    parallel:
        linear 0.2 zoom 1.0
    linear 0.2 crop (0, 0, 1301, 426) xpos 0

transform choice_text_fadein:
    alpha 0.0
    linear 2 alpha 1.0


# =========================
# BUTTON HALVES
# =========================

# Route 1 (default theme)
image top_half_idle_r1 = "gui/choices/choice_yellow_right_idle_background.webp"
image top_half_hover_r1 = "gui/choices/choice_yellow_right_hover_background.webp"
image bottom_half_idle_r1 = "gui/choices/choice_yellow_left_idle_background.webp"
image bottom_half_hover_r1 = "gui/choices/choice_yellow_left_hover_background.webp"
# Route 2 (alt theme)
image top_half_idle_r2 = "gui/choices/choice_red_right_idle_background.webp"
image top_half_hover_r2 = "gui/choices/choice_red_right_hover_background.webp"
image bottom_half_idle_r2 = "gui/choices/choice_red_left_idle_background.webp"
image bottom_half_hover_r2 = "gui/choices/choice_red_left_hover_background.webp"

default hovered_choice = -1

# ======== CHOICE SCREEN =========

screen choice(items):
    vbox:
        spacing 40
        xalign 0.5
        yalign 0.5

        for idx, (caption, action, chosen) in enumerate(items):

            button:
                action action, Function(save_choices, caption)
                xalign 0.5
                xsize 1301
                ysize 426
                background None

                hovered SetVariable("hovered_choice", idx)
                unhovered SetVariable("hovered_choice", -1)

                fixed:
                    xysize (1301, 426)

                    # Show correct background for each button (idle or hover)
                    if idx == 0:
                        add (
                            "top_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "top_half_idle_r1" if current_route == "route1" else
                            "top_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "top_half_idle_r2"
                        ) xpos 0 ypos 0 at button_top_anim
                    else:
                        add (
                            "bottom_half_hover_r1" if current_route == "route1" and hovered_choice == idx else
                            "bottom_half_idle_r1" if current_route == "route1" else
                            "bottom_half_hover_r2" if current_route == "route2" and hovered_choice == idx else
                            "bottom_half_idle_r2"
                        ) xpos 0 ypos 0 at button_bottom_anim

                    # Only one mask per button
                    if idx == 0:
                        add "mask_top" xpos 0 ypos 0 at mask_top_anim
                    else:
                        add "mask_bottom" xpos 0 ypos 0 at mask_bottom_anim

                    # Centered text
                    text caption style "choice_text" xalign 0.5 yalign 0.6 at choice_text_fadein





















style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-
## game menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        add "gui/quick menu/nav_line.webp" pos (1835, 8)
        vbox:
            at ts_qm_fadein(-80)
            xsize 90
            spacing 5

            pos (1800, 55)

            imagebutton auto "gui/quick menu/auto_%s.webp":
                action Preference("auto-forward", "toggle")

            imagebutton auto "gui/quick menu/back_%s.webp":
                action Rollback()

            imagebutton auto "gui/quick menu/skip_%s.webp":
                action Skip() alternate Skip(fast=True, confirm=True)

            imagebutton auto "gui/quick menu/save_%s.webp":
                action ShowMenu('save')

            imagebutton auto "gui/quick menu/pause_%s.webp":
                action ShowMenu('pause_menu')



        # hbox:
            # style_prefix "quick"
            # style "quick_menu"

            # textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("Auto") action Preference("auto-forward", "toggle")
            # textbutton _("Save") action ShowMenu('save')
            # textbutton _("Q.Save") action QuickSave()
            # textbutton _("Q.Load") action QuickLoad()
            # textbutton _("Prefs") action ShowMenu('preferences')



## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")





## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    # if main_menu:
    #     add gui.main_menu_background
    # else:
    #     #add "gui/menu_background2.jpg"
    #     add gui.game_menu_background

    frame:
        background None
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size




## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better
## suit themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences


default pref1 = "Window"

default opconfig = 1

style preferencessidemenu is text

style preferencessidemenu_text:
    font "NotoSerifJP-VariableFont_wght.ttf"
    size 40
    color "#000000"  # Color naranja




# En screens.rpy o antes del screen:
define btn_skin_yellow = {
    "idle" : "gui/game menu/btn_nav_idle_background.webp",
    "hover": "gui/game menu/btn_nav_hover_background.webp",
    "sel_idle": "gui/game menu/btn_nav_selected_idle_background.webp",
    "sel_hover": "gui/game menu/btn_nav_selected_hover_background.webp",
    "idle_2": "gui/game menu/btn_idle_background.webp",
    "hover_2": "gui/game menu/btn_hover_background.webp",
    "color": "#000000"
}

define btn_skin_red = {
    "idle" : "gui/game menu/btn_nav_idle_background.webp",
    "hover": "gui/game menu/btn_nav_hover_background.webp",
    "sel_idle": "gui/game menu/btn_nav_red_selected_idle_background.webp",
    "sel_hover": "gui/game menu/btn_nav_red_selected_hover_background.webp",
    "idle_2": "gui/game menu/btn_idle_background.webp",
    "hover_2": "gui/game menu/btn_red_hover_background.webp",
    "color": "#ffffff"
}

define selected1 = 1
# persistent.loop1:


# screen preferences_old():

#     tag menu

#     style_prefix "preferencessidemenu"
#     add "gui/menu_background2.jpg"


#     $ skin = btn_skin_yellow if persistent.loop1 else btn_skin_red



#     text "SETTINGS":
#         font "NotoSerifJP-VariableFont_wght.ttf"
#         size 80
#         color "#ffffff"
#         xpos 55
#         ypos 30


#     hbox:
#         ypos 300
#         xpos 30
#         frame:
#             xsize 150
#             background None
#             add "gui/game menu/nav_line.webp" xoffset 40
#             vbox:
#                 spacing 40

#                 fixed:
#                     xsize 250
#                     ysize 100
#                     imagebutton:
#                         idle skin["idle"]
#                         hover skin["hover"]
#                         selected_idle skin["sel_idle"]
#                         selected_hover skin["sel_hover"]
#                         action SetVariable("opconfig",1)
#                     if opconfig == 1:
#                         text "General" xpos 125 yalign 0.5 color skin["color"]
#                     else:
#                         text "General" xpos 125 yalign 0.5 color "#000000"
#                 fixed:
#                     xsize 250
#                     ysize 100
#                     imagebutton:
#                         idle skin["idle"]
#                         hover skin["hover"]
#                         selected_idle skin["sel_idle"]
#                         selected_hover skin["sel_hover"]
#                         action SetVariable("opconfig",2)
#                     #text "Audio" xpos 125 yalign 0.5
#                     if opconfig == 2:
#                         text "Audio" xpos 125 yalign 0.5 color skin["color"]
#                     else:
#                         text "Audio" xpos 125 yalign 0.5 color "#000000"

#                 fixed:
#                     xsize 250
#                     ysize 100
#                     imagebutton:
#                         idle skin["idle"]
#                         hover skin["hover"]
#                         selected_idle skin["sel_idle"]
#                         selected_hover skin["sel_hover"]
#                         action SetVariable("opconfig",3)
#                     #text "Dialogue" xpos 125 yalign 0.5
#                     if opconfig == 3:
#                         text "Dialogue" xpos 125 yalign 0.5 color skin["color"]
#                     else:
#                         text "Dialogue" xpos 125 yalign 0.5 color "#000000"

#                 fixed:
#                     xsize 250
#                     ysize 100
#                     imagebutton:
#                         idle skin["idle"]
#                         hover skin["hover"]
#                         selected_idle skin["sel_idle"]
#                         selected_hover skin["sel_hover"]
#                         action SetVariable("opconfig",4), SetVariable("selected1",4)
#                     #text "Accessibility/\nControls" xpos 125 yalign 0.5
#                     if opconfig == 4:
#                         text "Accessibility/\nControls" xpos 125 yalign 0.5 color skin["color"]
#                     else:
#                         text "Accessibility/\nControls" xpos 125 yalign 0.5 color "#000000"
#         null width 500

#         if opconfig == 1:
#             use config_general2()
#         elif opconfig == 2:
#             use config_audio()
#         elif opconfig == 3:
#             use config_dialogue()
#         elif opconfig == 4:
#             use config_accessibility()

#     use confirm_config()



# screen confirm_config():
#     $ skin = btn_skin_yellow if persistent.loop1 else btn_skin_red
#     frame:
#         xpos 1025
#         ypos 965
#         background "gui/game menu/btn_backgroud.webp"
#         #background None
#         #Left button
#         hbox:
#             xoffset 30
#             frame:
#                 xsize 411
#                 ysize 60
#                 yoffset 10
#                 background None
#                 imagebutton:
#                     idle skin["idle_2"]
#                     hover skin["hover_2"]
#                     xalign 0.5
#                     if main_menu:
#                         action ShowMenu("main_menu") #action Return()
#                     else:
#                         action Return() #Hide("preferences")
#                 text "CONFIRM" xalign 0.3 yalign 0.5 size 30
#             #Right button
#             frame:
#                 xsize 411
#                 ysize 60
#                 yoffset 10
#                 background None
#                 imagebutton:
#                     idle skin["idle_2"]
#                     hover skin["hover_2"]
#                     xalign 0.5
#                     if main_menu:
#                         action ShowMenu("main_menu") #Return()
#                     else:
#                         action Return() #Hide("preferences")
#                 text "BACK" xalign 0.3 yalign 0.5 size 30





default cell_hight_1 = 100
default cell_hight_2 = cell_hight_1*4

style estilo_text is text

style estilo_text:
    font "NotoSerifJP-VariableFont_wght.ttf"
    size 40
    color "#000000"  # Color naranja
    #outlines [(2, "#000000", 0, 0)]
    #kerning 1.0
    #bold True


style estilo_label:
    font "NotoSerifJP-VariableFont_wght.ttf"
    color "#000000"
    size 40


screen config_general2():
    style_prefix "estilo"
    hbox:
        xsize 1060
        yoffset 30
        #xoffset 250
        vbox:
            spacing 10
            xsize 500
            ysize cell_hight_2
            label _("Display") yalign 0.1 text_style "estilo_label"
            label _("Skip: Unseen text") yalign 0.1 text_style "estilo_label"
            label _("Skip: After choices") yalign 0.1 text_style "estilo_label"
            label _("Skip: Transitions") yalign 0.1 text_style "estilo_label"
        null width 50

        vbox:
            spacing 10
            ################################################################################
            hbox:
                ysize cell_hight_1
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"
                        hover "gui/settings/btn_left_arrow_hover.png"
                        xalign 1.0
                        action [SetVariable("pref1","window"),Preference("display", "window")]
                        sensitive (pref1 != "window" )
                frame:
                    background None
                    xsize 300
                    yfill True
                    if pref1 == "window":
                        text _("WINDOW"):
                            xalign 0.5
                            #yalign 0.5
                    else:
                        text _("FULLSCREEN"):
                            xalign 0.5
                            #yalign 0.5
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_right_arrow_idle.png"
                        hover "gui/settings/btn_right_arrow_hover.png"
                        xalign 0.0
                        action [SetVariable("pref1","fullscreen"),Preference("display", "fullscreen")]
                        sensitive (pref1 != "fullscreen" )
            ################################################################################
            hbox:
                ysize cell_hight_1
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"
                        hover "gui/settings/btn_left_arrow_hover.png"
                        xalign 1.0
                        action Preference("skip", "toggle")
                        sensitive _preferences.skip_unseen  # Solo activa si Skip All está activado
                frame:
                    background None
                    xsize 300
                    if _preferences.skip_unseen:
                        text _("ON"):
                            xalign 0.5
                            #yalign 0.5
                    else:
                        text _("Off"):
                            xalign 0.5
                            #yalign 0.5
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_right_arrow_idle.png"
                        hover "gui/settings/btn_right_arrow_hover.png"
                        xalign 0.0
                        action Preference("skip", "toggle")
                        sensitive not _preferences.skip_unseen  # Solo activa si Skip All está desactivado
            ################################################################################
            hbox:
                ysize cell_hight_1
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"
                        hover "gui/settings/btn_left_arrow_hover.png"
                        xalign 1.0
                        action Preference("after choices", "toggle")
                        sensitive _preferences.skip_after_choices  # Solo activa si Skip está activado
                frame:
                    background None
                    xsize 300
                    if _preferences.skip_after_choices:
                        text _("ON"):
                            xalign 0.5

                    else:
                        text _("OFF"):
                            xalign 0.5

                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_right_arrow_idle.png"
                        hover "gui/settings/btn_right_arrow_hover.png"
                        xalign 0.0
                        action Preference("after choices", "toggle")
                        sensitive not _preferences.skip_after_choices  # Solo activa si Skip está desactivado
            ################################################################################
            hbox:
                ysize cell_hight_1
                frame:
                    background None
                    xsize 100
                    imagebutton:
                        idle "gui/settings/btn_left_arrow_idle.png"
                        hover "gui/settings/btn_left_arrow_hover.png"
                        xalign 1.0
                        action Preference("transitions", "toggle")
                        sensitive _preferences.transitions  # Solo activa si las transiciones están habilitadas

                frame:
                    background None
                    xsize 300
                    # Columna 3 - Texto
                    if _preferences.transitions:
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
                        action Preference("transitions", "toggle")
                        sensitive not _preferences.transitions  # Solo activa si las transiciones están deshabilitadas










screen config_general():
    grid 4 4 spacing 10:
        #xsize 860
        #xpos 670
        #ypos 332
        #yalign 0.5
        yoffset 150

        # Renglon 1    ################################
        # Columna 1 - Etiqueta
        label _("Display")

        # Columna 2 - Flecha Izqu
        imagebutton:
            idle "gui/settings/btn_left_arrow_idle.png"
            hover "gui/settings/btn_left_arrow_hover.png"
            xalign 1.0
            action [SetVariable("pref1","window"),Preference("display", "window")]
            sensitive (pref1 != "window" )


        # Columna 3 - Texto
        if pref1 == "window":
            text _("Window"):
                size 24
                xalign 0.5
                yalign 0.5
        else:
            text _("Fullscreen"):
                size 24
                xalign 0.5
                yalign 0.5

        # Columna 4 - Flecha derecha
        imagebutton:
            idle "gui/settings/btn_right_arrow_idle.png"
            hover "gui/settings/btn_right_arrow_hover.png"
            xalign 0.0
            action [SetVariable("pref1","fullscreen"),Preference("display", "fullscreen")]
            sensitive (pref1 != "fullscreen" )

        # Renglon 2    ################################
        # Columna 1 - Etiqueta
        label _("Skip: Unseen Text")

        #Columna 2 - Flecha Izqu
        imagebutton:
            idle "gui/settings/btn_left_arrow_idle.png"
            hover "gui/settings/btn_left_arrow_hover.png"
            xalign 1.0
            action Preference("skip", "toggle")
            sensitive _preferences.skip_unseen  # Solo activa si Skip All está activado

        # Columna 3 - Texto
        if _preferences.skip_unseen:
            text _("On"):
                size 24
                xalign 0.5
                yalign 0.5
        else:
            text _("Off"):
                size 24
                xalign 0.5
                yalign 0.5

        # Columna 4 - Flecha derecha
        imagebutton:
            idle "gui/settings/btn_right_arrow_idle.png"
            hover "gui/settings/btn_right_arrow_hover.png"
            xalign 0.0
            action Preference("skip", "toggle")
            sensitive not _preferences.skip_unseen  # Solo activa si Skip All está desactivado

        # Renglon 3    ################################
        # Columna 1 - Etiqueta
        label _("Skip: After Choices")

        #Columna 2 - Flecha Izqu
        # Flecha izquierda (para desactivar - After Choices)
        imagebutton:
            idle "gui/settings/btn_left_arrow_idle.png"
            hover "gui/settings/btn_left_arrow_hover.png"
            xalign 1.0
            action Preference("after choices", "toggle")
            sensitive _preferences.skip_after_choices  # Solo activa si Skip está activado

        # Columna 3 - Texto
        if _preferences.skip_after_choices:
            text _("On"):
                size 24
                xalign 0.5
                yalign 0.5
        else:
            text _("Off"):
                size 24
                xalign 0.5
                yalign 0.5

        # Flecha derecha (para activar - Skip)
        imagebutton:
            idle "gui/settings/btn_right_arrow_idle.png"
            hover "gui/settings/btn_right_arrow_hover.png"
            xalign 0.0
            action Preference("after choices", "toggle")
            sensitive not _preferences.skip_after_choices  # Solo activa si Skip está desactivado

        # Renglon 4    ################################
        # Columna 1 - Etiqueta
        label _("Skip: Transitions")

        #Columna 2 - Flecha Izqu
        # Flecha izquierda (para desactivar - After Choices)
        # Flecha izquierda (para desactivar)
        imagebutton:
            idle "gui/settings/btn_left_arrow_idle.png"
            hover "gui/settings/btn_left_arrow_hover.png"
            xalign 1.0
            action Preference("transitions", "toggle")
            sensitive _preferences.transitions  # Solo activa si las transiciones están habilitadas

        # Columna 3 - Texto
        if _preferences.transitions:
            text _("On"):
                size 24
                xalign 0.5
                yalign 0.5
        else:
            text _("Off"):
                size 24
                xalign 0.5
                yalign 0.5

        # Flecha derecha (para activar - Skip)
        imagebutton:
            idle "gui/settings/btn_right_arrow_idle.png"
            hover "gui/settings/btn_right_arrow_hover.png"
            action Preference("transitions", "toggle")
            sensitive not _preferences.transitions  # Solo activa si las transiciones están deshabilitadas


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




style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text




style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    style_prefix "history"

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "gui/history_background.webp"

    fixed:
        xysize (config.screen_width, config.screen_height)

        label "HISTORY" 

        viewport:
            xysize (1120, 725)
            pos (373, 237)

            mousewheel True draggable True pagekeys True
            scrollbars "vertical" yinitial 1.0

            has vbox

            for h in _history_list:

                if h.kind == "choice":
                    vbox:
                        text "CHOSEN:":
                            color RED
                        text "       [h.what]"

                else:

                    frame:
                        has vbox
                        if h.who:
                            label h.who:
                                substitute False
                                ## Take the color of the who text
                                ## from the Character, if set
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                                xsize 280   # this number and the null width
                                            # number should be the same

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            substitute False

                null height 50
                add "gui/history_divider.webp"
                null height 50

            if not _history_list:
                label _("The dialogue history is empty.")

        ### NAV ###
        if not persistent.loop1:
            $ tt_color = BLACK
        else:
            $ tt_color = WHITE
            
        frame:
            at ts_enterX(80)


            style_prefix "help_gm"
        
            hbox:
                button:
                    text _("BACK") hover_color tt_color

                    action Return()


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }



############################################################
### HISTORY STYLES ###
############################################################

style history_frame:
    # xsize 1030
    # ysize 725
    background None

style history_vbox:
    spacing 20

# style history_name:
#     xalign 1.0

# style history_name_text:
#     textalign 1.0
#     align (1.0, 0.0)
#     color '#f93c3e'

style history_text:
    textalign 0.0
    color BLACK
    font NOTO_JP

style history_label:
    is sl_label

style history_label_text:
    is sl_label_text







#     use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

#         style_prefix "history"

#         for h in _history_list:

#             window:

#                 ## This lays things out properly if history_height is None.
#                 has fixed:
#                     yfit True

#                 if h.who:

#                     label h.who:
#                         style "history_name"
#                         substitute False

#                         ## Take the color of the who text from the Character,
#                         ## if set.
#                         if "color" in h.who_args:
#                             text_color h.who_args["color"]

#                 $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                 text what:
#                     substitute False

#         if not _history_list:
#             label _("The dialogue history is empty.")


# ## This determines what tags are allowed to be displayed on the history screen.

# define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


# style history_window is empty

# style history_name is gui_label
# style history_name_text is gui_label_text
# style history_text is gui_text

# style history_label is gui_label
# style history_label_text is gui_label_text

# style history_window:
#     xfill True
#     ysize gui.history_height

# style history_name:
#     xpos gui.history_name_xpos
#     xanchor gui.history_name_xalign
#     ypos gui.history_name_ypos
#     xsize gui.history_name_width

# style history_name_text:
#     min_width gui.history_name_width
#     textalign gui.history_name_xalign

# style history_text:
#     xpos gui.history_text_xpos
#     ypos gui.history_text_ypos
#     xanchor gui.history_text_xalign
#     xsize gui.history_text_width
#     min_width gui.history_text_width
#     textalign gui.history_text_xalign
#     layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5





################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "screen overlay"

    ## TEXT COLOR CHANGE ##

    if not persistent.loop1:
        $ tt_color = BLACK
    else:
        $ tt_color = WHITE


    frame:
        at ts_fadein(0.5)

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                button:
                    text _("Yes"):
                        hover_color tt_color
                    action yes_action

                if no_action:
                    button:
                        text _("No"):
                            hover_color tt_color
                        action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame:
    background "frame black"
    xminimum 1114
    yminimum 700

    align (0.5, 0.5)
    yoffset -40

    padding (100, 90)

style confirm_button:
    xysize (280, 120)
    background None
    hover_background Transform("long_btn_hover_no_frame", xysize=(280, 120))


style confirm_text:
    is pm_text
    align (0.5, 0.5)

style confirm_label_text:
    color WHITE
    size 40
    font NOTO_JP
    bold False
    italic False
    xsize 700
    text_align 0.5
    

# style confirm_frame is gui_frame
# style confirm_prompt is gui_prompt
# style confirm_prompt_text is gui_prompt_text
# style confirm_button is gui_medium_button
# style confirm_button_text is gui_medium_button_text

# style confirm_frame:
#     background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
#     padding gui.confirm_frame_borders.padding
#     xalign .5
#     yalign .5

# style confirm_prompt_text:
#     textalign 0.5
#     layout "subtitle"

# style confirm_button:
#     properties gui.button_properties("confirm_button")

# style confirm_button_text:
#     properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly
        ## if config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed
## at once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using
## speech bubbles. The bubble screen takes the same parameters as the say
## screen, must create a displayable with the id of "what", and can create
## displayables with the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", 5, 5, tile=False)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", 5, 5, tile=False)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", 5, 5, tile=False)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", 5, 5, tile=False)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
