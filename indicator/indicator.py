class Indicator:
    def __init__(self, df, open='Open', high='High', low='Low', close='Close'):
        self._df = df
        self._open = open
        self._high = high
        self._low = low
        self._close = close
        self._params = {}
    
    def get_indicator(self):
        """
        overwrite the method
        """
    
    def plot_ndicator(self):
        """
        overwrite the method
        """