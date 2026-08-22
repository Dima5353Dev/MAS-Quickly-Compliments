# ============================================================
# Quickly Compliments
# by Dima5353 from Russia with love <3
#
# Monika After Story 0.12.18 and 0.12.15
# ============================================================


init -990 python:

    if not hasattr(persistent, "qc_language"):
        persistent.qc_language = "en"

    if persistent.qc_language not in ["en", "ru", "es", "pt"]:
        persistent.qc_language = "en"


    if not hasattr(persistent, "qc_button_position"):
        persistent.qc_button_position = 2


    if not hasattr(persistent, "qc_button_hidden"):
        persistent.qc_button_hidden = False


    def qc_set_language(language):

        persistent.qc_language = language

        renpy.save_persistent()
        renpy.restart_interaction()


    def qc_set_position(position):

        persistent.qc_button_position = position
        persistent.qc_button_hidden = False

        renpy.save_persistent()
        renpy.restart_interaction()


    def qc_hide_button():

        persistent.qc_button_hidden = True

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

        return 95


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

            return "Submod settings"


        elif text_id == "title":

            if language == "ru":
                return "Быстрые Комплименты"

            elif language == "es":
                return "Cumplidos Rápidos"

            elif language == "pt":
                return "Elogios Rápidos"

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

            return "Button position"


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


    $ _qc_noises_installed = hasattr(
        store.hkb_button,
        "_otter_noises_enabled"
    )


    if _qc_noises_installed:

        $ _qc_noises_enabled = (
            store.hkb_button._otter_noises_enabled
        )

        $ store.hkb_button._otter_noises_enabled = False


    $ mas_HKBRaiseShield()

    $ store.mas_hotkeys.talk_enabled = False

    $ store.mas_globals.dlg_workflow = True

    $ store.hkb_button.music_enabled = True


    call monika_compliments


    show monika at t11


    $ store.mas_globals.dlg_workflow = _qc_dlg_workflow

    $ store.mas_hotkeys.talk_enabled = _qc_hotkeys_enabled


    if _qc_noises_installed:

        $ store.hkb_button._otter_noises_enabled = (
            _qc_noises_enabled
        )


    $ mas_HKBDropShield()

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