raise NotImplementedError
# [BUG] Once root permission is given to this script, it can only execute the main script with root permittion, 
#       which finally causes the Fcitx not working. For this I added a NotImplementedError at the head of this file
#       to stop users executing it.


import keyboard
import subprocess
import sys
import os

success=False

print("Hello, "+os.getlogin())

if len(sys.argv)>1:
    sudo_relaunch=sys.argv[1].startswith("--sudo_relaunch")
    print("Program restarted with --sudo_relaunch")
else:
    sudo_relaunch=False

try:
    #os.system(f"sudo -S python{sys.version_info.major}.{sys.version_info.minor} {os.getcwd()}/MinecraFcitx.py --close-instead-of-minimize")
    keyboard.add_hotkey("ctrl+shift+space",lambda:os.system(\
        f"sudo {os.getlogin()} python{sys.version_info.major}.{sys.version_info.minor} {os.getcwd()}/MinecraFcitx.py --close-instead-of-minimize"))
    print("HOTKEY BINDED! ENJOY!")
    success=True
    #subprocess.call("sudo -k",shell=True)
except Exception as e:
    #abc=xyz
    #win.destroy()
    print("Hotkey binding failed!")
    if not sudo_relaunch:
        print("This might because of you are running this without root permittion.")
        print("The program will restart with sudo command.")
        print("Please enter password later if asked.")
        #import tkinter.simpledialog as askbox
        print("RUN COMMAND: "+f"sudo -S python{sys.version_info.major}.{sys.version_info.minor} '{sys.argv[0]}' --sudo_relaunch")
        ENABLE_BETTER_PWD_INPUT=False
        if ENABLE_BETTER_PWD_INPUT:
            import tkinter
            root=tkinter.Tk()
            root.withdraw()
            import tkinter.simpledialog as askbox
            pwd=askbox.askstring("Enter Password","Enter Password for Sudo Command",show="*")
            subprocess.Popen(f"sudo -S python{sys.version_info.major}.{sys.version_info.minor} '{sys.argv[0]}' --sudo_relaunch",
                            stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate(pwd.encode())
        else:
            os.system(f"sudo -S python{sys.version_info.major}.{sys.version_info.minor} '{sys.argv[0]}' --sudo_relaunch")
    else:
        print(e)
        raise e

if success:
    input("Press [ENTER] here too quit the program. ")
