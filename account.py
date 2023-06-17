import re

class Account:
    def __init__(self, params: str):
        settings = params.strip().replace(' ', '').split('|')
        self.symbol = settings[0]
        self.name = settings[1]
        self.lifespan = settings[2]
        self.interval = settings[3]
        self.keywords = self.__assign_keywords(settings[4])
    
    @staticmethod
    def to_seconds(expression: str) -> int:
        formatted = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', expression.strip())
        values = [s.strip() for s in formatted if s is not None and s.strip() != '']
        
        digit = int(values[0])
        unit = values[1]
        
        match unit:
            case 'sec':
                return digit
            case 'min':
                return digit * 60
            case 'hrs':
                return digit * 3600
            case _:
                raise Exception('Wrong time unit provided in account settings')

    @classmethod
    def __assign_keywords(self, keywords: str) -> str | list[str]:
        return '*' if keywords == '*' else keywords.split(',')