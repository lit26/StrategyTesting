import pandas as pd
from indicator.SMA import SMA
from strategy.util import cross
from strategy.strategy import Strategy
from plot_function import PlotlyPlot

class SMAstrategy(Strategy):
    def I(self, fast, slow):
        SMA_fast = SMA(self._df)
        self._df[f'SMA{fast}'] = SMA_fast.get_indicator(fast)
        SMA_slow = SMA(self._df)
        self._df[f'SMA{slow}'] = SMA_slow.get_indicator(slow)
        self._signal = cross(self._df[f'SMA{fast}'], self._df[f'SMA{slow}'])
        if self._plot:
            self._pp_plot = PlotlyPlot(self._df, 'Date', 'Close', 'Open','High', 'Low',
                                        main_plot_type='Candlestick', range_slider=True)
            SMA_fast.plot_indicator(self._pp_plot, 'blue')
            SMA_slow.plot_indicator(self._pp_plot, 'yellow')