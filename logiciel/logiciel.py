import os

try:
    import customtkinter as ctk
    import pyautogui
    import sys
    import ctypes
    import hashlib
except:
    os.system("pip install customtkinter && pip install pyautogui && pip install hashlib")

if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def hash_string_sha256(input_string):
    # Créez un objet de hachage SHA-256
    sha256_hash = hashlib.sha256()
    
    # Mettez à jour l'objet de hachage avec les données de la chaîne encodée en bytes
    sha256_hash.update(input_string.encode('utf-8'))
    
    # Obtenez le hachage en format hexadécimal
    return sha256_hash.hexdigest()




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

login = ctk.CTk()
login.geometry("500x350")
login.resizable(False, False)
login.title("OptimiseX")
login.iconbitmap("logiciel\X.ico")
auto = False
listeuser = []
chemin_fichier = "user.txt"
created = True
true = False

try:
    with open("autoconnect.txt", "r", encoding="utf-8-sig") as fichier:
        true = True
except:
    true = False


try:
    with open(chemin_fichier, 'r', encoding='utf-8-sign') as fichier:
        for ligne in fichier:
            listeuser.append(ligne.strip())

except:
    created = False

if true==True:
    os.system("start logiciel\LogicielPart2.py")
    login.destroy()

def connexion():
    global auto
    email = champ1.get()
    password = champ2.get()
    check = checkbox.get()
    true = True
    if created==False:
        pyautogui.alert("""Thanks to click on "Register" """)
    else:
        if email!=str(listeuser[0]):
            pyautogui.alert("E-mail is not avaible")
            true = False
        elif hash_string_sha256(password)!=listeuser[1]:
            pyautogui.alert("Incorrect Password")
            true = False
        if true==True:
            if check==1:
                autoconnect()
            os.system("start logiciel\LogicielPart2.py")
            login.destroy()


def register():
    global created
    email = champ1.get()
    password = champ2.get()
    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(f"{email}\n")
        fichier.write(hash_string_sha256(password))
        fichier.write("\n")
    with open(chemin_fichier, 'r', encoding='utf-8-sig') as fichier:
        for ligne in fichier:
            listeuser.append(ligne.strip())
            created = True
    pyautogui.alert("""Now, click on "Login" """)

def autoconnect():
    pyautogui.alert(""" To disable "Autoconnect", go in the user center""")
    with open("autoconnect.txt", "w", encoding="utf-8") as fichier:
        fichier.write("")

frame = ctk.CTkFrame(master=login)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login")
label.pack(pady=12, padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="E-mail")
champ1.pack(pady=12)

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
champ2.pack(pady=12)

button = ctk.CTkButton(master=frame, text="Login", command=connexion)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="stay loged in")
checkbox.pack(pady=12, padx=10)

signup = ctk.CTkButton(master=frame, text="Register", command=register)
signup.pack(pady=12, padx=100)

login.mainloop()