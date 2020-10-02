#proof of concept
def set_logger(custom_log):
    set_logger.__custom_logger = custom_log


def log(text):
    set_logger.__custom_logger.log(text)
      

    
