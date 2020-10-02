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


def _general_log(color, intro_text, full_text):
    """general function used to print logs, used by other funnctions to avoid repetition

    :param [color]: color to wrte the text in
    :param [intro_text]: intro text displayed in color
    :param [text]: text to log to screen or to file
    """
    if logger_options["is_timestamp_enabled"]:
        time = datetime.now()
        t_format = time.strftime(logger_options["log_timestamp_format"])
        print(f"{RESET}{color}{Styling.bold}{t_format}{intro_text}{RESET}{full_text}{RESET}")
    else:
        print(f"{RESET}{color}{Styling.bold}{intro_text}{RESET}{full_text}{RESET}")
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], {intro_text}, full_text)


def error(text):
    """prints an error level message
    
    :param [text]: text to print to console and to file(if enabled)
    """
    _general_log(FGColor.red, "[-] Error: ", text)

def warning(text):
    """prints a warning level message
    
    :param [text]: text to print to console and to file(if enabled)
    """
    _general_log(FGColor.yellow, "[!] Warning: ", text)

def info(text):
    """prints an info level message
    
    :param [text]: text to print to console and to file(if enabled)
    """
    _general_log(FGColor.blue, "[?] Info: ", text)

def success(text):
    """prints a success level message
    
    :param [text]: text to print to console and to file(if enabled)
    """
    _general_log(FGColor.green, "[+] Success: ", text)

def critical(text):
    """prints a critical level message
    
    :param [text]: text to print to console and to file(if enabled)
    """
    pass


def enable_save_to_txt(path=""):
    if path != "":
        logger_options["log_path"] = path

    logger_options["save_to_file"] = True

def disable_save_to_txt():
    pass


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

def disable_timestamp():
    logger_options["is_timestamp_enabled"] = False


def setCustomColor(number):
    print(f"\u001b[38;5;{number}m")


def setCustomBGColor(number):
    print(f"\u001b[48;5;{number}m")
