import random

# Color codes for Termux terminal
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
MAGENTA = '\033[95m'

def ask_question(question, options):
    print(f"\n{BOLD}{question}{RESET}")
    for i, option in enumerate(options, 1):
        print(f"{CYAN}{i}.{RESET} {option}")
    
    while True:
        try:
            choice = int(input(f"\n{YELLOW}Enter your choice (1-4): {RESET}"))
            if 1 <= choice <= 4:
                return choice
            else:
                print(f"{RED}Invalid choice! Enter 1-4{RESET}")
        except ValueError:
            print(f"{RED}Please enter a number!{RESET}")

def show_banner():
    print(f"{MAGENTA}")
    print("=" * 50)
    print(f"{YELLOW}{BOLD}   🍲  GHANA FOOD PERSONALITY QUIZ  🇬🇭   {RESET}")
    print(f"{MAGENTA}=" * 50)
    print(f"{RESET}")

def main():
    show_banner()
    print(f"{YELLOW}{BOLD}ABOUT THIS APP:{RESET}")
    print(f"{GREEN}Discover which Ghanaian food matches your personality!{RESET}")
    print(f"Created by: Kingsford\n")
    print("Banku, Waakye, Fufu, Kelewele - which one are you?")
    
    input(f"\n{BOLD}Press Enter to start...{RESET}")
    
    score = {"Banku + Tilapia": 0, "Waakye": 0, "Fufu": 0, "Kelewele": 0}
    
    # Question 1
    q1 = ask_question("1. What's your vibe on a Saturday night?", 
                      ["Chill at home with music 🎵", "Street party & dance 💃", "Deep talks with friends 🗣️", "Adventures & exploring 🗺️"])
    if q1 == 1: score["Banku + Tilapia"] += 1
    elif q1 == 2: score["Waakye"] += 1
    elif q1 == 3: score["Fufu"] += 1
    else: score["Kelewele"] += 1
    
    # Question 2
    q2 = ask_question("2. Pick your energy level:", 
                      ["Calm & steady 😌", "Busy & always moving ⚡", "Strong & reliable 💪", "Spicy & fun 🌶️"])
    if q2 == 1: score["Banku + Tilapia"] += 1
    elif q2 == 2: score["Waakye"] += 1
    elif q2 == 3: score["Fufu"] += 1
    else: score["Kelewele"] += 1
    
    # Question 3
    q3 = ask_question("3. Your ideal meal time?", 
                      ["Afternoon with family 👨‍👩‍👧‍👦", "Morning before work ☀️", "After workout 🏋️", "Late night snack 🌙"])
    if q3 == 1: score["Banku + Tilapia"] += 1
    elif q3 == 2: score["Waakye"] += 1
    elif q3 == 3: score["Fufu"] += 1
    else: score["Kelewele"] += 1
    
    # Get result
    result = max(score, key=score.get)
    
    print(f"\n{BOLD}{YELLOW}================ RESULTS ================{RESET}")
    print(f"{BOLD}{GREEN}🎉 You are: {result}! 🎉{RESET}")
    
    if result == "Banku + Tilapia":
        print(f"{CYAN}Calm, reliable, and loved by everyone 🔥")
        print("You bring people together and everyone trusts you!{RESET}")
    elif result == "Waakye":
        print(f"{YELLOW}Energetic, colorful, and always on the go 💛")
        print("Life of the party! You never have a dull moment!{RESET}")
    elif result == "Fufu":
        print(f"{GREEN}Strong, dependable, and the backbone 💪")
        print("People lean on you. You're the foundation!{RESET}")
    else:
        print(f"{RED}Spicy, adventurous, and unforgettable 😎")
        print("You keep life exciting! Never boring with you!{RESET}")
    
    print(f"\n{BOLD}Your scores:{RESET}")
    for food, points in score.items():
        print(f"  {food}: {points}/3")
    
    print(f"{YELLOW}{BOLD}========================================{RESET}\n")
    print(f"{GREEN}Screenshot this and share with friends!{RESET}")

if __name__ == "__main__":
    main()
