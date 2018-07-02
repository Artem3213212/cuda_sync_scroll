import os
from cudatext import *
import cudatext_cmd as cmds

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_sync_scroll.ini')

HorizontalScrol = True
VerticalScrol = True

def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'

class Command:
    
    def __init__(self):
        global HorizontalScrol
        global VerticalScrol
        HorizontalScrol = str_to_bool(ini_read(fn_config, 'op', 'HorizontalScrol', bool_to_str(HorizontalScrol)))
        VerticalScrol = str_to_bool(ini_read(fn_config, 'op', 'VerticalScrol', bool_to_str(VerticalScrol)))

    def config(self):
        ini_write(fn_config, 'op', 'HorizontalScrol', bool_to_str(HorizontalScrol))
        ini_write(fn_config, 'op', 'VerticalScrol', bool_to_str(VerticalScrol))
        file_open(fn_config)
        
    def Vertical(self):
        global VerticalScrol
        VerticalScrol=not VerticalScrol

    def Horizontal(self):
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
        
"""
AAAAAAAAAAAAAAAAAAA
a 
wsv
fa
e
fa
s
ea
f
a
e

as
d
as
df
a
sd
f
as
df
as
d
fa
sd
fa
sdf
a
d
f
as
fd
as
df
a

fd
as
f
das
f
da
sf

das
fa

df
a
df
a
sdf

"""