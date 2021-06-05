from ta.trend import SMAIndicator
from indicator.indicator import Indicator

class SMA(Indicator):
    def get_indicator(self, n):
        self._params = {'n':n}
        self._df[f'SMA{n}'] = SMAIndicator(close=self._df[self._close], window=n).sma_indicator()
        return self._df[f'SMA{n}']
    
    def plot_indicator(self, pp_plot, color='black', row=1):
        n = self._params['n']
        pp_plot.addLine(self._df[f'SMA{n}'], name=f'SMA{n}', row=row, color=color, showlegend=False)
    