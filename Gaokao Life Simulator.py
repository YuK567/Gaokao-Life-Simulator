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

def choice(prompt, options):
    slow_print(prompt, color=Fore.CYAN)
    for i, option in enumerate(options,1):
        print(f"{i}. {option}")
    while True:
        inp=input("Choose an option: S=ave, L=Load, Q=Quit: ").strip().lower()
        if inp =='s':
            save_game()
            continue
        elif inp =='l':
            load_game()
            continue
        elif inp =='q':
            slow_print("Thanks for playing! Progress saved!", color=Fore.MAGENTA)
            save_game()
            sys.exit()
        try:
            pick = int(inp)
            if 1 <= pick <= len(options):
                return pick
        except ValueError:
            pass
        print("Invalid choice. Please try again.")
        
def show_stats():
    print(Fore.YELLOW + f"\n🧠 Knowledge: {player['knowledge']} | 💪 Energy: {player['energy']} | 💖 Mental: {player['mental']}")
    print(Fore.MAGENTA + f"🤝 Mei: {player['mei']} | ⚔️ Chen Hao: {player['chen']} | 👨‍👩‍👧 Parents: {player['parents']}\n")

def save_game():
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(player, f, indent=2)
    slow_print("Game saved successfully!", color=Fore.GREEN)

def load_game():
    global player
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            player = json.load(f)
        slow_print("Game loaded successfully!", color=Fore.GREEN)
        show_stats()
    else:
        slow_print("No save file found.", color=Fore.RED)
        return False
    
def events_week():
    events = [
        {"desc": "Late-night cram session", "options": [
            {"text": "Push through and study", "effects": {"knowledge": +5, "energy": -10}},
            {"text": "Sleep early", "effects": {"energy": +10, "knowledge": -2}}
        ]},
        {"desc": "Mei calls you for help", "options": [
            {"text": "Help her", "effects": {"mei": +10, "knowledge": -2}},
            {"text": "Ignore her", "effects": {"mei": -5, "mental": -5}}
        ]},
        {"desc": "Chen Hao challenges you to a math duel", "options": [
            {"text": "Accept", "effects": {"knowledge": +5, "mental": -5, "chen": +5}},
            {"text": "Decline", "effects": {"mental": +5, "chen": -5}}
        ]},
        {"desc": "Parents do a surprise check on your notes", "options": [
            {"text": "Show them your plan", "effects": {"knowledge": +5, "parents": +5}},
            {"text": "Hide some notes", "effects": {"parents": -5, "mental": +5}}
        ]},
        {"desc": "Found a study hack online", "options": [
            {"text": "Try it", "effects": {"knowledge": +7, "mental": +2}},
            {"text": "Ignore it", "effects": {"mental": +1}}
        ]}
    ]
    event = random.choice(events)
    slow_print(f"Event: {event['desc']}", color=Fore.MAGENTA)
    for i, opt in enumerate(event['options'],1):
        print(f"{i}. {opt['text']}")
    while True:
        try:
            pick = int(input("Choose: "))-1
            if 0 <= pick < len(event['options']):
                for key, val in event['options'][pick]['effects'].items():
                    player[key] += val
                break
        except:
            print("Invalid choice. Please try again.")
    show_stats()
    save_game()
    ##################################PLAYER STATS##################################
    
player = {
    "knowledge": 50,
    "energy": 60,
    "mental": 70,
    "mei": 40,
    "chen": 30,
    "parents": 50,
    "independent": False,
    "scene": "start" 
}

    ##################################SCENES##################################

def scene_start():
    slow_print("Welcome to Gaokao Life Simulator!", color=Fore.CYAN)
    show_stats()
    player["scene"] = "morning"
    save_game
    scene_morning()

def scene_morning():
    slow_print("Scene 1: Monday Morning", color=Fore.CYAN)
    