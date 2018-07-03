import os
from cudatext import *
import cudatext_cmd as cmds

HorizontalScrol = False
VerticalScrol = False

class Command:
    
    def __init__(self):
        pass

    def config(self):
        pass
        
    def toggle_vert(self):
        global VerticalScrol
        VerticalScrol=not VerticalScrol

    def toggle_horz(self):
        global HorizontalScrol
        HorizontalScrol=not HorizontalScrol

    def on_scroll(self,ed_self):
        global HorizontalScrol
        global VerticalScrol
        if VerticalScrol:
            pos=ed_self.get_prop(PROP_SCROLL_VERT)
            for h in ed_handles():
                e=Editor(h)
                e.set_prop(PROP_SCROLL_VERT,pos)
                e.cmd(cmds.cmd_RepaintEditor)
        if HorizontalScrol:
            pos=ed_self.get_prop(PROP_SCROLL_HORZ)
            for h in ed_handles():
                e=Editor(h)
                e.set_prop(PROP_SCROLL_HORZ,pos)
                e.cmd(cmds.cmd_RepaintEditor)
           
