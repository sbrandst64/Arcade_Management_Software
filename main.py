import os
import webbrowser
from tkinter import *
import customtkinter as ctk
from PIL import Image
from CTkListbox import *

ipaddress = 0
port = 0

NES = {"console": "NES",
       "extensions": ".exe",
       "filepath": "/home/pi/RetroPie/roms/nes"
       }

SNES = {"console": "SNES",
        "extensions": ".smc",
        "filepath": "/home/pi/RetroPie/roms/snes"}  # .swc".fig", ".mgd", ".sfc",

GAMEBOY = {"console": "GAMEBOY",
           "extensions": ".gb\0",
           "filepath": "/home/pi/RetroPie/roms/gb"
           }

DREAMCAST = {"console": "DREAMCAST",
             "extensions": [".cdi", ".gdi"],
             "filepath": ""}

GBA = {"console": "GBA",
       "extensions": ".gba",
       "filepath": "/home/pi/RetroPie/roms/gba"
       }

GBC = {"console": "GBC",
       "extensions": ".gbc",
       "filepath": "/home/pi/RetroPie/roms/gbc"
       }

N64 = {"console": "N64",
       "extensions": [".n64", ".v64", ".z64"],
       "filepath": "/home/pi/RetroPie/roms/n64"
       }

MAME = {"console": "MAME",
        "extensions": ".zip",
        "filepath": "/home/pi/RetroPie/roms/fba"
        }

DS = {"console": "DS",
      "extensions": ".nds",
      "filepath": "/home/pi/RetroPie/roms/fds"
      }

options = [NES, SNES, GAMEBOY, DREAMCAST, GBA, GBC, N64, MAME, DS]
downloadPath = r"C:\Users\Brandstetter\Downloads"
currentConsoleFilter = "."

global downloadList
global numberOfDownloads


def Transfer_Button_Clicked():
    i = 0


def Online_Search_Button_Clicked():
    webbrowser.open('https://www.romsgames.net/roms/')


def Select_Download(game):
    print(game)


def Select_Emulator(emu):
    global numberOfDownloads

    print(emu)
    i = 0
    while i < len(options):
        cuconsole = options[i]
        i = i + 1
        if cuconsole["console"] == emu:
            print(cuconsole["extensions"])
            global currentConsoleFilter
            currentConsoleFilter = cuconsole["extensions"]
    i = 0
    while i < numberOfDownloads:
        downloadList.delete(i)
        i = i + 1
    i = 0
    numberOfDownloads = 0
    while i < len(AllFiles):

        if AllFiles[i].endswith(currentConsoleFilter):
            downloadList.insert(numberOfDownloads, AllFiles[i])
            numberOfDownloads = numberOfDownloads + 1
            print(numberOfDownloads)
        i = i + 1


def Delete_Game_Clicked():
    oi = 0


def GetDownloads(downloadList):
    global numberOfDownloads
    global AllFiles
    i = 0

    os.chdir(downloadPath)
    os.getcwd()

    AllFiles = os.listdir()

    while i < len(AllFiles):  ##fill in download list
        downloadList.insert(i, AllFiles[i])
        i = i + 1

    numberOfDownloads = i


def SetUpGui():
    gui = ctk.CTk()
    gui.title("Arcade-Verwaltung")
    gui.geometry('900x400')

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    gui.resizable(False, False)

    onlineSearchButton = ctk.CTkButton(master=gui, text="Online-Search", command=Online_Search_Button_Clicked,
                                       hover_color='#1e7c2f', fg_color='#2aad41')
    onlineSearchButton.place(relx=0.17, rely=0.1, anchor=ctk.CENTER)

    transferButton = ctk.CTkButton(gui, text="Transfer --> ", command=Transfer_Button_Clicked, border_color="green")
    transferButton.place(relx=0.425, rely=0.55, anchor=ctk.CENTER)

    deleteButtonImage = ctk.CTkImage(Image.open("delete-button.png"), size=(120, 30))
    deleteButton = ctk.CTkButton(gui, width=6, height=20, text="", command=Delete_Game_Clicked(),
                                 image=deleteButtonImage, fg_color="transparent", hover_color='#cd0019')
    deleteButton.place(relx=0.75, rely=0.05)

    dropmenue = CTkListbox(gui, width=90, height=50,
                           command=Select_Emulator)  # values=["NES", "SNES", "Gameboy", "DREAMCAST", "GBA", "GB", "GBC", "N64", "MAME", "DS"]
    dropmenue.place(relx=0.55, rely=0.3)
    dropmenue.insert(0, "NES")
    dropmenue.insert(1, "SNES")
    dropmenue.insert(2, "GAMEBOY")
    dropmenue.insert(3, "DREAMCAST")
    dropmenue.insert(4, "GBA")
    dropmenue.insert(5, "GBC")
    dropmenue.insert(6, "N64")
    dropmenue.insert(7, "MAME")
    dropmenue.insert("END", "DS")

    downloadLabel = ctk.CTkLabel(gui, text="Downloads")
    downloadLabel.place(relx=0.13, rely=0.22)
    emuLabel = ctk.CTkLabel(gui, text="Emulator")
    emuLabel.place(relx=0.58, rely=0.22)
    arcadeLabel = ctk.CTkLabel(gui, text="Arcade")
    arcadeLabel.place(relx=0.8, rely=0.22)

    global downloadList
    downloadList = CTkListbox(gui, command=Select_Download)
    downloadList.place(relx=0.05, rely=0.3)
    GetDownloads(downloadList)
    onArcadeList = CTkListbox(gui)
    onArcadeList.place(relx=0.7, rely=0.3)

    gui.mainloop()


SetUpGui()

###### GUI - Related Stuff - END ######


# client = SSHClient

# client.connect('example.com', username='user', password='secret')
# client.close()
