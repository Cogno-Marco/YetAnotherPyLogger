from logger import log
from pathlib import Path
from logger import FGColor

# print(REVERSED + "Hola" + RESET)
# print(BOLD + "Hola")
# print(UNDERLINE + "Hola" + RESET)

log.error("An Error Occurred Unexpectedly")
log.warning("Something strange is happening")
log.success("Everything is working fine")
log.info("Something is working...")

log.enable_save_to_txt(path=Path.cwd())
log.enable_timestamp()

log.info("Some text")
log.error("Some error")

log.set_log_timestamp_format("[%H:%M]")

log.info("Other text")

log.color(FGColor.red,      " .----------------. ")
log.color(FGColor.green,    "|          _       |")
log.color(FGColor.yellow,   "|      _.-'|'-._   |")
log.color(FGColor.blue,     "| .__.|    |    |  |")
log.color(FGColor.magenta,  "|     |_.-'|'-._|  |")
log.color(FGColor.cyan,     "| '--'|    |    |  |")
log.color(FGColor.white,    "| '--'|_.-'`'-._|  |")
log.color(FGColor.red,      "| '--'          `  |")
log.color(FGColor.green,    " '----------------'")


# example API usage

# log.INFO("some text") #prints "[?] INFO: some text" with colors
# log.enable_save_to_txt("C:/SomeFolder") #stars saving following logs to txt into path, if empty saves to class position
# log.WARNING("something's happening") #prints "[!] WARNING: something's happening" with colors both to cmd and to txt
# log.enable_date_timestamp("dd/mm/yy") #starts printing text with date timestamp with the given format (default = "dd/mm/yy")
# log.enable_time_timestamp("hh:mm:ss") #stars printing text with time timestamp  with the given format (default = "hh:mm:ss")
# log.disable_colors()
# log.enable_colors()

# stuff to test: template method, strategy, classes/inheritance, composition, many little classes combined into one

# implementing your own logger

from logger import log_context, custom_logger
from pathlib import Path


class MyLogger(custom_logger.MiniLog):
    def log(self, text):
        print(text)


log_context.set_logger(MyLogger())

log_context.log("text")
