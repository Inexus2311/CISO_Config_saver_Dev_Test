# Imports
import platform
import getpass
import sys
import os
import argparse
'# import paramiko'

# Menu mode
# mode = ""

"# Functions"
# **************************************************#
# Update save Directory and filename of switch_List
# **************************************************#


def change_values(arg1, arg2):
    while not os.path.exists(arg1):
        print("Der Pfad {0} ist nicht vorhanden.".format(arg1))
        user_input = input(
            "Geben Sie einen gültigen Pfad ein oder beenden Sie das Programm mit Q !\n"
        )
        if Quit(user_input):
            pass
        else:
            arg1 = user_input

    while not os.path.exists(arg2):
        # os.system("clear")
        user_input = input(
            "Geben Sie eine gültige Datei ein oder beenden Sie das Programm mit Q !\n"
        )
        if Quit(user_input):
            pass
        else:
            arg2 = user_input
            print("Die Datei {0} ist vorhanden.".format(arg2))

    return [arg1, arg2]


# **************************************************#
# Close Programm
# **************************************************#

def Quit(arg1):
    if arg1.lower() == "q":
        print("Programm wird beendet! ")
        sys.exit()
    else:
        return 0

# **************************************************#
# Check if a file can be reading
# **************************************************#


def check_reading(file_name):
    try:
        file = open(file_name, "r")
        print(f"[+]... Reading file {file_name} was successfully")
        file.close()
    except file.errors:
        print("Die Datei konnte nicht geöffnet werden.")
        os.exit()

# **************************************************#
# SCP-Connection routine
# **************************************************#


def scp_authenticaten(zpath, file_name):
    username = input("Geben Sie Ihren TACAS-Username ein!: ")
    password = getpass.getpass("Bitte geben Sie Ihr Passwort ein!: ")
    # password = input("Bitte geben Sie Ihr Passwort ein!: ")
    """
    #Connection Details
    for line in file_list:
        hostname = line.strip()
        #Create a SSH client
        client = paramiko.SSHClient()
        # Make sure that we add the remote server's SSH key automatically
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #Connect to the client
        try:
            client.connect(hostname,username=username,password=password)
            print("SSH session to %s is open" %hostname)
            break
        except client.error:
            print("[-] Authentifizierung fehlgeschlagen!")
            break
    """
    if username == "" or password == "":
        return 0

    with open(file_name, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                print(
                    "[-] Keine Liste in File enthalten! Vorgang wird abgebrochen!")
                sys.exit()
            else:
                if line.isalpha() and len(line) >= 0:
                    print(
                        "[-] Leere Zeile in File enthalten! Vorgang wird abgebrochen!"
                    )
                    sys.exit()
                else:
                    switch_name = line.strip()
                    if "/" in zpath:
                        file = zpath+switch_name
                    else:
                        file = zpath + "/"+switch_name
                    system = platform.system()
                    if system == "Linux":
                        command = f"sshpass -p {password} scp {username}@{switch_name}:running-config {file}_test.txt"
                    elif system == "Windows":
                        command = f"scp {username}@{switch_name}:running-config  {file}_test.txt"
                    else:
                        print("Unbekanntes Betriebssystem")
                    try:
                        # os.system('echo ' + password + ' | ' + command)
                        if os.system(command) != 0:
                            raise Exception(
                                "[-] SSH Authentication failed!")
                        else:
                            print("[+] SSH Connection passed")
                            if os.path.isfile(f"{switch_name}_test.txt"):
                                print(
                                    "[+] Die Testdatei {switch_name}_test.txt ist bereits vorhanden!")
                                break
                            else:
                                print(
                                    f"[+] Testfile: {switch_name}_test.txt wurde erstellt!")
                            ans = input(
                                f"[?] Soll die Datei {switch_name}_test.txt gelöscht werden? Y/N\n")

                            while check_input(ans):
                                ans = input(
                                    "[-] Falsche Eingabe!\n"f"Soll die Datei {switch_name}_test.txt beibehalten werden? Y/N\n")
                            if ans.lower() == "y":
                                if "/" in zpath:
                                    file_save = zpath+switch_name+"_test.txt"
                                else:
                                    file_save = zpath + "/"+switch_name+"_test.txt"
                                if os.path.isfile(file_save):
                                    os.remove(file_save)
                                else:
                                    print("[-] File not found!")
                            elif ans.lower() == "n":
                                pass
                            break
                    except Exception:
                        print("[-] SSH Connection Authentication failed!")
                        print("[-] Command failed to excecute")
                        sys.exit()
    return [username, password]

# **************************************************#
# Save Config file from Switch
# **************************************************#


def config_save(zpath, file):
    # Check SSH Connection
    print("Checking the SCP Connection.....")
    creds = scp_authenticaten(zpath, file)
    if creds == 0:
        sys.exit()

    file_name = file
    with open(file_name, "r") as f:
        for line in f:
            # print(f"{line}", end="")
            switch_name = line.strip()
            if "/" in zpath:
                file = zpath + switch_name
            else:
                file = zpath + "/" + switch_name
            # print(switch_name)
            if switch_name:
                # command = f"sshpass -p {creds[1]} scp -q {creds[0]}@{switch_name}:running-config  {zpath}/{file_name}.txt"
                command = (
                    f"scp -q {creds[0]}@{switch_name}:running-config {file}.txt")
                if os.path.isfile(f"{file}.txt"):
                    print(f"[+] {switch_name}.txt bereits vorhanden!")
                    continue
                else:
                    print(f"Saving on Switch: {switch_name}")
                    try:
                        if os.system(command) != 0:
                            raise Exception("[-] Wrong Command does not exist")
                    # print(subprocess.check_output(os.system(command),shell=True)
                    except Exception:
                        print("[-] Command couldn't excecute")
                        sys.exit()

                    if os.path.isfile(f"{file}.txt"):
                        print(
                            f"[+] Die Datei {switch_name}.txt wurde erfolgreich heruntergeladen!"
                        )
                    else:
                        print(
                            f"[-] Die Datei {switch_name}.txt konnte nicht heruntergeladen werden!"
                        )
                        break
            else:
                continue

# **************************************************#
# Check arguments are valid
# **************************************************#


def check_arguments(arg1, arg2):
    print("Überprüfung folgende Eingabe:\n")
    print("[+] Zielpfad: {0}\nFilename: {1}\n".format(arg1, arg2))
    check = False

    # Prüfen, ob Parameter vorhanden sind
    if not os.path.exists(arg1):
        return check

    if not os.path.exists(arg2):
        return check  # Pfad vorhanden

    check = True

    print("[+] Der Pfad {0} ist vorhanden.".format(arg1))
    print("[+] Die Datei {0} ist vorhanden.".format(arg2))

    return check
# **************************************************#
# Print Message to finish script
# **************************************************#


def finish():
    print("[+]... done!")
    sys.exit()
    exit()

# **************************************************#
# Default Config Mode routine
# **************************************************#


def default_mode(zpath, file):
    # Check your valid arguments
    if check_arguments(zpath, file):
        check_reading(file)
        print("Starting saving Configs from Switch:")
        config_save(zpath, file)
        finish()
    else:
        while not check_arguments(zpath, file):
            string = change_values(zpath, file)
            zpath = string[0]
            file = string[1]

        check_reading(file)
        print("Starting saving Configs from Switch:")
        config_save(zpath, file)
        finish()

# **************************************************#
# Argument Config Mode routine
# **************************************************#


def argument_mode(arg1, arg2):
    if check_arguments(arg1, arg2):
        check_reading(arg2)
        print("Starting saving Configs from Switch:")
        config_save(arg1, arg2)
        finish()
    else:
        string = change_values(arg1, arg2)
        arg1 = string[0]
        arg2 = string[1]
        check_reading(arg2)
        print("Starting saving Configs from Switch:")
        config_save(arg1, arg2)
        finish()

# **************************************************#
# Helper-Menue
# **************************************************#


def Menu(argv):
    print(
        f"usage: {argv[0]} [-sd save director] [-sw_list Switch_liste]\nExample: python3 {argv[0]} -sd C:/user/path -sw_list test_file.txt\n"
    )


# **************************************************#
# Parser
# **************************************************#

def parse_args():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument('-sd', "--save_director", help="save_directory")
    parser.add_argument('-sw_list', "--switch_list", help="list of switch")
    args = parser.parse_args()
    return args

# **************************************************#
# Check your Inputs
# **************************************************#


def check_input(ans):
    if ans.lower() == 'y':
        return False
    elif ans.lower() == 'n':
        return False
    else:
        return True
