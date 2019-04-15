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

        info_v = ed_self.get_prop(PROP_SCROLL_VERT_INFO)
        info_h = ed_self.get_prop(PROP_SCROLL_HORZ_INFO)
        pos_v = info_v['smooth_pos']
        pos_h = info_h['smooth_pos']
        max_v = info_v['smooth_pos_last']
        max_h = info_h['smooth_pos_last']

        grp = ed_self.get_prop(PROP_INDEX_GROUP)
        e = ed_group(1 if grp==0 else 0)
        if e is None: return

        info2_v = e.get_prop(PROP_SCROLL_VERT_INFO)
        info2_h = e.get_prop(PROP_SCROLL_HORZ_INFO)
        max2_v = info2_v['smooth_pos_last']
        max2_h = info2_h['smooth_pos_last']

        #checks for max are needed to workaround CudaText bug, 
        #with scroll at end with non-equal height files
        if self.sync_v:
            if pos_v<max_v and pos_v<max2_v:
                e.set_prop(PROP_SCROLL_VERT_SMOOTH, pos_v)

        if self.sync_h:
            if pos_h<max_h and pos_h<max2_h:
                e.set_prop(PROP_SCROLL_HORZ_SMOOTH, pos_h)

        e.cmd(cmds.cmd_RepaintEditor)


    def on_state(self, ed_self, state):

        if state==APPSTATE_GROUPS:
            if not groups_ok():
                self.sync_h = False
                self.sync_v = False
            self.update()
