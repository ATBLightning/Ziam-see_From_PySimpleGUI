#6001012630047
#Tummanoon Kitcharas-anan
#For more information ==> http://myblogmysoftware.blogspot.com/

import PySimpleGUI as sg
import random

IO = []
def UI():
    for i in range(28,0,-1):
        IO.append(str(i))

def Shuffle_Ran():
    UI()
    random.shuffle(IO)

UI()

def gui1():
    global gui_rows, window
    gui_rows = [[sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop()),sg.RealtimeButton(IO.pop())],
                [sg.T(' ' * 10), sg.SimpleButton('Random', size = (13,1), button_color=('black','orange'))]
                ]

    window = sg.FlexForm('Siam', auto_size_text=True,default_button_element_size=(5, 2),auto_size_buttons=False)
    window.Layout(gui_rows)

gui1()

def loop1():
    while (True):
        button, values = window.ReadNonBlocking()
        if button is None:
            pass
            #print(button)
        if values is None:
            break
        if button == 'Random':
            Shuffle_Ran()
            #print(IO)
            gui1()           
loop1()          