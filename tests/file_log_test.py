import unittest
from unittest.mock import patch 
from io import StringIO
from logger import log
from datetime import datetime
import os

class TestLogMethods(unittest.TestCase):

    RESET = "\u001b[0m"
    BLUE = "\u001b[38;5;12m"
    RED = "\u001b[38;5;9m"
    GREEN = "\u001b[38;5;10m"
    YELLOW = "\u001b[38;5;11m"
    
    BOLD = "\33[1m"
    TEXT = "working"
    DEFAULT_TIME_FORMAT = "[%Y-%m-%d %H:%M:%S]"
    
    def setUp(self) -> None:
        log.disable_timestamp()
        log.disable_save_to_txt()
        log.set_log_timestamp_format(self.DEFAULT_TIME_FORMAT)
        
        #delete old file
        os.remove("approval_test_check.txt")
        
    
    #approval test to check if file is consistent
    def test_consistency(self):
        #create file
        log.enable_save_to_txt("approval_test_check.txt")

        log.info("testing info clean")
        log.error("testing error clean")
        log.warning("testing warning clean")
        log.success("testing success clean")
        
        #get its data
        to_check = ""
        with open("approval_test_check.txt", "r") as f1:
            to_check = f1.read()
        
        #get target data
        target = ""
        with open("approval_test_valid.txt", "r") as f2:
            target = f2.read()
            
        self.assertEqual(to_check, target)
    
     
if __name__ == '__main__':
    unittest.main()