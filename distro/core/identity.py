import os

def show_banner():
    # Cores para o terminal
    cyan = "\033[96m"
    reset = "\033[0m"
    
    print(f"{cyan}")
    print("  _____  _____  _____  _____  __  __  ")
    print(" |  __ \|  __ \|_   _|/ ____||  \/  | ")
    print(" | |__) | |__) | | | | (___  | \  / | ")
    print(" |  ___/|  _  /  | |  \___ \ | |\/| | ")
    print(" | |    | | \ \ _| |_ ____) || |  | | ")
    print(" |_|    |_|  \_\_____|_____/ |_|  |_| ")
    print(f"{reset}")
    
    try:
        with open("version.txt", "r") as f:
            print(f" --- {f.read().strip()} ---")
    except:
        print(" --- Distro Prisma: Online ---")

if __name__ == "__main__":
    show_banner()

