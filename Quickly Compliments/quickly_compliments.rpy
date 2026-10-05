# ============================================================
# Quickly Compliments
# by Dima5353 from Russia with love <3
#
# Monika After Story 0.12.19, 0.12.18, 0.12.15 and 0.11.9!
# ============================================================


init -990 python:

    if not hasattr(persistent, "qc_language"):
        persistent.qc_language = "en"

    if persistent.qc_language not in ["en", "ru", "es", "pt"]:
        persistent.qc_language = "en"


    valid_positions = [0, 1, 2, 3, 4, 5]

    if not hasattr(persistent, "qc_button_position"):
        persistent.qc_button_position = 2
    elif persistent.qc_button_position not in valid_positions:
        persistent.qc_button_position = 2


    if not hasattr(persistent, "qc_button_hidden"):
        persistent.qc_button_hidden = True


    def qc_set_language(language):

        persistent.qc_language = language

        renpy.save_persistent()
        renpy.restart_interaction()


    def qc_set_position(position):

        persistent.qc_button_position = position
        persistent.qc_button_hidden = False

        qc_sync_journal_position()

        renpy.save_persistent()
        renpy.restart_interaction()


    def qc_hide_button():

        persistent.qc_button_hidden = True

        qc_sync_journal_position()

        renpy.save_persistent()
        renpy.restart_interaction()


    def qc_button_ypos():

        if persistent.qc_button_position == 0:
            return 15

        elif persistent.qc_button_position == 1:
            return 55

        elif persistent.qc_button_position == 2:
            return 95

        elif persistent.qc_button_position == 3:
            return 135

        elif persistent.qc_button_position == 4:
            return 175

        elif persistent.qc_button_position == 5:
            return 215
        
        return 95


    def qc_sync_journal_position():

        if not hasattr(store, "journal_left_stack_ypos"):
            return

        old_ypos = getattr(
            store,
            "_qc_journal_registered_ypos",
            None
        )

        if old_ypos is not None:

            try:

                while old_ypos in store.journal_left_stack_ypos:
                    store.journal_left_stack_ypos.remove(
                        old_ypos
                    )

            except (AttributeError, ValueError):
                pass

        store._qc_journal_registered_ypos = None


        if persistent.qc_button_hidden:
            return


        if hasattr(store, "journal_register_left_button"):

            ypos = qc_button_ypos() + 35

            store.journal_register_left_button(ypos)

            store._qc_journal_registered_ypos = ypos


    def qc_text(text_id):

        language = persistent.qc_language


        if text_id == "praise":

            if language == "ru":
                return "Похвалить"

            elif language == "es":
                return "Elogiar"

            elif language == "pt":
                return "Elogiar"

            return "Praise"


        elif text_id == "submod_settings":

            if language == "ru":
                return "Настройки сабмода"

            elif language == "es":
                return "Ajustes del submod"

            elif language == "pt":
                return "Configurações do submod"

            return "Submod Settings"


        elif text_id == "title":

            if language == "ru":
                return "Быстрые комплименты"

            elif language == "es":
                return "Cumplidos rápidos"

            elif language == "pt":
                return "Elogios rápidos"

            return "Quickly Compliments"


        elif text_id == "language":

            if language == "ru":
                return "Язык"

            elif language == "es":
                return "Idioma"

            elif language == "pt":
                return "Idioma"

            return "Language"


        elif text_id == "button_position":

            if language == "ru":
                return "Положение кнопки"

            elif language == "es":
                return "Posición del botón"

            elif language == "pt":
                return "Posição do botão"

            return "Button Position"


        elif text_id == "position_1":

            if language == "ru":
                return "Положение 1"

            elif language == "es":
                return "Posición 1"

            elif language == "pt":
                return "Posição 1"

            return "Position 1"


        elif text_id == "position_2":

            if language == "ru":
                return "Положение 2"

            elif language == "es":
                return "Posición 2"

            elif language == "pt":
                return "Posição 2"

            return "Position 2"


        elif text_id == "position_3":

            if language == "ru":
                return "Положение 3"

            elif language == "es":
                return "Posición 3"

            elif language == "pt":
                return "Posição 3"

            return "Position 3"


        elif text_id == "position_4":

            if language == "ru":
                return "Положение 4"

            elif language == "es":
                return "Posición 4"

            elif language == "pt":
                return "Posição 4"

            return "Position 4"


        elif text_id == "position_5":

            if language == "ru":
                return "Положение 5"

            elif language == "es":
                return "Posición 5"

            elif language == "pt":
                return "Posição 5"

            return "Position 5"


        elif text_id == "position_6":

            if language == "ru":
                return "Положение 6"

            elif language == "es":
                return "Posição 6"

            elif language == "pt":
                return "Posição 6"

            return "Position 6"


        elif text_id == "hide":

            if language == "ru":
                return "Скрыть"

            elif language == "es":
                return "Ocultar"

            elif language == "pt":
                return "Ocultar"

            return "Hide"


        elif text_id == "close":

            if language == "ru":
                return "Закрыть"

            elif language == "es":
                return "Cerrar"

            elif language == "pt":
                return "Fechar"

            return "Close"


        return text_id


style qc_praise_ru_text is hkb_button_text:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    size 22


style qc_submod_settings_button is generic_button_light:

    xalign 0.0
    padding (8, 5, 8, 5)


style qc_submod_settings_button_dark is generic_button_dark:

    xalign 0.0
    padding (8, 5, 8, 5)


style qc_submod_settings_text is generic_button_text_light:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    text_align 0.5


style qc_submod_settings_text_dark is generic_button_text_dark:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    text_align 0.5


style qc_settings_text is generic_button_text_light:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    text_align 0.5


style qc_settings_text_dark is generic_button_text_dark:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    text_align 0.5


style qc_settings_button is generic_button_light:

    xsize 300
    ysize 35
    padding (8, 5, 8, 5)
    xalign 0.5


style qc_settings_button_dark is generic_button_dark:

    xsize 300
    ysize 35
    padding (8, 5, 8, 5)
    xalign 0.5


style qc_settings_button_text is generic_button_text_light:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    text_align 0.5


style qc_settings_button_text_dark is generic_button_text_dark:

    font "Submods/Quickly Compliments/Aller_Rg.ttf"
    text_align 0.5


label quick_compliments:

    $ _qc_hotkeys_enabled = store.mas_hotkeys.talk_enabled
    $ _qc_dlg_workflow = store.mas_globals.dlg_workflow

    $ mas_HKBRaiseShield()
    $ store.mas_hotkeys.talk_enabled = False

    $ store.mas_globals.dlg_workflow = True
    
    $ _qc_noises_installed = hasattr(
        store.hkb_button,
        "_otter_noises_enabled"
    )

    if _qc_noises_installed:

        $ _qc_noises_enabled = (
            store.hkb_button._otter_noises_enabled
        )

        $ store.hkb_button._otter_noises_enabled = False

    $ store.hkb_button.music_enabled = True

    python:
        Event.checkEvents(mas_compliments.compliment_database)

        compliments_menu_items = [
        (ev.prompt, ev_label, not seen_event(ev_label), False)
        for ev_label, ev in mas_compliments.compliment_database.iteritems()
        if (
            Event._filterEvent(
                ev,
                unlocked=True,
                aff=mas_curr_affection,
                flag_ban=EV_FLAG_HFM
            )
            and (
                not hasattr(ev, "checkConditional")
                or ev.checkConditional()
            )
        )
    ]

        compliments_menu_items.sort()

    $ final_item = ("Oh nevermind.", False, False, False, 20)

    show monika at t21

    call screen mas_gen_scrollable_menu(compliments_menu_items, mas_ui.SCROLLABLE_MENU_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    if _return:
        $ _qc_compliment = _return

        python:
            if hasattr(mas_compliments, "compliment_delegate_callback"):
                mas_compliments.compliment_delegate_callback()

        show monika at t11

        call expression _qc_compliment

        if _return is not None:
            $ _qc_ret_items = _return.split("|")

            if "love" in _qc_ret_items:
                $ mas_ILY()

    else:
        show monika at t11
        
    if _qc_noises_installed:

        $ store.hkb_button._otter_noises_enabled = (
            _qc_noises_enabled
        )

    return


screen quick_compliments_button():

    zorder 16


    if not persistent.qc_button_hidden:

        if (
            mas_HKBIsVisible()
            and store.mas_submod_utils.current_label
                != "mas_piano_setupstart"
        ):

            if store.mas_globals.in_idle_mode:

                if persistent.qc_language == "ru":

                    textbutton qc_text("praise"):

                        style "hkb_button"
                        text_style "qc_praise_ru_text"

                        xpos 0.05
                        ypos qc_button_ypos()

                else:

                    textbutton qc_text("praise"):

                        style "hkb_button"

                        xpos 0.05
                        ypos qc_button_ypos()


            elif store.hkb_button.talk_enabled:

                if persistent.qc_language == "ru":

                    textbutton qc_text("praise"):

                        style "hkb_button"
                        text_style "qc_praise_ru_text"

                        xpos 0.05
                        ypos qc_button_ypos()

                        action Function(
                            renpy.call,
                            "quick_compliments"
                        )

                else:

                    textbutton qc_text("praise"):

                        style "hkb_button"

                        xpos 0.05
                        ypos qc_button_ypos()

                        action Function(
                            renpy.call,
                            "quick_compliments"
                        )


            else:

                if persistent.qc_language == "ru":

                    textbutton qc_text("praise"):

                        style "hkb_button"
                        text_style "qc_praise_ru_text"

                        xpos 0.05
                        ypos qc_button_ypos()

                else:

                    textbutton qc_text("praise"):

                        style "hkb_button"

                        xpos 0.05
                        ypos qc_button_ypos()


screen quickly_compliments_settings():

    if persistent._mas_dark_mode_enabled:

        textbutton qc_text("submod_settings"):

            style "qc_submod_settings_button_dark"
            text_style "qc_submod_settings_text_dark"

            action Show(
                "quickly_compliments_settings_window"
            )

    else:

        textbutton qc_text("submod_settings"):

            style "qc_submod_settings_button"
            text_style "qc_submod_settings_text"

            action Show(
                "quickly_compliments_settings_window"
            )


screen quickly_compliments_settings_window():

    modal True

    zorder 200


    if persistent._mas_dark_mode_enabled:

        $ _qc_button_style = "qc_settings_button_dark"
        $ _qc_button_text_style = "qc_settings_button_text_dark"
        $ _qc_text_style = "qc_settings_text_dark"

    else:

        $ _qc_button_style = "qc_settings_button"
        $ _qc_button_text_style = "qc_settings_button_text"
        $ _qc_text_style = "qc_settings_text"


    frame:

        padding (25, 20, 25, 20)

        xalign 0.5
        yalign 0.5


        vbox:

            spacing 8

            xalign 0.5


            text qc_text("title"):

                style _qc_text_style
                xalign 0.5


            null height 8


            text qc_text("language"):

                style _qc_text_style
                xalign 0.5


            textbutton _("English"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_language != "en"
                )

                action Function(
                    qc_set_language,
                    "en"
                )


            textbutton _("Русский"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_language != "ru"
                )

                action Function(
                    qc_set_language,
                    "ru"
                )


            textbutton _("Español"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_language != "es"
                )

                action Function(
                    qc_set_language,
                    "es"
                )


            textbutton _("Português (Brasil)"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_language != "pt"
                )

                action Function(
                    qc_set_language,
                    "pt"
                )


            null height 8


            text qc_text("button_position"):

                style _qc_text_style
                xalign 0.5


            textbutton qc_text("position_1"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_button_hidden
                    or persistent.qc_button_position != 0
                )

                action Function(
                    qc_set_position,
                    0
                )


            textbutton qc_text("position_2"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_button_hidden
                    or persistent.qc_button_position != 1
                )

                action Function(
                    qc_set_position,
                    1
                )


            textbutton qc_text("position_3"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_button_hidden
                    or persistent.qc_button_position != 2
                )

                action Function(
                    qc_set_position,
                    2
                )


            textbutton qc_text("position_4"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_button_hidden
                    or persistent.qc_button_position != 3
                )

                action Function(
                    qc_set_position,
                    3
                )


            textbutton qc_text("position_5"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_button_hidden
                    or persistent.qc_button_position != 4
                )

                action Function(
                    qc_set_position,
                    4
                )


            textbutton qc_text("position_6"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    persistent.qc_button_hidden
                    or persistent.qc_button_position != 5
                )

                action Function(
                    qc_set_position,
                    5
                )


            textbutton qc_text("hide"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                sensitive (
                    not persistent.qc_button_hidden
                )

                action Function(
                    qc_hide_button
                )


            null height 10


            textbutton qc_text("close"):

                style _qc_button_style
                text_style _qc_button_text_style

                xalign 0.5

                action Hide(
                    "quickly_compliments_settings_window"
                )


init 5 python:

    if "quick_compliments_button" not in config.overlay_screens:

        config.overlay_screens.append(
            "quick_compliments_button"
        )

    qc_sync_journal_position()


# А я знаю, что ты это читаешь. ;) 
