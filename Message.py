class MessageBox:
    def __init__(self, name=None):
        self.error = "Program occurs an error! Closing Program now!"
        self.msgData = """Geben Sie eine gültige Datei ein \
oder beenden Sie das Programm mit Q !\n"""
        self.close = "Closing Program immediately!"
        self.errData = "Die Datei konnte nicht geöffnet werden."
        self.errNolist = "[-] Keine Liste in File enthalten! \
Vorgang wird abgebrochen!"
        self.errRow = "[-] Leere Zeile in File enthalten! \
Vorgang wird abgebrochen!"
        self.savPath = "Bitte geben Sie den Pfad an, \
wo die Configs gespeichert werden sollen: \n"
        self.saveList = "Bitte geben Sie den Name der Liste an. \
(local oder mit Pfadangabe): \n"

    def failed_target(self, name):
        self.msgTarget = f"""[-] Die Datei {name} \
existiert nicht auf dem Zielhost!"""
        return self.msgTarget

    def InputError(self, name):
        self.msgErr1 = f"Input: {name} contains invalid characters!"
        return self.msgErr1

    def read_success(self, name):
        self.msgRead = f"[+]... Reading file {name} was successfully"
        return self.msgRead

    def path_error(self, arg1):
        first = "Der Pfad: {0} ist nicht vorhanden.".format(arg1)
        second = "Geben Sie einen gültigen Pfad ein oder \
beenden Sie das Programm mit Q !\n"
        self.pathErr = first+second
        return self.pathErr

    def sucess_data(self, name):
        self.msg = "Die Datei: {0} ist vorhanden.".format(name)
        return self.msg

    def test_success_data(self, name):
        self.msg = f"[+] Die Testdatei {name}_test.txt \
ist bereits vorhanden!"
        return self.msg

    def test_create_data(self, name):
        self.msg = f"[+] Testfile: {name}_test.txt wurde erstellt!"
        return self.msg

    def quest_data_create(self, name):
        self.msg = f"[?] Soll die Datei {name}_test.txt \
gelöscht werden? Y/N\n"
        return self.msg

    def err_input(self, name):
        self.msg = "[?] Falsche Eingabe!\n"f"Soll die Datei {name}_test.txt \
beibehalten werden? Y/N\n"
        return self.msg

    def down_sucess(self, name):
        self.msg = f"[+] Die Datei {name}.txt \
wurde erfolgreich heruntergeladen!"
        return self.msg

    def down_err(self, name):
        self.msg = f"[-] Die Datei {name}.txt \
konnte nicht heruntergeladen werden!"
        return self.msg

    def menu_help(self, argv):
        self.msgHelp = f"""usage: {argv[0]} [-sd save director] \
[-sw_list Switch_liste]\n\
Example: python3 {argv[0]} -sd C:/user/path -sw_list test_file.txt\n"""
        return self.msgHelp
