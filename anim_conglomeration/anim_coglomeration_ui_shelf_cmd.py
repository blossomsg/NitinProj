import anim_conglomeration.mass_playblast_lay_func


def main():
    """
    The main function is to run the code and exit on recalling the tool
    Returns:None

    """
    # CAVEAT: "win" var is global so that it can be used in multiple situations in the script
    global win
    # CAVEAT: first it will try to close if the win exist
    try:
        win.close()
    except:
        pass
    win = anim_conglomeration.mass_playblast_lay_func.MassPlayblastLayFunc()
    # CAVEAT: if the exception is raised the window will be shown
    win.show()
