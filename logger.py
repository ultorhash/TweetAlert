
from enum import Enum
 
class Color(Enum):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Logger:
    @staticmethod
    def scrapping_started(symbol: str) -> None:
        print(f'Scrapping {Color.BOLD.value}{Color.BLUE.value}{symbol}{Color.END.value} stared.')
    
    @staticmethod
    def scrapping_ended(symbol: str, interval_expression: str) -> None:     
        print(\
          f'Scrapping for {Color.BOLD.value}{Color.BLUE.value}{symbol}{Color.END.value} ended, ' \
          f'next in {Color.BOLD.value}{Color.GREEN.value}{interval_expression}{Color.END.value}.' \
        )