import os
from cudatext import *
import cudatext_cmd as cmds

class Command:
    sync_v = False
    sync_h = False
    
    def __init__(self):
        pass

    def config(self):
        pass
        
    def toggle_vert(self):
        self.sync_v = not self.sync_v

    def toggle_horz(self):
        self.sync_h = not self.sync_h

    def on_scroll(self,ed_self):
    
        if self.sync_v:
            pos=ed_self.get_prop(PROP_SCROLL_VERT)
            for h in ed_handles():
                e=Editor(h)
                e.set_prop(PROP_SCROLL_VERT,pos)
                e.cmd(cmds.cmd_RepaintEditor)
        if self.sync_h:
            pos=ed_self.get_prop(PROP_SCROLL_HORZ)
            for h in ed_handles():
                e=Editor(h)
                e.set_prop(PROP_SCROLL_HORZ,pos)
                e.cmd(cmds.cmd_RepaintEditor)
           
