import sys, time,json,os,random
from colorama import Fore, Back, Style, init
init(autoreset=True)   

SAVE_FILE = "gaokao_save.json"

def slow_print(text, delay=0.02, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Style.RESET_ALL)
