# Keystroke Logger (main.py)

A basic keylogger script written in Python using the `pynput` library. It listens for keyboard events and logs keystrokes into a `log.txt` file.

> ⚠️ **Disclaimer:** This script is intended strictly for educational purposes or ethical use on personal devices. Unauthorized use to monitor others' activity is illegal and unethical.

---

## 📌 Features

- Captures keystrokes using `pynput.keyboard.Listener`
- Handles common special keys (space, enter, backspace, arrows, etc.)
- Logs all captured input into a file named `log.txt`
- Lightweight and easy to run

---

## 🛠️ Requirements

- Python 3.x  
- pynput library  

Install dependencies:

```bash
pip install pynput
