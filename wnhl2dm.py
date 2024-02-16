from pymem import *
from pymem.process import *
from tkinter import *
from tkinter import messagebox

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


def WallhackOFF():
        mem.write_int(getPtrAddr(game_module + 0x004BD9D0, [0x88, 0xC, 0x118, 0x4F8, 0x478]), 1)

def WallhackON():
        mem.write_int(getPtrAddr(game_module + 0x004BD9D0, [0x88, 0xC, 0x118, 0x4F8, 0x478]), 2)

def StaticLightOFF():
        mem.write_int(getPtrAddr(game_module + 0x004B75BC, [0x0, 0x1C4, 0x28, 0x4, 0x6A8]), 0)

def StaticLightON():
        mem.write_int(getPtrAddr(game_module + 0x004B75BC, [0x0, 0x1C4, 0x28, 0x4, 0x6A8]), 1)

def About():
      msg=messagebox.showinfo( "About", "WnyNot Half-Life 2 DeathMatch Build 16.02.2024")
      


Twallhack = Label(root, text = "Wallhack", bg='black', fg='white' ).place(x=0,y=0,width=318,height=30)
Twallhack = Label(root, text = "Static Light", bg='black', fg='white').place(x=0,y=110,width=318,height=30)
Twallhack = Label(root, text = "Developed", bg='black', fg='white').place(x=0,y=130,width=319,height=106)
Button1 = Button(root, text ="ON", bg='#ec03fc', fg='white' , command = WallhackON)
Button1.place(x=130,y=30,width=59,height=30)
Button2 = Button(root, text ="OFF", bg='#ec03fc', fg='white' , command = WallhackOFF)
Button2.place(x=130,y=70,width=60,height=30)
Button3 = Button(root, text ="About", bg='#ec03fc', fg='white' , command = About)
Button3.place(x=0,y=210,width=70,height=25)

root.mainloop()




