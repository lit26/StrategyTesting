import pandas as pd
import plotly.graph_objects as go

class Strategy:
    def __init__(self, df, plot=True):
        self._open = False
        self._trades = []
        self._orders = []
        self._signal = None
        self._df = df
        self._plot = plot
        self._df['Date'] = pd.to_datetime(self._df['Date'])
    
    def I(self):
        '''
        overwrite the method
        '''

    def _plot_action(self):
        df_buy = self._df[self._df['actions'] == 1]
        df_sell = self._df[self._df['actions'] == -1]
        self._pp_plot._fig.add_trace(go.Scatter(
            x=df_buy['Date'],
            y=df_buy['Low'],
            name='buy',
            mode="markers+text",
            marker_symbol='triangle-up',
            text=["Buy"]*len(df_buy),
            textposition="bottom center",
            marker=dict(color='yellow', size=13),
            showlegend=False
        ), row=1, col=1)
        self._pp_plot._fig.add_trace(go.Scatter(
            x=df_sell['Date'],
            y=df_sell['High'],
            name='sell',
            mode="markers+text",
            marker_symbol='triangle-down',
            text=["Sell"]*len(df_sell),
            textposition="top center",
            marker=dict(color='blue', size=13),
            showlegend=False
        ), row=1, col=1)

    def run(self):
        self._action()
        df_trades, df_stat = self._analysis()
        return df_trades, df_stat

    def _action(self):
        # get trades
        actions = []
        for i, signal in enumerate(self._signal):
            if signal == 1:
                self._trades.append({
                        'Open': self._df.iloc[i]['Close'],
                        'Open_date': self._df.iloc[i]['Date'],
                    })
                self._open = True
                actions.append(1)
            elif signal == -1 and self._open:
                open_position = self._trades[-1]
                open_position['Close'] = self._df.iloc[i]['Close']
                open_position['Close_date'] = self._df.iloc[i]['Date']
                open_position['P/L'] = (open_position['Close'] - open_position['Open'])/open_position['Open']
                self._trades[-1] = open_position
                self._open = False
                actions.append(-1)
            else:
                actions.append(0)
        self._df['actions'] = actions

        # plot action
        if self._plot:
            self._plot_action()
            self._pp_plot.show()
    
    def _analysis(self):
        df_trades = pd.DataFrame(self._trades)
        df_trades['P/L(%)'] = df_trades.apply(lambda x: round(x['P/L']*100, 2), axis=1)
        df_trades = df_trades[['Open', 'Open_date', 'Close', 'Close_date', 'P/L(%)']]
        # get stat of the trades
        n_trades = len(self._trades)
        returns = [i['P/L'] for i in self._trades]
        pos_returns = [i for i in returns if i > 0]
        total_pl = 1
        for trade in returns:
            total_pl = total_pl * (1 + trade)
        win_rate = round(len(pos_returns)*100 / n_trades,2)
        total_pl = round(total_pl*100,2)
        data = {'Stat': [n_trades, win_rate, total_pl]}
        df_stat = pd.DataFrame(data, index=['# Trades','Win Rate(%)', 'Returns(%)'])
        return df_trades, df_stat

