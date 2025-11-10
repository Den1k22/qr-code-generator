

from pathlib import Path
import subprocess
import os

root = Path(__file__).resolve().parent.parent

MAIN_CONST = os.path.join(root, "qr_code_generator/main.py")
ICON_WINDOWS = os.path.join(root, "make_build/icon.ico")
PROGRAM_NAME = '"QR Code Generator.exe"'
OUTPUT_DIR = os.path.join(root, "dist")

command = f"python -m nuitka --onefile --standalone --windows-console-mode=disable --windows-icon-from-ico={ICON_WINDOWS} --output-dir={OUTPUT_DIR} --output-filename={PROGRAM_NAME} {MAIN_CONST}"
print(command)
subprocess.call(command, shell=True)

a = input("Press Enter to exit")
