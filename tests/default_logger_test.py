import unittest
from unittest.mock import patch 
from io import StringIO
from logger import log


class TestLogMethods(unittest.TestCase):

    RESET = "\u001b[0m"
    BLUE = "\u001b[38;5;12m"
    BOLD = "\33[1m"
    TEXT = "working"
    
    def setUp(self) -> None:
        log.disable_timestamp()
    
    def test_info_as_expected(self):
        expected_log = f"{self.RESET}{self.BLUE}{self.BOLD}[?] Info: {self.RESET}{self.TEXT}{self.RESET}\n"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.info(self.TEXT)
            self.assertEqual(fake_out.getvalue(), expected_log) 


if __name__ == '__main__':
    unittest.main()