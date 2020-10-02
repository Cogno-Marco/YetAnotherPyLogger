import unittest
from unittest.mock import patch 
from io import StringIO
from logger import log


class TestLogMethods(unittest.TestCase):

    RESET = "\u001b[0m"
    BLUE = "\u001b[38;5;12m"
    BOLD = "\33[1m"
    
    def test_upper(self):
        text = "working"
        expected_log = f"{self.RESET}{self.BLUE}{self.BOLD}[?] Info: {self.RESET}{text}{self.RESET}"
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            log.info(text)
            for ch1,ch2 in zip(fake_out.getvalue(), expected_log):
                print(f"ch1:{ch1}, ch2:{ch2}\n")
            self.assertEqual(fake_out.getvalue(), expected_log) 

if __name__ == '__main__':
    unittest.main()