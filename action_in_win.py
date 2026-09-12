import PIL
from PIL import ImageGrab
import pyautogui as kymo
import time
import os
from PIL import Image as pill
import pygetwindow as gw
import webbrowser as wb
import subprocess as sp
import pyperclip
import cv2


study_section = 0


# ============================= SHORT NAMES =============================

apps_names = {

    # Browsers
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",
    "opera": "opera.exe",
    "brave": "brave.exe",
    "vivaldi": "vivaldi.exe",

    # Development
    "vscode": "Code.exe",
    "visual_studio": "devenv.exe",
    "pycharm": "pycharm64.exe",
    "intellij": "idea64.exe",
    "android_studio": "studio64.exe",
    "git": "git.exe",
    "github_desktop": "GitHubDesktop.exe",
    "notepad++": "notepad++.exe",

    # Gaming
    "steam": "steam.exe",
    "epic_games": "EpicGamesLauncher.exe",
    "xbox": "XboxPcApp.exe",
    "ea": "EADesktop.exe",
    "ubisoft": "upc.exe",
    "battle_net": "Battle.net.exe",
    "riot_client": "RiotClientServices.exe",
    "minecraft": "MinecraftLauncher.exe",
    "roblox": "RobloxPlayerBeta.exe",

    # Communication
    "discord": "Discord.exe",
    "whatsapp": "WhatsApp.exe",
    "telegram": "Telegram.exe",
    "slack": "slack.exe",
    "zoom": "Zoom.exe",
    "teams": "ms-teams.exe",
    "skype": "Skype.exe",

    # Media
    "spotify": "Spotify.exe",
    "vlc": "vlc.exe",
    "obs": "obs64.exe",
    "itunes": "iTunes.exe",
    "audacity": "audacity.exe",

    # Microsoft Office
    "word": "WINWORD.EXE",
    "excel": "EXCEL.EXE",
    "powerpoint": "POWERPNT.EXE",
    "outlook": "OUTLOOK.EXE",
    "onenote": "ONENOTE.EXE",
    "onedrive": "OneDrive.exe",

    # Windows
    "files": "explorer.exe",
    "notepad": "notepad.exe",
    "paint": "mspaint.exe",
    "calculator": "CalculatorApp.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "terminal": "wt.exe",
    "task_manager": "Taskmgr.exe",
    "settings": "SystemSettings.exe",
    "control_panel": "control.exe",
    "registry_editor": "regedit.exe",
    "snipping_tool": "SnippingTool.exe",

    # Other
    "camera": "WindowsCamera.exe",
    "notion": "Notion.exe"
}


# ============================= WEBSITES =============================

websites = {

    # Search
    "google": "https://www.google.com",
    "bing": "https://www.bing.com",
    "duckduckgo": "https://duckduckgo.com",
    "docs": "https://docs.google.com/document/u/0/",

    # AI
    "chatgpt": "https://chatgpt.com",
    "gemini": "https://gemini.google.com",
    "claude": "https://claude.ai",
    "perplexity": "https://www.perplexity.ai",

    # Social Media
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "tiktok": "https://www.tiktok.com",
    "reddit": "https://www.reddit.com",
    "x": "https://x.com",
    "linkedin": "https://www.linkedin.com",
    "pinterest": "https://www.pinterest.com",

    # Communication
    "discord": "https://discord.com",
    "telegram": "https://web.telegram.org",
    "whatsapp": "https://web.whatsapp.com",
    "messenger": "https://www.messenger.com",
    "gmail": "https://mail.google.com",
    "outlook": "https://outlook.live.com",

    # Entertainment
    "netflix": "https://www.netflix.com",
    "spotify": "https://open.spotify.com",
    "twitch": "https://www.twitch.tv",
    "prime_video": "https://www.primevideo.com",
    "disney_plus": "https://www.disneyplus.com",

    # Gaming
    "steam": "https://store.steampowered.com",
    "epic_games": "https://store.epicgames.com",
    "roblox": "https://www.roblox.com",
    "minecraft": "https://www.minecraft.net",
    "xbox": "https://www.xbox.com",
    "playstation": "https://www.playstation.com",
    "nintendo": "https://www.nintendo.com",

    # Shopping
    "amazon": "https://www.amazon.com",
    "ebay": "https://www.ebay.com",
    "walmart": "https://www.walmart.com",
    "target": "https://www.target.com",
    "best_buy": "https://www.bestbuy.com",
    "etsy": "https://www.etsy.com",
    "aliexpress": "https://www.aliexpress.com",

    # Education
    "wikipedia": "https://www.wikipedia.org",
    "khan_academy": "https://www.khanacademy.org",
    "coursera": "https://www.coursera.org",
    "edx": "https://www.edx.org",
    "freecodecamp": "https://www.freecodecamp.org",

    # Developer
    "github": "https://github.com",
    "gitlab": "https://gitlab.com",
    "stackoverflow": "https://stackoverflow.com",
    "npm": "https://www.npmjs.com",
    "pypi": "https://pypi.org",

    # News
    "bbc": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "ny_times": "https://www.nytimes.com",
    "reuters": "https://www.reuters.com",

    # Maps / Travel
    "google_maps": "https://maps.google.com",
    "google_earth": "https://earth.google.com",
    "tripadvisor": "https://www.tripadvisor.com",

    # Microsoft
    "microsoft": "https://www.microsoft.com",
    "office": "https://www.office.com",
    "onedrive": "https://onedrive.live.com"
}


# ============================= DISTRACTIONS =============================

distractions = [
    "Steam.exe",
    "EpicGamesLauncher.exe",
    "XboxPcApp.exe",
    "RobloxPlayerBeta.exe",
    "Discord.exe",
    "WhatsApp.exe",
    "Telegram.exe",
    "chrome.exe",
    "msedge.exe",
    "firefox.exe"
]


# ============================= WINDOW MANAGER =============================

class WindowManager:

    @staticmethod
    def maximize_window():

        window = gw.getActiveWindow()

        if window:
            window.maximize()
            print("Window maximized.")

        else:
            print("No active window found.")

    @staticmethod
    def minimize_window():

        window = gw.getActiveWindow()

        if window:
            window.minimize()
            print("Window minimized.")

        else:
            print("No active window found.")

    @staticmethod
    def minimize_all():

        kymo.hotkey("win", "m")


# ============================= OPEN APPLICATION =============================

def open_app(app_name):

    if app_name not in apps_names:

        print(f"Application '{app_name}' not found.")
        return

    kymo.hotkey("win", "s")

    time.sleep(0.5)

    kymo.write(app_name)

    kymo.press("enter")

    time.sleep(2)

    WindowManager.maximize_window()


# ============================= CLOSE APPLICATION =============================

def close_app(app_name):

    if app_name not in apps_names:

        print(f"Application '{app_name}' not found.")
        return

    exe_name = apps_names[app_name]

    sp.run(
        ["taskkill", "/IM", exe_name, "/F"],
        stdout=sp.DEVNULL,
        stderr=sp.DEVNULL
    )

    print(f"{app_name} closed.")


# ============================= WEB BROWSER =============================

def open_browser():

    url = input("Website name: ").lower()

    if url in websites:

        wb.open(websites[url])

        time.sleep(2)

        WindowManager.maximize_window()

    else:

        print("Website not found.")


# ============================= TAKE SCREENSHOT =============================

def take_screenshot():

    timestamp = time.strftime("%Y%m%d_%H%M%S")

    folder = r"C:\screen shot"

    os.makedirs(folder, exist_ok=True)

    filename = os.path.join(
        folder,
        f"screenshot_{timestamp}.png"
    )

    screenshot = ImageGrab.grab()

    screenshot.save(filename)

    print(f"Screenshot saved as {filename}")


# ============================= OPEN TASK MANAGER =============================

def open_taskmanager():

    kymo.hotkey("ctrl", "shift", "esc")


# ============================= COPY =============================

def copy():

    text = input("Text to copy: ")

    pyperclip.copy(text)

    print("Copied.")


# ============================= PASTE =============================

def paste():

    text = pyperclip.paste()

    print(text)


# ============================= FOCUS MODE =============================

def focus_mode():

    global study_section

    print("Focus mode activated.")


    WindowManager.maximize_window()

    kymo.press("enter")

    WindowManager.minimize_all()
    
    WindowManager.minimize_all()

    open_app("spotify")

    WindowManager.maximize_window
   
    kymo.moveTo(71 ,421, duration=0.1)

    kymo.click()
   
    WindowManager.minimize_window()
    
    open_app("edge")

    
    open_app("pompower")
    
    kymo.press("enter")

    kymo.write(f"HI , REMIND TO TAKE A BREAK ! study section # {study_section}")

    print(f"Study section: {study_section}")

    study_section += 1


# ============================= DEVELOPER MODE =============================

def developer_mode():

    # Close distractions

    for app in distractions:

        sp.run(
            ["taskkill", "/IM", app, "/F"],
            stdout=sp.DEVNULL,
            stderr=sp.DEVNULL
        )

    # Open developer websites

    wb.open(websites["chatgpt"])

    wb.open(websites["claude"])

    wb.open(websites["github"])

    wb.open(websites["docs"])

    # Open PowerShell

    open_app("powershell")

    # Minimize everything

    kymo.hotkey("win", "m")

    # Open VS Code

    open_app("vscode")

    time.sleep(2)

    WindowManager.maximize_window()

    # Greeting message

    kymo.hotkey("ctrl", "p")

    kymo.write(
        "HI THIS IS YOUR AUTOMATION ASSISTANT, "
        "DON'T FORGET TO TAKE A BREAK!"
    )


# =============================================================================
# ================================= FILES =====================================
# =============================================================================

DESKTOP_PATH = os.path.join(
    os.path.expanduser("~"),
    "OneDrive",
    "Desktop"
)


# ============================= CREATE FOLDER =============================

def create_folder():

    folder_name = input("Folder name: ")

    folder_path = os.path.join(
        DESKTOP_PATH,
        folder_name
    )

    os.makedirs(
        folder_path,
        exist_ok=True
    )

    print(f"Folder created: {folder_path}")


# ============================= CREATE FILE =============================

def create_file():

    file_name = input("File name: ")

    file_path = os.path.join(
        DESKTOP_PATH,
        f"{file_name}.txt"
    )

    open(file_path, "w").close()

    print(f"File created: {file_path}")


# ============================= DELETE FILE =============================

def delete_file():

    file_name = input("File name to delete: ")

    file_path = os.path.join(
        DESKTOP_PATH,
        file_name
    )

    if os.path.isfile(file_path):

        os.remove(file_path)

        print(f"File deleted: {file_path}")

    else:

        print("File not found.")


# ============================= MAIN =============================

def main():

    while True:

        print("\n=============================")
        print("       LIST OF ACTIONS")
        print("=============================")

        print("1. Open application")
        print("2. Close application")
        print("3. Maximize current window")
        print("4. Minimize current window")
        print("5. Open website")
        print("6. Take screenshot")
        print("7. Focus mode")
        print("8. Developer Mode")
        print("9. Exit")
        print("10. Create file")
        print("11. Create folder")
        print("12. Delete file")
        print("13. Open Task Manager")
        print("14. Copy")
        print("15. Paste")

        print("=============================")

        choice = input("Choose: ").lower()


        # ================= OPEN APP =================

        if choice == "1":

            app_name = input(
                "Application name: "
            ).lower()

            open_app(app_name)


        # ================= CLOSE APP =================

        elif choice == "2":

            app_name = input(
                "Application name: "
            ).lower()

            close_app(app_name)


        # ================= MAXIMIZE =================

        elif choice == "3":

            WindowManager.maximize_window()


        # ================= MINIMIZE =================

        elif choice == "4":

            WindowManager.minimize_window()


        # ================= WEBSITE =================

        elif choice == "5":

            open_browser()


        # ================= SCREENSHOT =================

        elif choice == "6":

            take_screenshot()


        # ================= FOCUS MODE =================

        elif choice == "7":

            focus_mode()


        # ================= DEVELOPER MODE =================

        elif choice == "8":

            developer_mode()


        # ================= EXIT =================

        elif choice == "9":

            print("Exiting now...!")

            break


        # ================= CREATE FILE =================

        elif choice == "10":

            create_file()


        # ================= CREATE FOLDER =================

        elif choice == "11":

            create_folder()


        # ================= DELETE FILE =================

        elif choice == "12":

            delete_file()


        # ================= TASK MANAGER =================

        elif choice == "13":

            open_taskmanager()


        # ================= COPY =================

        elif choice == "14":

            copy()


        # ================= PASTE =================

        elif choice == "15":

            paste()



        # ================= INVALID =================

        else:

            print("Invalid choice.")


# ============================= START PROGRAM =============================

if __name__ == "__main__":

    main()