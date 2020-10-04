from datetime import datetime
from pathlib import Path
from . import FGColor, Styling, BGColor
import os

RESET = "\u001b[0m"


logger_options = {
    "save_to_file": False,
    "log_path": Path.cwd(),
    "log_file_name": "logs.txt",
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
        print(
            f"{RESET}{color}{Styling.bold}{t_format}{intro_text}{RESET}{full_text}{RESET}")
    else:
        print(f"{RESET}{color}{Styling.bold}{intro_text}{RESET}{full_text}{RESET}")
    if logger_options["save_to_file"]:
        if logger_options["is_timestamp_enabled"]:
            time = datetime.now()
            t_format = time.strftime(logger_options["log_timestamp_format"])
            _save_to_txt(f"{t_format}{intro_text}{full_text}\n")
        else:
            _save_to_txt(f"{intro_text}{full_text}\n")


def error(text):
    # TODO: add more inputs
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


def enable_save_to_txt(name="logs.txt", path=""):
    """enables saving logs to file, but with disabled colors

    param [name]: name of the file to save logs in, if empty or None defaults to "logs.txt"
    param [path]: path to save the file in, if empty or None path is default
    """

    if name != "" or name != None:
        logger_options["log_file_name"] = name
    if path != "" or path != None:
        logger_options["log_path"] = path

    logger_options["save_to_file"] = True


def disable_save_to_txt():
    """disables file saving logs"""
    logger_options["save_to_file"] = False


def _save_to_txt(text):
    with open(os.path.join(logger_options["log_path"], logger_options["log_file_name"]), "a+") as f:
        f.write(text)


def set_log_timestamp_format(format: str):
    logger_options["log_timestamp_format"] = format


def enable_timestamp():
    """enables timestamps into logs, 
    see set_log_timestamp_format to change the format of the timestamp
    """
    logger_options["is_timestamp_enabled"] = True


def disable_timestamp():
    """disables timestamps into logs"""
    logger_options["is_timestamp_enabled"] = False
