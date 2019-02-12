import anim_conglomeration.mass_playblast_lay_func

def main():
    global win
    try:
        win.close()
    except: pass
    win = anim_conglomeration.mass_playblast_lay_func.MassPlayblastLayFunc()
    win.show()