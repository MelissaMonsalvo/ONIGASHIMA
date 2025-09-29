## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load



############################################################
## PYTHON ###
############################################################
init python:
    def format_playtime(seconds):
        # Get hours no remain
        h = int(seconds// 3600)

        # Now take leftover from hour and convert to minutes
        m = int((seconds % 3600) // 60)

        # Get seconds after all hours are calculated
        s = int(seconds % 60)
        return f"{h:02}:{m:02}:{s:02}"


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 652
define config.thumbnail_height = 367

############################################################
### SAVE/LOAD SCREEN ###
############################################################

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))



screen file_slots(title):
    default selected_slot = None
    default skin = btn_skin_yellow


    if current_route == "route1":
        $ tt_color = BLACK
    elif current_route == "route2":
        $ tt_color = WHITE



    ## ACTUAL SCREEN ##

    add gui.game_menu_background

    fixed:
        xysize (config.screen_width, config.screen_height)

        style_prefix "sl"

        label title.upper()

        ### FILE SLOTS ###
        viewport id "sl_vp":
            draggable True
            pagekeys True
            mousewheel True

            scrollbars None yinitial 0.0


            has vbox

            for i in range(9):
                $ slot = i + 1

                button:
                    style_prefix "sl_btn"

                    if FileLoadable(slot):
                        
                        if selected_slot == slot:
                            action FileAction(slot)
                        else:
                            action SetLocalVariable("selected_slot", slot)

                        hbox:
                            text _("Slot #{}".format(slot)):
                                xalign 0.0
                                hover_color tt_color
                                selected_color tt_color

                            hbox:
                                xsize 500
                                xpos 0.5
                                xfill True

                                text FileSaveName(slot):
                                    hover_color tt_color
                                    selected_color tt_color

                                text FileTime(slot,
                                    format=_("{#file_time}%x")
                                ):
                                    xalign 1.0
                                    hover_color tt_color
                                    selected_color tt_color

                            text "{}".format(format_playtime(renpy.get_game_runtime())):
                                xalign 1.0
                                hover_color tt_color
                                selected_color tt_color

                    else:
                        hbox:
                            text _("NO DATA") xalign 0.0
                        if selected_slot == slot:
                            action FileAction(slot)
                        else:
                            action SetLocalVariable("selected_slot", slot)

    bar value YScrollValue("sl_vp"):
        style "vscrollbar"
        xsize 20
        ysize 622
        pos (1055, 250)


    ### PREVIEW SLOT THUMB ###

    if selected_slot:
        vbox:
            style_prefix "sl_thumb"

            frame:

                add FileScreenshot(selected_slot) align (0.5, 0.5)

            text FileSaveName(selected_slot):
                xalign 0.5
                font NOTO_JP_BOLD
                size 60
            


    # This means the player can hover this save
    # slot and hit delete to delete it
    key "save_delete" action FileDelete(slot)


    ### CONFIRM/REVERT ### # in screen_name_input
    frame:
        at ts_enterX(80)


        style_prefix "sl_gm"

        hbox:
            button:
                text title.upper() hover_color tt_color

                if title == "Load":
                    sensitive (selected_slot and FileLoadable(selected_slot))
                else:
                    sensitive selected_slot


                action FileAction(selected_slot)


            button:
                text _("DELETE") hover_color tt_color

                action FileDelete(selected_slot)

            button:
                text _("BACK") hover_color tt_color

                action Return()


############################################################
### SAVE/LOAD STYLES ###
############################################################
style sl_viewport:
    xysize (1055, 622)

    pos (0, 250)


style sl_vbox:
    spacing 5


style sl_label:
    pos GM_TITLE_POS
    ysize 60
    margin (0, 0)

style sl_label_text:
    font NOTO_JP
    color WHITE
    size GM_TITLE_SIZE

style sl_btn_button:
    xysize (1083, 120)
    background None
    hover_background "long_btn_hover_no_frame"
    selected_background "long_btn_hover_no_frame"

    padding SL_BTN_PADDING

style sl_btn_hbox:
    xsize 860
    align (0.5, 0.5)

style sl_btn_text:
    color BLACK
    font NOTO_JP
    size 30

### THUMB ###
style sl_thumb_vbox:
    xysize (758, 476)

    pos (1130, 195)

style sl_thumb_frame:
    background "frame black"
    xysize (758, 476)

style sl_thumb_text:
    font NOTO_JP
    color BLACK
    size 30

### NAV ###
style sl_gm_frame:
    xysize (1385, 95)
    anchor (1.0, 1.0)
    pos (1920, 1060)

    background Frame("gui/game menu/btn_backgroud.png", 20, 10)
    padding GM_LONG_BTN_PADDING


style sl_gm_hbox:
    is ni_hbox

style sl_gm_button:
    is ni_button

style sl_gm_text:
    is ni_text




screen file_slots_old(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of
            ## the buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text

# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text

# style page_label:
#     xpadding 75
#     ypadding 5
#     xalign 0.5

# style page_label_text:
#     textalign 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

# style page_button:
#     properties gui.button_properties("page_button")

# style page_button_text:
#     properties gui.text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

# style slot_button_text:
#     properties gui.text_properties("slot_button")
