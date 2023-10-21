# This script is not part of the project. 
# The major objective of the script is counting how many code lines are there in the project.


import os
import pyfiglet
from colorama import init, Fore, Style


init()

def print_large_text(text, color=Fore.WHITE, bold=True):
    f = pyfiglet.Figlet()
    ascii_art = f.renderText(text)
    if bold:
        ascii_art = "\033[1m" + ascii_art
    colored_ascii_art = color + ascii_art + Style.RESET_ALL
    print(colored_ascii_art)

def count_lines_in_files_with_extensions(extensions):
    total_lines = 0

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    total_lines += len(lines)

    return total_lines

if __name__ == "__main__":
    extensions_to_count = (".ipynb", ".py")
    total_lines = count_lines_in_files_with_extensions(extensions_to_count)

    text_to_display = f"Bugün Yazılan Toplam Kod Sayısı: {total_lines}"
    print_large_text(text_to_display, color=Fore.WHITE)
