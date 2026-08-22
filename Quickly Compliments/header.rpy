# ============================================================
# |Register|
#
# Quickly Compliments
# by Dima5353 from Russia with love <3
#
# Monika After Story 0.12.18 and 0.12.15
# ============================================================

init -990 python:
    store.mas_submod_utils.Submod(
        author="Dima5353 from Russia with love",
        name="Quickly Compliments",
        description="This submod adds a 'Praise' button, allowing you to quickly access Monika’s compliments!",
        version="1.0.0",
        settings_pane="quickly_compliments_settings"
    )
    
init -989 python:

    if store.mas_submod_utils.isSubmodInstalled(
        "Submod Updater Plugin"
    ):

        store.sup_utils.SubmodUpdater(
            submod="Quickly Compliments",
            user_name="Dima5353Dev",
            repository_name="MAS-Quickly-Compliments"
        )