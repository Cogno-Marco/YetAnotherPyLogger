import unittest
from unittest.mock import patch 
from io import StringIO
from logger import log
from datetime import datetime


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
    
    def test_info_timestamp_as_expected(self):
        log.enable_timestamp()
        time_format = "[%Y-%m-%d %H:%M:%S]"
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.BLUE}{self.BOLD}{time_formatted}[?] Info: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.info(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
    def test_warning_timestamp_as_expected(self):
        log.enable_timestamp()
        time_format = "[%Y-%m-%d %H:%M:%S]"
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.YELLOW}{self.BOLD}{time_formatted}[!] Warning: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.warning(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
    def test_error_timestamp_as_expected(self):
        log.enable_timestamp()
        time_format = "[%Y-%m-%d %H:%M:%S]"
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.RED}{self.BOLD}{time_formatted}[-] Error: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.error(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
    def test_success_timestamp_as_expected(self):
        log.enable_timestamp()
        time_format = "[%Y-%m-%d %H:%M:%S]"
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.GREEN}{self.BOLD}{time_formatted}[+] Success: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.success(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
    def test_format_change_info(self):
        log.enable_timestamp()
        time_format = "[%H:%M:%S]"
        log.set_log_timestamp_format(time_format)
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.GREEN}{self.BOLD}{time_formatted}[+] Success: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.success(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
            
    
    def test_format_change_warning(self):
        log.enable_timestamp()
        time_format = "[%H:%M:%S]"
        log.set_log_timestamp_format(time_format)
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.YELLOW}{self.BOLD}{time_formatted}[!] Warning: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.warning(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
    def test_format_change_error(self):
        log.enable_timestamp()
        time_format = "[%H:%M:%S]"
        log.set_log_timestamp_format(time_format)
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.RED}{self.BOLD}{time_formatted}[-] Error: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.error(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
    def test_format_change_success(self):
        log.enable_timestamp()
        time_format = "[%H:%M:%S]"
        log.set_log_timestamp_format(time_format)
        
        time = datetime.now()
        time_formatted = time.strftime(time_format)
        
        expected_log = f"{self.RESET}{self.GREEN}{self.BOLD}{time_formatted}[+] Success: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.success(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log)
    
     
if __name__ == '__main__':
    unittest.main()