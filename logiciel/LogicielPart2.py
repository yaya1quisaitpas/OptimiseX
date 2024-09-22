import os

try:
    import subprocess
    import customtkinter as ctk
    import pyautogui
    import ctypes
    import sys
except:
    os.system("pip install customtkinter && pip install pyautogui && pip install tk && pip install pycuda")
    pyautogui.alert("The program will restart")
    os.system("start logiciel\logiciel.py")
    sys.exit()

from ctypes import wintypes

try:
    with open("nvidia.txt", "r", encoding="utf-8-sig") as fichier:
        nv = True
except:
    nv = False

winmm = ctypes.WinDLL('winmm')

# Définir les fonctions timeBeginPeriod et timeEndPeriod
timeBeginPeriod = winmm.timeBeginPeriod
timeEndPeriod = winmm.timeEndPeriod


SPI_GETFILTERKEYS = 0x0032
SPI_SETFILTERKEYS = 0x0033
FKF_FILTERKEYSON = 0x00000001
FKF_AVAILABLE = 0x00000002

class FILTERKEYS(ctypes.Structure):
    _fields_ = [
        ('cbSize', wintypes.UINT),
        ('dwFlags', wintypes.DWORD),
        ('iWaitMSec', wintypes.DWORD),
        ('iDelayMSec', wintypes.DWORD),
        ('iRepeatMSec', wintypes.DWORD),
        ('iBounceMSec', wintypes.DWORD)
    ]

user32 = ctypes.WinDLL('user32', use_last_error=True)


def reset_set_filter_keys():
    firstpression = 999
    delaypression = 999
    repeatepression = 500
    bounce = 100
    fk = FILTERKEYS()
    fk.cbSize = ctypes.sizeof(FILTERKEYS)
    fk.dwFlags = FKF_FILTERKEYSON
    fk.iWaitMSec = firstpression      # Temps avant d'accepter la première pression
    fk.iDelayMSec = delaypression     # Temps entre les pressions de touches
    fk.iRepeatMSec = repeatepression   # Temps entre les répétitions de touches
    fk.iBounceMSec = bounce  # Temps pour filtrer les doubles frappes accidentelles

    # Appliquer les paramètres avec SystemParametersInfo
    result = user32.SystemParametersInfoW(SPI_SETFILTERKEYS, fk.cbSize, ctypes.byref(fk), 0)
    if result:
        pyautogui.alert("Keyboard sucessfuly reset")
    else:
        pyautogui.alert("error")

def set_filter_keys():
    firstpression = 0
    delaypression = 130
    repeatepression = 10
    bounce = 0
    fk = FILTERKEYS()
    fk.cbSize = ctypes.sizeof(FILTERKEYS)
    fk.dwFlags = FKF_FILTERKEYSON
    fk.iWaitMSec = firstpression      # Temps avant d'accepter la première pression
    fk.iDelayMSec = delaypression     # Temps entre les pressions de touches
    fk.iRepeatMSec = repeatepression   # Temps entre les répétitions de touches
    fk.iBounceMSec = bounce  # Temps pour filtrer les doubles frappes accidentelles

    # Appliquer les paramètres avec SystemParametersInfo
    result = user32.SystemParametersInfoW(SPI_SETFILTERKEYS, fk.cbSize, ctypes.byref(fk), 0)
    if result:
        pyautogui.alert("Keyboard sucessfuly optimised")
    else:
        print("error")

def set_timer_resolution():
    result = timeBeginPeriod(1)
    if result == 0:
        pyautogui.alert(f"Resolution was changed to 1ms")
    else:
        print("Error")


def has_nvidia_gpu():
    try:
        output = subprocess.check_output(["dxdiag", "/t", "dxdiag_output.txt"], universal_newlines=True)
        with open("dxdiag_output.txt", "r") as file:
            dxdiag_output = file.read()
            if "NVIDIA" in dxdiag_output:
                return True
    except subprocess.CalledProcessError:
        return False
    finally:
        # Nettoyage du fichier temporaire
        import os
        if os.path.exists("dxdiag_output.txt"):
            os.remove("dxdiag_output.txt")

    return False

def create_nvidia():
    with open("nvidia.txt", "w", encoding="utf-8") as fichier:
        fichier.write("")

frame = 0
label = 0

if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def usercenter():
    listeuser = []
    isuser = False
    try:
        with open("user.txt", 'r', encoding='utf-8-sig') as fichier:
            for ligne in fichier:
                listeuser.append(ligne.strip())
            isuser = True
    except:
        pyautogui.alert("Unvaible user, the program will restart")
        os.system("start logiciel\logiciel.py")
        logiciel.destroy()
    
    if isuser:
        usercenter2(listeuser[0], listeuser[1])

def deletetemp():
    os.system("start opti\clean_temp.bat")
def highperf():
    os.system("start opti\high_alim.bat")
def gamemode():
    os.system("start opti\gamemode.bat")
def nogamemode():
    os.system(r"start opti\nogamemode")
def acceleration():
    os.system(r"start opti\accel.bat")
def noacceleration():
    os.system(r"start opti\noaccel.bat")
def window():
    os.system(r"start opti\windowedopti.bat")
def nowindow():
    os.system(r"start opti\nowindowedopti.bat")
def nvidiagpu():
    global nv
    pyautogui.alert("Please wait (click ok)")
    pyautogui.alert("This action can take one minute (click ok)")
    if nv:
        pyautogui.alert("Your pc have a nvidia GPU")
    
    else:
        if has_nvidia_gpu():
            pyautogui.alert("Your pc has a nvidia GPU")
            create_nvidia()
        else:
            pyautogui.alert("Your pc dosen't have a nvidia GPU")
def reseau_fx():
    os.system(r"start opti\reseau.bat")
def reseau_fx2():
    os.system(r"start opti\reseau.py")
def help1():
    os.system("start https://www.tiktok.com/@yayatech795")

mode = "dark"
mode2 = "dark-blue"

ctk.set_appearance_mode(mode)
ctk.set_default_color_theme(mode2)


logiciel = ctk.CTk()
logiciel.geometry("960x540")
logiciel.resizable(False, False)

logiciel.title("OptimiseX")
logiciel.iconbitmap("logiciel\X.ico")

bienvenue = ctk.CTkLabel(master=logiciel, text="Welcome in OptimiseX")
bienvenue.pack(padx=10, pady=12)

user = ctk.CTkButton(master=logiciel, text="", width=36, height=36, corner_radius=18, command=usercenter)
user.place(relx=0.955, rely=0.0148)

deltemp = ctk.CTkButton(master=logiciel, text="Delete temp files", width=465, height=35, command=deletetemp)
deltemp.place(relx=0.01, rely=0.25)

highalim = ctk.CTkButton(master=logiciel, text="Optimize alimentation options", width=465, height=35, command=highperf)
highalim.place(relx=0.51, rely=0.25)

gamode = ctk.CTkButton(master=logiciel, text="Enable game mode", width=465, height=35, command=gamemode)
gamode.place(relx=0.01, rely=0.35)

nogamode = ctk.CTkButton(master=logiciel, text="Disable game mode", width=465, height=35, command=nogamemode)
nogamode.place(relx=0.51, rely=0.35)

accel = ctk.CTkButton(master=logiciel, text="Enable Hardware-Accelerated GPU Scheduling", width=465, height=35, command=acceleration)
accel.place(relx=0.01, rely=0.45)

noaccel = ctk.CTkButton(master=logiciel, text="Disable Hardware-Accelerated GPU Scheduling", width=465, height=35, command=noacceleration)
noaccel.place(relx=0.51, rely=0.45)

win = ctk.CTkButton(master=logiciel, text="Enable Windowed Game Optimizations", width=465, height=35, command=window)
win.place(relx=0.01, rely=0.55)

nowin = ctk.CTkButton(master=logiciel, text="Disable Windowed Game Optimizations", width=465, height=35, command=nowindow)
nowin.place(relx=0.51, rely=0.55)

nvidia = ctk.CTkButton(master=logiciel, text="Test your gpu", width=465, height=35, command=nvidiagpu)
nvidia.place(relx=0.51, rely=0.65)

timer = ctk.CTkButton(master=logiciel, text="Optimise Delay", width=465, height=35, command=set_timer_resolution)
timer.place(relx=0.01, rely=0.65)

keyboard = ctk.CTkButton(master=logiciel, text="Optimise Keyboard", width=465, height=35, command=set_filter_keys)
keyboard.place(relx=0.01, rely=0.75)

keyboard_reset = ctk.CTkButton(master=logiciel, text="Reset keyboard optimisations", width=465, height=35, command=reset_set_filter_keys)
keyboard_reset.place(relx=0.51, rely=0.75)

reseau = ctk.CTkButton(master=logiciel, text="Internet optimisations 1", width=465, height=35, command=reseau_fx)
reseau.place(relx=0.01, rely=0.85)

reseau2 = ctk.CTkButton(master=logiciel, text="Internet optimisations 2", width=465, height=35, command=reseau_fx2)
reseau2.place(relx=0.51, rely=0.85)

def destroyframe():
    global label
    global frame
    frame.destroy()
    label.destroy()

def autoco():
    os.system("del autoconnect.txt")

def delete():
    os.system("del user.txt")

def usercenter2(nom, password):
    global frame
    global label
    info = f"""
Infos : 

Name        :       {nom}
 """
    frame = ctk.CTkFrame(master=logiciel, width=960, height=540, fg_color="black")
    frame.place(relx=0, rely=0)
    label = ctk.CTkLabel(master=frame, width=960, height=1, text="", fg_color="black")
    label.place(relx=0, rely=0)
    exit = ctk.CTkButton(master=frame, text="Exit", command=destroyframe)
    exit.place(relx=0.84, rely=0.917)
    infos = ctk.CTkLabel(master=frame, text=info, width=945)
    infos.place(relx=0.008, rely=0.1)
    autoconnect = ctk.CTkButton(master=frame, text="Disable Autoconnect", command=autoco, width=945, height=25)
    autoconnect.place(relx=0.008, rely=0.4)
    deleteuser = ctk.CTkButton(master=frame, text="Delete User", command=delete, width=945, height=25)
    deleteuser.place(relx=0.008, rely=0.46)
    help = ctk.CTkButton(master=frame, text="help", command=help1)
    help.place(relx=0.02, rely=0.917)

logiciel.mainloop()