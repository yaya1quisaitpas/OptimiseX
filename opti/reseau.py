import os
import subprocess
import platform
import ctypes
import sys

def hide_console():
    # Obtenir le handle de la console
    kernel32 = ctypes.WinDLL('kernel32')
    hwnd = kernel32.GetConsoleWindow()
    if hwnd != 0:
        # Masquer la fenêtre de la console
        ctypes.windll.user32.ShowWindow(hwnd, 0)  # SW_HIDE = 0

def main():
    hide_console()
    # Votre code ici
    print("Ce texte ne sera pas visible dans la fenêtre de la console")


# Fonction pour exécuter une commande et afficher la sortie
def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {command}")
        print(e.output)

# Fonction pour vider le cache DNS
def flush_dns():
    if platform.system() == "Windows":
        run_command("ipconfig /flushdns")
    else:
        run_command("sudo systemd-resolve --flush-caches")

# Fonction pour renouveler l'adresse IP
def renew_ip():
    if platform.system() == "Windows":
        run_command("ipconfig /release")
        run_command("ipconfig /renew")
    else:
        run_command("sudo dhclient -r")
        run_command("sudo dhclient")

# Fonction pour réinitialiser la pile TCP/IP
def reset_tcp_ip():
    if platform.system() == "Windows":
        run_command("netsh int ip reset")
        run_command("netsh winsock reset")
    else:
        print("Cette fonction est limitée à Windows pour le moment.")

# Fonction pour changer les serveurs DNS (exemple avec Google DNS)
def set_dns():
    if platform.system() == "Windows":
        run_command('netsh interface ipv4 set dns name="Ethernet" source=static address=8.8.8.8')
        run_command('netsh interface ipv4 add dns name="Ethernet" addr=8.8.4.4 index=2')
    else:
        run_command('sudo nmcli device modify eth0 ipv4.dns "8.8.8.8 8.8.4.4"')
        run_command('sudo systemctl restart NetworkManager')

# Fonction pour tester le ping vers un serveur (exemple avec Google)
def test_ping(host="8.8.8.8"):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {host}"
    run_command(command)

# Fonction principale d'optimisation
def optimize_network():
    print("Vider le cache DNS...")
    flush_dns()

    print("Renouveler l'adresse IP...")
    renew_ip()

    print("Réinitialiser la pile TCP/IP...")
    reset_tcp_ip()

    print("Changer les serveurs DNS pour Google DNS...")
    set_dns()

    print("Test du ping...")
    test_ping()

    print("Optimisation terminée.")

main()
optimize_network()