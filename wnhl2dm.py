from pymem import *
from pymem.process import *
from tkinter import *
import datetime as dt
from os import system as cmd



#this is only in case the cheat is launched via the cmd
cmd("title WhyNot Debug")
cmd("cls")



mem = Pymem("hl2.exe")
game_module = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll


def getPtrAddr(address, offsets):
    addr = mem.read_int(address)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr



root = Tk()
root['bg'] = 'black'
root.title('WhyNot HL2DM')
root.geometry('320x240')
root.resizable(width=False, height=False)

date = dt.datetime.now()


def WallhackOFF():
        mem.write_int(getPtrAddr(game_module + 0x004BD9D0, [0x88, 0xC, 0x118, 0x4F8, 0x478]), 1)

def WallhackON():
        mem.write_int(getPtrAddr(game_module + 0x004BD9D0, [0x88, 0xC, 0x118, 0x4F8, 0x478]), 2)

def DisableCustomSprayON():
        mem.write_int(getPtrAddr(game_module + 0x004C6AB0, [0x94, 0xC, 0x118, 0x1C, 0x41C]), 1)
      
def DisableCustomSprayOFF():
        mem.write_int(getPtrAddr(game_module + 0x004C6AB0, [0x94, 0xC, 0x118, 0x1C, 0x41C]), )

Twallhack = Label(root, text = "Wallhack", bg='black', fg='white' ).place(x=0,y=0,width=318,height=30)
Twallhack = Label(root, text = "DisableSprays", bg='black', fg='white').place(x=0,y=110,width=318,height=30)
Time= Label(root, text =f"{date:%A, %B %d, %Y}", bg='black', fg='white' ).place(x=0,y=200,width=317,height=36)
Button1 = Button(root, text ="ON", bg='#ec03fc', fg='white' , command = WallhackON)
Button1.place(x=130,y=30,width=59,height=30)
Button2 = Button(root, text ="OFF", bg='#ec03fc', fg='white' , command = WallhackOFF)
Button2.place(x=130,y=70,width=60,height=30)
Button3 = Button(root, text ="ON", bg='#ec03fc', fg='white' , command = DisableCustomSprayON)
Button3.place(x=130,y=140,width=60,height=30)
Button4 = Button(root, text ="OFF", bg='#ec03fc', fg='white' , command = DisableCustomSprayOFF)
Button4.place(x=130,y=180,width=60,height=30)


root.mainloop()




