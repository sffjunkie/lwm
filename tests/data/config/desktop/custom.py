def float_to_front(qtile):
    """ Bring all floating windows of the group to front """
    for window in qtile.currentGroup.windows:
        if window.floating:
            window.cmd_bring_to_front()
