from datetime import datetime
from pathlib import Path
from . import FGColor, Styling, BGColor

RESET = "\u001b[0m"


logger_options = {
    "save_to_file": False,
    "log_path": Path.cwd(),
    "log_timestamp_format": "[%Y-%m-%d %H:%M:%S]",
    "is_timestamp_enabled": False
}


def error(text):
    if logger_options["is_timestamp_enabled"]:
        time = datetime.now()
        t_format = time.strftime(logger_options["log_timestamp_format"])
        print(f"{RESET}{FGColor.red}{Styling.bold}{t_format}[-] Error: {RESET}{text}{RESET}")
    else:
        print(f"{RESET}{FGColor.red}{Styling.bold}[-] Error: {RESET}{text}{RESET}")
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Error", text)


def warning(text):
    print(f"{RESET}{FGColor.yellow}{Styling.bold}[!] Warning: {RESET}{text}{RESET}")
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Warn", text)


def info(text):
    print(f"{RESET}{FGColor.blue}{Styling.bold}[?] Info: {RESET}{text}{RESET}")
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Info", text)


def success(text):
    print(f"{RESET}{FGColor.green}{Styling.bold}[+] Success: {RESET}{text}{RESET}")
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Success", text)

def critical(text):
    pass


def enable_save_to_txt(path=""):
    if path != "":
        logger_options["log_path"] = path

    logger_options["save_to_file"] = True


def save_to_txt(path, type, message):
    time = datetime.now()
    text = (
        time.strftime(logger_options["log_timestamp_format"])
        + " - "
        + type.capitalize()
        + ": "
        + message
        + "\n"
    )

    file = open(Path.joinpath(logger_options["log_path"], "logs.txt"), "a+")
    file.write(text)


def set_log_timestamp_format(format: str):
    logger_options["log_timestamp_format"] = format

def enable_timestamp():
    logger_options["is_timestamp_enabled"] = True

def disablke_timestamp():
    logger_options["is_timestamp_enabled"] = False


def setCustomColor(number):
    print(f"\u001b[38;5;{number}m")


def setCustomBGColor(number):
    print(f"\u001b[48;5;{number}m")
