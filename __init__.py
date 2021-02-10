import os
from cudatext import *


fn_icon = os.path.join(os.path.dirname(__file__), 'terminal_2.png')

class Command:
    def __init__(self):
        self.h_dlg = None
    
    def open_init(self):

        self.h_dlg = self.init_form()

        #app_proc(PROC_BOTTOMPANEL_ADD_DIALOG, (self.title, self.h_dlg, fn_icon))

    def init_form(self):

        h = dlg_proc(0, DLG_CREATE)
        dlg_proc(h, DLG_PROP_SET, prop={
            'border': False,
            })

        n = dlg_proc(h, DLG_CTL_ADD, 'button_ex')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
            'name': 'btn',
            'align': ALIGN_CLIENT,
            'sp_a': 15,
            })

        return h
        
    def open(self):
        if not self.h_dlg:
            self.open_init()
            
            app_proc(PROC_BOTTOMPANEL_ADD_DIALOG, ('Fake 2', self.h_dlg, fn_icon))
            app_proc(PROC_BOTTOMPANEL_ACTIVATE, 'Fake 2')
        
            removed = app_proc(PROC_BOTTOMPANEL_REMOVE, 'Fake')
            print('removed default sidebar icon: '+str(removed))
            
            
    def print_active(self):
        panel = app_proc(PROC_BOTTOMPANEL_GET, '')
        print('active sidebar: '+panel)   

        