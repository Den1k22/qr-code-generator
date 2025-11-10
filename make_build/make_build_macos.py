

from pathlib import Path
import subprocess
import os

root = Path(__file__).resolve().parent.parent

MAIN_CONST = os.path.join(root, "qr_code_generator/main.py")
ICON_WINDOWS = ""
PROGRAM_NAME = '"QR Code Generator.exe"'
OUTPUT_DIR = os.path.join(root, "dist")

# --macos-app-icon=ikon.icns
command = f"python3 -m nuitka --standalone --macos-create-app-bundle --output-dir={OUTPUT_DIR} --output-filename={PROGRAM_NAME} {MAIN_CONST}"
print(command)
subprocess.call(command, shell=True)

a = input("Press Enter to exit")
