# Import the Libraries
import pandas as pd
import numpy as np

# Define initial portfolio value and risk-free rate
initial_portfolio_value = 6500
rfir = 0.05

#Import the DataSet
tradelog = pd.read_csv('C:/Users/Lenovo/Desktop/Internship Task/task1/tradelog.csv')

# Find Total Trades
total_trades = len(tradelog)
print(total_trades)

#Create Profit Column
tradelog['Profit'] = (tradelog['Exit Price'] - tradelog['Entry Price'])

# Profitable Trades
pft = len(tradelog[tradelog['Profit']>0])

# Loss Making Trades
lmt = len(tradelog[tradelog['Profit']<0])

# Win Rate
win_rate = pft/total_trades

#Loss Rate
loss_rate = lmt/total_trades

# Average Profit Per Trade
appt = np.mean(tradelog['Profit'][tradelog['Profit'] > 0])

# Average Loss Per Trade
alpt = np.mean((tradelog['Profit'][tradelog['Profit'] < 0])*-1)

# Risk Reward Ratio
rrr = appt / alpt

# Expectancy
expectancy = (win_rate * appt) - (loss_rate * alpt)

# Average ROR Per Trade
arorpt = (appt - rfir) / alpt

# Sharpe Ratio
standard_deviation = np.std(tradelog['Profit'])
sharpe_ratio = (appt - rfir) / standard_deviation

# Maximum Drawdown
cumulative_returns = tradelog["Profit"].cumsum()
max_drawdown = cumulative_returns.max() - cumulative_returns.min()

# Maximum Drawdown Percentage
mdp = max_drawdown/cumulative_returns.max()

# CAGR
endval = cumulative_returns.iloc[-1] + initial_portfolio_value
cagr = ((endval / initial_portfolio_value) ** (1 / total_trades)) - 1

# Calmer Ratio
calmar_ratio = cagr / mdp

# Save final output report to CSV file

output_data = pd.DataFrame({
    'Total Trades': [total_trades],
    'Profitable Trades': [pft],
    'Loss-Making Trades': [lmt],
    'Win Rate': [win_rate],
    'Average Profit per trade': [appt],
    'Average Loss per trade': [alpt],
    'Risk Reward Ratio': [rrr],
    'Expectancy': [expectancy],
    'Average ROR per trade': [arorpt],
    'Sharpe Ratio': [sharpe_ratio],
    'Max Drawdown': [max_drawdown],
    'Max Drawdown Percentage': [mdp],
    'CAGR': [cagr],
    'Calmar Ratio': [calmar_ratio]
})
output_data.to_csv('C:/Users/Lenovo/Desktop/Internship Task/task1/strategy_results.csv', index=False)

# Optional: Print the results
print(output_data)
