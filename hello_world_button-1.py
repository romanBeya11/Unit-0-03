'''
Created By Roman Beya
Created on 14-Sep-2017
Created For ICS3U
This program displays hello world when a button called click me!!! is pressed
'''

import ui

def hello_world_touch_up_inside(sender):
   view['hello_world_label'].text = ("Hello World!!!!!!!!!")
view = ui.load_view()
view.present('sheet')
