import sys
from Config_func import *
"# Python Script for savi ng the configs from all switch Series with a list"
"# Created by Insomnia"
"# Version 1.0.0"
version = "1.0.0"
sys.stdout = open(1, "w", encoding="utf-8",closefd=False)

# **************************************************#
# Main
# **************************************************#


def main():
    args = parse_args()
    # print(len(vars(args)))
    print(f"Automatic Switch Config saver Version {version}\n")

    if args.save_director != None and args.switch_list != None:
        print("[+] Willkommen im argument Config Mode! [+]\n")
        zpath = args.save_director
        file = args.switch_list
        argument_mode(zpath, file)
        finish()

    if args.save_director == None and args.switch_list == None:
        print("[+] Willkommen im default Config Mode! [+]\n")
        zpath = input(
            "Bitte geben Sie den Pfad an, wo die Configs gespeichert werden sollen: \n"
        )
        file_name = input(
            "Bitte geben Sie den Name der Liste an. (local oder mit Pfadangabe): \n"
        )

    if args.save_director != None and args.switch_list == None or args.save_director == None and args.switch_list != None:
        zpath = args.save_director
        file = args.switch_list
        val = change_values(str(zpath), str(file))
        zpath = val[0]
        file = val[1]

    default_mode(zpath, file_name)
    finish()

# **************************************************#
# Main routine
# **************************************************#


if __name__ == "__main__":
    main()

"""TO DO """
# script über Argumente ausführen ex. script.py arg1 arg2
# Wiederholende Funktionien auslaggern
# Command befehl überprüfen
