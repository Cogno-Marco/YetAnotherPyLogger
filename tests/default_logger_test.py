import unittest
from unittest.mock import patch 
from io import StringIO
from logger import log


class TestLogMethods(unittest.TestCase):

    RESET = "\u001b[0m"
    BLUE = "\u001b[38;5;12m"
    RED = "\u001b[38;5;9m"
    GREEN = "\u001b[38;5;10m"
    YELLOW = "\u001b[38;5;11m"
    
    BOLD = "\33[1m"
    TEXT = "working"
    
    def setUp(self) -> None:
        log.disable_timestamp()
    
    def test_info_as_expected(self):
        expected_log = f"{self.RESET}{self.BLUE}{self.BOLD}[?] Info: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.info(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
            
    def test_warning_as_expected(self):
        expected_log = f"{self.RESET}{self.YELLOW}{self.BOLD}[!] Warning: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.warning(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log) 
    
    def test_error_as_expected(self):
        expected_log = f"{self.RESET}{self.RED}{self.BOLD}[-] Error: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.error(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log) 
    
    def test_success_as_expected(self):
        expected_log = f"{self.RESET}{self.GREEN}{self.BOLD}[+] Success: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.success(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log) 
            
if __name__ == '__main__':
    unittest.main()