import os
from cudatext import *
import cudatext_cmd as cmds

def groups_ok():
    return app_proc(PROC_GET_GROUPING,'') in [GROUPS_2HORZ, GROUPS_2VERT]
    

class Command:
    sync_v = False
    sync_h = False
    
    def __init__(self):
        pass

    def update(self):
        act = (self.sync_v or self.sync_h) and groups_ok()
        if act:
            ev = 'on_scroll,on_state'
            msg_status('Sync Scroll: active')
        else:
            ev = ''
            msg_status('Sync Scroll: inactive')
        app_proc(PROC_SET_EVENTS,__name__+';'+ev+';;')

    def toggle_vert(self):
        if not groups_ok():
            return msg_status('Cannot activate Sync Scroll for current groups mode')
        self.sync_v = not self.sync_v
        self.update()
        
    def toggle_horz(self):
        if not groups_ok():
            return msg_status('Cannot activate Sync Scroll for current groups mode')
        self.sync_h = not self.sync_h
        self.update()

    def on_scroll(self,ed_self):
        vpos=ed_self.get_prop(PROP_SCROLL_VERT)
        hpos=ed_self.get_prop(PROP_SCROLL_HORZ)
        grp=ed_self.get_prop(PROP_INDEX_GROUP)
        e=ed_group(1 if grp==0 else 0)
        if e is not None:
            if self.sync_v:
                e.set_prop(PROP_SCROLL_VERT,vpos)
            if self.sync_h:
                e.set_prop(PROP_SCROLL_HORZ,hpos)
            e.cmd(cmds.cmd_RepaintEditor)
                
    def on_state(self, ed_self, state):
        if state==APPSTATE_GROUPS:
            if not groups_ok():
                self.sync_h = False
                self.sync_v = False
            self.update()
