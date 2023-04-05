'# Imports'
from Message import MessageBox
from Config_func import default_mode, finish, change_values,\
    check_input_valid, argument_mode, parse_args
import sys
"# Python Script for saving the configs from all switch Series with a list"
"# Created by Insomnia"
"# Version 1.2.1"

'# Imports'
version = "1.2.1"
sys.stdout = open(1, "w", encoding="utf-8", closefd=False)

# **************************************************#
# Main routine
# **************************************************#


def main():
    messages = MessageBox()
    args = parse_args()
    # print(len(vars(args)))
    print(f"Automatic Switch Config saver Version {version}\n")

    if args.save_director is not None and args.switch_list is not None:
        print("[+] Willkommen im argument Config Mode! [+]\n")
        zpath = check_input_valid(args.save_director)
        file = check_input_valid(args.switch_list)
        argument_mode(zpath, file)
        finish()

    if args.save_director is None and args.switch_list is None:
        print("[+] Willkommen im default Config Mode! [+]\n")
        zpath = input(messages.savPath)
        zpath = check_input_valid(zpath)
        file = input(messages.saveList)
        file = check_input_valid(file)
        default_mode(zpath, file)

    if (args.save_director is not None and args.switch_list is None):
        zpath = check_input_valid(args.save_director)
        file = check_input_valid(args.switch_list)
        val = change_values(str(zpath), str(file))
        zpath = val[0]
        file = val[1]
        argument_mode(zpath, file)
    elif (args.save_director is None and args.switch_list is not None):
        zpath = check_input_valid(args.save_director)
        file = check_input_valid(args.switch_list)
        val = change_values(str(zpath), str(file))
        zpath = val[0]
        file = val[1]
        argument_mode(zpath, file)

    finish()

# **************************************************#
# Main
# **************************************************#


if __name__ == "__main__":
    main()

"""TO DO """
# script über Argumente ausführen ex. script.py arg1 arg2
# Wiederholende Funktionien auslaggern
# Command befehl überprüfen
