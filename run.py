import core
import sys
from bot_settings import settings, write_default_settings, read_settings
from pathlib import Path
from colorama import init, Fore, Style

settings_path = Path("settings.yaml")

print(Style.NORMAL + Fore.LIGHTBLUE_EX + "Starting the bot...")

print(Style.NORMAL + Fore.LIGHTBLUE_EX + "Loading config file...")

try:
    read_settings(settings_path)
except FileNotFoundError:
    print(Fore.YELLOW + Style.BRIGHT + "The config file could not be found, generating a default one.")
    write_default_settings(settings_path)
    sys.exit()
else:
    print(Style.BRIGHT + Fore.GREEN + "Config file loaded successfully.")

print(Style.NORMAL + Fore.LIGHTBLUE_EX + "Begin crafting...")

core.run()
