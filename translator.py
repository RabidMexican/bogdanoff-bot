class Translator:

    def __init__(self):
        self.details = {
            'FROMSYMBOL': 'From',
            'TOSYMBOL': 'To',
            'PRICE': 'Price',
            'LASTVOLUME': 'Volume',
            'VOLUME24HOUR': '24h volume',
            'OPEN24HOUR': '24h open',
            'HIGH24HOUR': '24h high',
            'LOW24HOUR': '24h low',
            'CHANGE24HOUR': '24h change',
            'CHANGEPCT24HOUR': '24h percent change',
        }

    def get_detail(self, name):
      if name in self.details:
        return self.details[name]
